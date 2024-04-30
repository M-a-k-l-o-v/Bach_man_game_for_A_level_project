import bcrypt
from db_manager import Login




# Example usage:
# password = "mysecretpassword"

scores = [0,0,0,0,0]

def get_new_score():
    new_score = input("")
    return new_score
# new_score = get_new_score()

# should get email from user registeration if user doesnt exist and should get from db if user exists
# !!!!!!! not yet done !!!!!!!!!!!
def get_email():
    email = input("")
    return email
# email = get_email()

def get_username():
    username = input("")
    return username
# username = get_username()

def get_password():
    password = input("")
    return password
# password = get_password()


# might not neeed

# !!!!!!!!!!!!!!!
#username = 'jeff'
#password = 12344
#email = 'mmarvellous69@gmail.com'
#player = Login(username, password, email)
    
    # queury username in database
    # if queury returns true 
    #cuser_exists = True
#hashed_password = copied hashed_password belonging to user 
    # elif queury returns false
    # user_exists = False
        # prompt user does not exist 
        # prompt for signup or continue
    

# if user_exists:
    
   # amend_score(username, scores)

# Amend the scores of an existing user
#else:
    #insert_high_score(user_name, scores)
#print(get_top_high_scores_global())



def verify_password(password, hashed_password):
    correct_password = bcrypt.checkpw(password.encode('utf-8'), hashed_password)
    return correct_password

        #prompt user doesnt exist, opening signup page 
        # button on signup page is clicked
    
    


def hash_password(password):
    # Generate a salt and hash the password with bcrypt
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

    # database.ammend(new_user_username, hashed_password, email, top_five_score)
    # prompt account made, enjoy game!