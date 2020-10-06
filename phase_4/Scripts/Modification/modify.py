import subprocess as sp
import Scripts.Modification.deletion as deletion
import Scripts.Modification.insertion as insertion
import Scripts.Modification.updation as updation

def main():
	print("Which of the following Modification would you like to do?")
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

