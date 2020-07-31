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
from pynput.keyboard import Key, Controller
import sqlite3



def main():

    database = "game_times.db"
    exe_names = "games_list.txt"
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    games_list = get_games_list(exe_names)
    print (games_list)
    active_gaming = False

    i = 0

    while i <= 1:
        
        time.sleep(3)
        w = win32.win32gui
        w.GetWindowText(w.GetForegroundWindow())
        pid = win32.win32process.GetWindowThreadProcessId(w.GetForegroundWindow())
        
        current_exe_name = psutil.Process(pid[-1]).name().strip()

        print(active_gaming, current_exe_name)

        if current_exe_name in games_list and active_gaming == False:
            record_game_start(conn, cursor, current_exe_name)
            active_gaming = True
        
        
    
    return


def check_game_times():

    return

def get_games_list(games_path):

    games_file = open(games_path, 'r')
    
    games_list = []
    for line in games_file:
        strip_line = line.strip()
        games_list.append(strip_line)


    return games_list

def pause_game():

    keyboard = Controller()
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)

    return

def record_game_start(conn: sqlite3.Connection, cursor: sqlite3.Cursor, exe_name: str):

    cursor.execute('''insert into gaming values (?, julianday('now'), NULL, NULL);''', (exe_name,))
    conn.commit()


    return

def record_game_end():

    # will also calculate time of game period
    return
main()