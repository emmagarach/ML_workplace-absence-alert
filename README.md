Proyectos ML
#  🎯 Workplace Absence Alert 

## 📄 Problema / Problem

**Análisis y predicción del absentismo laboral** utilizando el dataset *Employee Absenteeism at Work*, que contiene información sobre empleados de una empresa en Brasil.

El absentismo laboral es un problema común en las organizaciones y tiene un impacto directo en la productividad, la planificación operativa y el clima laboral. Mediante la predicción de conductas de ausentismo, la empresa puede anticiparse y diseñar estrategias más eficaces de gestión del talento y bienestar.

El **objetivo** es predecir el absentismo laboral y detectar patrones de comportamiento que permitan anticipar posibles casos de ausencia frecuente. Entre las preguntas que se busca responder se encuentran:  
- ¿Qué variables personales o laborales están más relacionadas con el absentismo?
- ¿Es posible predecir si un empleado faltará al trabajo en función de su perfil?

---

**Analysis and prediction of employee absenteeism** using the *Employee Absenteeism at Work* dataset, which includes information from employees of a company in Brazil.

Absenteeism is a common issue in organizations and directly impacts productivity, operational planning, and workplace climate. Predicting absentee behavior allows companies to anticipate future cases and design more effective talent management and wellness strategies.

The **goal** is to predict employee absenteeism and identify behavioral patterns that help anticipate frequent absences. Key questions include:  
- Which personal or work-related variables are most related to absenteeism?  
- Can we predict if an employee will be absent based on their profile?

---

## 🔎 Dataset

- **Nombre**: *Employee Absenteeism at Work*
- **Fuente**: Público. Disponible en [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/445/absenteeism+at+work)
- **Descripción**: El conjunto de datos contiene 740 registros de empleados de una empresa de servicios sanitarios en Brasil. Incluye variables como edad, nivel educativo, transporte, motivo de ausencia, tiempo de ausencia en horas, entre otras.
---
- **Name**: *Employee Absenteeism at Work*
- **Source**: Public. Available at [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/445/absenteeism+at+work)
- **Description**: The dataset contains 740 records of employees from a healthcare service company in Brazil. It includes variables such as age, education level, transportation, reason for absence, absenteeism time in hours, among others.

---

## 📈 Solución adoptada / Adopted solution

Se realizó un análisis exploratorio de los datos (EDA) para comprender las relaciones entre las variables y su influencia en el absentismo. Luego se construyeron modelos de clasificación (Logistic Regression, KNN, Random Forest, XGBoost y LightGBM) para predecir el tiempo de ausencia en horas.

La evaluación de los modelos se realizó utilizando las siguientes métricas de clasificación:

- **Accuracy:** proporción de predicciones correctas sobre el total.
- **Precision:** porcentaje de predicciones de "ausente" que realmente lo fueron.
- **Recall:** porcentaje de empleados ausentes correctamente identificados.


El objetivo es que el modelo permita a la empresa anticipar **posibles ausencias significativas**, mejorando la planificación de recursos y la gestión operativa con una interpretación práctica y accionable de los datos.

---

An exploratory data analysis (EDA) was conducted to understand the relationships between variables and their influence on absenteeism. Then, classification models (Logistic Regression, KNN, Random Forest, XGBoost, and LightGBM) were built to predict the number of hours of absence.

The models were evaluated using the following classification metrics:

- **Accuracy:** the proportion of correct predictions over the total.
- **Precision:** the percentage of "absent" predictions that were actually correct.
- **Recall:** the percentage of truly absent employees correctly identified.

The goal of the model is to enable the company to anticipate significant absences, improving resource planning and operational management with a practical and actionable interpretation of the data.

## 📁 Estructura del repositorio / Repository structure
La estructura del repositorio está organizada para facilitar la **reproducibilidad y claridad** del proyecto:

- `src/`: carpeta principal con el **código fuente** del proyecto.
    - `data_sample/`: datos de muestra para **ejecutar y probar el código** sin exponer datos originales.
    - `img/`: imágenes utilizadas (gráficas, diagramas, portada).
    - `models/`: modelos entrenados guardados en `pickle` o `joblib` para su reutilización.
    - `notebooks/`: notebooks de **análisis exploratorio y pruebas**.
    - `utils/`: funciones auxiliares y módulos reutilizables para mantener limpio el código.
- `main.ipynb`: notebook final con el **flujo de trabajo completo** documentado.
- `presentation.pdf`: soporte visual para la **presentación de resultados**.
- `README.md`: resumen del proyecto con **descripción, estructura y pasos de uso**.

---

The repository structure is organized to ensure **clarity and reproducibility**:

- `src/`: main folder containing the **project source code**.
    - `data_sample/`: sample data files to **run and test the code** without exposing original data.
    - `img/`: images used in the project (charts, diagrams, cover images).
    - `models/`: trained models saved as `pickle` or `joblib` for reuse.
    - `notebooks/`: notebooks for **exploratory analysis and testing**.
    - `utils/`: helper functions and reusable modules to keep the main code clean.
- `main.ipynb`: final notebook with the **fully documented workflow**.
- `presentation.pdf`: visual support for **results presentation**.
- `README.md`: project summary with **description, structure, and usage instructions**.

