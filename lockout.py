#!/usr/bin/python3

from datetime import datetime
import sys
import schedule
import time

def main(): 
  makeup()
  
def makeup():
  
  current = datetime.now().strftime('%d-%m-%Y')
  #time = datetime.now.strftime('')
  
  #pulls the date contents and stors them in a file
  this_date = open('[insert director path here]')
  
  #pulls the contents of the date.txt file and assigns them to a variabel
  stored_date = this_date.reat().strip()
  
  #compare todays date and date stored in file
  if(current != stored_date):
    print("Dont Lock Computer")
    this_date.seek(0)
    this_date.write(current)
    
  else:
  #lock the computer and set a timer
    lockComp()
  
  
def lockComp():
  print("lock Computer")
  
main()
