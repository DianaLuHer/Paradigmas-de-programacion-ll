from mysql.connector import pooling, Error

class Conexion:
    pool = None

    # Indica que no se requiere crear un objeto
    @classmethod
    def get_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    host="localhost",
                    user="root",
                    password="root",
                    database="Video_juego",
                    pool_name="video_juego_pool",
                    pool_size=5
                )
                print("Pool creado")
                return cls.pool
            except Error as e:
                print(f"Error al crear el pool: {e}")
        else:
            return cls.pool
    @classmethod
    def get_conexion(cls):
        return cls.get_pool().get_connection()
