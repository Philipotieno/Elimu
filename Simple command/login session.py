log_reg = str(input("Are you registered user? y/n? Press q to quit: "))

class signin(object):
   def __init__(self):
       self.users = { }
       if log_reg == "y":
          self.login()
       elif log_reg == "n":
          self.register()
          
          
   def register(self):
      name = input("Full name: ")
      email = input("Enter your email: ")
      username = input("Prefered username: ")
      
      if username in self.users:
        print("Username name already exist!")
      else:
        createPassw = input("Create password: ")
        self.users[username] = createPassw
        print("User created")
        print("welcome ", name, "your username is ", username)
      


   def login(self):
      username = input('Enter your username  ')
      password = input('Enter your password  ')
      if username in self.users and self.users[username] == password:
        print("You are now logged in as ",username)
      else:
        print("User doesn't exist or wrong password!")
        

        
a = signin()
a.register()
a.login()
