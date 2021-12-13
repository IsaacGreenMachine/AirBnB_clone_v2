#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import environ

try:
    if environ['HBNB_TYPE_STORAGE'] == "db":
        from models.engine.db_storage import DBStorage
        storage = DBStorage()
    else:
        from models.engine.file_storage import FileStorage
        storage = FileStorage()
except KeyError:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
# except KeyError:
#     print("environment variable HBNB_TYPE_STORAGE failed")
except Exception as ex:
    print("error in init with import or DBstorage")
    print(ex.args)
finally:
    storage.reload()
