log_reg = eval(input("To register press 1 and enter, to log in press 2 and enter: "))

if log_reg == 1:
    def reg():
        name = input("Full name: ")
        email = input("Enter your email: ")
        username = input("Prefered username: ")
        password = input("Password: ")
        print("welcome ", name, "your username and is ", username)

    reg()
    
elif log_reg == 2:
    def login ():

        username = input("username: ")
        password = input("Password: ")
        print("You are now logged in as ", username)

    login()
