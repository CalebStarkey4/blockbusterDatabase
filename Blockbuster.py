from xml.dom import minidom
import sqlite3 as sql
import xml.etree.ElementTree as ET
from urllib.request import urlopen
import gc
import mysql.connector

def addRecord():
    print("This is to add a record.")


def dropRecord():
    print("This is to drop a record.")


def updateRecord():
    print("This is to update a record.") 

    
def getRecord():

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Alpay21109.!",
        database="MySQL80"
)

    """db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                        user="root",         # your username
                        passwd="Alpay21109.!",  # your password
                        db="MySQL80")        # name of the data base

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    # Use all the SQL you like
    cur.execute("SELECT * FROM YOUR_TABLE_NAME")

    # print all the first cell of all the rows
    for row in cur.fetchall():
        print(row[0])

    db.close()"""

    """conn = sql.connect("moviesDB.db")
    cur = conn.cursor()

    createTableCommand = CREATE TABLE NSA_DATA (
    username VARCHAR(50),
    phonenumber VARCHAR(15),
    password VARCHAR(50),
    baddeedcount INT,
    secrets VARCHAR(250)
    );

    cur.execute(createTableCommand)
    conn.commit()"""


    

    """dburl = ("http://www.w3.org/2001/XMLSchema-instance")

    root = ET.parse(urlopen(dburl)).getroot()
    cpids = [el.text for el in root.findall('.//user/cpid')]
    print(cpids)

    conn = sql.connect("GridcoinTeam.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS GRIDCOINTEAM (cpid TEXT)''') 
    c.executemany("INSERT INTO GRIDCOINTEAM VALUES (?);", cpids)
    conn.commit()       
    conn.close()

    conn = sql.connect("GridcoinTeam.db")
    c = conn.cursor()
    cpids = c.execute('select cpid from GRIDCOINTEAM').fetchall()
    conn.close()

    print(cpids)

    gc.collect()"""

    

    """rawxml='''<?xml version="1.0" encoding="UTF-8" ?>
    <chat xmlns="http://test.org/net/1.3">
        <event sender="Frank" time="2016-02-03T22:58:19+01:00" />
        <message sender="Karen" time="2016-02-03T22:58:19+01:00">
            <div>
                <span>Hello Frank</span>
            </div>
        </message>
        <message sender="Frank" time="2016-02-03T22:58:39+01:00">
            <div>
                <span>Hi there Karen</span>
            </div>
            <div>
                <span>I'm back from New York</span>
            </div>
        </message>
        <message sender="Karen" time="2016-02-03T22:58:56+01:00">
            <div>
                <span>How are you doing?</span>
                <span>Everything OK?</span>
            </div>
        </message>
    </chat>'''

    ns={'msg' : "http://test.org/net/1.3"}
    xml = ET.fromstring(rawxml)

    for msg in xml.findall("msg:message", ns):
        print("Sender: " + msg.get("sender"))
        print("Time: " + msg.get("time"))
        body=""
        for d in msg.findall("msg:div", ns):
            body = body + ET.tostring(d, encoding="unicode")
        print("Content: " + body)"""


    """file = minidom.parse('movies.xml')

    print(file.firstChild.tagName)

    title = file.getElementByTagName("MOV_ID")
    print("%s fields:", title)"""

    """for skill in title:
        print(skill.getAttribute("name"))"""



    """models = file.getElementsByTagName('row')
    print('\nAll attributes:')
    for elem in models:
        print(elem.attributes['name'].value)

    print('\nmodel #2 data:')
    print(models[0].firstChild.data)

    print('model #2 attribute:')
    print(models[1].attributes['001'].value)"""


def filterRecord():
    print("This is to filter a record.")


getRecord()