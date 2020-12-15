"""
Author: Rawley Collins
Program: db_connection.py

create database to hold information
"""
import sqlite3
from sqlite3 import Error
from customer import Customer
from shoppingCart import ShoppingCart


def create_connection(db):
	try:
		conn = sqlite3.connect(db)
		return conn
	except Error as err:
		print(err)
	return None


def create_table(conn, sql_create_table):
	try:
		c = conn.cursor()
		c.execute(sql_create_table)
	except Error as e:
		print(e)


def create_tables(conn):
	sql_create_customer_table = (""" CREATE TABLE IF NOT EXISTS customer (
                                        firstname text NOT NULL,
                                        lastname text NOT NULL,
                                        username text NOT NULL,
                                        password text NOT NULL
                                    ); """)

	sql_create_items_table = (""" CREATE TABLE IF NOT EXISTS items (
                                    id integer PRIMARY KEY,
                                    major text NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text,
                                    FOREIGN KEY (id) REFERENCES customer (id)
                                );""")
	if conn is not None:
		# create projects table
		create_table(conn, sql_create_customer_table)
		# create tasks table
		create_table(conn, sql_create_items_table)
	else:
		print("Unable to connect")


def insert_customer(conn, person): # needs work
	"""Create a new person for table
    :param conn:
    :param person:
    :return: person id
    """
	sql = ''' INSERT INTO person(firstname,lastname)
              VALUES(?,?,?,?) '''
	cur = conn.cursor()  # cursor object
	cur.execute(sql, person)
	return cur.lastrowid # returns the row id of the cursor object, the person id


def get_customer_by_username_and_password(username, password):
	c = conn.cursor()
	c.execute("SELECT * FROM customer WHERE username='username' AND password='password'", {'username': username, 'password': password})
	return c.fetchone()


def update_cart_add_item():
	pass


def remove_customer():
	with conn:
		c = conn.cursor()
		c.execute("DELETE FROM customer WHERE username= :username' AND password= :password'")


if __name__ == '__main__':
	#create_tables("pythonsqlite.db")

	conn = create_connection("studentDBMS.db")

	with conn:
		customer_1 = Customer("John", "Winchester", "Johnathan", "45564")
		person_id = insert_customer(conn, customer_1)

		student = (person_id, 'Songwriting', '2000-01-01')
		student_id = update_cart_add_item(conn, )

	with conn:
		rows = select_all_persons(conn)
		for row in rows:
			print(row)