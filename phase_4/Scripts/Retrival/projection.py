import pymysql
import pymysql.cursors
from tabulate import tabulate


def db_con(username, password, query):
    db = pymysql.connect("localhost", username, password, "data_kedavra")
    with db.cursor() as cur:
        cur.execute(query)
        data = cur.fetchall()

    return data


def issues_in_a_volume(username, password):
    vol_id = input("Enter Volume No.: ")
    query = "SELECT ISSUE_NO, DATE FROM MAGAZINE WHERE VOLUME_NO="+vol_id+";"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Issue No', 'Publication Date'], tablefmt='psql'))


def articles_with_a_particular_category(username, password):
    cat = input("Enter Category: ")
    query = "SELECT volume_no, issue_no, title, category FROM ARTICLE WHERE CATEGORY LIKE'%" + cat + "%';"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Vol No', 'Issue No', 'Title', 'Category'], tablefmt='psql'))


def sort_articles_by_name(username, password):
    query = "SELECT volume_no, issue_no, title, category FROM ARTICLE ORDER BY TITLE;"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Vol No', 'Issue No', 'Title', 'Category'], tablefmt='psql'))


def show_cartoons_with_a_particular_tag(username, password):
    tag = input("Search Tag: ")
    query = "SELECT VOLUME_NO, ISSUE_NO, CAPTION, IMAGE_URL, TAGS FROM CARTOON WHERE TAGS LIKE'%" + tag + "%';"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Vol No', 'Issue No', 'Caption', 'Cartoon URL', 'Tags'], tablefmt='psql'))


def subscribers_with_a_particular_subscription_type(username, password):
    subtype = input("Subscription Type (1, 2 or 3): ")
    query = "SELECT F_NAME, M_NAME, L_NAME, EMAIL FROM SUBSCRIBERS WHERE SUB_TYPE="+subtype+";"
