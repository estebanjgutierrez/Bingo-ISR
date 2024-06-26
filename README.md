# Bingo-ISR
Este repositorio consiste en instructivos y scripts que simulan situaciones en la preparación y durante el bingo

Hola! 
*Tutorial de cómo usar generador_grupos*:

1. Corregir el path: en la segunda celda del código (la larga) en la fila 9 dice "file_path". Cambien el path al correspondiente donde tienen el archivo excel con los apellidos y nombres de los misioneros que participan. Ojo!! el archivo excel que usen deben tener el formato apellidos-nombres en las columnas (es decir, en la primera columna deben estar todos los apellidos y en la segunda columna todos los nombres correspondientes).

2. Corregir la cantidad de grupos: a partir de la linea 20 podemos observar str con "Grupo de" x personas "-i" donde i es el numero de grupo con x cantidad de personas. Deben ajustar estas líneas acorde a la cantidad de grupos por tier y la cantidad de gente por cada grupo. Pueden terminar creando más listas o eliminando existentes? SI, dependiendo de la cantidad de gente por grupo y cantidad de grupos por tier.

*En cuanto a Simulador_bingo, la manera de utilizarlo es*:

1. Definir n_lineas y n_bingos acorde a la cantidad de lineas y bingos que desean simular que ocurra en una ronda.
2. Cambiar en la linea 58 el valor de "range(5)" acorde a la cantidad de rondas que quieras simular
3. Se simula que se compran 1200 cartones en cada ronda en la linea 26. Sean libres de cambiar dicho valor. Ojo que cada ronda simula que se compra la misma cantidad de cartones (podrían editar el código)

Cualquier duda contactar al galle por mail (ejgutierrezgarcia@gmail.com) o wpp (casi prefiero wpp)
Saludos!
Esteban.
