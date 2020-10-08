import subprocess as sp
import Scripts.Retrival.aggregate as aggregate
import Scripts.Retrival.analysis as analysis
import Scripts.Retrival.projection as projection
import Scripts.Retrival.search as search
import Scripts.Retrival.selection as selection
from termcolor import colored


def main(username, password):
    print(colored("Which of the following Retrivals would you like to perform?",
                  'cyan', attrs=['bold']))
    print(colored("""1. Selection
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
		Subscribers for a given Issue.""", 'yellow'))
    print(colored("""2. Projection
		Issues in a Volume.
		Articles with a particular category.
		Sort Articles by name.
		Show Cartoons with a particular Tag.
		Subscribers with a particular subscription type.""", 'yellow'))
    print(colored("""3. Aggregate
		Average number of subscribers for a Volume.
		Total number of articles in a Volume.
		Subscription Change between two given dates""", 'yellow'))
    print(colored("""4. Search
		Search Articles by name.
		Search Members by name""", 'yellow'))
    print(colored("""5. Analysis
		Most frequent category of Articles written by each Author.
		List of subscribers who subscribed between two consecutive Volumes.""", 'yellow'))

    ch = int(input(colored("Enter choice: ", 'green')))
    tmp = sp.call('clear', shell=True)

    if ch == 1:
        print(colored("Which of the following Selections would you like to perform?",
                      'cyan', attrs=['bold']), end='')
        print(colored("""
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
			14.Subscribers for a given Issue.""", 'yellow'))

        ch2 = int(input(colored("Enter choice: ", 'green')))
        tmp = sp.call('clear', shell=True)

        #
        #
        if ch2 == 1:
            selection.list_all_issues(username, password)

        elif ch2 == 2:
            selection.list_all_articles(username, password)

        elif ch2 == 3:
            selection.list_all_authors(username, password)

        elif ch2 == 4:
            selection.articles_from_a_particular_magazine_issue(
                username, password)

        elif ch2 == 5:
            selection.list_of_all_articles_written_by_an_author(
                username, password)

        elif ch2 == 6:
            selection.list_all_editors(username, password)

        elif ch2 == 7:
            selection.list_of_all_articles_edited_by_an_editor(
                username, password)

        elif ch2 == 8:
            selection.list_all_designers(username, password)

        elif ch2 == 9:
            selection.list_of_all_articles_designed_by_a_designer(
                username, password)

        elif ch2 == 10:
            selection.show_cartoons_by_designer(username, password)

        elif ch2 == 11:
            selection.show_cartoons_from_a_particular_issue(username, password)

        elif ch2 == 12:
            selection.show_cartoons_from_a_particular_volume(
                username, password)

        elif ch2 == 13:
            selection.subscribers_for_a_given_volume(username, password)

        elif ch2 == 14:
            selection.subscribers_for_a_given_issue(username, password)

        else:
            return
        #
        #

    elif ch == 2:
        print(colored("Which of the following Projections would you like to perform?",
                      'cyan', attrs=['bold']), end='')
        print(colored("""
			1. Issues in a Volume.
			2. Articles with a particular category.
			3. Sort Articles by name.
			4. Show Cartoons with a particular Tag.
			5. Subscribers with a particular subscription type""", 'yellow'))

        ch2 = int(input(colored("Enter choice: ", 'green')))
        tmp = sp.call('clear', shell=True)

        #
        #
        if ch2 == 1:
            projection.issues_in_a_volume(username, password)

        elif ch2 == 2:
            projection.articles_with_a_particular_category(username, password)

        elif ch2 == 3:
            projection.sort_articles_by_name(username, password)

        elif ch2 == 4:
            projection.show_cartoons_with_a_particular_tag(username, password)

        elif ch2 == 5:
            projection.subscribers_with_a_particular_subscription_type(
                username, password)

        else:
            return
        #
        #

    elif ch == 3:
        print(colored("Which of the following Aggregates would you like to perform?",
                      'cyan', attrs=['bold']), end='')
        print(colored("""
			1. Average number of subscribers for a Volume.
			2. Total number of articles in a Volume.
			3. Subscription Change between two given dates.""", 'yellow'))

        ch2 = int(input(colored("Enter choice: ", 'green')))
        tmp = sp.call('clear', shell=True)

        #
        #
        if ch2 == 1:
            aggregate.average_number_of_subscribers_for_a_volume()

        elif ch2 == 2:
            aggregate.total_number_of_articles_in_a_volume()

        elif ch2 == 3:
            aggregate.subscription_change_between_two_given_dates()

        else:
            return
        #
        #

    elif ch == 4:
        print(colored("Which of the following Searches would you like to perform?",
                      'cyan', attrs=['bold']), end='')
        print(colored("""
			1. Search Articles by name.
			2. Search Members by name""", 'yellow'))

        ch2 = int(input(colored("Enter choice: ", 'green')))
        tmp = sp.call('clear', shell=True)

        #
        #
        if ch2 == 1:
            search.search_articles_by_name()

        elif ch2 == 2:
            search.search_members_by_name()

        else:
            return
        #
        #

    elif ch == 5:
        print(colored("Which of the following Analysis would you like to perform?",
                      'cyan', attrs=['bold']), end='')
        print(colored("""
			1. Most frequent category of Articles written by each Author.
			2. List of subscribers who subscribed between two consecutive Volumes.""", 'yellow'))

        ch2 = int(input(colored("Enter choice: ", 'green')))
        tmp = sp.call('clear', shell=True)

        #
        #
        if ch2 == 1:
            analysis.most_frequent_category_of_articles_written_by_each_author()

        elif ch2 == 2:
            analysis.list_of_subscribers_who_subscribed_between_two_consecutive_volumes()

        else:
            return
        #
        #

    else:
        return
