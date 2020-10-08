import pymysql
import pymysql.cursors
from tabulate import tabulate


def db_con(username, password, query):
    db = pymysql.connect("localhost", username, password, "data_kedavra")
    with db.cursor() as cur:
        cur.execute(query)
        data = cur.fetchall()

    return data


def average_number_of_subscribers_for_a_volume():
    pass


def total_number_of_articles_in_a_volume():
    pass


def subscription_change_between_two_given_dates():
    pass
