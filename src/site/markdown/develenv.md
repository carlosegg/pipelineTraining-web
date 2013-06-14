Continuous Delivery con Develenv:
=================================

* [Introducción] (#Introduccin)
* [Uso del plugin para hacer CD] (#Uso_del_plguin_para_hacer_CD)
* [Customizción de los jobs] (#Customizacin_de_los_jobs)

Introducción:
-------------

Como se ha comentado las fases de la pipeline que nos permiten ir desde la compilación hasta la puesta en Producción de un producto/servicio son: Build, Package, Install, SmokeTest y Acceptance Test.

Develenv nos permite gestionar todas y cada una de las mismas mediante el plugin desarrollado por Carlos llamado [develenv-pipeline-plugin] (https://code.google.com/p/develenv-pipeline-plugin/).

En este plugin se contempla la posibilidad de construir diversos componentes (o módulos) y que la instalación de los mismos se distribuya por diversos entornos, así podemos tener muchas fases Build y Package, que terminan en una sola pipeline que agrupa las fases del Install, Smoke y Acceptance test (por entorno).

Uso del plugin para hacer CD:
-----------------------------

Con este plugin se nos añaden diversas cosas: Jobs/Scripts/etc.. pero lo fundamental para lo que queremos ahora mismo es la de la creación de una pipeline mediante el job llamado pipeline-ADMIN-01-addPipeline, este job nos solicita toda una serie de información:
organización,  project, version, modules, enviroments, adminUser

Una vez hemos suministrado la información correcta, este job creará todos los jobs necesarios usando los datos introducidos para generar el nombre de los mismos, quedando de la siguiente manera: 

### Para cada módulo: ####

- project-module-01-build
- project-module-02-Package

### Para cada entorno: ####

- project-ALL-03-Install
- project-ALL-04-smokeTest
- project-ALL-05-acceptanceTest

Customización de los jobs
=========================




https://siege.tid.es/repositorio/InsTelematicsExt