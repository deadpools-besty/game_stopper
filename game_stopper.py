''' 
python application that runs in the background to track the amount of time i've spent in games for
the day week or month to limit my play time once school starts 

future: could auto pause application once time limit is reached

could store data using a sql database -  different tables for each game, and in those tables time played
is listed and then there is a table for overall game sessions for the week
'''

import win32.win32gui
import win32.win32process
import time
import os
import subprocess
import psutil

i = 0

while i <= 1:
    time.sleep(3)
    w = win32.win32gui
    w.GetWindowText(w.GetForegroundWindow())
    pid = win32.win32process.GetWindowThreadProcessId(w.GetForegroundWindow())
    print(psutil.Process(pid[-1]).name())