# Bach-man

A Pac-Man-style maze game in Python, built for my A-level Computer Science project (2023–24). It has player accounts, a high-score table, and a test suite for the database layer.

## What it does

- **Game** (pygame): two maze levels, four ghosts with their own targeting rules, power pellets that make ghosts vulnerable for a few seconds, three lives.
- **Accounts** (SQLite + bcrypt): players sign up and log in; passwords and recovery tokens are stored as bcrypt hashes, never in plain text.
- **Password recovery**: a random recovery token is generated and emailed to the player over SMTP.
- **High scores**: each player keeps their best five scores; a global table shows the top five players.

## Layout

```
__main__.py        game loop, player and ghost logic
db_manager.py      accounts, hashing, recovery email, scores (SQLite)
Game/              maze layouts and drawing
Home/              home screen, buttons, login and high-score pop-ups
assets/            sprites and screen art
tests/             one file per database function
main_test.py       runs every test against separate test tables
```

## Run it

```bash
pip install pygame bcrypt
python __main__.py
```

Run from the repo root: the game loads `assets/` by relative path. `game_data.db` is created on first run.

Password recovery email needs an SMTP account. Set these before running (for Gmail, use an app password):

```bash
export BACHMAN_SMTP_USER="you@example.com"
export BACHMAN_SMTP_PASSWORD="your-app-password"
```

## Tests

```bash
python main_test.py
```

The tests use their own `test_username_table` and `test_scores_table`, and clear them afterwards. They print PASSED or FAILED per function. The recovery-email test only passes if the SMTP variables above are set.

## Limitations

- The tests are print-based scripts, not pytest, so a failure doesn't stop the run or return a non-zero exit code.
- Most game logic sits in one 1,300-line file with module-level state.
- An earlier version of this repo had the email password hard-coded in `db_manager.py`. It now reads it from the environment.

## Licence

MIT
