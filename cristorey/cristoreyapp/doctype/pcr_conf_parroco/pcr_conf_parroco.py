# Copyright (c) 2024, Jesus Alberto Flores Salazar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class PCRCONFPARROCO(Document):
	
	def on_update(self):
		self.generar_nombre_completo_parroco()

	def generar_nombre_completo_parroco(self):
		nombre_completo = " ".join(filter(None,
			[self.titulo,
			self.primernombre, 
			self.segundonombre,
			self.tercernombre, 
			self.primerapellido, 
			self.segundoapellido]))

		self.nombrecompletoparroco = nombre_completo
