from testdata import *
from test_setup import *


def TEST_INSERT_DETAILS():
    
    testuser8.insert_details()
    details = testuser8.user_info_extracts()
    password_check = testuser8.verify_password(details[6])
    username_check = testuser8.player_exists()
    if username_check and password_check:
        print('TEST INSERT DETAILS : PASSED')
    elif username_check and not password_check:
        print('TEST INSERT USERNAME : PASSED')
        print('TEST INSERT PASSWORD : FAILED')
    elif not username_check and password_check:
        print('TEST INSERT USERNAME : FAILED')
        print('TEST INSERT PASSWORD : PASSED')
    else:
        print('test failed: INSERT DETAILS')
