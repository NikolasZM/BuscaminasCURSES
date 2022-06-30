# BuscaminasCURSES
El clasico buscaminas con interfaz gráfica.<br>
<h2>Autor</h2>
Nikolas Zuñiga
</u1>
<h2>¿Qué se utilizó?</h2>
Para que el código funcione se utilizó varias funciones, encargadas de generar el campo, generar las minas, etc. Dentro se uso distintos elementos como listas anidadas, bucles for y while, y condicionales. Tambien se implementó el modulo CURSES, para poder realizar la interfaz gráfica.<br>
<h2>¿Cómo usar?</h2>
Al iniciar, se genera un campo de 8x8 casillas, con 7 minas en lugares aleatorios. El jugador tendrá que mover el puntero con las flechas hasta una casilla, despues al presionar m, minará esa casilla mostrando su número, si presiona p, se pondrá una bandera encima de la mina, si mina una casilla que es una mina, esta explotará cerrando el juego.
<h2>Ejemplo</h2>
---------------------------------------------<br>
| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
---------------------------------------------<br>
Escoge las coordenadas de la casilla que quieres minar (Ejemplo: 5 5): 5 5<br>
---------------------------------------------<br>
---------------------------------------------<br>
| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
| _ | _ | _ | _ | 0 | 0 | 1 | _ | _ | _ |<br>
| _ | _ | _ | _ | 0 | 0 | 0 | _ | _ | _ |<br>
| _ | _ | _ | _ | 0 | 0 | 0 | _ | _ | _ |<br>
| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
---------------------------------------------<br>
Escoge las coordenadas de la casilla que quieres minar (Ejemplo: 5 5): 3 7<br>
---------------------------------------------<br>
| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
| _ | _ | _ | _ | _ | _ | _ | X | _ | _ |<br>
| _ | _ | _ | _ | 0 | 0 | 1 | _ | _ | _ |<br>
| _ | _ | _ | _ | 0 | 0 | 0 | _ | _ | _ |<br>
| _ | _ | _ | _ | 0 | 0 | 0 | _ | _ | _ |<br>
| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
---------------------------------------------<br>
Ups, minaste una mina. El juego termino.!!!!!
