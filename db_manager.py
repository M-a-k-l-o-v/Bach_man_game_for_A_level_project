import sqlite3
import json
import bcrypt
import secrets
import string
import smtplib
from email.mime.text import MIMEText

username_table  = 'username_table'
scores_table = 'scores_table'
email_error_message =  'sorry, email failed to send'

conn = sqlite3.connect('game_data.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS username_table (
                player_name TEXT PRIMARY KEY,
                password TEXT,
                recovery_token TEXT
                )''')
cursor.execute('''CREATE TABLE IF NOT EXISTS scores_table (
                scoreID INTEGER PRIMARY KEY,
                score1 INTEGER,
                score2 INTEGER,
                score3 INTEGER,
                score4 INTEGER,
                score5 INTEGER,
                player_name TEXT,
                FOREIGN KEY (player_name) REFERENCES username_table(player_name)
                )''')

class Login:
    def __init__(self, username, password, username_table, scores_table):
        self.login = False
        self.username_table = username_table
        self.scores_table = scores_table
        self.user = username
        self.password = password
        # self.email = self.additional_info[2]
        self.user_exist = self.player_exists()
        #self.new_user_score = [0,0,0,0,0]
        self.forgot_password = False
        #self.game_start = False
    
    def login_process(self):
        if self.user_exist:
            self.additional_info = self.user_info_extracts()
            print(self.additional_info)
            self.hashed_password =  self.additional_info[5]
            self.hashed_recovery_token = self.additional_info[6]
            password_verification = self.verify_password(self.hashed_password)
            if password_verification:
                self.login = True
                if self.login:
                    user_score = self.get_top_high_scores_private()
                    user_access =  self.maze_two_access()           
                return self.login, user_score, user_access
            elif not password_verification and self.forgot_password:
                   self.recovery_token = self.get_recovery_token()
                   if self.verify_recovery_token(self.hashed_recovery_token):
                        self.login = True
                        if self.login:
                            user_score = self.get_top_high_scores_private()
                            user_access =  self.maze_two_access()
                   return self.login, user_score, user_access
            else:
               retry_message = print('Wrong password, try again.')
               return retry_message
            
        else: 
            self.email = self.get_email()
            details = self.insert_details()
            print(details)
            self.send_recovery_token(details)
            self.login = True
            if self.login:
                user_score = self.get_top_high_scores_private()
                user_access =  self.maze_two_access()
            return self.login, user_score, user_access

    def player_exists(self):
        cursor.execute('SELECT COUNT(*) FROM {username_table} WHERE player_name = ?'.format(username_table=self.username_table), (self.user,))
        count = cursor.fetchone()[0]
        print('player_exists runs')
        return count > 0

    def user_info_extracts(self):
        cursor.execute('''
            SELECT s.score1, s.score2, s.score3, s.score4, s.score5, u.password, u.recovery_token 
            FROM {username_table} u
            JOIN {scores_table} s ON u.player_name = s.player_name
            WHERE u.player_name = ?
        '''.format(scores_table=self.scores_table, username_table=self.username_table), (self.user,))
        rows = cursor.fetchall()
        additional_info = []
        for row in rows:
            user_scores = [int(score) for score in row[:5]] 
            hashed_password = row[5]
            user_recovery_token = row[6]
            
            additional_info.extend(user_scores)
            additional_info.append(hashed_password)
            additional_info.append(user_recovery_token)
        print('user_info_extracts runs')
        return additional_info

    def maze_two_access(self):
        sorted_rows = self.get_top_high_scores_global()
        top_5 = []
        for row in sorted_rows:
            top_5.append(row[0])
            print('top 5 players : '  + str(top_5))
        is_in_top_5 = self.user in top_5
        if is_in_top_5:  
            second_level_access = True
        else:
            second_level_access = False
        print('maze_two_access runs')
        print(second_level_access)
        return second_level_access

    def get_email(self):
        email = input("please enter your email:   ")
        return email

    def get_recovery_token():
        recovery_token = input("enter recovery token :  ")
        print('get_recovery_token runs')
        return recovery_token

    def generate_random_key(self, length=12):
            key = string.ascii_letters + string.digits
            print('generate_random_key runs')
            return ''.join(secrets.choice(key) for _ in range(length))
        
    def insert_details(self):
        scores = [0, 0, 0, 0, 0]

        recovery_token = self.generate_random_key()
        hashed_password = str(self.hash_password())
        hashed_recovery_token = str(self.hash_password())

        hashed_recovery_token_json = json.dumps(hashed_recovery_token)
        hashed_password_json = json.dumps(hashed_password)
        #scores_json = json.dumps(scores)

        cursor.execute('INSERT INTO {username_table} (player_name, password, recovery_token) VALUES (?, ?, ?)'.format(username_table=self.username_table),
                    (self.user, hashed_password_json, hashed_recovery_token_json))
        #player_id = cursor.lastrowid
        cursor.execute('INSERT INTO {scores_table} (player_name, score1, score2, score3, score4, score5) VALUES (?, ?, ?, ?, ?, ?)'.format(scores_table=self.scores_table),
                    (self.user, *scores))
        conn.commit()
        print('insert_details runs')
        return recovery_token
        
    def get_top_high_scores_global(self):
        cursor.execute('''
            SELECT {username_table}.player_name, MAX(score1) AS top_score
            FROM {username_table}
            LEFT JOIN {scores_table} ON {username_table}.player_name = {scores_table}.player_name
            WHERE score1 IS NOT NULL
            GROUP BY {username_table}.player_name
            ORDER BY top_score DESC
            LIMIT 5
        '''.format(scores_table=self.scores_table, username_table=self.username_table))
        rows = cursor.fetchall()
        print('get_top_high_scores_global runs')
        return rows

    def get_top_high_scores_private(self):
        cursor.execute('''SELECT s.player_name, s.score1, s.score2, s.score3, s.score4, s.score5
                        FROM {scores_table} s
                        JOIN {username_table} u ON s.player_name = u.player_name
                        WHERE u.player_name = ?'''.format(scores_table=self.scores_table, username_table=self.username_table), (self.user,))
        row = cursor.fetchone()
        if row:
            self.user, score1, score2, score3, score4, score5 = row
            user_top_scores = [score1, score2, score3, score4, score5]
        else:
            user_top_scores = None
        print('get_top_high_scores_private runs')
        return user_top_scores

    def amend_score(self, new_scores):
        sorted_new_scores = sorted(new_scores, reverse=True)
        scores_json = json.dumps(sorted_new_scores)  # Serialize new scores to JSON string
        cursor.execute('UPDATE {} SET scores = ? WHERE player_name = ?'.format(self.database), (scores_json, self.user))
        conn.commit()

    def hash_password(self):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(self.password.encode('utf-8'), salt)
        print('hash_password runs')
        return hashed_password

    def verify_password(self, hashed_password):
        hash_password_cleaned = hashed_password[3:-2]
        byte_string = bytes(hash_password_cleaned, 'utf-8')
        correct_password = bcrypt.checkpw(self.password.encode('utf-8'), byte_string)
        print('verify_password runs')
        return correct_password

    def verify_recovery_token(self, hashed_password):
        hash_password_cleaned = hashed_password[3:-2]
        byte_string = bytes(hash_password_cleaned, 'utf-8')
        correct_password = bcrypt.checkpw(self.recovery_token.encode('utf-8'), byte_string)
        print('verify_password runs')
        return correct_password

    def send_recovery_token(self, message):
        sender_email = '911bachman911@gmail.com'
        sender_password = 'zpbv mywa qzlq furx'
        smtp_server = 'smtp.gmail.com'
        smtp_port = 465

        msg = MIMEText(message)
        msg['Subject'] = 'Bachman recovery token'
        msg['From'] = sender_email
        msg['To'] = self.email

        try:
            with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                print("waiting to login")
                server.login(sender_email, sender_password)
                print("waiting to send")
                server.sendmail(sender_email,self.email,msg.as_string())
            print("Text message sent successfully!")
        except Exception as error:
            print("Error sending text message:", error)

def close_database_connection():
    conn.close()