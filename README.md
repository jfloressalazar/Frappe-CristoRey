# Guía de Implementación de la Aplicación cristorey en Contenedores Docker

## Índice

---

## Creacion de contenedores

    docker-compose -f pwd.yml up -d

Eliminar ERPNext de contenedor BAcKEND1
(solo es necesario en este contenedor para afectar la base de datos)
    cd frappe-bench/
    bench --site frontend uninstall-app erpnext
Confirmar
    bench remove-app erpnext
Crear nueva aplicación para el cristorey cuando pida el título colocar  CristoReyApp
    bench new-app cristorey
Incorporar la nueva aplicación al sitio
    bench --site frontend install-app cristorey
    bench --site frontend set-config developer_mode 1
    bench --site frontend enable-scheduler
Clonar aplicación desde el repositorio de GitHub en la carpeta correcta y migración de fixtures para actualización de base de datos
    cd apps/cristorey &&  rm -rf .[^.]* * &&  git clone --branch main https://jfloressalazar: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@github.com/jfloressalazar/Frappe-CristoRey.git . &&  cd ../..
    bench --site frontend migrate
Activar Scripts de servidor en el sitio
    bench set-config -g server_script_enabled 1
Asegurar que el archivo sites/apps.txt  no esté presente la linea "cristorey" pero si "erpnext"

"Creacion" de app cristorey y Clonado de fuentes a otros contenedores 
Ejecutar y completar información
    bench new-app cristorey
Ejecutar para clonar fuentes desde el repositorio
    cd apps/cristorey &&  rm -rf .[^.]* * &&  git clone --branch main https://jfloressalazar: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@github.com/jfloressalazar/Frappe-CristoRey.git . &&  cd ../..
Asegurar que el archivo sites/apps.txt  no esté presente la linea "erpnext" pero si "cristorey"
Reiniciar conenedores para poner en linea la aplicación
    cristorey-production-frontend-1 cristorey-production-backend-1 cristorey-production-scheduler-1  cristorey-production-queue-long-1 cristorey-production-queue-short-1

Correr SEEDERS en backend-1
  bench execute cristorey.seeders.script.run

Colocar imagenes, logos, iconos perdidos, actuliza clave de admin, crear usuario de administrador de parroquia.