# Laboratorio No. 2 – Expresiones Regulares y Autómatas

**Nombre:** Ruth de León  
**Carné:** 22428  
**Carrera:** Ingeniería en Ciencia de la Computación y Tecnologías de la Información  
**Fecha de entrega:** 27 de julio de 2025  
**Curso:** Teoría de la Computación

Este repositorio contiene tres ejercicios que trabajan con expresiones regulares, verificación de balanceo y conversión de notaciones utilizando el algoritmo de **Shunting Yard**.

---

## 📂 Ejercicios

### **Ejercicio 1: Balanceo de Paréntesis**
**Objetivo:**  
Verificar que una expresión regular tenga correctamente balanceados los paréntesis, corchetes y llaves.

**Archivo:** `balance.py`  

**Ejecución:**
```bash
py balance.py
```

**Ejemplo de salida:**
```
Expresión: a(a|b)*b+a?
Paso 1: '(' → push → pila: ['(']
Paso 2: ')' → pop → pila: []
Resultado: Balanceado
```

---

### **Ejercicio 2: Inserción de Concatenación Explícita**
**Objetivo:**  
Formatear una expresión regular agregando de manera explícita el operador de concatenación `.` donde corresponda.

**Archivo:** `Shunting_Yard.py`  

**Ejemplo:**
Entrada:
```
(a|b)c*
```
Salida:
```
(a|b).c*
```

---

### **Ejercicio 3: Conversión Infix → Postfix (Shunting Yard)**
**Objetivo:**  
Convertir expresiones regulares de notación infix a postfix utilizando el algoritmo de **Shunting Yard**.

**Archivo:** `Shunting_Yard.py`  

**Ejecución:**
```bash
py Shunting_Yard.py
```

**Ejemplo de salida:**
```
Procesando: (a|t)c
Regex formateado: (a|t).c
Carácter: (  Pila: ['(']  Postfix: 
Carácter: a  Pila: ['(']  Postfix: a
Carácter: |  Pila: ['(', '|']  Postfix: a
Carácter: t  Pila: ['(', '|']  Postfix: at
Carácter: )  Pila: []  Postfix: at|
Carácter: .  Pila: ['.']  Postfix: at|
Carácter: c  Pila: ['.']  Postfix: at|c
Postfix final: at|c
```

---

## 📄 Archivos de Entrada
Todos los ejercicios pueden trabajar con archivos de texto (`*.txt`) que contengan **una expresión por línea**.

Ejemplo `solu_expres.txt`:
```
(a|b)c*
(a|t)c
ab+c?
```

---

## 🔗 Referencia
Pseudocódigo de Shunting Yard adaptado de:  
[https://gist.github.com/gbrolo/1a80f67f8d0a20d42828fb3fdb7be4de](https://gist.github.com/gbrolo/1a80f67f8d0a20d42828fb3fdb7be4de)

Video desarrollado para la explicación del código: (https://www.youtube.com/watch?v=SGKlfSNpEXM)  
