import sqlite3


def readTable():
    try:
        sqlite_connection = sqlite3.connect("sqlite_telephones.db")
        cursor = sqlite_connection.cursor()
        sqlite_read_query = '''SELECT * FROM telephones'''
        cursor.execute(sqlite_read_query)
        record = cursor.fetchmany(3)
        sqlite_connection.commit()
        cursor.close()
        return record[0], record[1], record[2]
    except sqlite3.Error as error:
        print("Ошибка: ", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close


