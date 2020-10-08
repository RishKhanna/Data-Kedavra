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
    pass


def sort_articles_by_name(username, password):
    pass


def show_cartoons_with_a_particular_tag(username, password):
    pass


def subscribers_with_a_particular_subscription_type(username, password):
    pass
