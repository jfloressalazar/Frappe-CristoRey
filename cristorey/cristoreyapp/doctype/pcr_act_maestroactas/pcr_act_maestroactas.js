// Copyright (c) 2024, Jesus Alberto Flores Salazar and contributors
// For license information, please see license.txt

frappe.ui.form.on("PCR-ACT-MAESTROACTAS", {
    nombretitular: function(frm) {
        // Copiar el valor de campo_origen a campo_destino
        frm.set_value('nombrebautizado', frm.doc.nombretitular);
    }
});
