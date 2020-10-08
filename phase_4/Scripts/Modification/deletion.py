import pymysql
import pymysql.cursors

def db_con(username, password, query):
	db = pymysql.connect("localhost", username, password, "data_kedavra")
	with db.cursor() as cur:
		cur.execute(query)
		data = cur.fetchall()
		db.commit()
	return data

def remove_a_member (username, password) :
	ssn = input("Enter the ID of the member to the removed: ")
	query = "DELETE FROM Members WHERE member_id=" + ssn
	data = db_con(username, password, query)
	# author
	query = "DELETE FROM author WHERE id=" + ssn
	data = db_con(username, password, query)
	# designer
	query = "DELETE FROM designer WHERE id=" + ssn
	data = db_con(username, password, query)
	# editor
	query = "DELETE FROM editor WHERE id=" + ssn
	data = db_con(username, password, query)
	# marketing
	query = "DELETE FROM marketing WHERE id=" + ssn
	data = db_con(username, password, query)
	return

def delete_an_article (username, password) :
	vol = input("Enter the Volume of the Article to the removed: ")
	issue = input("Enter the Issue of the Article to the removed: ")
	page = input("Enter the Page No. of the Article to the removed: ")
	# article
	query = "DELETE FROM article WHERE volume_no=" + vol + " AND issue_no=" + issue + " AND page_no=" + page
	data = db_con(username, password, query)
	# contribue 
	query = "DELETE FROM contribute WHERE volume_no=" + vol + " AND issue_no=" + issue + " AND page_no=" + page
	data = db_con(username, password, query)
	return

def unsubscribe (username, password) :
	email = input("Enter the email of the individual to be unsubscribed: ")
	# subscribers
	query = "DELETE FROM subscribes WHERE subscriber=" + email
	data = db_con(username, password, query)
	# subscribes
	query = "DELETE FROM subscribers WHERE email=" + email
	data = db_con(username, password, query)
	return

def remove_a_sponsor (username, password) :
	identity = input("Enter the ID of the Sponsor to be removed: ")
	# selling_advert
	query = "DELETE FROM selling_advert WHERE sponsor_id=" + identity
	data = db_con(username, password, query)
	# Sponsors
	query = "DELETE FROM Sponsors WHERE sponsor_id=" + identity
	data = db_con(username, password, query)
	return
