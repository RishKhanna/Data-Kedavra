import pymysql
import pymysql.cursors
from tabulate import tabulate

def db_con(username, password, query):
	db = pymysql.connect("localhost", username, password, "data_kedavra")
	with db.cursor() as cur:
		cur.execute(query)
		data = cur.fetchall()
		db.commit()

	return data

# Insertion functions start here >

# add a record for issue
def creating_an_issue (username, password) :
	print("Creating an issue: ")
	volume_no = input("Volume no: ")
	issue_no = input("Issue no: ")
	date = input("Date (YYYY-MM-DD): ")

	query = "INSERT into MAGAZINE values(" + volume_no + ", " + issue_no + ", \"" + date + "\");"

	db_con(username, password, query)


# add a author
def add_an_author (username, password) :
	print("Members available: ")
	retrieval_query = "SELECT * from members"
	data = db_con(username, password, retrieval_query)
	print(tabulate(data, headers=['Member ID', 'First Name', 'Middle Name', 'Last Name', 'Join Date', 'Superviser ID', 'Email'], tablefmt='psql'))

	print("Add an author:")
	auth_id = input("Author ID: ")
	language = input("Language the author works in: ")

	query = "INSERT into author values (" + auth_id + ", \"" + language + "\");"
	db_con(username, password, query)


# add a designer
def add_a_designer (username, password) :
	print("Members available: ")
	retrieval_query = "SELECT * from members"
	data = db_con(username, password, retrieval_query)
	print(tabulate(data, headers=[
		'Member ID', 'First Name', 'Middle Name', 'Last Name', 'Join Date', 'Superviser ID', 'Email'], tablefmt='psql'))

	print("Add a designer:")
	auth_id = input("Designer ID: ")
	software = input("Software the designer works in: ")

	query = "INSERT into designer values (" + auth_id + ", \"" + software + "\");"
	db_con(username, password, query)



# add an editor
def add_an_editor (username, password) :
	print("Members available: ")
	retrieval_query = "SELECT * from members"
	data = db_con(username, password, retrieval_query)
	print(tabulate(data, headers=[
		'Member ID', 'First Name', 'Middle Name', 'Last Name', 'Join Date', 'Superviser ID', 'Email'], tablefmt='psql'))

	print("Add an editor:")
	auth_id = input("Editor ID: ")
	genre = input("Genre the editor works in: ")

	query = "INSERT into editor values (" + auth_id + ", \"" + genre + "\");"
	db_con(username, password, query)


# add a marketer
def add_a_marketer (username, password) :
	print("Members available: ")
	retrieval_query = "SELECT * from members"
	data = db_con(username, password, retrieval_query)
	print(tabulate(data, headers=[
		'Member ID', 'First Name', 'Middle Name', 'Last Name', 'Join Date', 'Superviser ID', 'Email'], tablefmt='psql'))

	print("Add a marketer:")
	auth_id = input("Marketer ID: ")
	platform = input("Platform the marketer works with: ")

	query = "INSERT into marketing values (" + auth_id + ", \"" + platform + "\");"
	db_con(username, password, query)


# add a record for member
def add_a_member (username, password) :
	print("Add a member:")
	member_id = input("Member ID: ")
	name = input("Name: ")
	join_date = input("Date of Joining (YYYY-MM-DD): ")
	supervisor_id = input("Supervisor ID: ")
	email = input("Email: ")

	name = name.split()
	f_name = name[0]
	m_name = ""
	l_name = ""
	if len(name) == 2:
		l_name = name[1]
	elif len(name) != 1:
		m_name == " ".join(name[1:-1])

	query = "INSERT into members values(" + member_id + ", \"" + f_name + "\", \"" + m_name + "\", \"" + l_name + "\", \"" + join_date + "\", " + supervisor_id + ", \"" + email +"\");"

	db_con(username, password, query)


# add a record for subscriber
def add_a_subscriber (username, password) :
	print("Add a subscriber:")
	name = input("Name: ")
	email = input("Email: ")
	sub_type = input("Subscription type (enter the number of months subscribed for): ")
	sub_date = input("Date of Subscribing (YYYY-MM-DD): ")

	name = name.split()
	f_name = name[0]
	m_name = ""
	l_name = ""
	if len(name) == 2:
		l_name = name[1]
	elif len(name) != 1:
		m_name == " ".join(name[1:-1])

	query = "INSERT into subscribers values(\"" + email + "\"," + sub_type + ", \"" + sub_date +"\", \"" + f_name + "\", \"" + m_name + "\", \"" + l_name + "\");"

	db_con(username, password, query)


# add a record for sponsor
def add_a_sponsor (username, password) :
	print("Add a sponsor:")
	sponsor_id = input("Sponsor ID: ")
	product = input("Product: ")
	payment = input("Payment (Credit/ Net Banking): ")

	query = "INSERT into sponsors values (" + sponsor_id + ", \"" + product + "\", \"" + payment + "\");"

	db_con(username, password, query)



# CHANGES:
# - removed adding_tags_to_the_article() -- redundant
# - removed adding_tags_to_article() -- only categories, no tags
