Creando web del curso
=====================

Toda la documentación del proyecto estará escrita en formato markdown, y se 
utilizará maven para presentarla en formato web.

* [Proyecto inicial](#Proyecto_inicial)
* [Empaquetado del proyecto](#Empaquetado_del_proyecto)

Proyecto inicial
----------------

Se genera el proyecto a partir de un [arquitetipo maven](http://softwaresano-repomaven.googlecode.com/svn/sites/com.softwaresano.archetypes/standalone-archetype/index.html).

```
cd workspace
mvn -DarchetypeRepository=https://softwaresano-repomaven.googlecode.com/svn/archetypes-snapshots \
    -DarchetypeGroupId=com.softwaresano.archetypes -DarchetypeArtifactId=standalone-archetype -DarchetypeVersion=1.0.30-SNAPSHOT \
    -DgroupId=com.ss.training.pipeline -DartifactId=pipelineTraining -Dpackage=com.ss.training.pipeline.training -Dversion=1.0-SNAPSHOT \
    -DinteractiveMode=false archetype:generate
cd pipelineTraining
```
Se borran los ficheros que no se utilicen creados por este [arquitetipo maven](http://softwaresano-repomaven.googlecode.com/svn/sites/com.softwaresano.archetypes/standalone-archetype/index.html)

Creamos  la primera página de este curso, es decir,  el temario. Para ello generamos
la página [src/site/markdown/index.md](https://raw.github.com/carlosegg/pipelineTraining-web/develop/src/site/markdown/index.md)

```
TEMARIO
=======
  * [¿Qué es Continuous Delivery?](./cd/index.html)
    * [¿Qué es la deployment Pipeline?](./deploymentPipeline.html)
  * Ejemplos:
    * [PipelineTraining (Este curso)](./example.html)
    * [Desarrollo de develenv con la deployment pipeline](./develenv.html)
  * Ejercicios:
    * [Desarrollo sumadora web](./web-calculator.html)
```

Se crea el [build.sh](https://github.com/carlosegg/pipelineTraining-web/blob/4d483bc36c9eb345d8680a17e8a2bb1f0dd0f0d8/build.sh)
necesario para construir el proyecto 

```
#!/bin/bash
mvn clean site:site
```


Se les da permisos de ejecución

```
chmod u+x build.sh
```
Se hace el [primer commit](https://github.com/carlosegg/pipelineTraining-web/tree/b85f2089db0e359e585135ba12eb0988e0ae26d7) al repositorio

```
git init
git add *
git commit -a -m "Initial"
git remote add origin git@github.hi.inet:carlosegg/pipelineTraining-web.git
git push -u origin master
git checkout -b develop
git push origin develop
```

Empaquetado del proyecto
------------------------

Se utilizará la distribución Centos para desplegar esta aplicación web corriendo bajo apache. Por 
tanto es necesario crear un **rpm**. 

El fichero [web.spec](https://github.com/carlosegg/pipelineTraining-web/blob/develop/src/main/rpm/SPECS/web.spec)
contiene los scripts necesarios para la creación, instalación y desinstalación del
**rpm**.

Además se ha de definir el fichero de [configuración de apache](https://github.com/carlosegg/pipelineTraining-web/blob/b85f2089db0e359e585135ba12eb0988e0ae26d7/src/main/rpm/SOURCES/pipelineTraining/pipelineTraining.conf)
