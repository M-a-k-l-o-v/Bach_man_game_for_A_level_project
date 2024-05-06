from db_manager import *

test_username1 = 'FIRST_USER'
test_username2 = 'SECOND_USER'
test_username3 = 'THIRD_USER'
test_username4 = 'FORTH_USER'
test_username5 = 'FIFTH_USER'
test_username6 = 'SIXTH_USER'
test_username7 = 'SEVENTH_USER'
test_username8 = 'EIGHTH_USER'
test_password1 = 'jeffryDO'
test_password2 = 'iwashere123'
test_password3 = 'passwordisRpassword'

table_name = 'test_username_table'
table_name2 = 'test_scores_table'

test_username_table = 'test_username_table'
test_scores_table = 'test_scores_table'

testuser1 = Login(test_username1,test_password1, test_username_table,test_scores_table)
testuser2 = Login(test_username2,test_password1, test_username_table,test_scores_table)
testuser3 = Login(test_username3,test_password1, test_username_table,test_scores_table)
testuser4 = Login(test_username4,test_password2, test_username_table,test_scores_table)
testuser5 = Login(test_username5,test_password2, test_username_table,test_scores_table)
testuser6 = Login(test_username6,test_password2, test_username_table,test_scores_table)
testuser7 = Login(test_username7,test_password3, test_username_table,test_scores_table)
testuser8 = Login(test_username8,test_password3, test_username_table,test_scores_table)
