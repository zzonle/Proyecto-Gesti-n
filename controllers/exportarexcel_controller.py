import pandas as pd
from sqlalchemy import create_engine
from config.database import db_config


class ExportarExcel():
    def __init__(self):
        self.db_config = db_config
        
    def conectar(self):
        return create_engine(f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}")
    
    def exportar(self):
        query = """
                SELECT 
                    e.id AS ID,
                    e.nombre AS NOMBRE,
                    e.rut AS RUT,
                    d.nombre AS DEPARTAMENTO,
                    p.nombre_proyecto AS PROYECTO,
                    rt.fecha AS "FECHA REGISTRO",
                    rt.horas AS "HORAS TRABAJADAS",
                    rt.descripcion AS "DESCRIPCIÓN"
                FROM 
                    empleado e
                LEFT JOIN 
                    departamento d ON e.departamento_id = d.id
                LEFT JOIN 
                    registro_tiempo rt ON e.id = rt.empleado_id
                LEFT JOIN 
                    proyecto p ON rt.proyecto_id = p.proyecto_id;
                """
        with self.conectar().connect() as connection:
            return pd.read_sql(query, con=connection)