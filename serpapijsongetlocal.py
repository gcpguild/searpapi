"""
Google Engine Search by SerpAPI 
Python : Get the SerpAPI JSON is created by Google search engine.
------------------------------------------------------------------
Project contact: GCP Guild moderator, Kyndryl
Email: Ramamurthy.valavandan@kyndryl.com
Python API for Google Search Engine
Use Case: Creating the Temples List, Description of Temple, Co-ordinates, Distances from major cities in India.

Purpose : 
-----------
Get the SerpAPI JSON 
The JSON is outcome of the Google Search keywords
Download the JSON from SerPAPI for futher processing of JSON parser and 
CSVs generation of Keywords of Temples list in West Bengal and
Another CSV is : Links of Google Search Engine,  "pagination", "Organic Search", "Releated Search"

Keywords : 'Temples West Bengal'

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

Download from Git Hub

https://github.com/NATURE-LABS/temples/blob/main/serpapijsongetlocal.py

How to use
------------
python serpapijsongetlocal.py 

Contact 
--------
Kyndryl GCP Guild Moderator: Ramamurthy V 
Email: ramamurthy.valavandan@kyndryl.com
GCP Contact: gcpguild@gmail.com
Date: June 21, 2022.
Contributors: 42 key members from GCP Guild.

For SerpAPI Key request, please write an email request with an email subject of 'request for SerpApi Key'

Email: ramamurthy.valavandan@kyndryl.com
"""


import json, re, csv, os
from bs4 import BeautifulSoup
from pathlib import Path
from six.moves.urllib.request import urlopen

import pandas as pd

import urllib.request

import numpy as np

import requests
from requests import request
from urllib.error import URLError

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582"
}

def prt(p):

    width = len(p) + 4
    print('┏' + "━"*width + "┓")
    print('┃' + p.center(width) + '┃')
    print('┗' + "━"*width + "┛")

def checkparasegoostutintemple(wbsearchengine):
    try:
        response = requests.get(wbsearchengine)
        response.raise_for_status()
    except URLError as ue:
        pi="\'The Search Engine is not reachable \' :"
        p = ("{} {}".format(pi,wbsearchengine))
        prt(p)
    
        exit(1)
    
    else:
        pi="\'The Search Engine is reachable \' :"
        p = ("{} {}".format(pi,wbsearchengine))
        prt(p)

    

    return response.raise_for_status()


basepath = "C:"
codepath="google"
function = "serpapi"
N="\\"
namefile = "indias"
max_gs = 10 # maximum number of google search in href or urls

def statesutfile(sut):

    indiafilepushtxt = ''
    indiafilepushtxt = ("{}_{}_{}".format(namefile.capitalize(),sut,inputfile_google_json))
    serpapisearchedjsontempledata = ''
    serpapisearchedjsontempledata = ("{}{}{}".format(cre_directory,N,indiafilepushtxt))
    return serpapisearchedjsontempledata

indiatempledatadir = ("{}{}{}{}{}{}{}{}{}".format(basepath,N,codepath,N,function,N,namefile,N,"data"))

#creating directory --- start -- 
datadirgoo = ("{}_{}".format(namefile.capitalize(),"googlengine_temple_States_and_UTs"))

googledataindiastutdir = ("{}{}{}".format(indiatempledatadir,N,datadirgoo))

cre_directory = Path(googledataindiastutdir)
cre_directory.mkdir(parents=True, exist_ok=True)

indiastautfile = ("{}{}{}".format(googledataindiastutdir,N,"Ind_googlengine_states_ut_master.csv"))

path = Path(indiastautfile)


if path.is_file():
    pi="\'India States and UTs data : \' :"
    p = ("{} {}".format(pi,indiastautfile))
    prt(p)
    
else:
    pi="\'Data of States and UTs is missing!\' :"
    p = ("{} {}".format(pi,indiastautfile))
    prt(p)
    pi="\'Execute myindiagenStatesandUTdata.py First !\' :"
    statesutpy = "Get from Git Hub"
    p = ("{} {}".format(pi,statesutpy))
    prt(p)
    pi="\'Download :' :"
    statesutpy = "https://github.com/NATURE-LABS/India/blob/main/myindiagenStatesandUTdata.py"
    p = ("{} {}".format(pi,statesutpy))
    prt(p)
    pi="\'Save myindiagenStatesandUTdata.py \' :"
    statesutpy = "in c:\python\indias"
    p = ("{} {}".format(pi,statesutpy))
    prt(p)
    pi="\'Document :\' :"
    statesutpy = "https://github.com/NATURE-LABS/India/blob/main/Python%20Lab%20India_states_UT.docx"
    p = ("{} {}".format(pi,statesutpy))
    prt(p)
    exit(1)

def referal(serpapisearchedjsontempledata):
    print(serpapisearchedjsontempledata)

#print(indiastautfile)
#remove file if exists
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

#remove_if_exists(removefile = indiastautfile)
df = pd.read_csv(indiastautfile, delimiter=',',
on_bad_lines='skip', 
engine="python"
)

templesget = sorted([list(row) for row in df.values])

sul =  []

for t in templesget:

  #t = [("{}{}{}".format(t[0], " , ", t[1]))]
  
  m = [ x.strip() for x in ''.join(t).strip('[]').split(',') ]
  
  if m not in sul:
      sul.append(m[0])

  else:
        print("Duplicate is removed", t)

for statename in (sul):
    #statename = "West Bengal"
    patternspace = re.compile(r'\s+')
    statename = re.sub(patternspace, '-', statename)
    googledatastunindiadir = ''
    googledatastunindiadir = ("{}{}{}".format(googledataindiastutdir,N,statename))

    #print(googledatastunindiadir)

    cre_directory = Path(googledatastunindiadir)
    cre_directory.mkdir(parents=True, exist_ok=True)

    wbsearchengine = ''
    #wbsearchengine = "https://serpapi.com/searches/705208470e7f131d/62b0af88477c0eea070e70cb.json"
    wbsearchengine = "https://serpapi.com/searches/86d897a66db73848/62b115ac2e7d6bafc2e13610.json"
    inputfile_google_json = ''
    inputfile_google_json = re.sub(r'^.+/([^/]+)$', r'\1', wbsearchengine)

    
    check_serpapi_google_json = checkparasegoostutintemple(wbsearchengine)

    sepapi_json = ("{}_{}_{}".format(namefile.capitalize(),statename,inputfile_google_json))

    indiastautjsonfile = ''
    indiastautjsonfile = ("{}{}{}".format(googledatastunindiadir,N,sepapi_json))

    #print(indiastautjsonfile)

    indiafilepushtxt = ''
    indiafilepushtxt = ("{}_{}_{}".format(namefile.capitalize(),statename,inputfile_google_json))
    serpapisearchedjsontempledata = ''
    serpapisearchedjsontempledata = ("{}{}{}".format(cre_directory,N,indiafilepushtxt))

    #serpapisearchedjsontempledata = statesutfile(statename)
    sf = Path(serpapisearchedjsontempledata)
    if sf.is_file():
      pi= ("{}{}".format("State or UT name : ", statename))
      p = ("{}".format(pi))
      prt(p)

      pi="\'Google data of temples in state or UT for :\' :"
      p = ("{} {}".format(pi,statename))
      prt(p)
      p = ("{}".format(serpapisearchedjsontempledata))
      prt(p)

      readdata = referal(serpapisearchedjsontempledata)

    else:
      pi="\'Downloading Temples data of state or UT :\' :"
      p = ("{} {}".format(pi,statename))
      prt(p)
      pi ="JSON from SerpAPI.. "
      p = ("{} {}".format(pi, serpapisearchedjsontempledata))
      prt(p)
      headers = {"api_key": os.getenv("API_KEY")}
      file_stream = requests.get(wbsearchengine, stream=True)
      resp = request(method="GET",url=wbsearchengine, headers=headers)
      #with open(serpapisearchedjsontempledata, 'wb') as local_file:
      #  for data in file_stream:
      #    serpapisearchedjsontempledata.write(data)
      with open(serpapisearchedjsontempledata, "w") as my_file:
        my_file.write(resp.text)