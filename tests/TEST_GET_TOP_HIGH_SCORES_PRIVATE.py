from testdata import *
from test_setup import *

def TEST_GET_TOP_HIGH_SCORES_PRIVATE():
    
    highscore = testuser1.get_top_high_scores_private()
    test1 = 780 in highscore
    test2 = 650 in highscore
    test3 = 540 in highscore
    test4 = 350 in highscore
    test5 = 150 in highscore

    check = test1 and test2 and test3 and test4 and test5
    if check:
        print('TEST GET TOP HIGH SCORES PRIVATE : PASSED')
    elif not check:
        print('TEST GET TOP HIGH SCORES PRIVATE : FAILED')
    else:
        print('test failed: GET TOP HIGH SCORES PRIVATE')


    