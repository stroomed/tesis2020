## Asignación de responsabilidades
### Roles

•	Director de proyecto: Quien lidera y guia al equipo de proyecto.

•	Analista: Cumple la tarea de analizar y definir los requisitos del cliente.

•	Equipo QA: Velan para que los objetivos de calidad del proyecto sean cumplidos.

•	Control de riesgos: Evalua los riesgos y verifica existencia de errores dentro del proyecto.

•	Equipo de proyecto: Encargados del desarrollo del software.

### Roles y encargados

Rol | Responsable
-- | --
Director | Ricardo Gutiérrez
Analista | Fabricio Guzmán
Equipo QA | Gabriel Barria
Control de riesgos | Nicol Quintuy
Equipo de trabajo | Ricardo Gutiérrez, Fabricio Guzmán, Gabriel Barria, Nicol Quintuy.

### Actividades y responsables

Actividad ID No. | Nombre de actividad | Responsable
-- | -- | --
1 | Determinación del problema | Director de proyecto
2 | Identificación de requerimientos | Analista
3 | Elaboración del plan de calidad | Equipo QA
4 | Elaboración de plan de riesgos | Control de riesgos
5 | Adaptación de témplate | Equipo de trabajo
6 | Desarrollo de diagramas | Equipo de trabajo
7 | Creación de base de datos | Equipo de trabajo
8 | Desarrollo | Equipo de trabajo
9 | Pruebas y ajustes de errores | Equipo de trabajo
10 | Entrega de API | Equipo de trabajo
11 | Manual de usuario | Equipo de trabajo

## Plan de aseguramiento de calidad
### Propósito 
En proyectos de implementación, es normal que los planes de trabajo puedan sufrir cambios durante el transcurso de este, los cuales pueden afectar de forma negativa los objetivos generales del proyecto. Por esta razón, es importante crear mecanismos que ayuden a identificar y remediar cualquier problema que pueda afectar el correcto rumbo del proyecto.  

En el siguiente plan de aseguramiento de calidad, se busca definir los procedimientos y reglas fundamentales que permitan asegurar un correcto flujo del proyecto sin caer en desviaciones, el cual, también será aplicado a todos los procedimientos y entregables del proyecto. 

Los principales objetivos del plan son:

•	Mejorar la calidad del producto entregado monitoreándolo apropiadamente.

•	Asegurar el cumplimiento de estándares y procedimientos para el software.

•	Descubrir cualquier defecto del producto en cuanto se origine y facilitar la gestión de forma que se puedan tomar acciones correctoras.

•	Descubrir desvíos en el plan, y tomar decisiones que puedan corregir dichas desviaciones.

**Organización QA**

Para realizar acciones que ayuden a la buena gestión de la calidad, se debe crear un equipo que permita analizar las consecuencias que podrían tener las desviaciones del plan original y, también, para aplicar las correctas medidas que ayuden a cumplir el o los objetivos del proyecto. Cabe aclarar que es tarea de todos los socios el cumplir con el nivel de calidad y descubrir desviaciones en el proyecto.

El equipo QA es el encargado de monitorear como todas las tareas y responsabilidades de los diferentes equipos de trabajo son llevados a cabo en sus diferentes etapas del proyecto. Las responsabilidades del equipo QA se describen a continuación:

•	Verificar la completitud en los planes de desarrollo y de calidad del proyecto.

•	Participar como moderador en inspecciones de diseño, de código u otros productos. 

•	Revisar los planes de pruebas verificando el cumplimiento de los estándares. 

•	Revisar una muestra significativa de los resultados de pruebas para determinar el cumplimiento de los planes.

•	Auditar periódicamente la performance de los productos desarrollados para determinar el cumplimiento de los estándares 

•	Participar en todas las revisiones a fin de cada fase del proyecto y registrar formalmente si los estándares y procedimientos no se alcanzaron satisfactoriamente.
 
**Actividades del equipo QA**

•	Verificación de Entregables.

•	Verificación de documentación. 

•	Verificar la viabilidad de cada hito al comienzo de este.

•	Revisión y corroboración de viabilidad del proyecto.

•	Supervisión del cumplimiento de los estándares establecidos. 

**Revisión de Entregables**

Todos los productos entregables deberán ser revisados por el equipo QA, definiendo su conformidad en base a los estándares definidos y a los objetivos de cada uno de ellos.

En cuanto a los productos de software, los mismos desarrolladores, una vez concluidas cada una de sus etapas, deberán testear la correcta funcionalidad del producto, para que después el equipo de QA realice tests del producto a través de pruebas unitarias, determinando que cumplan con los requerimientos establecidos por el cliente.

Se deben comprobar que no queden pruebas sin revisar y de haberlas se tienen que documentar.
Verificación de documentación 
Especificación de Requerimientos

El documento de especificación de requisitos debe ser explicados correcta y completamente, permitiendo dar una explicación clara de las necesidades del cliente.
La especificación debe:

•	Ser completa:

a) Externa, respecto al alcance acordado.

b) Internamente, no deben existir elementos sin especificar.

•	Ser consistente, no puede haber elementos contradictorios.

•	Ser no ambigua, todo término referido al área de aplicación debe estar definido en un glosario.

•	Ser verificable, debe ser posible verificar siguiendo un método definido, si el producto final cumple o no con cada requerimiento.

•	Estar acompañada de un detalle de los procedimientos adecuados para verificar si el producto cumple o no con los requerimientos.

•	Debe existir un requerimiento de calidad.

Los requerimientos de calidad deben cumplir ciertas necesidades que el cliente espera del producto final. A continuación, se describen dichas necesidades:

•	Funcionalidad

•	Confiabilidad

•	Usabilidad

•	Eficiencia

•	Mantenibilidad

•	Portabilidad

**Estrategia de validación**

Para la estrategia de validación se debe revisar los siguientes puntos:

a) Los requerimientos descritos en el documento de requerimientos han sido aprobados por una autoridad apropiada. En este caso sería que cumplan con el acuerdo logrado entre el cliente y el equipo de proyecto.

b) Los requerimientos descritos en el documento de requerimientos son implementados en el diseño expresado en el documento de diseño.

c) El diseño expresado en el documento de diseño esta implementado en
código.

•	Validar que el código, cuando es ejecutado, se adecua a los requerimientos
expresados en el documento de requerimientos.
 

Para ejercer la estrategia se debe implementar una plantilla la cual tendrá como objetivo referenciar que se ha cumplido y que no, además de tener un control sobre las actividades.

Verificación | SI | NO | FM | NA | Observaciones 
-- | -- | -- | -- | --| --| 
**Gestión del proyecto**
¿Se ha definido el objetivo del proyecto? |   |   |   |   |  
¿Se ha definido el alcance del proyecto? |   |   |   |   |  
¿Se han listado los entregables que se generaran durante la ejecución   del proyecto, describiendo sus objetivos de calidad en términos de requerimientos   de salida de calidad y aprobación? |   |   |   |   |  
**Organización del equipo del proyecto**
¿Se ha descrito la estructura organizacional del equipo de   proyecto? |   |   |   |   |  
¿Se definieron los roles y responsabilidades? |   |   |   |   |  
Opciones y desviaciones del proceso
¿Se ha identificado el ciclo de vida y fases e iteraciones a   ser utilizadas en el proyecto? |   |   |   |   |  
¿Se han identificado y descrito las desviaciones del proceso   definidas por la administración del proyecto? |   |   |   |   |  
**Planificación del proyecto**
¿S e ha referenciado o descrito las estimaciones de tamaño, esfuerzo   y cualquier calculo e información de soporte? ¿Se ha referenciado a un documento   separado o incluido las estimaciones de costo e información de soporte? |   |   |   |   |  
¿Las estimaciones cuentan con información histórica? |   |   |   |   |  
¿Se ha descrito un plan de equipamiento necesario? |   |   |   |   |  
¿Se han indicado las necesidades de infraestructura? ¿Se ha referenciado   o incluido la adaptación a los ambientes de trabajos estándares de la organización? |   |   |   |   |  
¿Se ha descrito o referenciado un plan de recursos humanos? |   |   |   |   |  
¿Se ha identificado la capacitación requerida por los recursos   afectados y como se llevara a cabo? |   |   |   |   |  
**Programación**
¿Se ha referenciado o incluido en la programación de actividades,   tareas, recursos y responsabilidades asignadas |   |   |   |   |  
**Planes para las actividades de soporte**
¿Se ha descrito o referenciado el plan de calidad? |   |   |   |   |  
¿Se ha descrito o referenciado un plan de riesgos? |   |   |   |   |  
¿Se ha descrito o referenciado el plan de pruebas de software? |   |   |   |   |  
¿Se ha descrito o referenciado el plan de comunicaciones? |   |   |   |   |  
¿Se identificaron las dependencias criticas? |   |   |   |   |  
**Monitoreo y control de proyecto**
¿Se ha especificado el tipo y frecuencia de producción de los   reportes del proyecto? |   |   |   |   |  
¿Se ha especificado la frecuencia y asistencia de las reuniones   del equipo de proyecto? |   |   |   |   |  
¿Se ha especificado la frecuencia de las reuniones de aceptación   de Fase/Etapa? |   |   |   |   |  

### Referencias:

Acrónimo | Significado | Descripción
-- | -- | --
SI | Adecuado | El ítem se cumple correctamente
NO | No adecuado | El ítem no se cumple o se cumple solo en parte
FM | Falta mejora | El ítem se cumple, pero puede optimizarse
NA | No aplica | El ítem no aplica al proyecto

**Verificar la viabilidad de cada hito al comienzo de este.**

Se debe comprobar que cada hito que se pretende lograr sea viable, con respecto al proyecto.

**Revisión y corroboración de viabilidad del proyecto**

Se debe comprobar la viabilidad del proyecto, a través de revisiones meticulosas a las factibilidades descritas en el proyecto, determinando así si cumplen realmente con los estándares necesarios para determinar que cada factibilidad es consistente y verídica en relación con lo que se pretende lograr. Para ello se deben establecer las siguientes condiciones en cada factibilidad:
Factibilidad técnica

•	Se debe justificar todos los requerimientos de la factibilidad
Factibilidad económica

•	Debe justificar todos costos incluidos en el proyecto.

•	La valorización debe ser razonable. 
Factibilidad legal

•	Debe ser completo dando referencias de todas las restricciones que se puedan encontrar en el ámbito legal. 

**Supervisión del cumplimiento de los estándares establecidos.** 

Dentro de las tareas de supervisión se encuentran las siguientes:
Organizar auditorías internas para cada entregable del proyecto.
Ayudar a encontrar soluciones a los problemas y supervisar que se siguen en su resolución.
Comprobar que los socios siguen los procedimientos de control de calidad.

### ESTÁNDARES, PRÁCTICAS, CONVENCIONES Y MÉTRICAS
### Estándar de Gestión, Verificación y Prácticas

1. Se utilizan las prácticas definidas en la Gestión del Proyecto.
Como estándar se utiliza el documento de especificación de áreas del conocimiento, promovida por el Project Management Institute, Inc. (PMI), tomando como referencia principal las prácticas plasmadas en la Guía del PMBOK.

2. Se utiliza un estándar de codificación o Code Estándar en inglés, a pesar de no ser un estándar formal, la comunidad de programadores lo utiliza para ayudar hacer más legible el código y que permita ser reutilizado.

3. Se utilizan las prácticas definidas en el Plan de Verificación y Validación.
Como estándar se utiliza el documento de: “Std 1012-2004 IEEE Standard for
Software Verification and Validation Plans.” 

Resumen Std. IEEE 1012-2004 Standard for Software Verification and
Validation Plans
IEEE Standard for Software
Verification and Validation
Sponsor
Software Engineering Standards Committee
of the IEEE Computer Society
Approved 12 April 2005
American National Standards Institute
Approved 8 December 2004
IEEE-SA Standards Board

Resumen:

Los procesos de verificación y validación de software (V & V) permiten determinar si los productos de desarrollo de una actividad determinada están conforme a las disposiciones de dicha actividad y si el software cumple su uso previsto y las necesidades del usuario. El ciclo de vida del proceso V & V valida y verifica los requisitos especificados para los distintos niveles de integridad del software.
El ámbito de aplicación de los procesos V & V incluye el software desarrollado, el software de los computadores utilizados, el hardware, y las interfaces. Esta verificación y validación (V & V) es una norma que aborda todos los procesos del ciclo de vida del software, incluyendo la adquisición, suministro, desarrollo, operación y mantenimiento.

Esta norma es compatible con todos los modelos de ciclo de vida, sin embargo, no todos los modelos de ciclo de vida utiliza todos los procesos que figuran en esta norma.

Esta norma se refiere a software desarrollado, mantenido o reutilizado (legado, Commercial Off-theshelf (COTS), ítems no desarrollados). El término software también incluye el firmware, microcódigo, y la documentación.

Los procesos V & V incluyen el análisis, evaluación, revisión, inspección, valoración, y
pruebas de productos de software.

Palabras clave: IV&V, software integrity level, software life cycle, V&V, validation,
verification.
