// Copyright (c) 2024, Jesus Alberto Flores Salazar and contributors
// For license information, please see license.txt

frappe.ui.form.on("PCR-ACT-MAESTROACTAS", {
    nombretitular: function (frm) {
        // Copiar el valor de campo_origen a campo_destino
        if (frm.doc.tipoacta == 'FE DE BAUTISMO') {
            frm.set_value('nombrebautizado', frm.doc.nombretitular);
        }
        if (frm.doc.tipoacta == 'CONSTANCIA DE PRIMERA COMUNIÓN') {
            frm.set_value('nombrebenificiadoprimcomu', frm.doc.nombretitular);
        }
        if (frm.doc.tipoacta == 'CONFIRMACIÓN') {
            frm.set_value('nombrecompletoconfirmado', frm.doc.nombretitular);
        }
        if (frm.doc.tipoacta == 'SUPLETORIA DE BAUTISMO') {
            frm.set_value('nombrebautizadosuple', frm.doc.nombretitular);
        }
    },

    refresh: function (frm) {

        validarFormatImpresionDeActa(frm)
    },


});

function validarFormatImpresionDeActa(frm) {
    if (!frm.doc.formatoimpresion) {
        frappe.msgprint(__('No hay un formato de impresión definido para el tipo de acta.'));
        return;
    } else {
        cargarBotonImpresionPersonalizado(frm)
    }
}

function cargarBotonImpresionPersonalizado(frm) {
    // Agregar un botón personalizado
    frm.add_custom_button(__('Imprimir acta'), function () {
        let d = new frappe.ui.Dialog({
            title: 'Ingrese el motivo a colocar en el acta',
            fields: [
                {
                    label: 'Motivo',
                    fieldname: 'textomotivo',
                    fieldtype: 'Data',
                    reqd: 1
                }
            ],
            primary_action_label: 'Generar acta',
            primary_action(values) {
                d.hide();

                // Abrir la vista previa del formato de impresión con el texto
                let print_format = frm.doc.formatoimpresion; // Reemplaza con el nombre de tu formato de impresión
                let print_url = `/printview?doctype=${frm.doc.doctype}&name=${frm.doc.name}&format=${print_format}&no_letterhead=0&custom_text=${encodeURIComponent(values.textomotivo)}`;

                window.open(print_url, '_blank');
            }
        });
        d.show();
    });
}


