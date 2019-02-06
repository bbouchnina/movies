from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import pymysql.cursors


def connect_to_db():
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='movies',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
    return connection


