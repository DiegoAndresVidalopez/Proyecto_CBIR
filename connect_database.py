import mysql.connector

class ConnectDatabase:
    def __init__(self):
        self._host = "127.0.0.1"
        self._port = 3306
        self._user = "root"
        self._password = "root"
        self._database = "bdcbir"
        self.con = None
        self.cursor = None

    def connect_db(self):
        #establece la conecccion con la base de datos
        self.con = mysql.connector.connect(
            host= self._host,
            port = self._port,
            database = self._database,
            user = self._user,
            password=self._password
        )
    
        #creamos un cursor para ejecutar las consultas sql 
        self.cursor = self.con.cursor(dictionary=True)


    def insert_image(self,imagenSRC,vectorCaracteristicas,categoria):
        #iniciamos la coneccion con la base de datos
        self.connect_db()

        #construimos la consulta con los parametros pasados en la funcion
        sql = f"""
                INSERT INTO imagenes (imagen,vector_caracteristicas,categoria_id)
                VALUES ('{imagenSRC}','{vectorCaracteristicas}',{categoria});
        """

        try:
            #ejecuta el query para agregar la informacion 
            self.cursor.execute(sql)
            self.con.commit()
        
        except Exception as E:
            #se hace un rollback en caso de que alla un error
            self.con.rollback()
            return E
        
        finally:
            #cerramos la coneccion
            self.con.close()
        


