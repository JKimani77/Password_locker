import random
from user import User
from credentials import Creds

def create_user(nameone,nametwo,password):
    new_user = User(nameone,nametwo,password)
    return new_user

def save_user(user):
    user.save_person()

def find_user(nameone,password):
    return User.find_person(nameone,password)

def create_new_creds(account,password):
    new_credential = Creds(account,password)
    return new_credential

def save_creds(credentials):
    credentials.save_creds()

def del_creds(credentials):
    credentials.rm_creds()

def locate_credential(account):
    return Creds.find_by_acc_name(account)

def look_existing_credential(account):
    return Creds.credential_exists(account)

def display_credentials():
    return Creds.reveal_credentials()


def main():
    print('\n')
    while True:
        print(
            "***********  Welcome to password locker!!! ************"
        )
        print('\n')
        print("""Use these navigation codes to navigate: \n "nu"- add new user \n "lg"-login to your created account \n "ex"-to exit the system""")
        nav_code = input().lower()
        print('\n')