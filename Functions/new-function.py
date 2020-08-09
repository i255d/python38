#!/usr/bin/python3
#  Type wsl to get Ubuntu;  wsl --set-default-version 2
import subprocess
import tarfile
#first function
def kernel_func():
    uname = "uname"
    uname_arg = "-a"
    print("Collecting information about kernel with %s command:\n" % uname)
    subprocess.run([uname, uname_arg])

#second function
def disk_func():
    diskspace = "df"
    diskspace_arg = "-h"
    print("Gathering hard disk information using %s command:\n" % diskspace)
    subprocess.run([diskspace, diskspace_arg])

#create a function main wich will call the two functions
def main():
    kernel_func()
    disk_func()


for i in range(1):
    main()