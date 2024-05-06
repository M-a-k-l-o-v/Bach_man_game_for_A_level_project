from testdata import *
from test_setup import *

def TEST_AMEND_SCORE():
    testuser1.amend_score(350)
    testuser1.amend_score(650)
    testuser1.amend_score(540)
    testuser1.amend_score(780)
    testuser1.amend_score(110)

    highscore = testuser1.get_top_high_scores_private()
    test1 = 110 in highscore
    test2 = 150 in highscore
    test3 = 650 in highscore

    check = (not test1) and test2 and test3
    if check:
        print('TEST AMMEND SCORE, ACCEPTING ONLY ABOVE MINIMUM SCORE : PASSED')
    elif not check:
        print('TEST AMMEND SCORE, ACCEPTING ONLY ABOVE MINIMUM SCORE : FAILED')
    else:
        print('test failed: AMMEND SCORE')


