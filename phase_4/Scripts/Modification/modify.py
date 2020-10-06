import subprocess as sp
import Scripts.Modification.deletion as deletion
import Scripts.Modification.insertion as insertion
import Scripts.Modification.updation as updation

def main():
	print("Which of the following Modifications would you like to do?")
	print("""1. Insertion
		Creating an Issue.
		Adding Tags to Article.
		Adding Categories to the Article.
		Adding Tags to the Article.
		Add a Member.
		Add a Subscriber.
		Add a Sponsor.""")
	print("""2. Updation
		Modify the contents of the Article.
		Change the issue of an Article.
		Change the tags in an Article.
		Change the categories in an Article.
		Modify Member details.
		Modify Subscriber details""")
	print("""3. Deletion
		Remove a Member.
		Delete an Article.
		Unsubscribe.
		Remove a Sponsor""")

	ch = int(input("Enter choice: "))
	tmp = sp.call('clear', shell = True)

	if ch==1:
		print("Which of the following Insertions would you like to do?")
		print("""
		1. Creating an Issue.
		2. Adding Tags to Article.
		3. Adding Categories to the Article.
		4. Adding Tags to the Article.
		5. Add a Member.
		6. Add a Subscriber.
		7. Add a Sponsor.""")
		
		ch2 = int(input("Enter choice: "))
		tmp = sp.call('clear', shell = True)

		# 
		#
		if ch2==1:
			insertion.creating_an_issue()

		elif ch2==2:
			insertion.adding_tags_to_article()

		elif ch2==3:
			insertion.adding_categories_to_the_article()

		elif ch2==4:
			insertion.adding_tags_to_the_article()

		elif ch2==5:
			insertion.add_a_member()

		elif ch2==6:
			insertion.add_a_subscriber()

		elif ch2==7:
			insertion.add_a_sponsor()

		else:
			return
		#
		# 

	elif ch==2:
		print("Which of the following Updations would you like to do?")
		print("""
		1. Modify the contents of the Article.
		2. Change the issue of an Article.
		3. Change the tags in an Article.
		4. Change the categories in an Article.
		5. Modify Member details.
		6. Modify Subscriber details.""")

		ch2 = int(input("Enter choice: "))
		tmp = sp.call('clear', shell = True)

		# 
		#
		if ch2==1:
			updation.modify_the_contents_of_the_article()

		elif ch2==2:
			updation.change_the_issue_of_an_article()

		elif ch2==3:
			updation.change_the_tags_in_an_article()

		elif ch2==4:
			updation.change_the_categories_in_an_article()

		elif ch2==5:
			updation.modify_member_details()

		elif ch2==6:
			updation.modify_subscriber_details()

		else:
			return
		#
		# 

	elif ch==3:
		print("Which of the following Deletions would you like to do?")
		print("""
		1. Remove a Member.
		2. Delete an Article.
		3. Unsubscribe.
		4. Remove a Sponsor""")

		ch2 = int(input("Enter choice: "))
		tmp = sp.call('clear', shell = True)

		# 
		#
		if ch2==1:
			deletion.remove_a_member()

		elif ch2==2:
			deletion.delete_an_article()

		elif ch2==3:
			deletion.unsubscribe()

		elif ch2==4:
			deletion.remove_a_sponsor()

		else:
			return
		#
		# 

	else:
		return 