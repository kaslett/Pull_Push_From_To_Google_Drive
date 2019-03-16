
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import os.path

#List different directories
#Working Directory with Code:
main = "C://Users//15037//Desktop//"
#Directory where you want to download the data:
data = main + 'Data//'
os.chdir(data)
#Get the authority to upload to google drive:
gauth = GoogleAuth()
gauth.LoadCredentialsFile("my_creds.txt")
drive = GoogleDrive(gauth)


#Upload. Put the filename with wish you want to push from the directory
#Name the folder id, with which you want to push the file to.
#You have to use the id of the folder to pull it. The id can be found at the end of the url when you are on the 
#the webpage of the folder. For example for the folder, All_Hashtag_Data, has the url: https://drive.google.com/drive/folders/1IfmTV_jluJrwvbr4tHobCpO-xLKoeSdJ
#The folder id is the end of the url: 1IfmTV_jluJrwvbr4tHobCpO-xLKoeSdJ.
#The example code pushes a file (final_tweets_ver_2_womenswave.csv) to a folder (CAPP Test Team Drive/Practice).

filename = "final_tweets_ver_2_womenswave.csv"
fold_id = '1WT_Yijmx5LVKhfmChoiyEB4FtNUZExbQ'

#Function to upload the file:
def upload_file_team_dr(filename,fold_id):
    f = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": fold_id}]})
    os.chdir(data)
    f.SetContentFile(filename)
    f.Upload(param={'supportsTeamDrives': True})    


upload_file_team_dr(filename,fold_id)




