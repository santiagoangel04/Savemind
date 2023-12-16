# Proyecto SaveMind

¡Bienvenido a mi proyecto SaveMind!

## Descripción del proyecto

Este proyecto es la solucion de problemas a los cuales me enfrentaba cada dia,
esto con respecto al idioma ingles o idiomas los cuales estaba aprendiendo, este problema sumado con mi memoria hacia que palabras que para mi eran interesantes y utiles las olvidara, para eso creo este nuevo proyecto, el cual va ir mejorando cada vez mas, primero el proyecto sera un proyecto de consola, me dara las repuestas tipo api, dado que aun la idea de una interfas grafica no esta muy clara. El proyecto consistira en un traductor normal el cual me traducira la expresion, y si esta expresion me es interesante o no sabia su traduccion me arrojara una opcion que me pedira lo siguiente: "desea guardarla", dare si, si quiero hacerlo y si no, pues lo olvidara y no la guardara, esta palabra se estara recordando cada dia con una repeticion de 24h, con opcion de ser modificable, por el momento solo sera por gmail, despues podra sujetarse a cambios. Otra feature del mismo sera la posibilidad de agregarsele un contexto propio, y uno generado, asi este para que recordar el significado sea mas facil.
La idea de este proyecto se encuentra aun en fase de desarrollo debido que cada vez que el proyecto se construya de mejor manera se podran ver nuevas features.
***La realizacion de este proyecto lo estare haciendo sin frames, a manera de probar, luego mutare esto con un frame, para el tema del frontend, o mejor la parte visual de este proyecto se realizara con flet*** 


## Clonacion del repo

1. Clona el repositorio: `git clone https://github.com/santiagoangel04/Savemind.git`


## Librerias necesarias

Para utilizar este proyecto, descarga todos los paquetes utilizados para este proyecto, si no lo tienes descargados:
>[!important]
>Recomiendo la creacion de entornos virtuales para que el usos de librerias no sea engorroso.
1. Translate: Esta libreria nos ayudara para el tema de traducciones, actualmente en el proyecto solo se encuentra de ingles-español y español-ingles, proximante mas
    
```bash
pip install translate
```
2. Dotenv: Usualmente utilizado en el proyecto para la extracion de variable de entorno, esta libreria se debe usar con la libreria os
```bash
pip install python-dotenv
```
3. Mysql-conector: necesario para proder hacer cada parte de crud y acceso a dba.
>[!tip]
>revisa si se encuentra instalado, te ahorrara tiempo,
para esto puedes utilizar:
```bash
pip list
```
```bash
pip install mysql-connector-python
```
3. flet
```bash
pip install flet
```
## Features posibles
- lectura de imagenes que contengan texto en ingles, el cual sera pasado a un archivo txt, el usuario podra escribir las palabras que se le parescan interesantes y estas se guardaran tanto con la traduccion como con el contexto generado.
- Alerta de aprendizaje, esta alerta puede ser modificada por el usuario, como primera opcion, correos, se piensa poder enviar las alertas por whatsapp ***no tan viable, aunque puede suceder***,la siguiente feature sera poder agrupar cada palabra dependiendo su uso, ejemplo hello debe ir en greatings o saludos, dado que para esto se utiliza.

>to be continue