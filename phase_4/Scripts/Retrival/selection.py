import pymysql
import pymysql.cursors
from tabulate import tabulate


def db_con(username, password, query):
    db = pymysql.connect("localhost", username, password, "data_kedavra")
    with db.cursor() as cur:
        cur.execute(query)
        data = cur.fetchall()

    return data


def list_all_issues(username, password):
    query = "SELECT * FROM MAGAZINE;"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Volume No', 'Issue No', 'Publication Date'], tablefmt='psql'))


def list_all_articles(username, password):
    query = "SELECT volume_no, issue_no, title, category FROM MAGAZINE;"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Vol No', 'Issue No', 'Title', 'Category'], tablefmt='psql'))


def list_all_authors(username, password):
    query = "SELECT id, f_name, m_name, l_name, languages, email, join_date FROM author INNER JOIN Members on id=member_id;"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Author ID', 'First Name', 'Middle Name', 'Last Name', 'Languages', 'E-mail', 'Date of Joining'], tablefmt='psql'))


def articles_from_a_particular_magazine_issue(username, password):
    pass


def list_of_all_articles_written_by_an_author(username, password):
    id = input("Enter Author ID: ")
    # Todo


def list_all_editors(username, password):
    query = "SELECT id, f_name, m_name, l_name, genres, email, join_date FROM editor INNER JOIN Members on id=member_id;"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Editor ID', 'First Name', 'Middle Name', 'Last Name', 'Genres', 'E-mail', 'Date of Joining'], tablefmt='psql'))


def list_of_all_articles_edited_by_an_editor(username, password):
    pass


def list_all_designers(username, password):
    query = "SELECT id, f_name, m_name, l_name, softwaress, email, join_date FROM designer INNER JOIN Members on id=member_id;"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Designer ID', 'First Name', 'Middle Name', 'Last Name', 'Softwares', 'E-mail', 'Date of Joining'], tablefmt='psql'))


def list_of_all_articles_designed_by_a_designer(username, password):
    pass


def show_cartoons_by_designer(username, password):
    pass


def show_cartoons_from_a_particular_issue(username, password):
    pass


def show_cartoons_from_a_particular_volume(username, password):
    pass


def subscribers_for_a_given_volume(username, password):
    pass


def subscribers_for_a_given_issue(username, password):
    pass
