import subprocess as sp
import pymysql
import pymysql.cursors
import Scripts.Retrival.retrive as retrive
import Scripts.Modification.modify as modify

def fn1():
	query = "SHOW TABLES;"
	cur.execute(query)
	data = cur.fetchall()
	for i in range(len(data)):
		print(i,": ",data[i][0])

# call the function depending on the option chosen
def dispatch(ch):
	if ch == 1:
		fn1()
	elif ch==2:
		retrive.main()
	elif ch==3:
		query = modify.main()
		cur.execute(query)
		db.commit()

	else:
		print("Enter a valid option.")


while(1):
	tmp = sp.call('clear', shell = True)

	# get username and password through input
	print("Type exit to exit the application")
	username = input("Username: ")
	if(username == "exit"):
		break
	password = input("Password: ")

	if(password == "exit"):
		break

	# establish a MySQL connection
	try:
		# connect to DB
		db = pymysql.connect("localhost", username, password, "data_kedavra")
		tmp = sp.call('clear', shell = True)

		# show connection status to the user
		# ASK KSHITIJAA ABOUT THIS
		# if(db.opencur):
		# 	print("Connected")
		# else:
		# 	print("lol F")

		tmp = input("Enter any key to CONTINUE IN THIS REALM>")

		with db.cursor() as cur:

			qr = "source dump.sql"
			cur.execute(qr)
			# db.commit()


			while(1):
				# print the options available
				tmp = sp.call('clear', shell = True)
				print("Which operations would you like to perform to the database?")
				print("1. Show Tables.")
				print("2. Retrival")
				print("\tincludes: \n\t\t-> Selection.\n\t\t-> Projection.\n\t\t-> Aggregate.\n\t\t-> Search.\n\t\t-> Analysis.")
				print("3. Modification")
				print("\tincludes:\n\t\t-> Insertion.\n\t\t-> Updation.\n\t\t-> Deletion.")
				print("0. Logout")

				# get user input for option
				ch = int(input("Enter choice: "))
				tmp = sp.call('clear', shell = True)

				# to exit the option list
				if ch == 0:
					break
				else:
					dispatch(ch)
					tmp = input("Enter any key bro>")

	# error handling
	except Exception as e:
		tmp = sp.call('clear', shell = True)
		print(e)
		tmp = input("Press Enter to CONTINUE:")
