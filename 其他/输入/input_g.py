#!/usr/bin/env python3
 
import fileinput
 
 
 
with fileinput.input('test.txt') as f_input:
    for line in f_input:
        print(f_input.filename(),f_input.lineno(),line, end='')
  
  
  
 #调用
 #ls | ./fileinput.py
 #./fileinput.py < /etc/passwd