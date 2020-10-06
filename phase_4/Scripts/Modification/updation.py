import pymysql
import pymysql.cursors

def db_con(username, password, query):
	db = pymysql.connect("localhost", username, password, "data_kedavra")
	with db.cursor() as cur:
		cur.execute(query)
		data = cur.fetchall()
		db.commit()

	return data

# Updation functions start here >

def modify_the_title_of_the_article (username, password) :
	query = "Select volume_no, issue_no, page_no, title from article;"
	data = db_con(username, password, query)
	
	print("Articles available:")
	print("volume_no \tissue_no \tpage_no \ttitle")
	for i in data:
		print(str(i[0]) + "\t\t" + str(i[1]) + "\t\t" + str(i[2]) + "\t\t" + i[3])
	print("")

	print("Please enter the article details for the articleyou want to change the title of")
	volume_no = input("Volume number: ")
	issue_no = input("Issue number: ")
	page_no = input("Page number: ")
	get_title_query = "SELECT title from article where volume_no=\"" + volume_no + "\" AND issue_no=\"" + issue_no + "\" AND page_no=\"" + page_no + "\";"
	
	title = db_con(username, password, get_title_query)
	response = input("Please confirm that the title you want to modify is " + str(title) + " (y/n): ")

	if response == "y":
		new_title = input("New title: ")
		query = "UPDATE article SET title = \"" + new_title + "\" where volume_no=\"" + volume_no + "\" AND issue_no=\"" + issue_no + "\" AND page_no=\"" + page_no + "\";"

	else:
		pass

	return query

def change_the_issue_of_an_article () :
	pass

def change_the_tags_in_an_article () :
	pass

def change_the_categories_in_an_article () :
	pass

def modify_member_details () :
	pass

def modify_subscriber_details () :
	pass

# CHANGES
# - modify_the_contents_of_the_article -> modify_the_title_of_the_article
