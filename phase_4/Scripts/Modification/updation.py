import pymysql
import pymysql.cursors
from termcolor import colored
from tabulate import tabulate

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
	print(colored(tabulate(data, headers=['Volume No.', 'Issue No.', 'Page No.', 'Category', 'Title'], tablefmt='psql'), 'cyan'))
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
	print(colored(tabulate(data, headers=['Member ID', 'First Name', 'Middle Name', 'Last Name', 'Join Date', 'Superviser ID', 'Email'], tablefmt='psql'), 'cyan'))
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
	print(colored(tabulate(data, headers=['Email', 'Subscription Type', 'Subscription Date', 'First Name', 'Middle Name', 'Last Name'], tablefmt='psql'), 'cyan'))
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
	print(colored(tabulate(data, headers=['ID', 'Language'], tablefmt='psql'), 'cyan'))

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
	print(colored(tabulate(data, headers=['Volume No.', 'Issue No.', 'Tags', 'Image URL', 'Caption'], tablefmt='psql'), 'cyan'))
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
	print(colored(tabulate(data, headers=['Editor ID', 'Author ID', 'Desginer ID', 'Volume No.', 'Issue No.', 'Page No.'], tablefmt='psql'), 'cyan'))
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
	print(colored(tabulate(data, headers=['ID', 'Languages'], tablefmt='psql'), 'cyan'))
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


def modify_draws_details (username, password) :

	# get info about all the articles
	query = "Select * from draws;"
	data = db_con(username, password, query)
	# Display all the article details
	print(colored("Designers and their drawings available:", 'green', attrs=['bold']))
	print(colored(tabulate(data, headers=['ID', 'Cartoon'], tablefmt='psql'), 'cyan'))
	print("")

	# Select the detail to change
	print("What detail would you like to change?")
	print("\t1. Cartoon")
	ch = int(input("Enter the number corresponsding to the selected option: "))

	if ch == 1:
		field = "cartoon"
		field_name = "Cartoon"
	else:
		print("Please choose a valid option")
		return

	print()

	# get primary key of the article whose details have to be changed
	print("Please enter the details for the concerned Cartoon")
	dsgnr_id = input("ID: ")
	get_modification_details_query = "SELECT " + field + " from draws where designer_id=" + dsgnr_id + ";"
	to_modify = db_con(username, password, get_modification_details_query)
	response = input("Please confirm that the " + field_name + " you want to modify is " + str(to_modify[0][0]) + " (y/n): ")

	if response == "y":
		new_field = input("New " + field_name + ": ")
		updation_query = "UPDATE draws SET " + field + "= \"" + new_field + "\" where designer_id=" + dsgnr_id + ";"

	else:
		return

	db_con(username, password, updation_query)


def modify_editor_details (username, password) :

	# get info about all the articles
	query = "Select * from editor;"
	data = db_con(username, password, query)
	# Display all the article details
	print(colored("Editors available:", 'green', attrs=['bold']))
	print(colored(tabulate(data, headers=['ID', 'Language'], tablefmt='psql'), 'cyan'))
	print("")

	# Select the detail to change
	print("What detail would you like to change?")
	print("\t1. Genres")
	ch = int(input("Enter the number corresponsding to the selected option: "))

	if ch == 1:
		field = "genres"
		field_name = "Genres"
	else:
		print("Please choose a valid option")
		return

	print()

	# get primary key of the article whose details have to be changed
	print("Please enter the details for the concerned Editor")
	edit_id = input("ID: ")
	get_modification_details_query = "SELECT " + field + " from editor where id=\"" + edit_id + "\";"
	to_modify = db_con(username, password, get_modification_details_query)
	response = input("Please confirm that the " + field_name + " you want to modify is " + str(to_modify[0][0]) + " (y/n): ")

	if response == "y":
		new_field = input("New " + field_name + ": ")
		updation_query = "UPDATE editor SET " + field + "= \"" + new_field + "\" where id=\"" + edit_id + "\";"

	else:
		return

	db_con(username, password, updation_query)


def modify_magazine_details (username, password) :

	# get info about all the articles
	query = "Select * from magazine;"
	data = db_con(username, password, query)
	# Display all the article details
	print(colored("Articles available:", 'green', attrs=['bold']))
	print(colored(tabulate(data, headers=['Volume No.', 'Issue No.', 'Date'], tablefmt='psql'), 'cyan'))
	print("")

	# Select the detail to change
	print("What detail would you like to change?")
	print("\t1. Volume Number \n\t2. Issue Number \n\t3. Date")
	ch = int(input("Enter the number corresponsding to the selected option: "))

	if ch == 1:
		field = "volume_no"
		field_name = "Volume number"
	elif ch == 2:
		field = "issue_no"
		field_name = "Issue number"
	elif ch == 3:
		field = "date"
		field_name = "Date"
	else:
		print("Please choose a valid option")
		return

	print()

	# get primary key of the article whose details have to be changed
	print("Please enter the details for the concerned article")
	volume_no = input("Volume number: ")
	issue_no = input("Issue number: ")
	date = input("Date (YYYY-MM-DD): ")
	get_modification_details_query = "SELECT * from magazine where volume_no=" + volume_no + " AND issue_no=" + issue_no + " AND date=\"" + date + "\";"

	to_modify = db_con(username, password, get_modification_details_query)
	response = input("Please confirm that the " + field_name + " you want to modify is " + str(to_modify[0][ch-1]) + " (y/n): ")

	if response == "y":
		new_field = input("New " + field_name + ": ")
		updation_query = "UPDATE magazine SET " + field + "= " + new_field + " where volume_no=" + volume_no + " AND issue_no=\"" + issue_no + "\" AND date=\"" + date + "\";"

	else:
		return

	db_con(username, password, updation_query)


def modify_marketing_details (username, password) :

	# get info about all the articles
	query = "Select * from marketing;"
	data = db_con(username, password, query)
	# Display all the article details
	print(colored("Marketers available:", 'green', attrs=['bold']))
	print(colored(tabulate(data, headers=['ID', 'Platforms'], tablefmt='psql'), 'cyan'))
	print("")

	# Select the detail to change
	print("What detail would you like to change?")
	print("\t1. Platforms")
	ch = int(input("Enter the number corresponsding to the selected option: "))

	if ch == 1:
		field = "platforms"
		field_name = "Platforms"
	else:
		print("Please choose a valid option")
		return

	print()

	# get primary key of the article whose details have to be changed
	print("Please enter the details for the concerned Marketer")
	mkt_id = input("ID: ")
	get_modification_details_query = "SELECT " + field + " from marketing where id=\"" + mkt_id + "\";"
	to_modify = db_con(username, password, get_modification_details_query)
	response = input("Please confirm that the " + field_name + " you want to modify is " + str(to_modify[0][0]) + " (y/n): ")

	if response == "y":
		new_field = input("New " + field_name + ": ")
		updation_query = "UPDATE marketing SET " + field + "= \"" + new_field + "\" where id=\"" + mkt_id + "\";"

	else:
		return

	db_con(username, password, updation_query)


def modify_selling_advert_details (username, password) :

	# get info about all the articles
	query = "Select * from selling_advert;"
	data = db_con(username, password, query)
	# Display all the article details
	print(colored("Sponsors available:", 'green', attrs=['bold']))
	print(colored(tabulate(data, headers=['Sponsor ID', 'Marketer ID'], tablefmt='psql'), 'cyan'))
	print("")

	# Select the detail to change
	print("What detail would you like to change?")
	print("\t1. Sponsor ID\n\t2. Marketer ID")
	ch = int(input("Enter the number corresponding to the selected option: "))

	if ch == 1:
		field = "sponsor_id"
		field_name = "Sponsor ID"
	elif ch == 2:
		field = "marketers_id"
		field_name = "Marketer ID"
	else:
		print("Please choose a valid option")
		return

	print()

	# get primary key of the article whose details have to be changed
	print("Please enter the details for the concerned record")
	spon_id = input("Sponsor ID: ")
	mkt_id = input("Marketer ID: ")
	get_modification_details_query = "SELECT " + field + " from selling_advert where sponsor_id=\"" + spon_id + "\" and marketers_id = \"" + mkt_id + "\";"
	to_modify = db_con(username, password, get_modification_details_query)
	response = input("Please confirm that the " + field_name + " you want to modify is " + str(to_modify[0][0]) + " (y/n): ")

	if response == "y":
		new_field = input("New " + field_name + ": ")
		updation_query = "UPDATE selling_advert SET " + field + "= \"" + new_field + "\" where sponsor_id=\"" + spon_id + "\" and marketers_id = \"" + mkt_id + "\";"

	else:
		return

	db_con(username, password, updation_query)


# def modify_sponsors_details (username, password) :


# def modify_subscribes_details (username, password) :



# CHANGES
# - modify_the_contents_of_the_article -> modify_the_title_of_the_article
# - merged tags, title, category change for article into change_article_details()
