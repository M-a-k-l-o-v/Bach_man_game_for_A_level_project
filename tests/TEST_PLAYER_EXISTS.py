from testdata import *
from test_setup import *


def TEST_PLAYER_EXISTS():
    testuser3.login_process()
    check = testuser3.player_exists()
    if check:
        print('TEST PLAYER EXISTS : PASSED')
    elif not check:
        print('TEST PLAYER EXISTS : FAILED')
    else:
        print('test failed: PLAYER EXISTS')

