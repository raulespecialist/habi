# Resume
En esta herramienta los usuarios deben ser capaces de ver tanto los
inmuebles vendidos como los disponibles. Con el objetivo de hacer más fácil la búsqueda, se
espera que los usuarios puedan aplicar diferentes filtros a la búsqueda.
Adicionalmente, se espera que los usuarios puedan darle “me gusta” a los inmuebles con el fin
de tener un ranking interno de los inmuebles más llamativos.


# Historia de usuario
### Servicio de consulta
● Los usuarios pueden consultar los inmuebles con los estados: “pre_venta”, “en_venta” y
“vendido” (los inmuebles con estados distintos nunca deben ser visibles por el usuario).

● Los usuarios pueden filtrar estos inmuebles por: Año de construcción, Ciudad, Estado.

● Los usuarios pueden aplicar varios filtros en la misma consulta.

● Los usuarios pueden ver la siguiente información del inmueble: Dirección, Ciudad,
Estado, Precio de venta y Descripción.

### Servicio de “Me gusta” 
*Features*

● Los usuarios pueden darle me gusta a un inmueble en específico y esto debe quedar
registrado en la base de datos.

● Los “Me gusta” son de usuarios registrados, y debe quedar registrado en la base de
datos el histórico de “me gusta” de cada usuario y a cuáles inmuebles.

[Modelo para modulo "Me gusta"](https://github.com/raulespecialist/habi/wiki/Modelo-de-negocio-para-el-modulo-de-%22Me-gusta%22)


# Implementacion
git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main
#### Clonar
 

    git clone https://github.com/raulespecialist/habi.git
Ingresar al directorio
cd habi
Cree un entorno virtual
python -m venv .env 
Ingrese al entorno virtual
source .env/bin/activate
Dentro del entorno virtual (.env) actualizar pip
pip install --upgrade pip
Posteriormente instalar todos los requerimientos necesarios
pip install -r requirements.txt
Modificar el archivo `habi/habi_core/settings.py` lineas 78-87 por sus credenciales e ip y puerto, de la base de datos no expuestos aquí.

    DATABASES = {
	    'default': {
	    'ENGINE': 'django.db.backends.mysql',
	    'NAME': 'nombre_db',
	    'USER': 'usuario',
	    'PASSWORD': 'palabra%secreta',
	    'HOST': '0.0.0.0',
	    'PORT': '0000',
	    }
    }

Iniciar la API REST

    python manage.py runserver

Realizar TEST

    python manage.py test

Enviar peticiones a la API
Por medio de cURL 

    curl --location --request GET 'http://127.0.0.1:8000/api/v1/properties/?city=bogota&year=2000&status=4' \
    --form 'city="bogota"' \
    --form 'year="2000"' \
    --form 'status="4"'
Por medio del navegador web ingresando directamente con la URL mas los parámetros ejemplo:

    http://127.0.0.1:8000/api/v1/properties/?city=bogota&year=2000&status=4


[Modelo de negocio para modulo "Me gusta"](https://github.com/raulespecialist/habi/wiki/Modelo-de-negocio-para-el-modulo-de-%22Me-gusta%22)
