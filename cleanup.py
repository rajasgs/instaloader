'''
Created on 

@author: Raja CSP Raman

source:
    ?
'''

import sys
import os

def startpy():

    c_profilename = sys.argv[1]

    dir = c_profilename

    for file in os.listdir(dir):
        if file.endswith('.txt'):
            os.remove(os.path.join(dir, file))
        elif file.endswith('.json.xz'):
            os.remove(os.path.join(dir, file))
        elif file.endswith('.mp4'):
            os.remove(os.path.join(dir, file))
    
    print(f'Cleaned up {dir}')

if __name__ == '__main__':
    startpy()