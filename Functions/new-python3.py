#!/usr/bin/python3

print("Hellow, World!")

import tarfile
my_tar = tarfile.open('my_tar.tar.gz')
my_tar.extract('hello.txt','./my_folder')
my_tar.close()
## this is an example of calling a shell command
import subprocess
process = subprocess.Popen(['echo', 'More output'],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
stdout, stderr
