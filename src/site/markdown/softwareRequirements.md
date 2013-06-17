REQUISITOS SOFTWARE
===================

Para realizar este workshop sobre continuous delivery, es necesario
tener instalado y configurado el siguiente software.

* [Software de terceros] (#Software_de_tercerops)
* [Entorno de desarrollo] (#Conocimientos_previos)
* [Configuración de develenv](#Configuración_de_develenv)
* [Entornos de despliegue] (#Entornos_de_despliegue)

Requisitos Hardware
-------------------

Todo el curso se realiza sobre la máquina de cada uno de los participantes. En
cada máquina se alojarán 3 máquinas virtuales (1 para 
[develenv](http://develenv.softwaresano.com) con 1.5Gb de RAM, y 2 para 
los entornos de despliegue de 512Mb de RAM). 
Por tanto se recomiendan máquinas físicas con al menos 4Gb de RAM.

Software de terceros
--------------------

En las máquinas de cada uno de los participantes ha de estar instalado el siguiente
software:

* [Virtualbox 4.2.12 ó superior](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant 1.2.2 ó superior](http://downloads.vagrantup.com/tags/v1.2.2)
* [Eclipse](http://www.eclipse.org/downloads/) (no es imprescindible)

Configuración de develenv
-------------------------

Una vez instalado todo el software de terceros se ha de levantar la máquina
virtual que contiene [develenv](http://develenv.softwaresano.com).

```
carlosg@ironman:~$ mkdir -p workspace/cd_workshop/
carlosg@ironman:~$ cd workspace/cd_workshop/
carlosg@ironman: workspace/cd_workshop$ wget --no-check-certificate https://github.com/carlosegg/pipelineTraining-web/archive/develop.zip
carlosg@ironman: workspace/cd_workshop$ unzip develop.zip 
carlosg@ironman: workspace/cd_workshop$ cd pipelineTraining-web-develop/src/site/resources/vagrant/develenv 
carlosg@ironman: workspace/cd_workshop/pipelineTraining-web-develop/src/site/resources/vagrant/develenv$
```

Aunque del punto de vista del continuous delivery, debería haber un build separado
para development y otro para continous integration(develenv). Se utilizará la misma máquina, para evitar consumir
más recursos de la máquina física. Por tanto deberíamos compartir un directorio entre
la máquina física y la máquina de continuos integration(develenv). Para ello editar
el fichero Vagrantfile que se encuentra en el directorio y modificar el parámetro 
**config.vm.synced_folder***. 

```
  # Sustituir "/Users/carlosg/workspace" por el directorio compartido de la máquina física donde se desarrollará la aplicación.
  config.vm.synced_folder "/Users/carlosg/workspace", "/home/vagrant/workspace"
```

Una vez configurado el directorio compartido ya se puede arrancar la máquina la máquina.

```
carlosg@ironman: workspace/cd_workshop/pipelineTraining-web-develop/src/site/resources/vagrant/develenv$ vagrant plugin install vagrant-vbguest
carlosg@ironman: workspace/cd_workshop/pipelineTraining-web-develop/src/site/resources/vagrant/develenv$ vagrant up
carlosg@ironman: workspace/cd_workshop/pipelineTraining-web-develop/src/site/resources/vagrant/develenv$ vagrant ssh 
```

Dependiendo del hardware de la máquina develenv puede tardar en arrrancar varios
minutos. Mientras arranca se pueden hacer las siguientes comprobaciones:

Abrir un navegador donde se muestre la documentación de develenv:

http://192.168.33.2

Al cabo de unos minutos debería estar arrancado develenv:

http://192.168.33.2/jenkins, http://192.168.33.2/sonar, http://192.168.33.2/nexus
y http://192.168.33.2/grid/console

*NOTA!!* _Lo mejor es añadir esta máquina al /etc/hosts de la máquina donde se levantan las virtuales con vagrant._

La configuración de usuarios y password de esta máquina es:

```
User:password
root:vagrant
vagrant:vagrant
develenv:develenv (For http://192.168.33.2/jenkins,http://192.168.33.2/nexus,
http://192.168.33.2/sonar y http://192.168.33.2/develenv/admin)
```

Entornos de despliegue
----------------------

Para el workshop sólo se utilizarán 2 entornos de despliegue(integration y qa)

Para integración (192.168.33.3):

```
carlosg@ironman:~$ cd workspace/cd_workshop/pipelineTraining-web-develop/src/site/resources/vagrant/integration
carlosg@ironman: workspace/cd_workshop/pipelineTraining-web-develop/src/site/resources/vagrant/integration$ vagrant plugin install vagrant-vbguest
carlosg@ironman: workspace/cd_workshop/pipelineTraining-web-develop/src/site/resources/vagrant/integration$ vagrant up
carlosg@ironman: workspace/cd_workshop/pipelineTraining-web-develop/src/site/resources/vagrant/integration$ vagrant ssh
carlosg@ironman: workspace/cd_workshop/pipelineTraining-web-develop/src/site/resources/vagrant/integration$ ssh root@192.168.33.3
```

La configuración de usuarios y password de esta máquina es:

```
User:password
root:vagrant
vagrant:vagrant
```

Para qa (192.168.33.4):

```
carlosg@ironman:~$ cd workspace/cd_workshop/pipelineTraining-web-develop/src/site/resources/vagrant/qa
carlosg@ironman: workspace/cd_workshop/pipelineTraining-web-develop/src/site/resources/vagrant/qa$ vagrant plugin install vagrant-vbguest
carlosg@ironman: workspace/cd_workshop/pipelineTraining-web-develop/src/site/resources/vagrant/qa$ vagrant up
carlosg@ironman: workspace/cd_workshop/pipelineTraining-web-develop/src/site/resources/vagrant/qa$ vagrant ssh
carlosg@ironman: workspace/cd_workshop/pipelineTraining-web-develop/src/site/resources/vagrant/qa$ ssh root@192.168.33.4
```

La configuración de usuarios y password de esta máquina es:

```
User:password
root:vagrant
vagrant:vagrant
```