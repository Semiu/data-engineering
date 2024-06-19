#!/usr/bin/env bash

# process files
STR=$'1. This is a line\n2. This is a line\n3. This is a line.'
echo "$STR"
echo "$STR" > lines.txt
# print out and sort in reverse order and help in navigating 
cat lines.txt | sort -r | less
cat lines.txt | grep 3

# append to a file
echo "something\n" > append.txt
wc -l append.txt
echo "another thing" >> append.txt
wc -l append.txt

# Throw away stderr - (standard) output error won't be showing
ls -l /wrong/path 2> /dev/null

# Reading file parts
tail -f tail -f /var/log/dpkg.log # keep file opening while working on it
head -n 2 tail -f /var/log/dpkg.log # first two lines
tail -n 2 tail -f /var/log/dpkg.log # last two lines

# Using history
history | less
history | grep tail
!1
!! # to run previous command