import subprocess as sp
import Scripts.Retrival.aggregate as aggregate
import Scripts.Retrival.analysis as analysis
import Scripts.Retrival.projection as projection
import Scripts.Retrival.search as search
import Scripts.Retrival.selection as selection

def main():
	print("Which of the following Retrivals would you like to perform?")
	print("""1. Selection
		List all Issues.
		List all Articles.
		List all Authors.
		Articles from a particular Magazine Issue.
		List of all Articles written by an Author.
		List all Editors.
		List of all Articles edited by an Editor.
		List all Designers.
		List of all Articles designed by a Designer.
		Show Cartoons by Designer.
		Show Cartoons from a particular Issue.
		Show Cartoons from a particular Volume.
		Subscribers for a given Volume.
		Subscribers for a given Issue.""")
	print("""2. Projection
		Issues in a Volume.
		Articles with a particular category.
		Sort Articles by name.
		Show Cartoons with a particular Tag.
		Subscribers with a particular subscription type.""")
	print("""3. Aggregate
		Average number of subscribers for a Volume.
		Total number of articles in a Volume.
		Subscription Change between two given dates""")
	print("""4. Search
		Search Articles by name.
		Search Members by name""")
	print("""5. Analysis
		Most frequent category of Articles written by each Author.
		List of subscribers who subscribed between two consecutive Volumes.""")

	ch = int(input("Enter choice: "))
	tmp = sp.call('clear', shell = True)

	if ch==1:
		print("Which of the following Selections would you like to perform?")
		print("""
		1. List all Issues.
		2. List all Articles.
		3. List all Authors.
		4. Articles from a particular Magazine Issue.
		5. List of all Articles written by an Author.
		6. List all Editors.
		7. List of all Articles edited by an Editor.
		8. List all Designers.
		9. List of all Articles designed by a Designer.
		10.Show Cartoons by Designer.
		11.Show Cartoons from a particular Issue.
		12.Show Cartoons from a particular Volume.
		13.Subscribers for a given Volume.
		14.Subscribers for a given Issue.""")
		ch2 = int(input("Enter choice: "))
		tmp = sp.call('clear', shell = True)
	
		# 
		# 
		# 

	elif ch==2:
		print("Which of the following Projections would you like to perform?")
		print("""
		1. Issues in a Volume.
		2. Articles with a particular category.
		3. Sort Articles by name.
		4. Show Cartoons with a particular Tag.
		5. Subscribers with a particular subscription type""")
		ch2 = int(input("Enter choice: "))
		tmp = sp.call('clear', shell = True)

		# 
		# 
		# 

	elif ch==3:
		print("Which of the following Aggregates would you like to perform?")
		print("""
		1. Average number of subscribers for a Volume.
		2. Total number of articles in a Volume.
		3. Subscription Change between two given dates.""")
		ch2 = int(input("Enter choice: "))
		tmp = sp.call('clear', shell = True)

		# 
		# 
		# 

	elif ch==4:
		print("Which of the following Searches would you like to perform?")
		print("""
		1. Search Articles by name.
		2. Search Members by name""")
		ch2 = int(input("Enter choice: "))
		tmp = sp.call('clear', shell = True)

		# 
		# 
		# 

	elif ch==5:
		print("Which of the following Analysis would you like to perform?")
		print("""
		1. Most frequent category of Articles written by each Author.
		2. List of subscribers who subscribed between two consecutive Volumes.""")
		ch2 = int(input("Enter choice: "))
		tmp = sp.call('clear', shell = True)

		# 
		# 
		# 

	else:
		return