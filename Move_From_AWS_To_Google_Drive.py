"""
@author: Kevin Aslett
Created by Kevin Aslett on Sun April 11th, 2019
This code moves files from the AWS S3 servers to a specific google drive folder and DELETE the file in S3.

"""
#Import libraries

from __future__ import print_function
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import boto
#from boto.s3.connection import S3Connection
from boto.s3.key import Key
import re
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.http import MediaFileUpload
from apiclient import discovery
import boto3

#List different directories - These are examples
main = '/home/ubuntu/digiadv/'
data = '/home/ubuntu/digiadv/data'
temp = '/home/ubuntu/digiadv/data/Files_To_Move_To_Google_Drive'

#AWS Folder You will be pulling from:
aws_folder = ''

#Folder_id of file you are pulling from:
fold_id = ''

#Name of the AWS bucket you are pulling from:
aws_bucket = ''

#Region Name of the AWS bucket you are pulling from:
region = ''

os.chdir(main)
os.chdir(data)

#Load saved client credentials for google drive access
gauth = GoogleAuth()
gauth.LoadCredentialsFile("street_cred.txt")
drive = GoogleDrive(gauth)

#Load saved client credentials for google drive access
with open('token.pickle', 'rb') as token:
    creds = pickle.load(token)
service = build('drive', 'v3', credentials=creds)

#Get into Amazon Web Services
c = boto.s3.connect_to_region(region)
aws_bucket = c.get_bucket(aws_bucket)
files_to_collect = aws_bucket.list(prefix=aws_folder)

session = boto3.Session(
    region_name= region
)

#Function to upload the file to Google Drive:
def upload_file_team_dr(filename,fold_id):
    f = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": fold_id}]})
    f.SetContentFile(filename)
    os.chdir(data)
    f.Upload(param={'supportsTeamDrives': True})

count = 0
for entry in files_to_collect:
    count += 1
    if count > 1:
        zip_key = entry
        zip_name = str(entry)
        zip_name = re.sub('<Key: ' + aws_bucket + ',' + aws_folder + '/', '', zip_name)
        zip_name = re.sub('>', '', zip_name)
        os.chdir(temp)
        fname = str(zip_name)
        k = zip_key
        k.get_contents_to_filename(str(fname))
        real_count = count - 1
        try:
            upload_file_team_dr(str(fname),fold_id)
            print('Loaded ' + str(real_count) + ' files into Google Drive folder ' + str(aws_folder))
        except:
            print('Could not load' + str(fname) + ' file')
        os.chdir(temp)
        #Remove the file from the location you downloaded it to
        os.remove(str(fname))
        #Delete the file from S3
        s3 = session.resource("s3")
        obj = s3.Object(aws_bucket, aws_folder + '/' + fname)
        obj.delete()
