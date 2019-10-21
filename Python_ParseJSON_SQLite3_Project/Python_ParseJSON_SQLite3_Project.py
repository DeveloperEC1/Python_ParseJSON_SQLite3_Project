import urllib.request
import json 
import sqlite3

API_KEY = "4e0be2c22f7268edffde97481d49064a"

with urllib.request.urlopen("https://api.themoviedb.org/3/search/movie?/&query=Movie&api_key=" + API_KEY + "&language=en-US") as url:
    data = json.loads(url.read().decode())

    if data != "":
        print("Getting information starts...\n")

    for x in data["results"]:
        print("Title: " + x["title"] + "\n" + "Overview: " + x["overview"] + "\n" + "Vote Average: " + str(x["vote_average"]) + "\n")
        continue
    print("Getting information finished...\n\n")

def create_table():
    conn = sqlite3.connect("myDatabase.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS preson (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(first_name, last_name, age):
    conn = sqlite3.connect("myDatabase.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO preson VALUES(?,?,?)", (first_name, last_name, age))
    conn.commit()
    conn.close()

def delete_all_tasks(conn):
    sql = "DELETE FROM preson"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def view():
    database = "myDatabase.db"
    conn = create_connection(database)
    with conn:
        create_table()
        delete_all_tasks(conn);
        insert("Elior", "Cohen", 23)
    conn = sqlite3.connect('myDatabase.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM preson")
    rows = cur.fetchall()
    return rows
    conn.close()

def main():
    print(view())

if __name__ == '__main__':
    main()
