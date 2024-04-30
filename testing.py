import sqlite3
from db_manager import *



# testing variables
test_username = 'SISTE'
test_password = 'jeffryDO'
test_username_table = 'test_username_table'
test_scores_table = 'test_scores_table'

# testing database set up
conn = sqlite3.connect('game_data.db')
cursor = conn.cursor()


table_name = 'test_username_table'
cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
table_name2 = 'test_scores_table'
cursor.execute(f'DROP TABLE IF EXISTS {table_name2}')

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




def TEST_INSERT_DETAILS():
    test_login.insert_details()
    details = test_login.user_info_extracts()
    password_check = test_login.verify_password(details[6])
    username_check = test_login.player_exists()
    if username_check and password_check:
        print('TEST INSERT DETAILS : PASSED')
    else:
        print('TEST INSERT DETAILS : FAILED')



test_login = Login(test_username,test_password, test_username_table,test_scores_table)

def TEST_LOGIN():
    test_login.login_process()
    
def TEST_AMEND_SCORE():

def TEST_GET_TOP_HIGH_SCORES_GLOBAL():

def TEST_GET_TOP_HIGH_SCORES_PRIVATE():

def TEST_USER_INFO_EXTRACTS():

def TEST_MAZE_TWO_ACCESS():

def TEST_PLAYER_EXISTS():
    
def TEST_GENERATE_RANDOM_KEY():
    
def TEST_HASH_PASSWORD():

def TEST_VERIFY_PASSWORD_OR_RECOVERY():

def TEST_SEND_RECOVERY_TOKEN():




TEST_INSERT_DETAILS()
TEST_SEND_RECOVERY_TOKEN()
TEST_VERIFY_PASSWORD_OR_RECOVERY()
TEST_HASH_PASSWORD()
TEST_GENERATE_RANDOM_KEY()
TEST_PLAYER_EXISTS()
TEST_MAZE_TWO_ACCESS()
TEST_USER_INFO_EXTRACTS()
TEST_GET_TOP_HIGH_SCORES_PRIVATE()
TEST_GET_TOP_HIGH_SCORES_GLOBAL()
TEST_AMEND_SCORE()
TEST_LOGIN()

close_database_connection()