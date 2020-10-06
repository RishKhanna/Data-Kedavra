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
	