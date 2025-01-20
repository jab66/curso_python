## Extensiones Visual Studio Code

- Python (Microsoft)
- Pylint (Microsoft) - Linter

## Archivos .md (Markdown)

Abierto el archivo .md, presionar ctrl + shift + v para ver el archivo markdown.

## Versiones de python instaladas:
- `py --list (-0)`

![Imagen de ejemplo](imagenes/pylist.png)

## Crear entorno virtual con python 3.11
- `py -V:3.11 -m venv myenv`

## Activar el entorno virtual
- `myenv\Scripts\activate`

## Desactivar el entorno virtual
- `deactivate`

## Formateo de código

Instalar la extendión **autopep8 (Microsoft)**

  **Ejecucion manual**: shift + ctrl + p -->> Format Document<br>

  Para que cada vez que se guarde se haga el formato del codigo automaticamente<br>
    *configuration - settings - buscar:formatOnSave - marcar Format On Save*

## Para modificar el nombre de una variable en VSC:
- ctrl + shift + P
- Rename Symbol

## Version de pip
- `pip --version`

## Paquetes instalados
- `pip list`

## Instalacion de librerias
- `pip install requests`

## Desinstalar librerias
- `pip uninstall autopep8`

## Instalar una libreria especifica
- `pip install requests==2.18.1`

## Instalar una libreria especifica con * (ultima version según *)
- `pip install requests==2.18.*`

<br>Si este comando da un error de zsh, se debería pasar el install entre ', es decir </br>
'requests==2.18.*'

## pipenv
- se usa para que las dependencias no estén dentro de nuestro proyecto.
- evita usar el .gitignore para excluir las deps
- trabaja con los archivos Pipfile y Pipfile.lock

pip install pipenv<br>
pipenv graph<br><br>
![Imagen de ejemplo](imagenes/dependencias.png)

  
# Variables de entorno
- `pip install python-dotenv`
<br><br>
Si se declara una variable de entorno en el archivo .env y existe en Windows, tomará la de Windows.
<br>


## Selenium (pruebas automatizadas)
- bajar el driver del explorador que se va a usar 
ir a la pagina de PyPi y buscar Selenium, ingresar a la version oficial y ahí podremos bajar el driver del navegador que se vayamos a usar.

