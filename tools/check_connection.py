import os
from sqlalchemy import create_engine, text

qea_path = "[# Adjust this path]"

if not os.path.exists(qea_path):
    print(f"ERROR: el archivo no existe en esta ruta: {qea_path}")
else:
    print(f"Archivo encontrado, tamaño: {os.path.getsize(qea_path)} bytes")

    engine = create_engine(f"sqlite:///{qea_path}")
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT Object_ID, Name, Object_Type FROM t_object LIMIT 10")
        )
        rows = result.fetchall()
        print(f"Filas encontradas: {len(rows)}")
        for row in rows:
            print(row)