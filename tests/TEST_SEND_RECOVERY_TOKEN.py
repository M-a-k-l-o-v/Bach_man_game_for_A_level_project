from testdata import *
from test_setup import *

def TEST_SEND_RECOVERY_TOKEN():
    recovery_key_message = testuser2.generate_random_key()
    check  = testuser2.send_recovery_token(recovery_key_message)
    if check:
        print('TEST SEND RANDOM KEY : PASSED')
    elif not check:
        print('TEST SEND RANDOM KEY : FAILED')
    else:
        print('test failed: SEND RANDOM KEY')
    
        