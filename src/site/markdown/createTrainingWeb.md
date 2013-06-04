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
    -DgroupId=com.pdi.training.pipeline -DartifactId=pipelineTraining -Dpackage=com.pdi.training.pipeline.training -Dversion=1.0-SNAPSHOT \
    -DinteractiveMode=false archetype:generate
cd pipelineTraining
```
Se borran los ficheros que no se utilicen creados por este [arquitetipo maven](http://softwaresano-repomaven.googlecode.com/svn/sites/com.softwaresano.archetypes/standalone-archetype/index.html)

Creamos  la primera página de este curso, es decir,  el temario. Para ello generamos
la página [src/site/markdown/index.md](https://pdihub.hi.inet/pipeline/pipelineTraining-web/raw/7ba5fa12979dabf7434b8e3e1407eca2a7d35315/src/site/markdown/index.md)

```
TEMARIO
=======

* [¿Qué es la deployment Pipeline?](./deploymentPipeline.html)
* [Ejemplo Pipeline (Este curso)](./example.html)
```

Se crea el [build.sh](https://pdihub.hi.inet/pipeline/pipelineTraining-web/raw/b41df2c691fa0a69b2f83d3433f324c9d6f16801/build.sh)
necesario para construir el proyecto 

```
#!/bin/bash
mvn clean site:site
```


Se les da permisos de ejecución

```
chmod u+x build.sh
```
Se hace el [primer commit](https://pdihub.hi.inet/pipeline/pipelineTraining-web/tree/b41df2c691fa0a69b2f83d3433f324c9d6f16801) al repositorio

```
git init
git add *
git commit -a -m "Initial"
git remote add origin git@pdihub.hi.inet:carlosg/pipelineTraining.git
git push -u origin master
git checkout -b develop
git push origin develop
```

Empaquetado del proyecto
------------------------

Se utilizará la distribución Centos para desplegar esta aplicación web corriendo bajo apache. Por 
tanto es necesario crear un **rpm**. 

El fichero [web.spec](https://pdihub.hi.inet/pipeline/pipelineTraining-web/blob/b258ac7a63c68db03ac42fced07fa1b3be266714/src/main/rpm/SPECS/web.spec)
contiene los scripts necesarios para la creación, instalación y desinstalación del
**rpm**.

Además se ha de definir el fichero de [configuración de apache](https://pdihub.hi.inet/pipeline/pipelineTraining-web/blob/ebccca4cc7dd2b4c341849cff457e43e8de61128/src/main/rpm/SOURCES/pipelineTraining/pipelineTraining.conf)


