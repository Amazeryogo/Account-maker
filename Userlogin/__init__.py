# These are the  user settings
import random
import time

Thelist = {}
Password = {}
Level = {}


def GetusernameandPassword():
    with open("Usernames.txt")as file:
        for line in file:
            line = line.rstrip('\n')
            username, password, accountId = line.split('/')
            Thelist[username] = accountId
            Password[password] = accountId


def login():
    user = input("Enter username: ")
    if user == '.Create':
        print('Generating a new account:')
        add = input('Enter your new username:')
        subt = input('Enter Password')
        print('working on' + " " + add + '\'s account..')
        add_user(add, subt)
    elif user in Thelist:
        print('welcome! Please enter your password:')
        passwor = input(":")
        if Password[passwor] in Password:
            print('Welcome!' + user)
            # join  your service here!
        else:
            print('Error! wrong password! try again!')
            login()
    elif user == '<help>':
        print('Here are the usernames with their account numbers:')
        print(Thelist)
        login()
    else:
        print('Error! username not found! maybe  the spelling is wrong or you haven\'t created one!\n'
              'if you havent, write .Create to create a new account, if you do not remember write <help> ')
        login()


def main():
    print('Welcome')
    login()


def add_user(name, password):
    with open('Usernames.txt', 'a') as file:
        file.write('\n' + name + '/' + password + '/' + Id)
    with open('ingamestuff', 'a') as file:
        file.write('\n' + name + '/' + 'Lv1')
        Thelist[name] = Id
        Password[password] = Id
        Level[name] = 'Lv1'
        print('yeah.. Account info collected!')
        print('It might take a while.. so keep patience..\n')
        print('Generating.....')

        time.sleep(120)
        print('login with your username in style!')
        main()


Id = str(random.randrange(100000, 999999))
