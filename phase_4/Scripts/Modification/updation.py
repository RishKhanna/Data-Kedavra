import pymysql
import pymysql.cursors
from termcolor import colored

def db_con(username, password, query):
	db = pymysql.connect("localhost", username, password, "data_kedavra")
	with db.cursor() as cur:
		cur.execute(query)
		data = cur.fetchall()
		db.commit()

	return data

# Updation functions start here >

def change_article_details (username, password) :

	# get info about all the articles
	query = "Select * from article;"
	data = db_con(username, password, query)
	# Display all the article details
	print(colored("Articles available:", 'green', attrs=['bold']))
	print(colored("volume_no \tissue_no \tpage_no \t category \ttitle", 'blue'))
	for i in data:
		print(colored(str(i[0]) + "\t\t" + str(i[1]) + "\t\t" + str(i[2]) + "\t\t" + i[3] + "\t\t" + i[4], 'cyan'))
	print("")

	# Select the detail to change
	print("What detail would you like to change?")
	print("\t1. Volume Number \n\t2. Issue Number \n\t3. Page number \n\t4. Category \n\t5. Title")
	ch = int(input("Enter the number corresponsding to the selected option: "))

	if ch == 1:
		field = "volume_no"
		field_name = "Volume number"
	elif ch == 2:
		field = "issue_no"
		field_name = "Issue number"
	elif ch == 3:
		field = "page_no"
		field_name = "Page number"
	elif ch == 4: 
		field = "category"
		field_name = "Category"
	elif ch == 5:
		field = "title"
		field_name = "Title"
	else:
		print("Please choose a valid option")
		pass
		return

	print()

	# get primary key of the article whose details have to be changed
	print("Please enter the details for the concerned article")
	volume_no = input("Volume number: ")
	issue_no = input("Issue number: ")
	page_no = input("Page number: ")
	get_modification_details_query = "SELECT * from article where volume_no=\"" + volume_no + "\" AND issue_no=\"" + issue_no + "\" AND page_no=\"" + page_no + "\";"

	to_modify = db_con(username, password, get_modification_details_query)
	response = input("Please confirm that the " + field_name + " you want to modify is " + str(to_modify[0][ch-1]) + " (y/n): ")

	if response == "y":
		new_field = input("New " + field_name + ": ")
		updation_query = "UPDATE article SET " + field + "= \"" + new_field + "\" where volume_no=\"" + volume_no + "\" AND issue_no=\"" + issue_no + "\" AND page_no=\"" + page_no + "\";"

	else:
		pass
		return

	db_con(username, password, updation_query)


def modify_member_details (username, password) :

	# get info about all the articles
	query = "Select * from members;"
	data = db_con(username, password, query)
	# Display all the article details
	print(colored("Members available:", 'green', attrs=['bold']))
	print(colored("Member ID \tFirst Name \tMiddle Name \t Last Name \tJoin Date \tSuperviser ID \tEmail", 'blue'))
	for i in data:
		print(colored(str(i[0]) + "\t\t" + str(i[1]) + "\t\t" + str(i[2]) + "\t\t" + i[3] + "\t\t" + str(i[4]) + "\t\t" + str(i[5]) + "\t\t" + i[6], 'cyan'))
	print("")

	# Select the detail to change
	print("What detail would you like to change?")
	print("\t1. First Name \n\t2. Middle Name \n\t3. Last Name \n\t4. Join date (YYYY-MM-DD) \n\t5. Superviser ID \n\t6. Email")
	ch = int(input("Enter the number corresponsding to the selected option: "))

	if ch == 1:
		field = "f_name"
		field_name = "First Name"
	elif ch == 2:
		field = "m_name"
		field_name = "Middle Name"
	elif ch == 3:
		field = "l_name"
		field_name = "Last Name"
	elif ch == 4: 
		field = "join_date"
		field_name = "Join Date"
	elif ch == 5:
		field = "superviser_id"
		field_name = "Superviser ID"
	elif ch == 6:
		field = "email"
		field_name = "Email"
	else:
		print("Please choose a valid option")
		pass
		return

	print()

	# get primary key of the article whose details have to be changed
	print("Please enter the details for the concerned Member")
	member_id = input("Member ID: ")
	get_modification_details_query = "SELECT * from members where member_id=\"" + member_id + "\";"

	to_modify = db_con(username, password, get_modification_details_query)
	response = input("Please confirm that the " + field_name + " you want to modify is " + str(to_modify[0][ch]) + " (y/n): ")

	if response == "y":
		new_field = input("New " + field_name + ": ")
		updation_query = "UPDATE members SET " + field + "= \"" + new_field + "\" where member_id=\"" + member_id + "\";"

	else:
		pass
		return

	db_con(username, password, updation_query)
	pass

def modify_subscriber_details () :
	pass

# CHANGES
# - modify_the_contents_of_the_article -> modify_the_title_of_the_article
# - merged tags, title, category change for article into change_article_details()
