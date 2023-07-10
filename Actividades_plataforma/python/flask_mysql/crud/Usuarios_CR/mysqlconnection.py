# un cursor es el objeto que usamos para interactuar con la base de datos
import pymysql.cursors

# esta clase nos dará una instancia de una conexión a nuestra base de datos
class MySQLConnection:
    def __init__(self, db):
        # cambiar el usuario y la contraseña según sea necesario
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='root',
                                    db=db,
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor,
                                    autocommit=True)
        # establecer la conexión a la base de datos
        self.connection = connection

    # el método para consultar o actualizar la base de datos
    def execute_query(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
                if query.lower().startswith(("select", "show", "describe")):
                    # consulta de selección
                    cursor.execute(query, data)
                    result = cursor.fetchall()
                    return result
                else:
                    # consulta de actualización
                    cursor.execute(query, data)
                    self.connection.commit()
                    affected_rows = cursor.rowcount
                    return affected_rows
            except Exception as e:
                # si la consulta falla, el método devolverá FALSE
                print("Something went wrong:", e)
                return False

    def close(self):
        # cerrar la conexión
        self.connection.close()

# connectToMySQL recibe la base de datos que estamos usando y la usa para crear una instancia de MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)