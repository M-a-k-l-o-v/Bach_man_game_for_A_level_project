import sqlite3
import pygame
# from ..Game.game import score

# Initialize Pygame
# pygame.init()

# Connect to SQLite database
conn = sqlite3.connect('highscore.sqlite3')
cursor = conn.cursor()

# Create high scores table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS highscores (
                Username TEXT PRIMARY KEY,
                rank INTEGER,
                score INTEGER
                )''')

# Insert a new high score
def insert_high_score(Username, score):
    cursor.execute('INSERT INTO highscores (Username, score) VALUES (?, ?)', (Username, score))
    conn.commit()

# Retrieve top 10 high scores
def get_top_high_scores():
    cursor.execute('SELECT Username, score FROM highscores ORDER BY score DESC LIMIT 5')
    return cursor.fetchall()

# Close the database connection
def close_database_connection():
    conn.close()

# Example usage
insert_high_score('Player1', 100)
insert_high_score('Player2', 150)
print(get_top_high_scores())

# Close the database connection when done
close_database_connection()
