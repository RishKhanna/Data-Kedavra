import pymysql
import pymysql.cursors
from tabulate import tabulate


def db_con(username, password, query):
    db = pymysql.connect("localhost", username, password, "data_kedavra")
    with db.cursor() as cur:
        cur.execute(query)
        data = cur.fetchall()

    return data


def average_number_of_subscribers_for_a_volume(username, password):
    qr1 = "CREATE VIEW SUB AS SELECT VOLUME, COUNT(SUBSCRIBER) AS NUM FROM SUBSCRIBES GROUP BY VOLUME;"
    qr2 = "SELECT * FROM SUB;"
    qr3 = "SELECT AVG(NUM) FROM SUB;"
    qr4 = "DROP VIEW SUB;"
    db_con(username, password, qr1)
    table = db_con(username, password, qr2)
    result = db_con(username, password, qr3)
    db_con(username, password, qr4)
    print(tabulate(table, headers=[
          'Volume No', 'Subscriber Count'], tablefmt='psql'))
    print("Average Number of Subscribers: " + str(float(result[0][0])))


def total_number_of_articles_in_a_volume(username, password):
    query = "SELECT VOLUME_NO, COUNT(VOLUME_NO) AS ARTICLES FROM CONTRIBUTE GROUP BY VOLUME_NO;"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Volume No', 'Article Count'], tablefmt='psql'))


def subscription_change_between_two_given_dates(username, password):
    date1 = input("Enter First Date (YYYY-MM-DD): ")
    date2 = input("Enter Second Date (YYYY-MM-DD): ")
    query = "SELECT SUB_DATE, F_NAME, M_NAME, L_NAME, EMAIL FROM SUBSCRIBERS WHERE SUB_DATE > '" + \
        date1 + "' AND SUB_DATE <= '" + date2 + "' ORDER BY SUB_DATE;"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Subscription Date', 'First Name', 'Middle Name', 'Last Name', 'E-Mail'], tablefmt='psql'))
