# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 20:54:29 2019

@author: 15037
"""

from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
gauth.SaveCredentialsFile("mycreds.txt")
