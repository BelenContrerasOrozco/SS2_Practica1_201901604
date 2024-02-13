# etl.py
import pyodbc
import pandas as pd

# Conexión a SQL Server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost\SQLEXPRESS;'
                      'Database=TsunamiDatabase_Practica1;'
                      'Trusted_Connection=yes;')

#borrar el modelo
def borrar_modelo():
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS Tsunamis;')
    cursor.commit()
    print("Modelo borrado con éxito.")

#crear el modelo
def crear_modelo():
    
    print("Modelo creado con éxito.")

#extraer informacion
def extraer_informacion(ruta_archivos):
    
    print(f"Información extraída de {ruta_archivos}.")

#cargar informacion
def cargar_informacion():
    
    print("Información cargada con éxito.")

#consultas
def realizar_consultas():

    conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=localhost\SQLEXPRESS;'
                      'DATABASE=TsunamiDatabase_Practica1;'
                      'Trusted_Connection=yes;')

    cursor = conn.cursor()

    #menu 
    while True:
        print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("\nSeleccione una opción:")
        print("1) SELECT COUNT(*) de todas las tablas")
        print("2) Cantidad de tsunamis por año")
        print("3) Tsunamis por país y años")
        print("4) Promedio de Total Damage por país")
        print("5) Top 5 de países con más muertes")
        print("6) Top 5 de años con más muertes")
        print("7) Top 5 de años que más tsunamis han tenido")
        print("8) Top 5 de países con mayor número de casas destruidas")
        print("9) Top 5 de países con mayor número de casas dañadas")
        print("10) Promedio de altura máxima del agua por cada país")
        print("x) Salir")

        opcion2 = input("Opción: ").lower()

        if opcion2 == '1':
            # 1. SELECT COUNT(*) de todas las tablas
            cursor.execute("SELECT (SELECT COUNT(*) FROM dbo.Worksheet$) as TotalTsunamis;")
            print(cursor.fetchone())
            input("Presiona ENTER para continuar...")
        elif opcion2 == '2':
            # 2. Cantidad de tsunamis por año
            cursor.execute("SELECT Year, COUNT(*) as CantidadTsunamis FROM dbo.Worksheet$ GROUP BY Year ORDER BY Year;")
            print(cursor.fetchall())
            input("Presiona ENTER para continuar...")
        elif opcion2 == '3':
            # 3. Tsunamis por país y años
            cursor.execute("SELECT Country, MAX(CASE WHEN rn = 1 THEN Year END) AS Año1, MAX(CASE WHEN rn = 2 THEN Year END) AS Año2, MAX(CASE WHEN rn = 3 THEN Year END) AS Año3 FROM (  SELECT     Country,    Year,    ROW_NUMBER() OVER (PARTITION BY Country ORDER BY Year) AS rn  FROM     Tsunamis) AS t WHERE   rn <= 3 GROUP BY   Country;")
            print(cursor.fetchall())
            input("Presiona ENTER para continuar...")
        elif opcion2 == '4':
             # 4. Promedio de Total Damage por país
            cursor.execute("SELECT Country, AVG(TotalDamageDescription) AS PromedioTotalDamage FROM dbo.Worksheet$ GROUP BY Country;")
            print(cursor.fetchall())
            input("Presiona ENTER para continuar...")
        elif opcion2 == '5':
             # 5. Top 5 de países con más muertes:
            cursor.execute("SELECT TOP 5 Country, SUM(TotalDeaths) AS TotalMuertes FROM dbo.Worksheet$ GROUP BY Country ORDER BY TotalMuertes DESC;")
            print(cursor.fetchall())
            input("Presiona ENTER para continuar...")
        elif opcion2 == '6':
            # 6. Top 5 de años con más muertes
            cursor.execute("SELECT TOP 5 Year, SUM(TotalDeaths) AS TotalMuertes FROM dbo.Worksheet$ GROUP BY Year ORDER BY TotalMuertes DESC;")
            print(cursor.fetchall())
            input("Presiona ENTER para continuar...")
        elif opcion2 == '7':
            # 7. Top 5 de años que más tsunamis han tenido
            cursor.execute("SELECT TOP 5 Year, COUNT(*) AS CantidadTsunamis FROM dbo.Worksheet$ GROUP BY Year ORDER BY CantidadTsunamis DESC;")
            print(cursor.fetchall())
            input("Presiona ENTER para continuar...")
        elif opcion2 == '8':
            # 8. Top 5 de países con mayor número de casas destruidas
            cursor.execute("SELECT TOP 5 Country, SUM(TotalHousesDestroyed) AS CasasDestruidas FROM dbo.Worksheet$ GROUP BY Country ORDER BY CasasDestruidas DESC;")
            print(cursor.fetchall())
            input("Presiona ENTER para continuar...")
        elif opcion2 == '9':
            # 9. Top 5 de países con mayor número de casas dañadas
            cursor.execute("SELECT TOP 5 Country, SUM(TotalHousesDamaged) AS CasasDañadas FROM dbo.Worksheet$ GROUP BY Country ORDER BY CasasDañadas DESC;")
            print(cursor.fetchall())
            input("Presiona ENTER para continuar...")
        elif opcion2 == '10':
            # 10. Promedio de altura máxima del agua por cada país
            cursor.execute("SELECT Country, AVG(MaxWaterHeight) AS PromedioAlturaAgua FROM dbo.Worksheet$ GROUP BY Country;")
            print(cursor.fetchall())
            input("Presiona ENTER para continuar...")
        elif opcion2 == 'x':
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

    # Cierra la conexión
    conn.close()

# Menú principal
while True:
    print("----------------------------------------------------")
    print("-------------------- PRACTICA 1 --------------------")
    print("------------ Ana Belén Contreras Orozco ------------")
    print("-------------------- 201901604 ---------------------")
    print("----------------------------------------------------")
    print("\nSeleccione una opción:")
    print("a) Borrar modelo")
    print("b) Crear modelo")
    print("c) Extraer información")
    print("d) Cargar información")
    print("e) Realizar consultas")
    print("x) Salir")

    opcion = input("Opción: ").lower()

    if opcion == 'a':
        borrar_modelo()
    elif opcion == 'b':
        crear_modelo()
    elif opcion == 'c':
        ruta_archivos = input("Ingrese la ruta de los archivos: ")
        extraer_informacion(ruta_archivos)
    elif opcion == 'd':
        cargar_informacion()
    elif opcion == 'e':
        realizar_consultas()
    elif opcion == 'x':
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")

conn.close()