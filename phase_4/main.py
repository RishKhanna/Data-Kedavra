import subprocess as sp
import pymysql
import pymysql.cursors
import Scripts.Retrival.retrive as retrive
import Scripts.Modification.modify as modify
from termcolor import colored


def fn1():
    query = "SHOW TABLES;"
    cur.execute(query)
    data = cur.fetchall()
    for i in range(len(data)):
        if i < 10:
            print(colored(str(i) + " : " + data[i][0], "yellow"))
        else:
            print(colored(str(i)+": " + data[i][0], "yellow"))

# call the function depending on the option chosen


def dispatch(ch):
    if ch == 1:
        fn1()
    elif ch == 2:
        retrive.main(username, password)
    elif ch == 3:
        modify.main(username, password)

    else:
        print(colored("Enter a valid option.", 'red'))


while(1):
    tmp = sp.call('clear', shell=True)

    # get username and password through input
    print(colored("Type exit to exit the application", 'red'))
    username = input(colored("Username: ", 'cyan'))
    if(username == "exit"):
        break
    password = input(colored("Password: ", 'cyan'))

    if(password == "exit"):
        break

    # establish a MySQL connection
    try:
        # connect to DB
        db = pymysql.connect("localhost", username, password, "data_kedavra")
        tmp = sp.call('clear', shell=True)

        # show connection status to the user
        # ASK KSHITIJAA ABOUT THIS
        # if(db.opencur):
        # 	print("Connected")
        # else:
        # 	print("lol F")

        tmp = input(
            colored("Enter any key to CONTINUE IN THIS REALM>", 'green'))

        with db.cursor() as cur:

            # qr = "source dump.sql"
            # cur.execute(qr)
            # db.commit()

            while(1):
                # print the options available
                tmp = sp.call('clear', shell=True)
                print(colored(
                    "Which operations would you like to perform to the database?", 'blue', attrs=['bold']))
                print(colored("1. Show Tables.", 'cyan', attrs=['bold']))
                print(colored("2. Retrival", 'cyan', attrs=['bold']))
                print(colored(
                    "\tincludes: \n\t\t-> Selection.\n\t\t-> Projection.\n\t\t-> Aggregate.\n\t\t-> Search.\n\t\t-> Analysis.", 'yellow'))
                print(colored("3. Modification", 'cyan', attrs=['bold']))
                print(colored(
                    "\tincludes:\n\t\t-> Insertion.\n\t\t-> Updation.\n\t\t-> Deletion.", 'yellow'))
                print(colored("0. Logout", 'red', attrs=['bold']))

                # get user input for option
                ch = int(input(colored("Enter choice: ", 'green')))
                tmp = sp.call('clear', shell=True)

                # to exit the option list
                if ch == 0:
                    break
                else:
                    dispatch(ch)
                    tmp = input(colored("Press Enter to CONTINUE >", 'green'))

    # error handling
    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        tmp = input(colored("Press Enter to CONTINUE:", 'green'))
