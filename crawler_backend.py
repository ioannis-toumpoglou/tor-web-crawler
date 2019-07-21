######################################################################
##                                                                  ##
##  DATABASE THAT HOLDS RECORDS OF THE URLS AND THEIR TEXT CONTENT  ##
##                                                                  ##
######################################################################


import sqlite3
from time import sleep

def connect():
    sleep(2)
    conn = sqlite3.connect('crawler_database.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY, url TEXT, status TEXT)")       # Create the table that contains the list of urls
    cur.execute("CREATE TABLE IF NOT EXISTS page_content (id INTEGER PRIMARY KEY, url TEXT, threat_type TEXT, html_code TEXT, text TEXT)")     # Create the table that contains the HTML code plus the text content
    conn.commit()
    conn.close()

def insert_page(url):
    conn = sqlite3.connect('crawler_database.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO urls VALUES (NULL, ?, NULL)", (url,))
    conn.commit()
    conn.close()

def insert_status(url, status):
    conn = sqlite3.connect('crawler_database.db')
    cur = conn.cursor()
    cur.execute("UPDATE urls SET status=? WHERE url=?", (status,url))
    conn.commit()
    conn.close()

def insert_content(url, html_code):
    conn = sqlite3.connect('crawler_database.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO page_content VALUES (NULL, ?, NULL, ?, NULL)", (url, html_code))
    conn.commit()
    conn.close()

def insert_threat_type(url, threat_type):
    conn = sqlite3.connect('crawler_database.db')
    cur = conn.cursor()
    cur.execute("UPDATE page_content SET threat_type=? WHERE url=?", (threat_type,url))
    conn.commit()
    conn.close()

def insert_text(url, text):
    conn = sqlite3.connect('crawler_database.db')
    cur = conn.cursor()
    cur.execute("UPDATE page_content SET text=? WHERE url=?", (text, url))
    conn.commit()
    conn.close()

def check_url(url):
    conn = sqlite3.connect('crawler_database.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM urls WHERE url=?", (url,))
    data = cur.fetchone()
    if data is not None:
        return True
    conn.commit()
    conn.close()

def check_url_content(url):
    conn = sqlite3.connect('crawler_database.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM page_content WHERE url=?", (url,))
    data = cur.fetchone()
    if data is not None:
        return True
    conn.commit()
    conn.close()

def view_urls():
    conn = sqlite3.connect('crawler_database.db')
    cur = conn.cursor()
    cur.execute("SELECT url FROM urls")
    rows = cur.fetchall()
    conn.close()
    return rows

def view_content():
    conn = sqlite3.connect('crawler_database.db')
    cur = conn.cursor()
    cur.execute("SELECT url FROM page_content")
    rows = cur.fetchall()
    conn.close()
    return rows

def page_content():
    conn = sqlite3.connect('crawler_database.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM page_content")
    rows = cur.fetchall()
    conn.close()
    return rows

def get_links_second():
    conn = sqlite3.connect('crawler_database_2.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM urls")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(url="", html_code=""):
    conn = sqlite3.connect('crawler_database.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM page_content WHERE url=? OR content=?", (url, html_code))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(url):
    conn = sqlite3.connect('crawler_database.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM urls WHERE url=?",(url,))
    cur.execute("DELETE FROM page_content WHERE url=?",(url,))
    conn.commit()
    conn.close()

def update(id, url, html_code):
    conn = sqlite3.connect('crawler_database.db')
    cur = conn.cursor()
    cur.execute("UPDATE page_content SET url=?, content=? WHERE id=?",(url, html_code, id))
    conn.commit()
    conn.close()

connect()
