import sqlite3


def readTable():
    try:
        sqlite_connection = sqlite3.connect("sqlite_menu.db")
        cursor = sqlite_connection.cursor()
        sqlite_read_query = '''SELECT * FROM menu'''
        cursor.execute(sqlite_read_query)
        record = cursor.fetchall()
        sqlite_connection.commit()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Ошибка: ", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close


def getFood(food):
    try:
        sqlite_connection = sqlite3.connect("sqlite_menu.db")
        cursor = sqlite_connection.cursor()
        sqlite_get_query = '''SELECT type_food, name_food, description FROM menu
                              JOIN food ON menu.type=food.type_food
                              WHERE type = ?'''
        cursor.execute(sqlite_get_query, (food,))
        sqlite_connection.commit()
        records = cursor.fetchall()
        cursor.close()
        for record in records:
            return record[0], record[1], record[2]
    except sqlite3.Error as error:
        print("При работе с SQLite возникла ошибка: ", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


