## Creación entorno virtual

Para poder usar esta app de Django es necesario instalar el Entorno Virtual de Python. Es necesario seguir los siguientes pasos.

    Python -m venv env

Esto creara el directorio env si no existe y además creara directorios dentro de el que contienen una copia del interprete de Python y varios archivos mas.
Una vez creado el entorno virtual, es necesario activarlo.

Para Windows

    env\Scripts\activate.bat
   
   Para Mac/Unix
   

    env/bin/activate
Luego de esto, el entorno virtual cambiara el prompt de la consola, indicando que en este momento se encuentra utilizando.

Además de esto, hay que instalar las dependencias de esta aplicación.

Para instalar las dependencias de esta aplicación, siga estos pasos:

> `pip install -r api/requirements.txt`
> 
> En caso de que surja algún error, revisar bien si al momento de ejecutar el comando se encuentra en el directorio donde se encuentre el archivo requirements.txt

Ahora crear las migraciones de la app para el entorno virtual

    python manage.py migrate

Cuando se complete este proceso, hay que ejecutar el siguiente comando:

    python manage.py makemigrations

Si todo esto ha salido bien, es posible entrar a los endpoints y así posteriormente usarlos.

Para activar el servicio hay que ejecutar el siguiente comando:

    python manage.py runserver




## Metodo PDF

Al momento de que el servicio este ejecutándose, es posible entrar al siguiente endpoint para generar el pdf con el nombre respectivamente.

[Link en localhost](http://127.0.0.1:8000/api/generarPdf/)

> ([http://127.0.0.1:8000/api/generarPdf/)

Al momento de entrar a la pagina, hay que ingresar un nombre para que el método post funcione y genere el documento en formato PDF con el nombre en su interior del documento y como nombre

![enter image description here](https://i.postimg.cc/zDPcYQrv/image.png)


 
Posterior a esto, se envía la variable por el body de la request y devuelve la variable dentro del PDF y en su interior el nombre.

![enter image description here](https://i.postimg.cc/fTzm5zF0/image.png)

Este es el resultado en el documento:
![enter image description here](https://i.postimg.cc/3NSRtT4g/image.png)



## Metodo Get

Para el primer metodo, que en este caso es GET se puede ver en el archivo "views.py" que funciona de la siguiente forma:
![enter image description here](https://i.postimg.cc/fytnhnq7/image.png)
 En caso de que esta clase tenga un máximo de 3 como solicitudes en total, arrojara un error de servicio no disponible.
(http://127.0.0.1:8000/api/solicitud/)

Donde se podrá ingresar un numero, para así poder generar una inserción en la base de datos, para posteriormente comprobarlo antes de ingresarlo y en caso de que tenga mas de 3, arrojar error.

