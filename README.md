# Práctica 4: Pruebas unitarias

**Nombre del equipo:** La Orden del Fénix

**Integrantes:**
- Ortiz Trujillo Jimena
- Astrid Flores Corona
- Ivone Alejandra Flores Leyva

Esta práctica consiste en diseñar y ejecutar pruebas unitarias para verificar el comportamiento de un sistema de cobro de estacionamiento a partir de las reglas establecidas en su modelo.

El objetivo es comprobar que los resultados obtenidos por la implementación coincidan con los resultados esperados, identificar errores y analizar la importancia de diseñar pruebas antes de evaluar el código.

El proyecto contempla el uso de pytest para Python y JUnit 5 para Java.

# Ejecución de las pruebas en Python

## Requisitos

Tener Python instalado.

Instalar las dependencias indicadas en requirements.txt.

# Instalación

Desde una terminal, entrar en el directorio python:

'''
cd python
python -m pip install -r requirements.txt
'''

# Ejecutar las pruebas

'''
pytest -v
'''

La opción -v muestra individualmente los casos ejecutados y sus resultados.

# Resultado obtenido

Las pruebas unitarias de Python verifican los casos normales, las fronteras, las entradas inválidas y las interacciones entre reglas.

La suite de Python cuenta con 16 ejecuciones aprobadas. Durante las pruebas iniciales se identificaron errores en la implementación, por lo que se realizaron correcciones para cumplir con las reglas del modelo.

# Ejecución de las pruebas en Java

La práctica contempla una versión en Java con JUnit 5 y Maven.

Para ejecutar las pruebas, se requiere un JDK y Maven correctamente instalados y configurados.

Desde una terminal, ejecutar:
'''
cd java
mvn test
'''

Este comando compila el proyecto y ejecuta las pruebas detectadas por Maven.

La implementación de Java también fue corregida para cumplir con las reglas del modelo del estacionamiento. Las pruebas unitarias permiten comprobar el comportamiento esperado en los casos evaluados.

Tanto Python como Java cuentan con pruebas unitarias para verificar el comportamiento del sistema. Sin embargo, que todas las pruebas pasen no garantiza por sí solo que el programa esté libre de todos los errores posibles.

# Preguntas

1. ¿Qué diferencia hay entre un caso normal y un caso frontera?

Un caso normal comprueba un valor habitual dentro de una regla. En cambio, un caso frontera evalúa valores cercanos a los límites, donde es más probable que existan errores en las condiciones. Por ejemplo, se prueban 14, 15 y 16 minutos para comprobar el límite del estacionamiento gratuito.

2. ¿Cuál de las pruebas es más importante y por qué?

La prueba de 61 minutos con un cliente frecuente es importante porque combina dos reglas: el cobro de una hora adicional iniciada y el descuento del 10 %. Permite verificar que ambas reglas se apliquen correctamente y que el resultado decimal sea de $31.50.

3. ¿Se encontró algún comportamiento que no coincidiera con el modelo?

Sí. Durante la ejecución inicial de las pruebas de Python se identificaron discrepancias en los límites de la tarifa gratuita, el cálculo de las horas adicionales y la aplicación del descuento a los boletos perdidos. Se corrigió la implementación y posteriormente las 16 pruebas de Python pasaron. También se realizaron correcciones en Java para cumplir con las reglas del modelo.

4. ¿Una suite con el 100 % de pruebas aprobadas demuestra que el programa es correcto?

No. Significa que el programa produjo los resultados esperados para los casos que se evaluaron. Pueden existir errores en situaciones que no fueron contempladas, por lo que es importante diseñar casos representativos, revisar los límites y ampliar las pruebas cuando sea necesario.

5. Si una IA generara automáticamente 50 pruebas, ¿qué tendría que revisar una persona?

Debe comprobar que cada prueba corresponda a una regla del modelo y que los resultados esperados sean correctos. También debe verificar que existan casos normales, fronteras e inválidos, y que no se repitan casos sin aportar cobertura adicional. Además, debe revisar las excepciones y las interacciones entre reglas, ejecutar las pruebas y analizar sus resultados.

# Conclusión

Las pruebas unitarias permiten comprobar de forma sistemática el comportamiento de un programa y detectar errores que pueden pasar inadvertidos durante una revisión del código. En esta práctica, el diseño de casos a partir del modelo permitió identificar discrepancias y corregir las implementaciones.

Que todas las pruebas pasen no garantiza que el sistema sea completamente correcto; demuestra que cumple con los comportamientos evaluados. Por ello, la calidad de una suite depende tanto de su ejecución como de la selección y justificación de sus casos de prueba.
