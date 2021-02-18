import json
import pyodbc

import config as cfg


def request_GET():
    print(cfg.DRIVER)
    connection = pyodbc.connect(cfg.DRIVER + cfg.SERVER + cfg.DATABASE + cfg.IS_TRUSTED)
    
    cursor = connection.cursor()
    cursor.execute('SELECT * from AssistantDB.dbo.Assistant FOR JSON AUTO')
    row = cursor.fetchone()

    return row    


def request_POST():
    pass


def request_UPDATE():
    pass


def request_DELETE():
    pass
