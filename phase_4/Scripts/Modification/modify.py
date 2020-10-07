import subprocess as sp
import Scripts.Modification.deletion as deletion
import Scripts.Modification.insertion as insertion
import Scripts.Modification.updation as updation
from termcolor import colored

def main(username, password):
	print(colored("Which of the following Modifications would you like to perform?",'cyan', attrs=['bold']))
	print(colored("""1. Insertion
			Creating an Issue.
			Adding Tags to Article.
			Adding Categories to the Article.
			Adding Tags to the Article.
			Add a Member.
			Add a Subscriber.
			Add a Sponsor.""", 'yellow'))
	print(colored("""2. Updation
			Modify Article details.
			Modify Member details.
			Modify Subscriber details
			Modiy Author details
			Modify Cartoon details
			Modify Contribution details""", "yellow"))
	print(colored("""3. Deletion
			Remove a Member.
			Delete an Article.
			Unsubscribe.
			Remove a Sponsor""", 'yellow'))

	ch = int(input(colored("Enter choice: ",'green')))
	tmp = sp.call('clear', shell = True)

	if ch==1:
		print(colored("Which of the following Insertions would you like to do?", 'cyan', attrs=['bold']),end="")
		print(colored("""
				1. Creating an Issue.
				2. Adding Categories to the Article.
				3. Add a Member.
				4. Add a Subscriber.
				5. Add a Sponsor.""",'yellow'))
		
		ch2 = int(input(colored("Enter choice: ",'green')))
		tmp = sp.call('clear', shell = True)

		# 
		#
		if ch2==1:
			query = insertion.creating_an_issue(username, password)

		elif ch2==2:
			query = insertion.adding_categories_to_the_article(username, password)

		elif ch2==3:
			query = insertion.add_a_member(username, password)

		elif ch2==4:
			query = insertion.add_a_subscriber(username, password)

		elif ch2==5:
			query = insertion.add_a_sponsor(username, password)

		else:
			return

		return query
		#
		# 

	elif ch==2:
		print(colored("Which of the following Updations would you like to do?", 'cyan', attrs=['bold']), end="")
		print(colored("""
				1. Modify Article details.
				2. Modify Member details.
				3. Modify Subscriber details.
				4. Modify Author details
				5. Modify Cartoon details
				6. Modify Contribution details""", 'yellow'))

		ch2 = int(input(colored("Enter choice: ",'green')))
		tmp = sp.call('clear', shell = True)

		# 
		#
		if ch2==1:
			query = updation.modify_article_details(username, password)

		elif ch2==2:
			query = updation.modify_member_details(username, password)

		elif ch2==3:
			query = updation.modify_subscriber_details(username, password)

		elif ch2 == 4:
			query = updation.modify_author_details(username, password)

		elif ch2 == 5:
			query = updation.modify_cartoon_details(username, password)

		elif ch2 == 6:
			query = updation.modify_contribution_details(username, password)

		else:
			return

		return query
		#
		# 

	elif ch==3:
		print(colored("Which of the following Deletions would you like to do?", 'cyan', attrs=['bold']), end="")
		print(colored("""
				1. Remove a Member.
				2. Delete an Article.
				3. Unsubscribe.
				4. Remove a Sponsor""", 'yellow'))

		ch2 = int(input(colored("Enter choice: ",'green')))
		tmp = sp.call('clear', shell = True)

		# 
		#
		if ch2==1:
			query = deletion.remove_a_member()

		elif ch2==2:
			query = deletion.delete_an_article()

		elif ch2==3:
			query = deletion.unsubscribe()

		elif ch2==4:
			query = deletion.remove_a_sponsor()

		else:
			return
		#
		# 

	else:
		return 
