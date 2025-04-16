import frappe
import csv
import json
import os
import time

def run():
    importar_paises()
    importar_departamentos()
    importar_municipios()
    importar_distritos()


def importar_paises():
    """
    Importa países desde el archivo MH-PAIS ubicado en la carpeta 'data'.
    """
    print("Iniciando importación de países desde CSV...")

    # Ruta del archivo CSV
    base_path = os.path.dirname(__file__)
    csv_file_path = os.path.join(base_path, "data", "MH-PAIS.CSV")    

    try:
        if not os.path.exists(csv_file_path):
            raise FileNotFoundError(f"El archivo {csv_file_path} no existe.")

        with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            if reader.fieldnames is None:
                raise ValueError("El archivo CSV no tiene encabezados o está vacío.")

            for idx, row in enumerate(reader, start=1):
                try:
                    codigo = row["Código"].strip()
                    nombre = row["Valores"].strip().upper()

                    # Verificar si el distrito ya existe
                    if not frappe.db.exists("PCR-MH-PAISES", {"codigo": codigo}):
                        # Crear el nuevo registro
                        frappe.get_doc({
                            "doctype": "PCR-MH-PAISES",
                            "codigo": codigo,
                            "nombre": nombre,
                        }).insert(ignore_permissions=True)
                        print(f"[Línea {idx}] Insertado: {nombre} en {codigo}")
                    else:
                        print(f"[Línea {idx}] País ya existente: {nombre} en {codigo}")
                except KeyError as ke:
                    print(f"[Línea {idx}] Error: Faltan columnas en el CSV - {ke}")
                except Exception as e:
                    print(f"[Línea {idx}] Error al procesar el registro: {e}")
    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")
    except ValueError as ve:
        print(f"Error en el archivo CSV: {ve}")
    except Exception as e:
        print(f"Error inesperado al importar país: {e}")

    print("Importación de países completada.")

def importar_departamentos():
    """
    Importa departamentos desde el archivo MH-DEPARTAMENTO.CSV ubicado en la carpeta 'data'.
    """
    print("Iniciando importación de departamentos desde CSV...")

    # Ruta del archivo CSV
    base_path = os.path.dirname(__file__)
    csv_file_path = os.path.join(base_path, "data", "MH-DEPARTAMENTO.CSV")

    try:
        if not os.path.exists(csv_file_path):
            raise FileNotFoundError(f"El archivo {csv_file_path} no existe.")

        with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            if reader.fieldnames is None:
                raise ValueError("El archivo CSV no tiene encabezados o está vacío.")

            for idx, row in enumerate(reader, start=1):
                try:
                    codigo = row["Código"].strip().upper()
                    nombre = row["Nombre"].strip().upper()

                    # Verificar si el departamento ya existe
                    if not frappe.db.exists("PCR-MH-DEPARTAMENTOS", {"codigo": codigo}):
                        # Crear el nuevo registro
                        frappe.get_doc({
                            "doctype": "PCR-MH-DEPARTAMENTOS",
                            "codigo": codigo,
                            "nombre": nombre,
                        }).insert(ignore_permissions=True)
                        print(f"[Línea {idx}] Insertado: {nombre} con código {codigo}")
                    else:
                        print(f"[Línea {idx}] Departamento ya existente: {nombre} con código {codigo}")
                except KeyError as ke:
                    print(f"[Línea {idx}] Error: Faltan columnas en el CSV - {ke}")
                except Exception as e:
                    print(f"[Línea {idx}] Error al procesar el registro: {e}")
    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")
    except ValueError as ve:
        print(f"Error en el archivo CSV: {ve}")
    except Exception as e:
        print(f"Error inesperado al importar departamentos: {e}")

    print("Importación de departamentos completada.")

def importar_municipios():
    """
    Importa municipios desde el archivo MH-MUNICIPIO.CSV ubicado en la carpeta 'data'.
    """
    print("Iniciando importación de municipios desde CSV...")

    # Ruta del archivo CSV
    base_path = os.path.dirname(__file__)
    csv_file_path = os.path.join(base_path, "data", "MH-MUNICIPIO.CSV")

    try:
        if not os.path.exists(csv_file_path):
            raise FileNotFoundError(f"El archivo {csv_file_path} no existe.")

        with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            if reader.fieldnames is None:
                raise ValueError("El archivo CSV no tiene encabezados o está vacío.")

            for idx, row in enumerate(reader, start=1):
                try:
                    codigo = row["Código"].strip().upper()
                    nombre = row["Nombre"].strip().upper()
                    departamento = row["Departamento"].strip().upper()

                    # Verificar si el municipio ya existe
                    if not frappe.db.exists("PCR-MH-MUNICIPIOS", {"nombre": nombre}):
                        # Crear el nuevo registro
                        frappe.get_doc({
                            "doctype": "PCR-MH-MUNICIPIOS",
                            "codigo": codigo,
                            "nombre": nombre,
                            "departamento": departamento,
                        }).insert(ignore_permissions=True)
                        print(f"[Línea {idx}] Insertado: {nombre} en departamento {departamento}")
                    else:
                        print(f"[Línea {idx}] Municipio ya existente: {nombre} en departamento {departamento}")
                except KeyError as ke:
                    print(f"[Línea {idx}] Error: Faltan columnas en el CSV - {ke}")
                except Exception as e:
                    print(f"[Línea {idx}] Error al procesar el registro: {e}")
    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")
    except ValueError as ve:
        print(f"Error en el archivo CSV: {ve}")
    except Exception as e:
        print(f"Error inesperado al importar municipios: {e}")

    print("Importación de municipios completada.")


def importar_distritos():
    """
    Importa distritos desde el archivo SISTEMA-DISTRITO ubicado en la carpeta 'data',
    asociando cada distrito al campo 'name' de MH-MUNICIPIO y obteniendo el departamento
    directamente desde el registro del municipio.
    """
    print("Iniciando importación de distritos desde CSV...")
    # Ruta del archivo CSV
    base_path = os.path.dirname(__file__)
    csv_file_path = os.path.join(base_path, "data", "MH-DISTRITO.CSV")
    try:
        if not os.path.exists(csv_file_path):
            raise FileNotFoundError(f"El archivo {csv_file_path} no existe.")
        with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            if reader.fieldnames is None:
                raise ValueError("El archivo CSV no tiene encabezados o está vacío.")
            for idx, row in enumerate(reader, start=1):
                try:
                    codigo = row["CÓDIGO"].strip().upper()
                    municipio_nombre = row["NOMBRE DEL MUNICIPIO"].strip().upper()
                    nombre = row["NOMBRE"].strip().upper()
                    # Buscar el registro del municipio en MH-MUNICIPIO
                    municipio_data = frappe.db.get_value(
                        "PCR-MH-MUNICIPIOS",
                        {"nombre": municipio_nombre},
                        ["name", "departamento"],
                        as_dict=True
                    )
                    if not municipio_data:
                        print(f"[Línea {idx}] Error: No se encontró el municipio '{municipio_nombre}'.")
                        continue
                    municipio_id = municipio_data["name"]
                    departamento = municipio_data["departamento"]
                    # Verificar si el distrito ya existe
                    if not frappe.db.exists("PCR-MH-DISTRITOS", {"codigo": codigo, "municipio": municipio_id}):
                        # Crear el nuevo registro
                        frappe.get_doc({
                            "doctype": "PCR-MH-DISTRITOS",
                            "codigo": codigo,
                            "departamento": departamento,
                            "municipio": municipio_id,
                            "nombre": nombre,
                        }).insert(ignore_permissions=True)
                        print(f"[Línea {idx}] Insertado: {nombre} en Municipio ID {municipio_id}, Departamento {departamento}")
                    else:
                        print(f"[Línea {idx}] Distrito ya existente: {nombre} en Municipio ID {municipio_id}")
                except KeyError as ke:
                    print(f"[Línea {idx}] Error: Faltan columnas en el CSV - {ke}")
                except Exception as e:
                    print(f"[Línea {idx}] Error al procesar el registro: {e}")
    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")
    except ValueError as ve:
        print(f"Error en el archivo CSV: {ve}")
    except Exception as e:
        print(f"Error inesperado al importar distritos: {e}")
    print("Importación de distritos completada.")

def importar_datosparroquia():
    """
    Inserta los Datos parroquia en el catálogo MH-TIPODOCUMENTO.
    """
    print("Iniciando inserción de Datos parroquia...")
    
    tipos_documento = [
        {"nombre": "PARROQUIA \"CRISTO REY\" EL PARAÍSO", "direccion": "Bo. El Centro frente a parque centrl, El Paraíso, Chalatenango.", "telefono": "+503 2356 0563", "correo": "cristorey0@gmail.com"},
    ]

    for idx, tipo in enumerate(tipos_documento, start=1):
        try:
            nombre = tipo["nombre"].strip()
            direccion = tipo["direccion"]           
            telefono = tipo["telefono"]           
            correo = tipo["correo"]           
            # Verificar si el tipo de documento ya existe
            if not frappe.db.exists("PCR-CONF-DATOSPARROQUIA", {"nombre": nombre}):
                # Crear el nuevo registro
                frappe.get_doc({
                    "doctype": "PCR-CONF-DATOSPARROQUIA",
                    "nombre": nombre,
                    "direccion": direccion,
                    "telefono": telefono,
                    "correo": correo,
                }).insert(ignore_permissions=True)
                print(f"[Registro {idx}] Insertado: Nombre {nombre}")
            else:
                print(f"[Registro {idx}] Tipo de documento ya existente: Nombre {nombre}")
        except KeyError as ke:
            print(f"[Registro {idx}] Error: Faltan claves en el registro - {ke}")
        except Exception as e:
            print(f"[Registro {idx}] Error al procesar el tipo de documento: {e}")
            
        print("Inserción de Datos parroquia completada.")