// Copyright (c) 2024, Jesus Alberto Flores Salazar and contributors
// For license information, please see license.txt

frappe.ui.form.on("PCR-ACT-MAESTROACTAS", {
    nombretitular: function(frm) {
        // Copiar el valor de campo_origen a campo_destino
        if (frm.doc.tipoacta=='FE DE BAUTISMO') {
            frm.set_value('nombrebautizado', frm.doc.nombretitular);
        } 
        if (frm.doc.tipoacta=='CONSTANCIA DE PRIMERA COMUNIÓN') {
            frm.set_value('nombrebenificiadoprimcomu', frm.doc.nombretitular);
        } 
        if (frm.doc.tipoacta=='CONFIRMACIÓN') {
            frm.set_value('nombrecompletoconfirmado', frm.doc.nombretitular);
        } 
    }
});
