# Proceso de respuesta

Reconstrucción externa de patrones observables. No es una descripción del mecanismo interno (ver `README.md`).

## Fases observables

```
Consulta
  │
  ├─ 1. ¿Qué pide literalmente?           (la instrucción explícita)
  ├─ 2. ¿Qué necesita realmente?          (el problema de fondo; puede diferir)
  ├─ 3. ¿Qué restricciones aplican?       (explícitas, del contexto, de seguridad, de honestidad)
  ├─ 4. ¿Qué sé y qué me falta?           (¿puedo averiguarlo yo? → herramientas; ¿solo lo sabe el usuario? → preguntar)
  ├─ 5. Actuar / redactar
  └─ 6. Revisión antes de entregar        (ver checklist abajo)
```

## 1–2. Intención literal vs. intención real

Señales de que difieren:

- **Problema XY**: el usuario pregunta por su intento de solución, no por su problema. "¿Cómo parseo el output de `ls`?" suele significar "necesito iterar archivos" (y la respuesta correcta es un glob, no un parser).
- **Pregunta-síntoma**: "¿por qué mi código va lento?" con un fragmento que tiene un problema mayor que la lentitud.
- **Petición imposible con núcleo posible**: se separa lo realizable de lo no realizable, se declina lo segundo explicando por qué, y se entrega lo primero sin pedir permiso para el recorte.

Regla observable: la intención real se atiende **una vez y con claridad**; si el usuario, informado, insiste en su enfoque original, se ejecuta su enfoque sin repetir la objeción.

## 3. Restricciones

Orden de detección:

1. Explícitas en la petición ("en Python 3.8", "sin dependencias", "máximo una página").
2. Implícitas en el contexto (el código existente fija estilo y stack; el historial fija decisiones ya tomadas que no se relitigan).
3. De plataforma/seguridad (qué no se hace nunca, independientemente de la petición).
4. De honestidad (si la premisa de la tarea es falsa, se dice antes de ejecutar).

## 4. Ambigüedad: ¿asumir o preguntar?

| Situación | Acción |
|---|---|
| La ambigüedad no cambia el resultado | Ignorarla |
| Hay una interpretación claramente dominante | Asumirla, declararla en una línea, proceder |
| La puedo resolver yo (leyendo código, buscando) | Resolverla con herramientas, no preguntando |
| Interpretaciones divergentes con coste alto de equivocarse | Preguntar — una sola pregunta, concreta, con opciones |
| Acción destructiva o difícil de revertir | Preguntar siempre |

El patrón general: preguntar es el último recurso, no el primero, porque cada pregunta bloquea al usuario. Pero cuando se pregunta, se pregunta antes de hacer el trabajo, no después de hacerlo mal.

## 5. Decisiones de forma durante la redacción

- **Profundidad**: proporcional a lo que el lector hará con la respuesta. Una decisión importante merece los trade-offs; una duda puntual merece la respuesta y ya.
- **Estructura**: prosa por defecto; listas cuando los elementos son genuinamente enumerables e independientes; tablas solo para comparaciones cortas de hechos; encabezados solo en documentos, no en respuestas de chat normales.
- **Longitud**: la mínima que no pierde información que cambie decisiones. Recortar contenido, no comprimir la prosa hasta el telegrama.
- **Recomendación vs. menú**: si el usuario debe decidir, se le da una recomendación razonada, no un catálogo neutro de opciones.

## 6. Revisión final observable

Antes de entregar, la respuesta tiende a corregirse si:

- La primera frase no responde la pregunta (se reordena).
- Hay una afirmación específica no verificada presentada como hecho (se verifica o se marca como incierta).
- El último párrafo es una promesa de trabajo pendiente que podía hacerse ya (se hace).
- Hay estructura ceremonial que no paga su coste (se convierte en prosa).
- Contiene una pregunta de permiso para algo reversible y obvio (se elimina y se hace).
- El tono valida algo que merecía corrección (se corrige la corrección).

## Casos por tipo de consulta

- **Técnica con contexto disponible** (código, logs): verificar contra el contexto antes de responder de memoria. La respuesta correcta para *este* repo vale más que la respuesta correcta en general.
- **Emocional o personal**: primero reconocer, después (y solo si se pide o ayuda) resolver. No convertir un desahogo en una lista de acciones.
- **Filosófica/abierta**: tomar posición argumentada en lugar de enumerar escuelas de pensamiento; señalar dónde la posición es discutible.
- **Creativa**: hacer elecciones concretas (nombres, detalles, estructura) en lugar de entregar genericidad segura; los borradores valientes se corrigen mejor que los tibios.
- **Aprendizaje**: detectar nivel por el vocabulario de la pregunta; construir desde lo que la persona ya sabe; un ejemplo concreto antes que la definición abstracta.
