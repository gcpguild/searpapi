"""
Google Engine Search by SerpAPI 
Python : Get the SerpAPI JSON is created by Google search engine.
------------------------------------------------------------------
Project contact: Google Cloud Guild moderator, Kyndryl
Email: gcpguild@gmail.com
Python API for Google Search Engine
Keywords : 'Google Cloud Services'
Project ID : Nature Labs
Use Case: Creating the keywords.

Purpose : 
-----------
Get the SerpAPI JSON 
The JSON is outcome of the Google Search keywords
Download the JSON from SerPAPI for futher processing of JSON parser and 
CSVs generation of Keywords of Google Cloud Services and
Another CSV is : Links of Google Search Engine,  "pagination", "Organic Search", "Releated Search"

After connecting to Google Search Engine API the JSON is generated
This program is used to connect Google Search API (SerpAPI) 
Download the searched information which is saved in the JSON file based on the Google Search Engine.
Create the necessary folders in local and download and save JSON for locally parse the search key.
---------------------------------------------------------------------------------------------------
SerpAPI Sponsorship
Google Engine is sponsored by SerpApi. SerApi has sponsored 40,000 credits for Google search
with the API Key for scraping Google and other search engines.

On behalf of Google Engine, researchers, we express our gratitude to SerpAPI LLC, for provisioning
their sponsorship SerpAPI's sponsorship has helped us make our research and social work contribution 
for speaking out greater audience.
With the advent of SerpAPI, Google Engine has addressed our research work on Temples in India 
with the experience of a blazingly fast, super easy to use, and data-rich API in 
Google Cloud Platform Search Engine on Big Query for Research in Google Cloud Engine. 
With SerpAPI, Google Engine will be helping the student community on projects.

About SerpApi
-------------
SERP API is a real-time API to access Google search results. 
It solves the issues of having to rent proxies, solving captchas, and JSON parsing.

Design and developed by :
-------------------------
Kyndryl Solutions Private Limited
Project Team : Google Cloud Platform - Guild.
Lab : Google Engine @ SerApi, LLC.
Project ID : Nature Labs
Directory  : C:\google\serpapi\indias\nature-labs\search
---------
Download from Git Hub

https://github.com/gcpguild/searpapi

How to use
------------
python serpapijsongetlocal.py 

Contact 
--------
Kyndryl GCP Guild Moderator: Ramamurthy V 
Google Cloud Contact: gcpguild@gmail.com (For Developers)
For Project Internal for Kyndryl : Google Guild
Date: Auu 09, 2022.
Contributors: 42 key members from Google Guild.

For SerpAPI Key request, please write an email request with an email subject of 'request for SerpApi Key'

Email: gcpguild@gmail.com
"""
#----------------------------------------------------------------------
wbsearchengine = "https://serpapi.com/searches/d7089ff6b5503824/62f1c629c7ad41d8921a6c6c.json"
namefile = 'google'
servicename = 'services'
import json, re, csv, os, platform, sys
from bs4 import BeautifulSoup
from pathlib import Path
import pandas as pd

import urllib.request
from subprocess import check_output
import requests
from requests import request
from urllib.error import URLError

#----------------------------------------------------------
def removen(string):
    for m in ('\n', '\r'):
        clean_string = re.sub(m, '', string)
        clean_string = clean_string.replace(m, '')
        clean_string = clean_string.rstrip()
        clean_string = clean_string.strip(m)
        clean_string = re.sub(m,' ', clean_string)
        mymano = ''
        for x in clean_string:
            mymano += ''+ x
        return mymano
#---------------------------------------------------
myos = platform.system()
#---------------------------------------------------
def fullyqualifydirs(mylist):
    mydircode = N.join(mylist)
    return mydircode
#-----------------------------------------------------
if (myos == "Linux" or myos == "linux2"):
    # linux
    N="/"
    homedirectory = str(Path.home())
    print(homedirectory)
    
    mylist = [ homedirectory, 'serpapi/python/app/nature-labs/google-cloud' ]
    basedir = fullyqualifydirs(mylist)
    print(basedir)
elif myos == "win32" or myos == "Windows":
    # Windows 
    N="\\"    
    basedir = 'C:\\serpapi\\python\\app\\nature-labs\\google-cloud'  
#--------------------------------------------------------------
if not basedir:
    basedir = os.getcwd()
#-----------------------------------------------------------------------------------------------------
mylist = [basedir, 'initialization.py']
initialdirectoryconfig = fullyqualifydirs(mylist)
#------------------------------------------------------------------------------------------------------
getdirectory = removen(check_output([sys.executable, initialdirectoryconfig], universal_newlines=True))
#-------------------------------------------------------------------------------------------------------
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582"
}
#-------------------------------------------------------------------------------------------------------
def prt(p):

    width = len(p) + 4
    print('┏' + "━"*width + "┓")
    print('┃' + p.center(width) + '┃')
    print('┗' + "━"*width + "┛")
#-------------------------------------------------------------------------------------------------------
def remove_if_exists(removefile):
    try:
        if os.path.exists(removefile):
            os.remove(removefile)
            #print ("File removed successfully", removefile)
            pi="\'File removed successfully \' :"
            p = ("{}{}".format(pi,removefile))
            prt(p)
    except:
        print("Error while deleting file ", removefile)


inputfile_google_json = ''
inputfile_google_json = re.sub(r'^.+/([^/]+)$', r'\1', wbsearchengine)

sepapi_json = ("{}_{}_{}".format(namefile.capitalize(),servicename,inputfile_google_json))


mylist = [getdirectory, sepapi_json]
download_json = fullyqualifydirs(mylist)

headers = {"api_key": os.getenv("SERP_API")}
file_stream = requests.get(wbsearchengine, stream=True)
resp = request(method="GET",url=wbsearchengine, headers=headers)
 
with open(download_json, "w", encoding="utf-8") as my_file:
    my_file.write(resp.text)