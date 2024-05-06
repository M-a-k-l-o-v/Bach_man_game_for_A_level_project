from testdata import *
from test_setup import *

def TEST_MAZE_TWO_ACCESS():
    testuser1.login_process()
    testuser1.amend_score(150)
    testuser3.login_process()
    testuser3.amend_score(350)
    testuser4.login_process()
    testuser4.amend_score(450)
    testuser5.login_process()
    testuser5.amend_score(550)
    testuser6.login_process()
    testuser6.amend_score(650)
    testuser7.login_process()
    testuser7.amend_score(750)


    check1 = testuser3.maze_two_access()
    check2 = testuser4.maze_two_access()
    check3 = testuser5.maze_two_access()
    check4 = testuser6.maze_two_access()
    check5 = testuser7.maze_two_access()
    check6 = testuser1.maze_two_access()

    confirm_top_5_access_maze = check1 and check2 and check3 and check4 and check5
    confirm_not_top_5_access_maze = check1 and check2 and check3 and check4 and check5 and check6
    if confirm_top_5_access_maze and not confirm_not_top_5_access_maze: 
        print('TEST MAZE TWO ACCESS : PASSED')
    elif confirm_top_5_access_maze and confirm_not_top_5_access_maze: 
        print('TEST MAZE TWO ACCESS : FAILED')
    else:
        print('test failed: MAZE TWO ACCESS')

