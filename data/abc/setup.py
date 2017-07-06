#-*-coding: UTF-8-*-
from distutils.core import setup
import py2exe
import chardet
# Powered by ***
setup(
    options =  {"py2exe" :
        {"compressed" : 1,
         "optimize" : 2,
         "bundle_files" : 3,
         "dll_excludes": [ "MSVCP90.dll", "mswsock.dll", "powrprof.dll","w9xpopen.exe"]
         }

         },
    description = "just for test",
    zipfile=None,
    windows=[{"script": "minesweeper.py","icon_resources":[(1,u"myicon.ico")]}])
options = {"py2exe" :
    {"compressed" : 1,
     "optimize" : 2,
     "bundle_files" : 2,
     "dll_excludes": [ "MSVCP90.dll", "mswsock.dll", "powrprof.dll","w9xpopen.exe"]
     }

     }
