import os,json,sys, platform, re
from pathlib import Path
from subprocess import check_output
from serpapi import GoogleSearch

api_key_serp =  os.getenv("SERP_API")  
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
#------------------------------------------------------------
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
    basedir = 'C:\\google\\serpapi\\indias\\nature-labs\\search'  
#--------------------------------------------------------------
if not basedir:
    basedir = os.getcwd()
#-----------------------------------------------------------------------------------------------------
mylist = [basedir, 'initialization.py']
initialdirectoryconfig = fullyqualifydirs(mylist)
#------------------------------------------------------------------------------------------------------
getdirectory = removen(check_output([sys.executable, initialdirectoryconfig], universal_newlines=True))
#---------------------------------------------------------------------------------

print(api_key_serp)

#search_query_key = "Google Cloud Services"

search_query_key = sys.argv[1]

if not (search_query_key):
    print (sys.argv[0], 'Search Query missing')
    exit(1)
print (search_query_key)

mylist = [getdirectory, 'google.json']
search_result_output_json = fullyqualifydirs(mylist)

search = GoogleSearch({"q": search_query_key,
"api_key": api_key_serp,
"num" : '100',
"output" : "JSON"
})
result = search.get_dict()
with open(search_result_output_json, 'w') as f:
    json.dump(result, f)