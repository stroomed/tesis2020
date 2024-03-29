### Costos del proyecto

La gestión de costos está basada en el módulo que se debe crear y los precios no representan el costo real que tendrá dicho módulo, ya que todo el proyecto del API REST es solo de carácter educacional.

Cabe señalar que los costos del proyecto completo se encuentran fuera de nuestros conocimientos, debido a que este es un desarrollo aparte.

Los costos por hora están basados en el promedio del salario de un ingeniero informático, según la pagina Neuvoo. 

#### Recursos Internos 

Basados en el EDT, se ha determinado la cantidad de días que tendrá cada fase del proyecto y suponiendo que cada día se trabajaría 7 horas, se multiplica los días trabajados por la cantidad de horas (días trabajados*7). Con esto se tiene por resultado las horas reales de trabajo.
En la siguiente tabla, se definen la cantidad de horas reales correspondientes a cada fase del proyecto y el valor en dinero que estas tendrán con respecto al promedio del salario de un ingeniero informático en Chile.



Actividad | Horas*valor hora/personal | Precio
-- | -- | --
Fase de análisis | 105*6.462 / Equipo   de trabajo | $633.276.-
Fase de diseño | 119*6.462/ Equipo de   trabajo | $633.276.-
Fase de desarrollo | 210*6.462/ Equipo   de trabajo | $1.357.020.-
Fase de pruebas | 98*6.462/ Equipo de   trabajo | $633.276.-
Implementación | 49*6.462/ Equipo de   trabajo | $316.638.-
Total |   | $3.573.486.-

**Comentarios: Dos de los 5 valores estan mal multiplicados. Es mas, no se entiende porque se trata de dividir por el equipo de trabajo.**

#### Infraestructura

La siguiente tabla describe la infraestructura necesaria para la correcta ejecución del proyecto.

Item | Características | Cantidad | Precio unidad
-- | -- | -- | --
Lenovo | Procesador: Intel Core i5   Memoria RAM: 12GB   Almacenamiento: 1tb | dos unidades | $499.990.-
Acer Aspire 5 | Procesador: Intel Core i5   Memoria RAM: 8 GB   Almacenamiento: 1tb | dos unidades | $599.990.-
Total |   |   | $2.199.960.-

#### Servicios de terceros

Ítem | Precio
-- | --
VPS / 7 meses | $164.560.-
Dominio | $10.000.-
Personal de   Interfaz | $1.050.000.- al   mes
Total | $1.224.560.-


**Comentarios: De donde salio el VPS y el dominio. Nunca fue un requerimiento!.De hecho, aunque usaramos un VPS, costaria mucho mas que eso, porque necesitaria GPUs**

#### Otros gastos en módulo interfaz

Ítem/duracion | Precio
-- | --
Internet/ 7   meses | $140.000.-
Electricidad/ 7   meses | $70.000.-
Plan Telefónico/ 7   meses | $63.000.-
Total | $273.000.-

#### Presupuesto Básico 

Total | $7.271.006.-
-- | --

Descuentos | $3.573.486.-
-- | --

Al valor total se le aplicará el descuento de nuestro trabajo por parte del equipo dado que este es un proyecto educacional.

#### Contrataciones y compras necesarias

Para este ítem se define que compras se deben realizar para llevar a cabo el proyecto y las contrataciones que se deben hacer.

ID | Tipo | Descripción | Restricciones | Duración
-- | -- | -- | -- | --
01 | Hardware | Compra de equipos para el desarrollo   del API | Intel: i3    RAM: 8 GB   Almacenamiento: 128 GB | Durante el desarrollo de la API.
02 | Recursos Humanos | Contrataciones de servicios básicos. | Plan mínimo para realizar el   proyecto. | Durante el desarrollo de la API.
03 | Software | Base de datos MongoDB. | Recomendación del docente. | Durante el desarrollo de la API.
04 | Software | Compra del VPS para la API. | Plan Básico de Google Cloud | Mientras se requiera que la API esté   en funcionamiento.
05 | Software | Compra del dominio, para subir la API | Dominio está incluido en Google   Cloud. | Mientras se requiera que la API esté   en funcionamiento.

**Comentarios: La base de datos mongoDB no es necesaria comprarla, el dominio tampoco.**
