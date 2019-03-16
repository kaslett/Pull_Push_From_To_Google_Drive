# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 19:01:20 2019

@author: 15037
"""

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
from googleapiclient.http import MediaIoBaseDownload
from apiclient import discovery
import io

#List different directories
#Working Directory with Code:
main = "C://Users//15037//Desktop//"
#Directory where you want to download the data:
data = main + 'Data//'

os.chdir(main)

#Two ways to pull
#One way is to pull a file using the filename and the other is to pull all the files froma folder. 
#The first strategy (pulling using a filename) is displayed below:
#The file should end up in the data folder

file_to_pull = 'final_tweets_ver_2_womenswave.csv'

with open('token_py27.pickle', 'rb') as token:
    creds = pickle.load(token)
service = build('drive', 'v3', credentials=creds)
os.chdir(data)
res = service.files().list(corpora='teamDrive',supportsTeamDrives=True,includeTeamDriveItems=True,teamDriveId='0AALD4Ye4LoUBUk9PVA',fields='files(id,parents,name,mimeType)',q="name ='" + file_to_pull + "' and trashed=false").execute()
file = res['files']
file = file[0]
file_id = file['id']
filename = file['name']
request = service.files().get_media(fileId=file_id)
fh = io.FileIO(filename, 'wb')
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()
    print("Download %d%%." % int(status.progress() * 100))



#The second strategy (pulling using a folder) is displayed below:
#All the files with this folder will be pulled. You have to use the id of the folder to pull it. The id can be found at the end of the url when you are on the 
#the webpage of the folder. For example for the folder, All_Hashtag_Data, has the url: https://drive.google.com/drive/folders/1IfmTV_jluJrwvbr4tHobCpO-xLKoeSdJ
#The folder id is the end of the url: 1IfmTV_jluJrwvbr4tHobCpO-xLKoeSdJ.
#The example code pulls from the folder: CAPP Test Team Drive/All_Hashtag_Data/Abolishice/Pictures.

folder_topull_id = '1h2LmgvbA6WBUGw2OACNdKtsSHyjza2VM'

res = service.files().list(corpora='teamDrive',supportsTeamDrives=True,includeTeamDriveItems=True,teamDriveId='0AALD4Ye4LoUBUk9PVA',fields='files(id,parents,name,mimeType)',q="parents ='" + folder_topull_id + "' and trashed=false").execute()
files = res['files']
os.chdir(data)
for i in range(0,len(files)):
    files_temp = files[i]
    file_id = files_temp['id']
    filename = files_temp['name']
    print('Downloading ' + filename)
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(filename, 'w')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))