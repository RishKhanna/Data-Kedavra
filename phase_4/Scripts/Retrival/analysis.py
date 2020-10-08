import pymysql
import pymysql.cursors
from tabulate import tabulate


def db_con(username, password, query):
    db = pymysql.connect("localhost", username, password, "data_kedavra")
    with db.cursor() as cur:
        cur.execute(query)
        data = cur.fetchall()

    return data


def most_frequent_category_of_articles_written_by_each_author(username, password):
    id = input("Enter Author ID: ")
    query = "SELECT CATEGORY FROM CONTRIBUTE INNER JOIN ARTICLE ON (CONTRIBUTE.VOLUME_NO, CONTRIBUTE.ISSUE_NO, CONTRIBUTE.PAGE_NO) = (ARTICLE.VOLUME_NO, ARTICLE.ISSUE_NO, ARTICLE.PAGE_NO) WHERE AUTHOR_ID=" + \
        id + " GROUP BY CATEGORY ORDER BY COUNT(CATEGORY) DESC LIMIT 1;"
    result = db_con(username, password, query)
    print("Most frequent category: " + result[0][0])


def list_of_subscribers_who_subscribed_between_two_consecutive_volumes(username, password):
    vol_id = int(input("First Volume: "))+1
    print("Second Volume: " + str(vol_id))
    query = "SELECT SUB_DATE, F_NAME, M_NAME, L_NAME, EMAIL FROM SUBSCRIBERS INNER JOIN SUBSCRIBES ON SUBSCRIBERS.EMAIL=SUBSCRIBES.SUBSCRIBER WHERE VOLUME =" + \
        str(vol_id)+" ORDER BY SUB_DATE;"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Subscription Date', 'First Name', 'Middle Name', 'Last Name', 'E-Mail'], tablefmt='psql'))
