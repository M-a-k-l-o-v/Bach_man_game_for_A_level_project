import sqlite3
from testdata import *


conn = sqlite3.connect('game_data.db')
cursor = conn.cursor()

cursor.execute(f'DROP TABLE IF EXISTS {table_name2}')
cursor.execute(f'DROP TABLE IF EXISTS {table_name}')

cursor.execute('''CREATE TABLE IF NOT EXISTS test_username_table (
                player_name TEXT PRIMARY KEY,
                password TEXT,
                recovery_token TEXT
                )''')
cursor.execute('''CREATE TABLE IF NOT EXISTS test_scores_table (
                scoreID INTEGER PRIMARY KEY,
                score1 INTEGER,
                score2 INTEGER,
                score3 INTEGER,
                score4 INTEGER,
                score5 INTEGER,
                player_name TEXT,
                FOREIGN KEY (player_name) REFERENCES username_table(player_name)
                )''')
