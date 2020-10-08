import pymysql
import pymysql.cursors
from tabulate import tabulate


def db_con(username, password, query):
    db = pymysql.connect("localhost", username, password, "data_kedavra")
    with db.cursor() as cur:
        cur.execute(query)
        data = cur.fetchall()

    return data


def search_articles_by_name(username, password):
    search = input("Search Article: ")
    query = "SELECT volume_no, issue_no, title, category FROM ARTICLE WHERE TITLE LIKE'%" + search + "%';"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Vol No', 'Issue No', 'Title', 'Category'], tablefmt='psql'))


def search_members_by_name(username, password):
    search = input("Search Member: ")
    query = "SELECT member_id, f_name, m_name, l_name, email, join_date FROM MEMBERS WHERE F_NAME LIKE '%" + \
        search + "%' OR M_NAME LIKE '%" + search + \
            "%' OR L_NAME LIKE '%" + search + "%';"
    table = db_con(username, password, query)
    print(tabulate(table, headers=[
          'Member ID', 'First Name', 'Middle Name', 'Last Name', 'E-mail', 'Date of Joining'], tablefmt='psql'))
