import time
import sqlite3 as sql
# def createDB():# Crear o conectar a la BD 'autoconocimiento.db'
#     conn = sql.connect("autoconocimientoJuanDiego.db")
#     print("Base de datos creada o conectada correctamente.")
#     conn.close()

# def createTable(): 
#     conn = sql.connect("autoconocimientoJuanDiego.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#                    CREATE TABLE IF NOT EXISTS users (
#                     user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     full_name TEXT NOT NULL,
#                     email TEXT UNIQUE NOT NULL,
#                     password_hash TEXT NOT NULL,
#                     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#                     ); """)
#     print("tabla creada exitosamente")    

def insertrow(user_id, full_name, email, password_hash, created_at):
    try:
        conn = sql.connect("autoconocimientoJuanDiego.db")
        cursor = conn.cursor()
        instruction = f"INSERT INTO users VALUES('{user_id}', '{full_name}', '{email}', '{password_hash}', '{created_at}')"
        cursor.execute(instruction)
        conn.commit()
        print("Datos insertados correctamente")
    except sql.operationalError as e:
        time.sleep(1)
        insertrow(user_id, full_name, email, password_hash, created_at)
    finally:
        conn.close()

def readrow():
    conn = sql.connect("autoconocimientoJuanDiego.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM users"
    cursor.execute(instruction)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

if __name__ == "__main__":
    #createDB()     # Primero creamos la base de datos
    #createTable()
    #insertrow(1, "Juan Diego", "juan@gmail.com", "123456", "2023-01-01")
    readrow()