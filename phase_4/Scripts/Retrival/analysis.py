import pymysql
import pymysql.cursors
from tabulate import tabulate


def db_con(username, password, query):
    db = pymysql.connect("localhost", username, password, "data_kedavra")
    with db.cursor() as cur:
        cur.execute(query)
        data = cur.fetchall()

    return data


def most_frequent_category_of_articles_written_by_each_author():
    pass


def list_of_subscribers_who_subscribed_between_two_consecutive_volumes():
    pass
