# Guía de Implementación de la Aplicación cristorey en Contenedores Docker

## Índice
2. [Creación e inicio de contenedores](#creacion-de-contenedores)
3. [Acceso al Contenedor](#acceso-al-contenedor)
4. [Configuración de la aplicación](#configuración-de-la-aplicación)
   1. [Creación de sitio y aplicación de Frappe](#creación-de-sitio-y-aplicación-de-frappe)
   3. [Configuración del Sitio](#configuración-del-sitio)
   4. [Clonación de repositorio](#clonación-de-repositorio)
   5. [Configuración final, importe de roles y ejecución de seeders](#configuración-final-y-ejecución-de-seeders)
5. [Inicio de la aplicación](#inicio-de-la-aplicación)
9. [Resolución de Problemas Comunes](#resolución-de-problemas-comunes)

---

## Creacion de contenedores

#### 1. Construccion de contenedores
s
Con la aplicación Docker Desktop iniciada y usando la terminal de windows, navegue hasta la carpeta donde se encuentra el archivo *`docker-compose-cristorey-app-frappe.yml`* y ejecute el comando:

    docker-compose -f ./docker-compose-cristorey-app-frappe.yml build


#### 2. Inicio de contenedores

Si todo ha marchado bien, luego de esa construcción, ejecute el comando para iniciar los contenedores:

    docker-compose -f ./docker-compose-cristorey-app-frappe.yml up -d

---

## Acceso al Contenedor

Deberá acceder al contendor en ejecución haciendo uso de la extensión **Dev Containers** de VSC.

##### 1. Inicie VSC y presione *`Ctrl+Shift+P`*
##### 2. Escriba *`Dev Containers`* y seleccione la opción *`Adjuntar al contenedor que está en ejecución`*
##### 3. Si los conenedores están iniciados aparecerán en la lista, deberá seleccionar el conentedor llamado *`cristorey-app-backend-1`*

---

## Configuración de la aplicación

En este apartado que se divide en secciones encontrará todos los comandos para poner en marcha la aplicación.
Se parte del entendido que hasta este punto usted ya está conectado a su contenedor haciendo uso de VSC.
Abra una terminal de VSC presionando `Ctrl+Ñ`

#### Creación de sitio y aplicación de Frappe

En este apartado se crea el entorno de Frappe, tanto el sitio ``(site)`` como la aplicacion ``(app)`` para ello se debe ejecutar los siguientes comandos:

Antes debemos asegurarnos de que no estamos en la carpeta frappe-bench, de ser así nos salimos con
   
   cd ~

  1. Iniciar el entorno virutal de python que permite la ejecición de comandos `bench`

    source cristorey/bin/activate

  2. Moverse a carpeta de Frappe

    cd frappe-bench

  3. Crear nuevo sitio (site) de Frappe `cristorey`, solicitará la contraseña de base de datos, **tambien solicitará que se establesca una contraseña para el usuario 'Administrator' para el sistema de Frappe** 

    bench new-site cristorey.site --db-host cristorey-app-db-1 --db-root-username root --mariadb-user-host-login-scope='%'

  4. Crear una nueva aplicación (app) de Frappe `cristorey`, en este caso se solicitará cierta información, como el nombre de la aplicación, descripción, autor, correo, licencia, rama de repositorio. Lo importante es que en el titulo de aplicacion coloque `CristoReyApp` 

    bench new-app cristorey

#### Configuración del Sitio

  1. Incorporar la app al site

    bench --site cristorey.site install-app cristorey

  2. Iniciar el modo desarrollador para el sitio

    bench --site cristorey.site set-config developer_mode 1

  3. Iniciar el scheduler del sitio

    bench --site cristorey.site enable-scheduler

  4. Establecer el sitio `cristorey.site` como sitio por defecto

    bench use cristorey.site

  5. Volver a establecer el modo desarrollador para el sitio

    bench --site cristorey.site set-config developer_mode 1

    
#### Clonación de repositorio

##### >> Importante: Recuerde especificar la `[rama]` desde  la cual se realizará la copia del repositorio.

  1. Cambiar al directorio donde se realizará la copia del repositorio

    cd apps/cristorey

  2. Borrar el contenido de la carpeta

    rm -rf .[^.]* *

  3. Clonar la aplicación desde el repositorio especificando la `[rama]`

    git clone --branch [rama] https://jfloressalazar:token@github.com/jfloressalazar/Frappe-CristoRey.git .

  4. Volver al directorio de frappe

    cd ../..
    
  5. Volver a establecer el modo desarrollador para el sitio
    
    bench --site cristorey.site set-config developer_mode 1


## Inicio de la aplicación

- Ingrese al navegador y escriba la siguiente URL: http://localhost:8600

- Inicie sesion con las credenciales 'Administrator' y la contraseña que usted espeficicó.

- En la pantalla principal, seleccione el idioma principal `Español(Guatemala)` 

- La configuración ha finalizado

## Resolución de Problemas Comunes
