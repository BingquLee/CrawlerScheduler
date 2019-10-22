# -*- coding: utf-8 -*-
import os
print(os.path.dirname(os.path.abspath(__file__)))
import sqlite3


conn = sqlite3.connect(r'E:\Documents\PythonProjects\CrawlerScheduler\db.sqlite3')

