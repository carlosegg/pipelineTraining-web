Ejecutando pipeline
===================

La pipeline se ejecutará cuando haya un cambio en la rama develop del repositorio de fuentes del proyecto [pipelineTraining-web](https://github.com/carlosegg/pipelineTraining-web). 

Si todo ha sido correcto acabará instalando, ejecutando los smoke tests y los acceptance Test en el entorno de [int](http://192.168.33.3/pipelineTraining)
![pipeline training deploy in int](./img/training/pipelineTrainingDeployInInt.png "Pipeline Training deploy in int")

Para instalar el ejemplo en un entorno diferente al de 
[int](http://192.168.33.2/pipelineTraining) hay que hacerlo a través del 
[panel de despliegues](http://192.168.33.2/develenv/dp/index.html?&executorPipelines=pipelineTraining%28develenv%29)

![Deployment Dashboard](./img/training/deploymentDashboard.png "Deployment dashboard")
