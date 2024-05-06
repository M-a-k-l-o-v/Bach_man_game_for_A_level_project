from testdata import *
from test_setup import *


def TEST_HASH_PASSWORD():
    testuser1.password = 'newpass3p98yib'
    hash1  = testuser1.hash_password
    hash2  = testuser1.hash_password

    check1 = hash1 == hash2
    if check1:
        print('TEST HASHED PASSWORD HOLD NO REPLICA : PASSED')
    elif not check1:
        print('TEST HASHED PASSWORD HOLD NO REPLICA : FAILED')
    else:
        print('test failed: HASHED PASSWORD HOLD NO REPLICA')
    testuser1.password = test_password1

    