# Copyright (c) 2024, Jesus Alberto Flores Salazar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import formatdate
from num2words import num2words
from datetime import datetime
import locale


class PCRACTMAESTROACTAS(Document):
	pass

@frappe.whitelist()
def format_date_custom():
	return formatdate(frappe.utils.nowdate(), "dd 'de' MMMM 'de' yyyy")

@frappe.whitelist()
def fecha_en_formato_legal(fecha):

    # Configurar locale en español
    locale.setlocale(locale.LC_TIME, "es_SV.utf8")

    # Convertir fecha si es un string
    if isinstance(fecha, str):
        fecha = datetime.strptime(fecha, "%Y-%m-%d")

    dia = num2words(fecha.day, lang="es")
    mes = fecha.strftime("%B").lower()  # Nombre del mes en español
    año = num2words(fecha.year, lang="es", to="year")

    # Armar el texto
    return f"{dia} días del mes de {mes} del año {año}"

# Registrar como método disponible en Frappe
@frappe.whitelist()
def formato_legal_actual():
    """
    Retorna la fecha actual en formato legal.
    """
    fecha_hoy = frappe.utils.nowdate()
    return fecha_en_formato_legal(fecha_hoy)