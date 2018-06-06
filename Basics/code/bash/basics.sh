#!/bin/bash

# list contents of directory
ls

# current directory
pwd

# go into directory
cd /path/to/directory

# create and remove directories
mkdir dir   # makes directory 'dir'
rmdir dir   # removes directory 'dir' (if empty)
rm -rf dir  # removes directory dir (and all its contents)  BE CAREFUL! THERE IS NO TURNING BACK!

# files manipulation
mv src dst  # move src to dst
cp src dst  # copies src to dst
rm file     # removes file