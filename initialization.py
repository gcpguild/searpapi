listimports =  [       
                        'uuid',
                        'psutil',
                        'ipaddress'
]

prepippkgs = [ 'wheel', 'google-search-results', 'platform', 'logging', 'sys','json','csv', 'os', 'socket', 're',  'pkg_resources']

fromimp_dict_obj = { 'pandas'       :   'pd',  
                    'pathlib'       :   'Path',
                    'datetime'      :   'datetime'
                            
}

cpu_dict_obj = { 'py-cpuinfo'   :   'cpuinfo' }

#---------------------------------------
import pkg_resources, re, os, sys, csv, json, socket, platform
from pathlib import Path
from itertools import filterfalse
from serpapi import GoogleSearch

from subprocess import check_output

installedmodules = []

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

installed_packages_list = sorted([(i.key) for i in pkg_resources.working_set])
#-----------------------------------------------
def tryingmodule(me, modulename):
    try:    
        exec(me)
    except ImportError as e:
        os.system('pip3 install ' + modulename)
#----------------------------------------------
requiredimportmodules = []
for impmod, aliasmod in fromimp_dict_obj.items():
    requiredimportmodules.append(impmod)
    if (impmod == 'pandas'):
        me = ("{} {} {} {}".format('import', impmod, 'as', aliasmod ))
    else:
        me = ("{} {} {} {}".format('from', impmod, 'import', aliasmod ))

    tryingmodule(me = me, modulename = impmod)


for e in listimports:
    requiredimportmodules.append(e)
    me = ("{} {}".format('import', e))

    tryingmodule(me = me, modulename = e)

for cpukey, cpuvalue in cpu_dict_obj.items():
    requiredimportmodules.append(cpukey)
    me = ("{} {}".format('import', cpuvalue ))
    tryingmodule(me = me, modulename = cpukey)

missingmodules = []

alreadyinstalled = []
for r in requiredimportmodules:
    if r in set(installed_packages_list):
        alreadyinstalled.append(r)
    else:
        missingmodules.append(r)

for f in list(filterfalse(set(installed_packages_list).__contains__, requiredimportmodules)):
    install_missing_packages = removen(f)
    os.system('pip3 install ' + install_missing_packages)
#-----------------------------------------------------
def fullyqualifydirs(mylist):
    mydircode = N.join(mylist)
    return mydircode
#------------------------------------------------------------------
myos = platform.system()
#-----------------------------------------------------
if (myos == "Linux" or myos == "linux2"):
    # linux
    N="/"
    homedirectory = str(Path.home())

    mylist = [ homedirectory, 'serpapi/python/app/nature-labs/google-cloud' ]
    basepath = fullyqualifydirs(mylist)
elif myos == "win32" or myos == "Windows":
    # Windows 
    N="\\"    
    basepath = 'C:\\serpapi\\python\\app\\nature-labs\\google-cloud'  
#-----------------------------------------------------------------
def mkingdirs(givenlist):
    mymanog = ''.join(givenlist)
    mk_dir = Path(mymanog)
    mk_dir.mkdir(parents=True, exist_ok=True)
    return mk_dir
#-------------------------------------------------------------------
givenlist = [basepath, 'data' ]
workingdir = mkingdirs(basepath)
os.chdir(workingdir)
#-------------------------------------------------------------------
cwd = os.getcwd()
myd = cwd.split(N)
#-----------------------------------------------------------------
def getstringswitch(check_string_name):
    dict={
           's0' : myd[0], 
           's1' : myd[1], 
           's2' : myd[2], 
           's3' : myd[3],
           's4' : myd[4],
           's5' : myd[5],
           'd'  : 'data',
           'max_gs' : 10
          }
    return dict.get(check_string_name, cwd)

givenlist = [basepath,N,getstringswitch(check_string_name = 'd')]

mkdirlist = mkingdirs(givenlist)

print (mkdirlist)