def creating_an_issue () :
	print("Creating an issue: ")
	volume_no = input("Volume no: ")
	issue_no = input("Issue no: ")
	date = input("Date (YYYY-MM-DD): ")

	query = "INSERT into MAGAZINE values(" + volume_no + ", " + issue_no + ", \"" + date + "\");"

	return query

def adding_categories_to_the_article () :
	pass

def add_a_member () :
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

	return query

def add_a_subscriber () :
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

	query = "INSERT into subscribers values(\"" + email + "\"," + sub_type + ", \"" + sub_date +  "\", \"" + f_name + "\", \"" + m_name + "\", \"" + l_name + "\");"

	return query

def add_a_sponsor () :
	print("Add a sponsor:")
	sponsor_id = input("Sponsor ID: ")
	product = input("Product: ")
	payment = input("Payment (Credit/ Net Banking): ")

	query = "INSERT into sponsors values (" + sponsor_id + ", \"" + product + "\", \"" + payment + "\");"

	return query

# CHANGES:
# - removed adding_tags_to_the_article() -- redundant
# - removed adding_tags_to_article() -- only categories, no tags
