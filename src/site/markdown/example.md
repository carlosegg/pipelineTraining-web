EJEMPLO DEPLOYMENT PIPELINE
===========================

El objetivo de este ejemplo es crear una web donde se explique el funcionamiento
de la **deployment pipeline**. Esta web debería ser desplegada en una url del
tipo http://host/pipelineTraining 


* [Conocimientos previos] (#Conocimientos_previos)
* [Requisitos software] (./softwareRequirements.html)
* [Configuración entornos de desarrollo] (#Configuracin_entornos_de_desarrollo)
* [Desarrollo del proyecto] (./projectDevelopment.html)
* [Creación del pipeline] (./createPipeline.html)
* [Ejecución de la pipeline] (./executePipeline.html)

Conocimientos previos
---------------------

Para trabajar con la **deploymente pipeline** se necesitan conocimientos en las
siguientes tecnologías/herramientas:

* Git(a nivel de línea de comandos)
* Maven(a nivel de línea de comandos)
* Java
* Scripting
* Linux a nivel de administrador(Distribuciones Centos y RedHat)

Requisitos software
-------------------

* Los [requisitos software] (./softwareRequirements.html) están descritos
[aquí](./softwareRequirements.html)


Configuración entornos de desarrollo
------------------------------------

Todo lo que se desarrolle ha de funcionar en los diferentes entornos, empezando
por el entorno del desarrollador. Herramientas como Eclipse facilitan el trabajo,
pero se ha de entender como funcionan las tecnologías que hay por debajo.

Para evitar problemas de codificaciones y de formato:

### Codificación UTF-8
Se utiliza la codificación **UTF-8**.

En eclipse

```
(Windows-->Preference-->Workspace --> Text File Encoding)
```

### Retorno de carro
Se utiliza el formato de retorno de carro de **unix**

En eclipse

```
(Windows-->Preferences-->Workspace--> New text line delimiter)
```

### Espacios en vez de tabuladores

En eclipse

```
(Windows-->Preferences-->General -->Editors --> Text Editors --> 
Displayed tab width(3) --> Insert spaces for tabs 3)

(Windows-->Preferences-->XML --> Editor--> Indent using spaces --> 
Indentation size --> 3)
```