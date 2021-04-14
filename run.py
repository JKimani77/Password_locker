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

        if nav_code == 'nu':
            print('-----------create username---------')
            auth_name = input()

            print('-----------create password---------')
            auth_pass = input()

            print('-----------confirm password---------')
            confirm_password = input()
            print('\n')

            while confirm_password != auth_pass:
                print("-----------Invalid Password !-----------")
                print("-----------Enter user name-----------")
                auth_pass = input()
                print("-----------Confirm your password-----------")
                confirm_password = input()
                print('\n')
                
            else:
                print(
                    f"Hello {auth_name}! You have successfully create your account! "
                )
                print('\n')
                print("                 ---------------- Proceed to login ----------------")
                print('\n')
                print("-----------Username-----------")
                loggin_name = input()
                print("-----------Your password-----------")
                loggin_pass = input()

                
            while loggin_name != auth_name or loggin_pass != auth_pass:
                print('\n')
                print("Invalid username or password")
                print("-----------Username-----------")
                loggin_name = input()
                print("-----------Your password-----------")
                loggin_pass = input()
                print('\n')

            else:
                print('\n')
                print(
                    f"---------------- Welcome {loggin_name} to your account----------------")
                print('\n')

                print("Select an option to continue: \n Enter 1, 2, 3, 4 or 5")
                print('\n')

            while True:
                print("1:view your saved credentials")
                print("2:Add new credentials")
                print("3:Remove  credentials")
                print("4:search new credentials")
                print("5:log out")
                nav_two = input()