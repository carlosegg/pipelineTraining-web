Repositorios
============

En todo proyecto existirán tres tipos de repositorio:

* Repositorios de desarrollo(Uno por cada componente)
* Repositorios de Smoke Tests. 
* Repositorios de Acceptance Test


Para empezar con un proyecto se han de dar los siguientes pasos:

  * [Creación de la organización](#Creacin_de_la_organizacin)
    * [Miembros de la organización](#Miembros_de_la_organizacin)
    * [Creación del equipo para integración continua](#Creacin_del_equipo_para_integracin_continua)
  * [Creación y configuración de los repositorios] (#Creacin_y_configuracin_de_los_repositorios)
    * [Creación del repositorio](#Creacin_del_repositorio)
    * [Configuración hook de jenkins](#Configuracin_hook_de_jenkins)
    * [Primer commit](#Primer_commit)

### Creación de la organización
#### Creación de la organización
![Creación organización](./img/training/pipelineTraining_newOrganization1.png)
#### Miembros de la organización
![Miembros de la organización](./img/training/pipelineTraining_newOrganization2.png)
#### Creación del equipo para integración continua
Para crear un equipo se accede a [https://pdihub.hi.inet/organizations/pipeline/teams](https://pdihub.hi.inet/organizations/pipeline/teams)
![Equipo de integración continua](./img/training/pipelineTraining_ContinousIntegrationTeam.png)

### Creación y configuración de los repositorios

#### Creación del repositorio
El propietario de la organización podrá dar de alta repositorios dentro de la organización.

Para crear un nuevo repositorio el se accede a [https://pdihub.hi.inet/organizations/pipeline/repositories/new](https://pdihub.hi.inet/organizations/pipeline/repositories/new)

En este ejemplo lo haremos para los acceptance Test.

![Nuevo repositorio](./img/training/pipelineTraining-acceptanceTest_newRepository.png)

![Nuevo repositorio creado](./img/training/pipelineTraining-acceptanceTest_newRepository2.png)

#### Configuración hook de jenkins

Cada vez que se haga un commit en el repositorio se active el job de jenkins se necesita añadir
un hook a la configuración del repo. Para ello se accede a [https://pdihub.hi.inet/pipeline/pipelineTraining-acceptanceTest/admin/hooks](https://pdihub.hi.inet/pipeline/pipelineTraining-acceptanceTest/admin/hooks)

![Configuración Hook de Jenkins](./img/training/jenkinsHook.png)

#### Primer commit

```
  mkdir -p pipelineTraining-acceptanceTest
  cd pipelineTraining-acceptanceTest/
  vi README.md 
  git init
  git add README.md
  git commit -m "first commit"
  git remote add origin git@github.com:carlosegg/pipelineTraining-acceptanceTest.git
  git push -u origin master
  git checkout -b develop
  git push origin develop
```


