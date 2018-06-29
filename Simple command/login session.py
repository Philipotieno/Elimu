log_reg = str(input("Are you registered user? y/n? Press q to quit: "))

class signin(object):
   
   def __init__(self):
      self.users = { }
      if log_reg == "y":
         self.login()
      elif log_reg == "n":
         self.register()
      elif log_reg != "q":
         print("You are quiting...........")
      else:
         print:("INVALID KEY")
         
         
   def register(self):
      write = [ ]
      comment = [ ]
      name = input("Full name: ")
      email = input("Enter your email: ")
      username = input("Prefered username: ")
      
      if username in self.users:
        print("Username name already exist!")
      else:
        createPassw = input("Create password: ")
        self.users[username] = createPassw
        print("User created")
        print("welcome ", name, "your username is ", username, "You can now write and comment on posts")
        write = input("Write a post: ")
        if not write:
           print("You have not posted anything")
        else:
           print("You have written your first post")
         
        view = int(input("To view your registration details and first post press 1"))
        if view == 1:
           print("Name: \n",name,"\nUsername and password:\n", self.users[username],"\nFirst post: \n", write)


   def login(self):
      write = [ ]
      comment = [ ]
      username = input('Enter your username  ')
      password = input('Enter your password  ')
      if username in self.users and self.users[username] == password:
         
        print("You are now logged in as ",username)
        write = input("Write a post: ")
        
      else:
        print("User doesn't exist or wrong password!")

        
a = signin()
