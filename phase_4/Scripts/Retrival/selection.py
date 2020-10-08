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
    query = "SELECT volume_no, issue_no, title, category FROM ARTICLE;"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Vol No', 'Issue No', 'Title', 'Category'], tablefmt='psql'))


def list_all_authors(username, password):
    query = "SELECT id, f_name, m_name, l_name, languages, email, join_date FROM author INNER JOIN Members on id=member_id;"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Author ID', 'First Name', 'Middle Name', 'Last Name', 'Languages', 'E-mail', 'Date of Joining'], tablefmt='psql'))


def articles_from_a_particular_magazine_issue(username, password):
    vol_id = input("Enter Volume No.: ")
    iss_id = input("Enter Issue No.: ")
    query = "SELECT VOLUME_NO, ISSUE_NO, TITLE, CATEGORY FROM ARTICLE WHERE VOLUME_NO=" + \
        vol_id+" AND ISSUE_NO="+iss_id+";"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Vol No', 'Issue No', 'Title', 'Category'], tablefmt='psql'))


def list_of_all_articles_written_by_an_author(username, password):
    id = input("Enter Author ID: ")
    query = "SELECT ARTICLE.VOLUME_NO, ARTICLE.ISSUE_NO, TITLE, CATEGORY FROM CONTRIBUTE INNER JOIN ARTICLE ON (CONTRIBUTE.VOLUME_NO, CONTRIBUTE.ISSUE_NO, CONTRIBUTE.PAGE_NO) = (ARTICLE.VOLUME_NO, ARTICLE.ISSUE_NO, ARTICLE.PAGE_NO) WHERE AUTHOR_ID=" + id + ";"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Vol No', 'Issue No', 'Title', 'Category'], tablefmt='psql'))


def list_all_editors(username, password):
    query = "SELECT id, f_name, m_name, l_name, genres, email, join_date FROM editor INNER JOIN Members on id=member_id;"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Editor ID', 'First Name', 'Middle Name', 'Last Name', 'Genres', 'E-mail', 'Date of Joining'], tablefmt='psql'))


def list_of_all_articles_edited_by_an_editor(username, password):
    id = input("Enter Editor ID: ")
    query = "SELECT ARTICLE.VOLUME_NO, ARTICLE.ISSUE_NO, TITLE, CATEGORY FROM CONTRIBUTE INNER JOIN ARTICLE ON (CONTRIBUTE.VOLUME_NO, CONTRIBUTE.ISSUE_NO, CONTRIBUTE.PAGE_NO) = (ARTICLE.VOLUME_NO, ARTICLE.ISSUE_NO, ARTICLE.PAGE_NO) WHERE EDITOR_ID="+id+";"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Vol No', 'Issue No', 'Title', 'Category'], tablefmt='psql'))


def list_all_designers(username, password):
    query = "SELECT id, f_name, m_name, l_name, softwaress, email, join_date FROM designer INNER JOIN Members on id=member_id;"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Designer ID', 'First Name', 'Middle Name', 'Last Name', 'Softwares', 'E-mail', 'Date of Joining'], tablefmt='psql'))


def list_of_all_articles_designed_by_a_designer(username, password):
    id = input("Enter Designer ID: ")
    query = "SELECT ARTICLE.VOLUME_NO, ARTICLE.ISSUE_NO, TITLE, CATEGORY FROM CONTRIBUTE INNER JOIN ARTICLE ON (CONTRIBUTE.VOLUME_NO, CONTRIBUTE.ISSUE_NO, CONTRIBUTE.PAGE_NO) = (ARTICLE.VOLUME_NO, ARTICLE.ISSUE_NO, ARTICLE.PAGE_NO) WHERE DESIGNER_ID="+id+";"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Vol No', 'Issue No', 'Title', 'Category'], tablefmt='psql'))


def show_cartoons_by_designer(username, password):
    id = input("Enter Designer ID: ")
    query = "SELECT CARTOON.VOLUME_NO, CARTOON.ISSUE_NO, CAPTION, IMAGE_URL, TAGS FROM DRAWS INNER JOIN CARTOON ON DRAWS.CARTOON=CARTOON.IMAGE_URL WHERE DESIGNER_ID="+id+";"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Vol No', 'Issue No', 'Caption', 'Cartoon URL', 'Tags'], tablefmt='psql'))


def show_cartoons_from_a_particular_issue(username, password):
    vol_id = input("Enter Volume No.: ")
    iss_id = input("Enter Issue No.: ")
    query = "SELECT VOLUME_NO, ISSUE_NO, CAPTION, IMAGE_URL, TAGS FROM CARTOON WHERE VOLUME_NO=" + \
        vol_id+" AND ISSUE_NO="+iss_id+";"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Vol No', 'Issue No', 'Caption', 'Cartoon URL', 'Tags'], tablefmt='psql'))


def show_cartoons_from_a_particular_volume(username, password):
    vol_id = input("Enter Volume No.: ")
    query = "SELECT VOLUME_NO, ISSUE_NO, CAPTION, IMAGE_URL, TAGS FROM CARTOON WHERE VOLUME_NO="+vol_id+";"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Vol No', 'Issue No', 'Caption', 'Cartoon URL', 'Tags'], tablefmt='psql'))


def subscribers_for_a_given_volume(username, password):
    vol_id = input("Enter Volume No.: ")
    query = "SELECT F_NAME, M_NAME, L_NAME, EMAIL, SUB_TYPE FROM SUBSCRIBERS INNER JOIN SUBSCRIBES ON SUBSCRIBERS.EMAIL=SUBSCRIBES.SUBSCRIBER WHERE VOLUME <="+vol_id+";"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'First Name', 'Middle Name', 'Last Name', 'E-Mail', 'Subscription Type'], tablefmt='psql'))


def subscribers_for_a_given_issue(username, password):
    vol_id = input("Enter Volume No.: ")
    iss_id = input("Enter Issue No.: ")
    query = "SELECT F_NAME, M_NAME, L_NAME, EMAIL, SUB_TYPE FROM SUBSCRIBERS INNER JOIN SUBSCRIBES ON SUBSCRIBERS.EMAIL=SUBSCRIBES.SUBSCRIBER WHERE VOLUME <" + \
        vol_id+" OR (VOLUME="+vol_id+" AND ISSUE<="+iss_id+");"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'First Name', 'Middle Name', 'Last Name', 'E-Mail', 'Subscription Type'], tablefmt='psql'))
