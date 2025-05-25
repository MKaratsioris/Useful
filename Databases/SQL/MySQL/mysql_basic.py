from MySQL.mysql_utils import connect_to_mysql, create_mysql_database, create_mysql_tables, print_mysql_table, query_error, add_data
from tables import TABLES
from mysql.connector.errors import Error
from datetime import date, datetime, timedelta

USER_NAME = "root"
PASSWORD = "mkar"
HOST = "localhost"
DB_NAME = 'CMF'
TABLE_NAMES = ["employees", "departments", "salaries", "dept_emp", "dept_manager", "titles"]
TABLE_INFOS = {
  "employees": "first_name, last_name, hire_date, gender, birth_date",
  "departments": "dept_no, dept_name",
  "salaries": "emp_no, salary, from_date, to_date",
  "dept_emp": "emp_no, dept_no, from_date, to_date",
  "dept_manager": "emp_no, dept_no, from_date, to_date",
  "titles": "emp_no, title, from_date, to_date"
  }



if __name__ == "__main__":
  tomorrow = datetime.now().date() + timedelta(days=1)
  
  config = {
    'user': USER_NAME,
    'password': PASSWORD,
    'host': HOST,
    'use_pure': False
  }
  
  add_employees_query = f"INSERT INTO {TABLE_NAMES[0]} ({TABLE_INFOS[TABLE_NAMES[0]]}) VALUES (%s, %s, %s, %s, %s)"
  new_employees = [
    ('Geert_01', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 1)),
    ('Geert_02', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 2)),
    ('Geert_03', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 3)),
    ('Geert_04', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 4)),
    ('Geert_05', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 5)),
    ('Geert_06', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 6)),
    ('Geert_07', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 7)),
    ('Geert_08', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 8)),
    ('Geert_09', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 9)),
    ('Geert_10', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 10)),
    ('Geert_11', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 11)),
    ('Geert_12', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 12)),
    ('Geert_13', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 13)),
    ('Geert_14', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14)),
    ]
  
  #add_salaries_query = f"INSERT INTO {TABLE_NAMES[2]} ({TABLE_INFOS[TABLE_NAMES[2]]}) VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)"
  #new_salaries = [
  #  (emp_no, 50000, tomorrow, date(9999, 1, 1)),
  #  ]
  
  
  try:
    mysql_db_connection = connect_to_mysql(config, attempts=3)
    if mysql_db_connection.is_connected():
        with mysql_db_connection.cursor() as cursor:
            create_mysql_database(cursor, DB_NAME)
            create_mysql_tables(cursor, TABLES)
            add_data(mysql_db_connection, cursor, DB_NAME, add_employees_query, new_employees)
            print_mysql_table(cursor, DB_NAME, TABLE_NAMES[0])
    exit(0)
  except Error as err:
    query_error(err, DB_NAME)
    exit(1)
  