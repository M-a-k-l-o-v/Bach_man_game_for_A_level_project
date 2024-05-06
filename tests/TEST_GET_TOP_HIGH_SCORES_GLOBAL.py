from testdata import *
from test_setup import *

def TEST_GET_TOP_HIGH_SCORES_GLOBAL():
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

    top_5_users = testuser1.get_top_high_scores_global()

    check1 = any(user == testuser3.user for user, _ in top_5_users)
    check2 = any(user == testuser4.user for user, _ in top_5_users)
    check3 = any(user == testuser5.user for user, _ in top_5_users)
    check4 = any(user == testuser6.user for user, _ in top_5_users)
    check5 = any(user == testuser7.user for user, _ in top_5_users)
    check6 = any(user == testuser1.user for user, _ in top_5_users)

    confirm_top_5_ranking = check1 and check2 and check3 and check4 and check5
    confirm_not_top_5_ranking = check1 and check2 and check3 and check4 and check6
    if confirm_top_5_ranking and not confirm_not_top_5_ranking: 
        print('TEST GET TOP HIGH SCORES GLOBAL : PASSED')
    elif confirm_top_5_ranking and confirm_not_top_5_ranking: 
        print('TEST GET TOP HIGH SCORES GLOBAL : FAILED')
    else :
        print('test failed: GET TOP HIGH SCORES GLOBAL')




