from testdata import *
from test_setup import *

def TEST_RANDOM_KEY():
    key1  = testuser1.generate_random_key()
    key2 = testuser1.generate_random_key()
    if not(key1 == key2):
        print('TEST RANDOM KEY GENERATION : PASSED')
    elif (key1 == key2):
        print('TEST RANDOM KEY GENERATION : FAILED')
    else:
        print('test failed: RANDOM KEY GENERATION')


 