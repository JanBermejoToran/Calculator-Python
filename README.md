# 🧮 Calculator - Python & Tkinter

Una calculadora de escritorio desarrollada en **Python** utilizando **Tkinter** como interfaz gráfica. El objetivo principal del proyecto ha sido aprender el funcionamiento de una interfaz gráfica, la gestión de eventos y el tratamiento de expresiones matemáticas sin utilizar librerías externas.

---

## 📸 Características

- Operaciones básicas:
  - Suma (+)
  - Resta (-)
  - Multiplicación (*)
  - División (/)

- Soporte para:
  - Números decimales
  - Paréntesis automáticos `()`
  - Botón **AC**
  - Botón **DEL**
  - Continuar operando después de obtener un resultado
  - Conversión automática de multiplicaciones implícitas
    - `5(5)` → `5*(5)`
    - `(5)(6)` → `(5)*(6)`

- Interfaz responsive realizada con **Tkinter Grid**.

---

# 📦 Requisitos

Antes de ejecutar el proyecto es necesario tener instalado:

- Python 3.10 o superior

Comprobar la instalación:

```bash
python --version
```

---

## 📥 Instalación

Clonar el repositorio:

```bash
git clone https://github.com/TU_USUARIO/Calculator-Python.git
```

Entrar en la carpeta:

```bash
cd Calculator-Python
```

Ejecutar:

```bash
python Calculator.py
```

---

# 📚 Librerías utilizadas

El proyecto únicamente utiliza librerías estándar de Python.

```python
tkinter
```

No es necesario instalar dependencias mediante `pip`.

---

# ⚙️ Funcionamiento

La aplicación mantiene una expresión en memoria mientras el usuario pulsa los botones.

Cuando se pulsa **=**

1. Se prepara la expresión.
2. Se corrigen multiplicaciones implícitas.
3. Se adapta la expresión para que Python pueda evaluarla.
4. Se utiliza `eval()` para obtener el resultado.

---

# 🚧 Dificultades encontradas

Durante el desarrollo aparecieron varios problemas interesantes:

## Gestión de resultados

Después de calcular una operación era necesario distinguir entre:

- continuar operando (`25 + 5`)
- comenzar una operación nueva

Para ello se implementó una variable de estado:

```python
resultadoMostrar
```

---

## Botón DEL

El comportamiento del botón **DEL** cambia dependiendo de si:

- se está escribiendo una operación
- se acaba de mostrar un resultado

Esto obligó a almacenar también la expresión anterior.

---

## Paréntesis automáticos

Uno de los retos fue decidir cuándo insertar:

```
(
```

y cuándo insertar

```
)
```

evitando producir expresiones inválidas.

---

## Multiplicaciones implícitas

Python no entiende expresiones como:

```
5(5)
```

o

```
(5)(6)
```

por lo que fue necesario convertirlas automáticamente en:

```
5*(5)

(5)*(6)
```

antes de evaluarlas.

---

## Tratamiento del porcentaje (%)

El porcentaje ha sido la parte más compleja del proyecto.

Python interpreta `%` como el operador **módulo**, mientras que una calculadora convencional utiliza el porcentaje de forma diferente.

Por ejemplo:

```
50 + 10%
```

debería producir:

```
55
```

y no

```
50.1
```

Para ello fue necesario crear una fase de preparación de la expresión antes de evaluarla.

---

# ⚠️ Limitaciones

Actualmente existen algunas limitaciones conocidas.

## Porcentaje

El porcentaje funciona únicamente en casos sencillos.

Ejemplos soportados:

```
50+10%
80-20%
50*10%
50/10%
```

Sin embargo, expresiones más complejas con múltiples operaciones o paréntesis pueden no comportarse exactamente igual que una calculadora científica.

Esto se debe a que el proyecto utiliza `eval()` y no un parser matemático propio.

---

## Eval()

La evaluación de expresiones se realiza mediante:

```python
eval()
```

Aunque resulta muy útil para fines educativos, una implementación profesional debería sustituirlo por un analizador de expresiones propio.

---

# 📁 Estructura

```
Calculator-Python/
│
├── Calculator.py
├── calculadora.png
└── README.md
```

---

# 🎯 Objetivos del proyecto

Este proyecto se ha desarrollado con fines de aprendizaje para practicar:

- Python
- Tkinter
- Interfaces gráficas
- Eventos
- Manipulación de cadenas
- Expresiones matemáticas
- Organización de código

---

# 🚀 Mejoras futuras

- Historial de operaciones.
- Cambio de tema (claro / oscuro).
- Operaciones científicas.
- Parser matemático propio.
- Mejor soporte para porcentajes complejos.
- Teclado físico.
- Atajos de teclado.
- Memoria (M+, M-, MR).

---

# 👨‍💻 Erik Catalan Rodriguez

Desarrollado como proyecto personal de aprendizaje utilizando **Python** y **Tkinter**.
