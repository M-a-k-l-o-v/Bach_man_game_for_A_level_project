from pgu import gui

def login_popup():
    app = gui.Desktop()
    app.connect(gui.QUIT, app.quit, None)

    container = gui.Container(width=650, height=650)
    table = gui.Table()

    lbl_username = gui.Label("Username:")
    txt_username = gui.Input(width=150)
    lbl_password = gui.Label("Password:")
    txt_password = gui.Input(width=150, password=True)

    def login_action():
        global username_entered, password_entered
        username_entered = txt_username.value
        password_entered = txt_password.value
        app.quit()

    btn_login = gui.Button("Login")
    btn_login.connect(gui.CLICK, login_action)

    table.td(gui.Spacer(width=150, height=50)) 
    table.tr()
    table.td(gui.Spacer(width=150, height=50)) 
    table.tr()
    table.td(lbl_username)
    table.td(txt_username)
    table.tr()
    table.td(gui.Spacer(width=150, height=10))  # Empty space line
    table.tr()
    table.td(lbl_password)
    table.td(txt_password)
    table.tr()
    table.td(gui.Spacer(width=150, height=10))  # Empty space line
    table.tr()
    table.td(btn_login, colspan=2)

    container.add(table, 0, 0)
    app.run(container)

    username = txt_username.value
    password = txt_password.value


    return username, password

def get_email_popup():
    app = gui.Desktop()
    app.connect(gui.QUIT, app.quit, None)

    container = gui.Container(width=650, height=650)
    table = gui.Table()

    lbl_Email = gui.Label("please enter an email for password recovery token:")
    lbl_Email.style.margin_left = 20  
    lbl_Email.style.margin_right = 20 
    lbl_Email.style.margin_top = 20  
    lbl_Email.style.margin_bottom = 20 
    txt_Email = gui.Input(width=200)

    def login_action():
        global Email_entered
        Email_entered = txt_Email.value
        app.quit()

    btn_login = gui.Button("Login")
    btn_login.connect(gui.CLICK, login_action)

    
    table.td(gui.Spacer(width=150, height=50)) 
    table.tr()
    table.td(lbl_Email)
    table.tr()
    table.td(txt_Email)
    table.tr()
    table.td(gui.Spacer(width=150, height=10)) 
    table.tr()
    table.td(gui.Spacer(width=150, height=10))
    table.tr()
    table.td(btn_login, colspan=1)

    container.add(table, 0, 0)
    app.run(container)

    Email = Email_entered
    return Email

def wrong_password_popup(message):
    app = gui.Desktop()
    app.connect(gui.QUIT, app.quit, None)

    container = gui.Container(width=650, height=650)
    table = gui.Table()

    lbl_try_again = gui.Label(message)
    lbl_try_again.style.margin_left = 20  
    lbl_try_again.style.margin_right = 20 
    lbl_try_again.style.margin_top = 20  
    lbl_try_again.style.margin_bottom = 20 

    def try_again_action():
        app.quit()
        login_popup()

    btn_try_again = gui.Button("try again")
    btn_try_again.connect(gui.CLICK, try_again_action)

    
    table.td(gui.Spacer(width=150, height=50)) 
    table.tr()
    table.td(lbl_try_again)
    table.tr()
    table.td(gui.Spacer(width=150, height=10))
    table.tr()
    table.td(btn_try_again, colspan=1)

    container.add(table, 0, 0)
    app.run(container)

def highscore_popup(top_5_global):

    app = gui.Desktop()
    app.connect(gui.QUIT, app.quit, None)
    leaderboard= top_5_global
    closed = False
    switch_to_scoreboard = False
    
    container = gui.Container(width=650, height=650)
    table = gui.Table()

    header = gui.Label('Leaderboard')
    lbl_first = gui.Label(str(leaderboard[0]))
    lbl_second = gui.Label(str(leaderboard[1]))
    lbl_third = gui.Label(str(leaderboard[2]))
    lbl_fourth = gui.Label(str(leaderboard[3]))
    lbl_fifth = gui.Label(str(leaderboard[4]))

    def close_action():
        nonlocal closed
        closed = True
        app.quit()

    def scoreboard_action():
        nonlocal switch_to_scoreboard
        switch_to_scoreboard = True
        app.quit()

    btn_close = gui.Button("close")
    btn_close.connect(gui.CLICK, close_action)

    btn_scoreboard = gui.Button("scoreboard")
    btn_scoreboard.connect(gui.CLICK, scoreboard_action)

    table.td(gui.Spacer(width=150, height=50)) 
    table.tr()
    table.td(header)
    table.tr()
    table.td(gui.Spacer(width=150, height=50)) 
    table.tr()
    table.td(lbl_first)
    table.tr()
    table.td(gui.Spacer(width=150, height=50)) 
    table.tr()
    table.td(lbl_second)
    table.tr()
    table.td(gui.Spacer(width=150, height=50)) 
    table.tr()
    table.td(lbl_third)
    table.tr()
    table.td(gui.Spacer(width=150, height=10))  
    table.tr()
    table.td(lbl_fourth)
    table.tr()
    table.td(gui.Spacer(width=150, height=10))
    table.tr()
    table.td(lbl_fifth)
    table.tr()
    table.td(gui.Spacer(width=150, height=10))  
    table.tr()
    table.td(btn_scoreboard, colspan=2)
    table.tr()
    table.td(gui.Spacer(width=150, height=10))  
    table.tr()
    table.td(btn_close, colspan=2)

    container.add(table, 0, 0)
    app.run(container)

    return closed, switch_to_scoreboard

def highscore_personal_popup(top_5_private):
    app = gui.Desktop()
    app.connect(gui.QUIT, app.quit)
    scoreboard= top_5_private
    closed = False
    switch_to_leaderboard = False
    
    container = gui.Container(width=650, height=650)
    table = gui.Table()

    header = gui.Label('Your top scores are')
    lbl_first = gui.Label(str(scoreboard[0]))
    lbl_second = gui.Label(str(scoreboard[1]))
    lbl_third = gui.Label(str(scoreboard[2]))
    lbl_fourth = gui.Label(str(scoreboard[3]))
    lbl_fifth = gui.Label(str(scoreboard[4]))


    def close_action():
        nonlocal closed
        closed = True
        app.quit()

    def leaderboard_action():
        nonlocal switch_to_leaderboard
        switch_to_leaderboard = True
        app.quit()

    btn_leaderboard = gui.Button("leaderboard")
    btn_leaderboard.connect(gui.CLICK, leaderboard_action)

    btn_close = gui.Button("close")
    btn_close.connect(gui.CLICK, close_action)

    table.td(gui.Spacer(width=150, height=50)) 
    table.tr()
    table.td(header)
    table.tr()
    table.td(gui.Spacer(width=150, height=50)) 
    table.tr()
    table.td(lbl_first)
    table.tr()
    table.td(gui.Spacer(width=150, height=50)) 
    table.tr()
    table.td(lbl_second)
    table.tr()
    table.td(gui.Spacer(width=150, height=50)) 
    table.tr()
    table.td(lbl_third)
    table.tr()
    table.td(gui.Spacer(width=150, height=10))  
    table.tr()
    table.td(lbl_fourth)
    table.tr()
    table.td(gui.Spacer(width=150, height=10))
    table.tr()
    table.td(lbl_fifth)
    table.tr()
    table.td(gui.Spacer(width=150, height=10))  
    table.tr()
    table.td(btn_leaderboard, colspan=2)
    table.tr()
    table.td(gui.Spacer(width=150, height=10))  
    table.tr()
    table.td(btn_close, colspan=2)

    container.add(table, 0, 0)
    app.run(container)

    return closed, switch_to_leaderboard

