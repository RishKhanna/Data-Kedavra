import subprocess as sp
import Scripts.Modification.deletion as deletion
import Scripts.Modification.insertion as insertion
import Scripts.Modification.updation as updation
from termcolor import colored

def main(username, password):
	print(colored("Which of the following Modifications would you like to perform?",'blue', attrs=['bold']))
	print(colored("1. Insertion", 'cyan', attrs=['bold']))
	print(colored("""
			Creating an Issue.
			Add an Author.
			Add a Designer.
			Add an Editor.
			Add a Marketer.
			Add a Member.
			Add a Subscriber.
			Add a Sponsor.""", 'yellow'))
	print(colored("2. Updation", 'cyan', attrs=['bold']))
	print(colored("""
			Modify Article details.
			Modify Member details.
			Modify Subscriber details
			Modiy Author details
			Modify Cartoon details
			Modify Contribution details
			Modify Designer details
			Modify Draws Details
			Modify Editor details
			Modify Magazine details
			Modify Marketing details
			Modify Selling Advert Details""", "yellow"))
	print(colored("3. Deletion", 'cyan', attrs=['bold']))
	print(colored("""
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
				2. Add an Author.
				3. Add a Designer.
				4. Add an Editor.
				5. Add a Marketer.
				6. Add a Member.
				7. Add a Subscriber.
				8. Add a Sponsor.""",'cyan'))
		
		ch2 = int(input(colored("Enter choice: ",'green')))
		tmp = sp.call('clear', shell = True)

		# 
		#
		if ch2==1:
			query = insertion.creating_an_issue(username, password)

		elif ch2==2:
			query = insertion.add_an_author(username, password)

		elif ch2==3:
			query = insertion.add_a_designer(username, password)

		elif ch2==4:
			query = insertion.add_an_editor(username, password)

		elif ch2==5:
			query = insertion.add_a_marketer(username, password)

		elif ch2==6:
			query = insertion.add_a_member(username, password)

		elif ch2==7:
			query = insertion.add_a_subscriber(username, password)

		elif ch2==8:
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
				6. Modify Contribution details
				7. Modify Designer details
				8. Modify Draws details
				9. Modify Editor details
				10. Modify Magazine details
				11. Modify Marketing details
				12. Modify Selling Advert Details""", 'cyan'))

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

		elif ch2 == 7:
			query = updation.modify_designer_details(username, password)

		elif ch2 == 8:
			query = updation.modify_draws_details(username, password)

		elif ch2 == 9:
			query = updation.modify_editor_details(username, password)

		elif ch2 == 10:
			query = updation.modify_magazine_details(username, password)

		elif ch2 == 11:
			query = updation.modify_marketing_details(username, password)

		elif ch2 == 12:
			query = updation.modify_selling_advert_details(username, password)

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
				4. Remove a Sponsor""", 'cyan'))

		ch2 = int(input(colored("Enter choice: ",'green')))
		tmp = sp.call('clear', shell = True)

		# 
		#
		if ch2==1:
			query = deletion.remove_a_member(username, password)

		elif ch2==2:
			query = deletion.delete_an_article(username, password)

		elif ch2==3:
			query = deletion.unsubscribe(username, password)

		elif ch2==4:
			query = deletion.remove_a_sponsor(username, password)

		else:
			return
		#
		# 

	else:
		return 
