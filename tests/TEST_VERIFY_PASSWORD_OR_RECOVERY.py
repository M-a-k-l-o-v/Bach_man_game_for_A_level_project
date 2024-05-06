from testdata import *
from test_setup import *

def TEST_VERIFY_PASSWORD_OR_RECOVERY():
  
    testuser1.login_process()
    testuser1.password = 'rick&morty'
    wrong_password_login, _  = testuser1.login_process()
    if not wrong_password_login:
        print('TEST PASSWORD VERIFICATION USING FALSE PASSWORD: PASSED')
    elif wrong_password_login:
        print('TEST PASSWORD VERIFICATION USING FALSE PASSWORD: FAILED')

    else:
        print('test failed: PASSWORD VERIFICATION USING FALSE PASSWORD')
    
    testuser1.password = test_password1

    
