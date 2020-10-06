def creating_an_issue () :
	print("Creating an issue:")
	volume_no = input("Volume no:")
	issue_no = input("Issue no:")
	date = input("Date(YYYY-MM-DD):")

	query = "INSERT into MAGAZINE values(" + volume_no + ", " + issue_no + ", \"" + date + "\");"

	return query

def adding_tags_to_article () :
	pass

def adding_categories_to_the_article () :
	pass

def adding_tags_to_the_article () :
	pass

def add_a_member () :
	pass

def add_a_subscriber () :
	pass

def add_a_sponsor () :
	pass
