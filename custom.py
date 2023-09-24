'''
Created on 

@author: Raja CSP Raman

source:
    ?
'''

import sys

def startpy():

    import subprocess

    # content = "instaloader profile carolineplsk --no-videos --no-video-thumbnails --no-metadata-json --no-compress-json"

    c_profilename = sys.argv[1]

    subprocess.run([
        "instaloader", 
        "profile", 
        c_profilename,
        "--no-videos",
        "--no-video-thumbnails",
        "--no-metadata-json",
        "--no-compress-json"
    ]) 
    

if __name__ == '__main__':
    startpy()