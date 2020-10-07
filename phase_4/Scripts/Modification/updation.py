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

def modify_article_details (username, password) :

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
		return

	print()

	# get primary key of the article whose details have to be changed
	print("Please enter the details for the concerned Member")
	member_id = input("Member ID: ")
	get_modification_details_query = "SELECT " + field + " from members where member_id=\"" + member_id + "\";"

	to_modify = db_con(username, password, get_modification_details_query)
	response = input("Please confirm that the " + field_name + " you want to modify is " + str(to_modify[0][0]) + " (y/n): ")

	if response == "y":
		new_field = input("New " + field_name + ": ")
		updation_query = "UPDATE members SET " + field + "= \"" + new_field + "\" where member_id=\"" + member_id + "\";"

	else:
		return

	db_con(username, password, updation_query)


def modify_subscriber_details (username, password) :

	# get info about all the articles
	query = "Select * from subscribers;"
	data = db_con(username, password, query)
	# Display all the article details
	print(colored("Subscribers available:", 'green', attrs=['bold']))
	print(colored("Email \t\t\t\tSubscription type \tSubscription Date \tFirst Name \tMiddle Name \t\tLast Name", 'blue'))
	for i in data:
		print(colored(str(i[0]) + "\t\t" + str(i[1]) + " months \t\t" + str(i[2]) + "\t\t" + (i[3]) + "\t\t" + str(i[4]) + "\t\t\t" + str(i[5]), 'cyan'))
	print("")

	# Select the detail to change
	print("What detail would you like to change?")
	print("\t1. Email \n\t2. Subscription Type \n\t3. Subscription Date(YYYY-MM-DD) \n\t4. First Name \n\t5. Middle Name \n\t6. Last Name")
	ch = int(input("Enter the number corresponsding to the selected option: "))

	if ch == 1:
		field = "email"
		field_name = "Email"
	elif ch == 2:
		field = "sub_type"
		field_name = "Subscription Type"
	elif ch == 3:
		field = "sub_date"
		field_name = "Subscription date"
	elif ch == 4:
		field = "f_name"
		field_name = "First Name"
	elif ch == 5:
		field = "m_name"
		field_name = "Middle Name"
	elif ch == 6:
		field = "l_name"
		field_name = "Last Name"
		field_name = "Email"
	else:
		print("Please choose a valid option")
		return

	print()

	# get primary key of the article whose details have to be changed
	print("Please enter the details for the concerned Subscriber")
	email = input("email: ")
	get_modification_details_query = "SELECT " + field + " from subscribers where email=\"" + email + "\";"
	to_modify = db_con(username, password, get_modification_details_query)
	response = input("Please confirm that the " + field_name + " you want to modify is " + str(to_modify[0][0]) + " (y/n): ")

	if response == "y":
		new_field = input("New " + field_name + ": ")
		updation_query = "UPDATE subscribers SET " + field + "= \"" + new_field + "\" where email=\"" + email + "\";"

	else:
		return

	db_con(username, password, updation_query)


def modify_author_details (username, password) :

	# get info about all the articles
	query = "Select * from author;"
	data = db_con(username, password, query)
	# Display all the article details
	print(colored("Authors available:", 'green', attrs=['bold']))
	print(colored("ID \tLanguage", 'blue'))
	for i in data:
		print(colored(str(i[0]) + "\t" + str(i[1]), 'cyan'))
	print("")

	# Select the detail to change
	print("What detail would you like to change?")
	print("\t1. Language")
	ch = int(input("Enter the number corresponsding to the selected option: "))

	if ch == 1:
		field = "languages"
		field_name = "Language"
	else:
		print("Please choose a valid option")
		return

	print()

	# get primary key of the article whose details have to be changed
	print("Please enter the details for the concerned Author")
	auth_id = input("ID: ")
	get_modification_details_query = "SELECT " + field + " from author where id=\"" + auth_id + "\";"
	to_modify = db_con(username, password, get_modification_details_query)
	response = input("Please confirm that the " + field_name + " you want to modify is " + str(to_modify[0][0]) + " (y/n): ")

	if response == "y":
		new_field = input("New " + field_name + ": ")
		updation_query = "UPDATE author SET " + field + "= \"" + new_field + "\" where id=\"" + auth_id + "\";"

	else:
		return

	db_con(username, password, updation_query)


def modify_cartoon_details (username, password) :

	# get info about all the articles
	query = "Select * from cartoon;"
	data = db_con(username, password, query)
	# Display all the article details
	print(colored("Cartoons available:", 'green', attrs=['bold']))
	print(colored("Volume no. \tIssue no. \tTags \t\t\tImage URL \t\t\t\tCaption", 'blue'))
	for i in data:
		print(colored(str(i[3]) + "\t\t" + str(i[4]) + "\t\t" + str(i[2]) + "\t\t" + i[0] + "\t\t\t\t" + i[1], 'cyan'))
	print("")

	# Select the detail to change
	print("What detail would you like to change?")
	print("\t1. Volume Number \n\t2. Issue Number \n\t3. Tag \n\t4. Image URL \n\t5. Caption")
	ch = int(input("Enter the number corresponsding to the selected option: "))

	if ch == 1:
		field = "volume_no"
		field_name = "Volume number"
	elif ch == 2:
		field = "issue_no"
		field_name = "Issue number"
	elif ch == 3:
		field = "tags"
		field_name = "Tag"
	elif ch == 4: 
		field = "image_url"
		field_name = "Image URL"
	elif ch == 5:
		field = "caption"
		field_name = "Caption"
	else:
		print("Please choose a valid option")
		return

	print()

	# get primary key of the article whose details have to be changed
	print("Please enter the details for the concerned cartoon")
	volume_no = input("Volume number: ")
	issue_no = input("Issue number: ")
	img_url = input("Image_URL: ")
	get_modification_details_query = "SELECT " + field + " from cartoon where volume_no=" + volume_no + " AND issue_no=" + issue_no + " AND image_url=\"" + img_url + "\";"
	to_modify = db_con(username, password, get_modification_details_query)
	response = input("Please confirm that the " + field_name + " you want to modify is " + str(to_modify[0][0]) + " (y/n): ")

	if response == "y":
		new_field = input("New " + field_name + ": ")
		updation_query = "UPDATE cartoon SET " + field + "= \"" + new_field + "\" where volume_no=\"" + volume_no + "\" AND issue_no=\"" + issue_no + "\" AND image_url=\"" + img_url + "\";"

	else:
		return

	db_con(username, password, updation_query)


def modify_contribution_details (username, password) :

	# get info about all the articles
	query = "Select * from contribute;"
	data = db_con(username, password, query)
	# Display all the article details
	print(colored("Contributions available:", 'green', attrs=['bold']))
	print(colored("Editor ID \tAuthor ID \tDesigner ID \tVolume no. \tIssue no. \tPage no.", 'blue'))
	for i in data:
		print(colored(str(i[0]) + "\t\t" + str(i[1]) + "\t\t" + str(i[2]) + "\t\t" + str(i[3]) + "\t\t" + str(i[4]) + "\t\t" + str(i[5]), 'cyan'))
	print("")

	# Select the detail to change
	print("What detail would you like to change?")
	print("\t1. Editor ID \n\t2. Author ID \n\t3. Designer ID \n\t4. Volume Number \n\t5. Issue Number \n\t6. Page no.")
	ch = int(input("Enter the number corresponding to the selected option: "))

	if ch == 1:
		field = "editor_id"
		field_name = "Editor ID"
	elif ch == 2:
		field = "author_id"
		field_name = "Author ID"
	elif ch == 3:
		field = "designer_id"
		field_name = "Designer ID"
	elif ch == 4:
		field = "volume_no"
		field_name = "Volume number"
	elif ch == 5:
		field = "issue_no"
		field_name = "Issue number"
	elif ch == 6:
		field = "page_no"
		field_name = "Page no."
	else:
		print("Please choose a valid option")
		return

	print()

	# get primary key of the article whose details have to be changed
	print("Please enter the details for the concerned contribution")
	volume_no = input("Volume number: ")
	issue_no = input("Issue number: ")
	page_no = input("Page no: ")
	get_modification_details_query = "SELECT " + field + " from contribute where volume_no=" + volume_no + " AND issue_no=" + issue_no + " AND page_no=\"" + page_no + "\";"
	to_modify = db_con(username, password, get_modification_details_query)
	response = input("Please confirm that the " + field_name + " you want to modify is " + str(to_modify[0][0]) + " (y/n): ")

	if response == "y":
		new_field = input("New " + field_name + ": ")
		updation_query = "UPDATE contribute SET " + field + "= \"" + new_field + "\" where volume_no=\"" + volume_no + "\" AND issue_no=\"" + issue_no + "\" AND page_no=\"" + page_no + "\";"

	else:
		return

	db_con(username, password, updation_query)


def modify_designer_details (username, password) :

	# get info about all the articles
	query = "Select * from designer;"
	data = db_con(username, password, query)
	# Display all the article details
	print(colored("Designers available:", 'green', attrs=['bold']))
	print(colored("ID \tLanguage", 'blue'))
	for i in data:
		print(colored(str(i[0]) + "\t" + str(i[1]), 'cyan'))
	print("")

	# Select the detail to change
	print("What detail would you like to change?")
	print("\t1. Softwares")
	ch = int(input("Enter the number corresponsding to the selected option: "))

	if ch == 1:
		field = "softwares"
		field_name = "Softwares"
	else:
		print("Please choose a valid option")
		return

	print()

	# get primary key of the article whose details have to be changed
	print("Please enter the details for the concerned Designer")
	dsgnr_id = input("ID: ")
	get_modification_details_query = "SELECT " + field + " from designer where id=\"" + dsgnr_id + "\";"
	to_modify = db_con(username, password, get_modification_details_query)
	response = input("Please confirm that the " + field_name + " you want to modify is " + str(to_modify[0][0]) + " (y/n): ")

	if response == "y":
		new_field = input("New " + field_name + ": ")
		updation_query = "UPDATE designer SET " + field + "= \"" + new_field + "\" where id=\"" + dsgnr_id + "\";"

	else:
		return

	db_con(username, password, updation_query)


# CHANGES
# - modify_the_contents_of_the_article -> modify_the_title_of_the_article
# - merged tags, title, category change for article into change_article_details()
