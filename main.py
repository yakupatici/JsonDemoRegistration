import sys
import json
import os



class User:
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        self.loadUser()

    def loadUser(self):
        if os.path.exists('users.json'):
            with open('users.json','r',encoding='utf-8') as file :
              users =  json.load(file)
              for user in users :
                  user = json.loads(user)
                  newUser = User(username=user['username'],password=user['password'],email=user['email'])
                  self.users.append(newUser)
              print(self.users)




    def register(self, user: User):
        self.users.append(user)
        self.saveToFile()
        print("The user has been registered...")

    def login(self,username,password):
        for user in self.users:
            if user.username == username and user.password == password :
                self.isLoggedIn = True
                self.currentUser = user
                print("Successfully logged into the system ")
                break
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("Logged out of the system")

    def identity(self):
        if self.isLoggedIn:
            print(f'username : {self.currentUser.username}')
        else:
            print("User is not logged in")



    def saveToFile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        with open('users.json','w') as file:
            json.dump(list,file)
repository = UserRepository()

while True:
    print("Menu".center(50,"*"))
    choice = input('1- Register\n2- Login\n3- Logout\n4- Identify\n5- Exit\nYour Choice : ')

    if choice == '5':
        break
        print("System is closed...")

    else:
        if choice == '1':# register
            username = input("Username : ")
            password = input("Password : ")
            email = input("E-mail : ")

            user = User(username=username,password=password,email=email)
            repository.register(user)

            print(repository.users)

        elif choice == '2':# login
            username = input("Username : ")
            password = input("Password : ")
            repository.login(username,password)
        elif choice =='3':
            repository.logout() # logout

        elif choice == '4':
            repository.identity()
        else:
            print("Wrong choice")

