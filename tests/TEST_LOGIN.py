from testdata import *
from test_setup import *

def TEST_LOGIN():
   
    testuser2.login_process()
    registered_player = testuser2.player_exists()
    if registered_player:
        print('TEST USER REGISTRATION : PASSED')
    elif not registered_player:
        print('TEST USER REGISTRATION : FAILED')
    

    testuser2.login_process()
    if testuser2.login:
        print('TEST USER LOGIN : PASSED')
    elif not testuser2.login:
        print('TEST USER LOGIN : FAILED')
    else:
        print('test failed: USER LOGIN')
