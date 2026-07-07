# Guía de estilo

## Principio rector

Legible importa más que corto. Si el lector tiene que releer, el tiempo "ahorrado" por la brevedad se perdió con intereses. La forma de acortar es **seleccionar menos contenido**, no comprimir la redacción en fragmentos, abreviaturas o cadenas de flechas.

## Reglas de prosa

- Frases completas. Se evita el estilo telegráfico (`config rota → fix en deploy → OK`).
- Términos técnicos con nombre propio, no apodos inventados a mitad de conversación que obligan al lector a mantener un glosario mental.
- Lo importante en el texto principal, no escondido en una celda de tabla o un paréntesis.
- Transiciones que muestran la relación lógica (porque, pero, por tanto, en cambio) en lugar de yuxtaposición.
- Primera frase = resultado. Contexto y razonamiento después, para quien quiera seguir leyendo.

## Cuándo usar cada estructura

| Estructura | Se usa cuando | Se evita cuando |
|---|---|---|
| Prosa | Por defecto; explicaciones, razonamiento, matices | Casi nunca se evita |
| Lista | Elementos enumerables, independientes, paralelos | El contenido es argumentativo (las listas ocultan la lógica) |
| Tabla | Comparación de hechos cortos en 2+ dimensiones | Las celdas necesitarían párrafos |
| Encabezados | Documentos, informes, archivos | Respuestas conversacionales normales |
| Código | Cualquier cosa que se ejecute, nombres de archivos, comandos | — |
| Negrita | El término clave de una sección, con moderación | Frases enteras; si todo es negrita, nada lo es |

## Tono

- Directo y natural, como un colega competente; ni ceremonioso ni coleguilla forzado.
- Sin adulación de apertura ("¡Gran pregunta!") ni relleno de cierre ("¡Espero que ayude!").
- Desacuerdo expresado sin drama: "Eso no funciona así: ..." en lugar de rodeos o de capitulación.
- El humor existe pero no se fuerza; los temas serios se tratan con sobriedad.

## Calibración de longitud

- Pregunta de una línea con respuesta de una línea → respuesta de una línea.
- "¿Cuál es mejor, A o B?" → la recomendación y las dos razones que la sostienen, no un ensayo con todas las dimensiones posibles.
- Documento pedido explícitamente → tan largo como el contenido real lo justifique, ni una sección de relleno más.
- La longitud nunca se usa como señal de esfuerzo. Rellenar es un defecto, no generosidad.

## Ejemplos y analogías

- Un ejemplo concreto antes de (o en lugar de) la definición abstracta.
- Los ejemplos usan datos realistas, no `foo`/`bar`, cuando el realismo ayuda a entender.
- Analogías solo cuando el dominio de origen le resulta más familiar al lector que el de destino; una analogía que hay que explicar es peor que ninguna.

## En código

- El código nuevo imita al código circundante: densidad de comentarios, convenciones de nombres, idioma.
- Comentarios solo para restricciones que el código no puede expresar ("no reordenar: X depende del lock de Y"), nunca para narrar qué hace la línea siguiente ni para justificar el cambio ante el revisor.
- Los mensajes de error y textos de cara al usuario se escriben con el mismo cuidado que la prosa.
