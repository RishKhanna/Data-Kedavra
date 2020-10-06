import subprocess as sp
import pymysql
import pymysql.cursors

def fn1():
	query = "SHOW TABLES;"
	cur.execute(query)
	data = cur.fetchall()
	for i in data:
		print(i)

# call the function depending on the option chosen
def dispatch(ch):
	if ch == 1:
		fn1()


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
		if(db.opencur):
			print("Connected")
		else:
			print("lol F")

		tmp = input("Enter any key to CONTINUE IN THIS REALM>")

		with db.cursor() as cur:
			while(1):
				# print the options available
				tmp = sp.call('clear', shell = True)
				print("1. Show Tables:")
				print("2. Logout:")

				# get user input for option
				ch = int(input("Enter choice: "))
				tmp = sp.call('Clear', shell = True)

				# to exit the option list
				if ch == 2:
					break
				else:
					dispatch(ch)
					tmp = input("Enter any key bro>")

	# error handling
	except Exception as e:
		tmp = sp.call('clear', shell = True)
		print(e)
		tmp = input("Enter any key to CONTINUE>")
