# Lista de Errores al implementar el uso de postgres en un proyecto de scrapy
Implementando la pipeline de carga a base de datos cometí muchos errores pero definitivamente aprendí de ellos, en este archivo me encargaré de documentar los errores que ocurrieron, por más pequeños que sean pueden volver a ocurrir lo cual puede ser problemático.

## Primer Error
Los errores ocurrieron sobre todo en la funcion store_db, ya que esta era la que llevaba a cabo el manejo de los elementos, el primer error ocurrió en las queries parametrizadas que seguían la forma de "%s", (var,) resulta que hay que obligatoriamente colocar un tuple como elemento que está al lado, cometí el error de eliminar la , y el problema es que (var) simplemente es var más (var,) es un tuple


## Segundo Error
El otro error que cometí fue pensar que para los valores numéricos tendría que utilizar %f o %i en vez de %s, cuando con todos los elementos debía utilizar %s este error pudo originarse al momento de tener la primera mala experiencia con las queries parametrizadas por falta de experiencia de uso.

## Tercer Error
Este puede ser por falta de experiencia al momento de usar postgres o sistemas que interconectan elementos con nombres similares, originalmente, coloqué nombres en Español en la base de datos y nombres ingleses en el item SteamGame, esto causó que hubiera una confusión al momento de utilizar el item['price'], estando yo solicitando item['precio'], lo cual retornaba null y fue descubierto el error con pruebas independientes según el campo.

## Cuarto Error
No colocar el self.connection.commit(), si no se coloca no se hará ningún cambio en la base de datos.

## Nota
Esto más que un error es un aprendizaje pero podría ser visto como un error de mi parte, originalmente, quería manejar el UPDATE dentro del except, esto era un error, ya que una vez dentro del except el item no se retorna al crawl original y no es agregado ni siquiera al JSON aún así sus datos sean correctos, la manera correcta de implementar esto era hacer un check if de si ya un elemento con el nombre existía dentro de la tabla juegos, si este existía sería llevado a cabo el UPDATE, si este no existía sería llevado a cabo el INSERT dentro de la clausula else.
El except simplemente estaba encargado de ayudar al programador a solucionar los problemas presentes en el código, para que este código funcione en otro ordenador simplemente habría que cambiar el valor de los campos de la conexión y los nombres de la base de datos y de la tabla.
El código nombrado en el cuál se presentaron los errores puede ser encontrado en el archivo pipelines.py precísamente es la SavingToPostgresPipeline.