Continuous Delivery con Develenv:
=================================

* [Introducción] (#Introduccin)
* [Uso del plugin para hacer CD] (#Uso_del_plguin_para_hacer_CD)
* [Customizción de los jobs] (#Customizacin_de_los_jobs)
* [Develenv con Develenv y la deployment pipeline] (#Develenv_con_Develenv_y_la_deployment_pipeline)
* [Uso de vagrant para desarrollo] (#Uso_de_vagrant_para_desarrollo)

Introducción:
-------------

Como se ha comentado las fases de la pipeline que nos permiten ir desde la compilación hasta la puesta en Producción de un producto/servicio son: Build, Package, Install, SmokeTest y Acceptance Test.

Develenv nos permite gestionar todas y cada una de las mismas mediante el plugin desarrollado por Carlos llamado [develenv-pipeline-plugin] (https://code.google.com/p/develenv-pipeline-plugin/).

En este plugin se contempla la posibilidad de construir diversos componentes (o módulos) y que la instalación de los mismos se distribuya por diversos entornos, así podemos tener muchas fases Build y Package, que terminan en una sola pipeline que agrupa las fases del Install, Smoke y Acceptance test (por entorno).

Uso del plugin para hacer CD:
-----------------------------

Con este plugin se nos añaden diversas cosas: Jobs/Scripts/etc.. pero lo fundamental para lo que queremos ahora mismo es la de la creación de una pipeline mediante el job llamado pipeline-ADMIN-01-addPipeline:

![Job pipeline-ADMIN-01-addPipeline](./img/training/adminPipeline_1.png "Job pipeline-ADMIN-01-addPipeline")

este job nos solicita toda una serie de información:
organización,  project, version, modules, enviroments, adminUser como podemos ver en la siguiente captura:

![Job parameters](./img/training/adminPipeline_2.png "Job parameters") 

Una vez hemos suministrado la información correcta, este job creará todos los jobs necesarios usando los datos introducidos para generar el nombre de los mismos, quedando de la siguiente manera: 

### Para cada módulo: ####

- project-module-01-build
- project-module-02-Package

### Agrupados en una pipeline de instalación y verificación: ####

- project-ALL-03-Install
- project-ALL-04-smokeTest
- project-ALL-05-acceptanceTest

![Ejecutando el Job de administración](./img/training/adminPipeline_3.png "Ejecutando el job de administración")

Customización de los jobs
=========================

Una vez tenemos los jobs creados, hay que configurar los pequeños detalles propios de los mismos, tal y como advierte la siguiente pantalla, que nos facilita enlaces para ejecutar las tareas pendientes y hacía los jobs para su customización:

![Next Steps](./img/training/adminPipeline_4.png "Next Steps")

Como podemos ver los pasos son:

1. Recargar Jenkins: Se han creado los jobs pero jenkins necesita releer el directorio para darse cuenta y que aparezcan en las vistas.

2. Revisar la tabla de despliegues: La tabla de despligues nos permite ver de manera compacta y concisa los entornos, las máquinas que lo conforman y que paquetes (RPM) hay que desplegar en cada una de ellas. Como la instalación de los mismos (los paquetes) se hace remotamente por SSH, hay que dar el nombre de un usuario con privilegios (que al menos pueda hacer: sudo yum install). Después desde la máquina con el entorno Develenv instalado, exportar la clave SSH del usuario develenv hacía esas máquinas.
Esta tabla aparece en el job llamado project-ALL-03-Install y es generada automáticamente a partir de los campos environments y adminUser que se suministran en el job pipeline-ADMIN-01-addPipeline:

![Deployment Table](./img/training/installJob_deploymenTable.png "Deployment Table")

Esta tabla, con ligeras modificaciones aparece también en los jobs project-ALL-04-smokeTest y project-ALL-05-acceptanceTest y básicamente lo que se busca es suministrar información al job para atacar a las URLs (APIs/etc) que se sirvan como parte del desarrollo y ayudar así a verificar el despliegue y el buen funcionamiento del mismo.

![somke/Acceptance Table](./img/training/configureRepos_acceptanceTest_5.png "Smoke/Acceptance Table")

3. Hay que configurar el respositorio de fuentes para 3 jobs distintos: Build, smokeTest y acceptanceTest. 

![Configuración repos en el job de AcceptanceTest](./img/training/configureRepos_acceptanceTest_1.png "Configuración de repos en el job de AcceptanceTest")

Esto es así ya que se contempla que, el código y los test que comprueban su correcta instalación y funcionamiento E2E, puedan estar en repos distintos.

![Configuración repos en el job de AcceptanceTest](./img/training/configureRepos_acceptanceTest_2.png "Configuración de repos en el job de AcceptanceTest")

También podemos ver que el trigger que dispara la ejecución de los jobs sigue el orden comentado más arriba:

![Trigger de ejecuciones](./img/training/configureRepos_acceptanceTest_4.png "Trigger de ejecuciones")

4. Finalmente y para que se dispare automáticamente toda la pipeline, falta configurar el Hook que permite que se inicie este flujo de jobs. Para ello, y dependiendo del software de control de versiones que usemos, tendremos que hacer unos pasos u otros. Aquí mostramos el caso de TID, donde hay una instalción de la versión Enterprise de github, en la que debemos configurar correctamente los llamados Service Hooks y en concreto uno llamado "Jenkins (GitHub plugin)":

![pdihub Service Hook](./img/training/jenkinsHook.png "pdihub Service Hook")

Simplemente hay que suministrar la URL a la que debe reportar (la máquina con la instalación de Develenv).

Develenv con Develenv y la deployment pipeline
----------------------------------------------

Para rizar el rizo y ser consecuentes con lo predicado, hemos usado el propio modelo de Continuous Delivery para construir Develenv. Así, hemos creado una pipeline que nos permite construir el proyecto develenv, empaquetarlo, instalarlo en algunas máquinas y verificar que esta instalación se ha completado con éxito y que ofrece la funcionalidad deseada, aquí podemos ver esa pipline:

![Develenv with Develenv](./img/training/develenvWithDevelenv.png "Develenv with Develenv")

En la siguiente imagen podemos ver las instalaciones en los distintos entornos (int y qa) y las pruebas que han superado cada una de ellas:

![Develenv Dashboard](./img/training/develenvDashboard_1.png "Develenv Dashboard")

En el mismo enlace podemos ver el estado actual de cada entorno, las máquinas que lo conforman, los paquetes instalados en cada uno de ellos, que build es el que se ha instalado y el posible rollback, a parte de todas las ejecuciones de la pipeline, con la fecha y hora, el número de build y el estado en el que están los entornos.

![Develenv Dashboard](./img/training/develenvDashboard_2.png "Develenv Dashboard")

Uso de vagrant para desarrollo
------------------------------

Como sabéis vagrant nos permite crear entornos de desarrollo ligeros, repetibles y portables, existen versiones tanto para Linux, MacOS o incluso Windows y el formato es exportable entre estos sistemas. Tiene diversos mecanismos de provision (Chef y pupppet), que nos permiten dejar la máquina configurada para el desarrollo del proyecto/iniciativa en el que estemos trabajando.
La idea es: usar la combinación de vagrant y puppet para crear máquinas virtuales que puedan funcionar en los entornos de los developers de los distintos proyectos, y que les permitan hacer test del código desarrolladdo por ellos de manera rápida y sencilla, sin tener que esperar a que se dispare una ejecución completa en el servidor de integración continua.

En el proyecto pipelineTraining-web y concretamente en el directorio src/site/resources/vagrant podemos encontrar 5 directorios: develenv, integration, prod-backend, prod-frontend y qa, donde se pueden ver ejemplos de esta idea, con los ficheros Vagrantfile y los perfiles de puppet para dejar las máquinas configuradas para que conformen una arquitectura completa.

Para el caso de Develenv, podemos encontrar el fichero Vagrant, los perfiles de puppet y todo lo necesario para contribuir al  desarrollo del proyecto en el siguiente [enlace] (http://develenv.softwaresano.com/development.html) y si se quisiera desplegar Develenv en una máquina Vagrant, basta con hacer un checkout del directorio:

```
svn co http://develenv.googlecode.com/svn/trunk/develenv/src/main/deploy/puppet deployDevelenv
cd deployDevelenv # Revisar los paths en el Vagrantfile
vagrant up
```
