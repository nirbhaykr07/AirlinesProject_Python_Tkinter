1.  Install Python v3.7.4 from the following path: https://www.python.org/ftp/python/3.7.4/python-3.7.4.exe
2.  Set Python path in System Env variable. Ex: C:\Users\username\AppData\Local\Programs\Python\Python37-32
3.  Set pip path in system Env variable. Ex: C:\Users\username\AppData\Local\Programs\Python\Python37-32\Scripts
4.  Create project folder in system.
5.  Copy the downloaded files in project folder and open that project path in command mode.
6.  Run the following command to install calendar package used in the project: pip install tkcalendar
7.  Install SQLite3 from the following path: https://www.sqlite.org/2019/sqlite-tools-win32-x86-3300100.zip
8.  Copy the contents of the extracted SQL files in the project folder.
9.  Download SQLite DB browser from the following path: https://download.sqlitebrowser.org/SQLiteDatabaseBrowserPortable_3.11.2_English.paf.exe
10. Run the SQLite DB browser and create tables and insert flight table records from "sql_cmds.sql" in the DB(DB name is test2.DB in the project) or use the sample DB attached.
11. Run the python project using the following command in command prompt: Python Airlines.py

Note:

1. Limitation: There is only one flight for a particular route(The code can be changed to allow multiple options for a route.)
2. Mail me on nirbay.kr07@gmail.com for any request/suggestion/query.