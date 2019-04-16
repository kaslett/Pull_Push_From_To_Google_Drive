# Steps to begin pulling files and pushing to Google Drive using python 2 and python 3

## Below are the steps: through each process. These are also located in the README file

### Process 1: Downloading from Google Drive.

#### Step 1: Visit the url https://developers.google.com/drive/api/v3/quickstart/python and follow the steps to download your own credentials.json file
* Click on the button: "Enable The Driver API"
* In the ensuing window click on the button: "DOWNLOAD CLIENT CONFIGURATION"
* This will download a file: "credentials.json"
* You will need to use this file to create the "token.pickle" that will give you the ability to download files from google.
* Open up a bash terminal. Enter into the command line: pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

#### Step 2: Open and then run python script: Get_proper_pickle_file.py
Note 1: Open the code in your preffered editor (I prefer spyder)
Note 2: Remember that if you create this pickled file in python 3 you can only use this pickle file in the future in python 3. Vice-verse for python 2.
* Adjust the code so that this script ensure that you have access to the file: "credentials.json" through a proper path. Set the working directory. Save the code.
* Run this script in the same environment that you installed the google API library. Once running, it will open an internet browser and ask you to log in to your google account. Log into the google account that gives you access to the drives/folders you want to push and pull from.
* This will give you a key that will give you access to every drive that your account can access. That key will be located in the pickled file: "token.pickle".

#### Step 3: Look through and run either the python script google_download_template_py2.py (in python2) or google_download_template_py3.py (in python3)
Note: Ensure that you have access to the file that you created previously: "token.pickle".

### Process 2: Uploading to Google Drive.

#### Step 1: Log in to your google account and visit the url: https://console.developers.google.com/apis/
* Click on the section on the left: Credentials
* Click on the Create Credentials button: "OAuth client ID".
* Click on Application Type: Other and then name it what you wish.
* This places at a screen with the client ID and secret ID, you can click OK.
* Click on that client ID in the list
* On that screen click the "DOWNLOAD JSON" button. This will download your client_secrets.JSON that you will need in the next step.
* pip install PyDrive

#### Step 2: Run the script "Get_Credentials_pydrive.py"
Note 1: Make sure you have access to the "client_secrets.JSON" file that you just created
This will create the my_creds.txt file that you will use in the next step.

#### Step 3: Look through and run the script "google_upload_template_py2_py3.py"
Note: Ensure that you have access to the "my_creds.txt" file that you just created
