SUMADORA WEB
============
 Implementación de una calculadora web que sólo sabe sumar números naturales
 de 2 cifras.

  * Test de aceptación
    * [Definición](https://pimpam.googlecode.com/svn/trunk/webCalculator-acceptanceTest/src/test/resources/com/softwaresano/examples/calculator/test/acceptance/WebCalculator.html)
    * [Implementación(concordion y selenium)](https://pimpam.googlecode.com/svn/trunk/webCalculator-acceptanceTest/src/test/java/com/softwaresano/examples/calculator/test/acceptance/WebCalculator.java)
  * Frontend web
    * [Interfaz](https://pimpam.googlecode.com/svn/trunk/webCalculator-frontend/src/main/webapp/index.html)
    * [Empaquetado](https://pimpam.googlecode.com/svn/trunk/webCalculator-frontend/src/main/rpm/SPECS/frontend.spec)
    * [Conexión con backend](https://pimpam.googlecode.com/svn/trunk/webCalculator-frontend/src/main/rpm/SOURCES/frontend/adder.conf)
  * Backend
    * [Tests unitarios](https://pimpam.googlecode.com/svn/trunk/webCalculator-backend/src/test/java/com/softwaresano/examples/calculator/test/Component.java)
    * [Implementación calculadora](http://pimpam.googlecode.com/svn/trunk/webCalculator-backend/src/main/java/com/softwaresano/examples/calculator/impl/Calculator.java)
    * [Implementación backend web](https://pimpam.googlecode.com/svn/trunk/webCalculator-backend/src/main/java/com/softwaresano/examples/calculator/web/Calculator.java)
    * [Empaquetado](https://pimpam.googlecode.com/svn/trunk/webCalculator-backend/src/main/rpm/SPECS/backend.spec) 
  * Deployment pipeline
    * [Creación](http://develenv.softwaresano.com/deploymentPipeline/index.html#Creacin_del_pipeline_Interfaz_Grfica)
    * Ejecución
      * 1.    [Ejecutar frontend](../../img/examples/webCalculator/executeFrontend.png)
      * 2.    [Ejecutar backend](../../img/examples/webCalculator/executeBackend.png)
      * 3.    Compilación, unitTest, métricas y modulos war
        * 3.1 [Compilación](../../img/examples/webCalculator/buildBackendResult.png)
        * 3.2 [Módulo war](../../img/examples/webCalculator/buildBackendNexus.png)      
        * 3.3 [Métricas de calidad del código](../../img/examples/webCalculator/buildBackendSonar.png)
      * 4.    Empaquetado
        * 4.1 [Generación del rpm](../../img/examples/webCalculator/buildBackendCreateRpm.png)
        * 4.2 [Publicación del rpm](../../img/examples/webCalculator/buildBackendRpm.png)      
      * 5.    [Despliegue en integración](../../img/examples/webCalculator/dp_integration.png)
      * 6. Despliegue en qa
        * 6.1   [Ejecución](../../img/examples/webCalculator/deployInQa.png)
        * 6.2   [Despliegue](../../img/examples/webCalculator/dp_qa.png)
      * 7. Exportación repositorios
        * 7.1   [Ejecución](../../img/examples/webCalculator/exportRepo.png)