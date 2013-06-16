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
  * Backend
    * [Tests unitarios](https://pimpam.googlecode.com/svn/trunk/webCalculator-backend/src/test/java/com/softwaresano/examples/calculator/test/Component.java)
    * [Implementación calculadora](https://pimpam.googlecode.com/svn/trunk/webCalculator-backend/src/main/java/com/softwaresano/examples/calculator/Calculator.java)
    * [Implementación backend web](https://pimpam.googlecode.com/svn/trunk/webCalculator-backend/src/main/java/com/softwaresano/examples/calculator/web/Calculator.java)
    * [Empaquetado](https://pimpam.googlecode.com/svn/trunk/webCalculator-backend/src/main/rpm/SPECS/backend.spec)
  * Deployment pipeline
    * [Creación](http://develenv.softwaresano.com/deploymentPipeline/index.html#Creacin_del_pipeline_Interfaz_Grfica)
    * Ejecución
      * 1.    [Ejecutar frontend](../../img/examples/webCalculator/executeFrontend.png)
      * 2.    [Ejecutar backend](../../executeBackend.png)
      * 1.    [Compilación, empaquetado, y despliegue](../../img/examples/webCalculator/dp_build.png)
      * 2.    [Despliegue en integración](../../img/examples/webCalculator/dp_integration.png)
      * 3. [Despliegue en qa](../../img/examples/webCalculator/dp_qa.png)

  	  


