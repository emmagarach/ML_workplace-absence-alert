Proyectos ML
#  🎯 Workplace Absence Alert 

## 📄 Problema / Problem

**Análisis y predicción del absentismo laboral** utilizando el dataset *Employee Absenteeism at Work*, que contiene información sobre empleados de una empresa en Brasil.

El absentismo laboral es un problema común en las organizaciones y tiene un impacto directo en la productividad, la planificación operativa y el clima laboral. Mediante la predicción de conductas de ausentismo, la empresa puede anticiparse y diseñar estrategias más eficaces de gestión del talento y bienestar.

El **objetivo** es predecir el absentismo laboral y detectar patrones de comportamiento que permitan anticipar posibles casos de ausencia frecuente. Entre las preguntas que se busca responder se encuentran:  
- ¿Qué variables personales o laborales están más relacionadas con el absentismo?  
- ¿Es posible predecir cuántas horas se ausentará un empleado en función de su perfil?

---

**Analysis and prediction of employee absenteeism** using the *Employee Absenteeism at Work* dataset, which includes information from employees of a company in Brazil.

Absenteeism is a common issue in organizations and directly impacts productivity, operational planning, and workplace climate. Predicting absentee behavior allows companies to anticipate future cases and design more effective talent management and wellness strategies.

The **goal** is to predict employee absenteeism and identify behavioral patterns that help anticipate frequent absences. Key questions include:  
- Which personal or work-related variables are most related to absenteeism?  
- Can we predict how many hours an employee will be absent based on their profile?

---

## 🔎 Dataset

- **Nombre**: *Employee Absenteeism at Work*
- **Fuente**: Público. Disponible en [UCI Machine Learning Repository]([https://archive.ics.uci.edu/dataset/445/absenteeism+at+work])
- **Descripción**: El conjunto de datos contiene 740 registros de empleados de una empresa de servicios sanitarios en Brasil. Incluye variables como edad, nivel educativo, transporte, motivo de ausencia, tiempo de ausencia en horas, entre otras.

The dataset contains 740 records from employees of a health service company in Brazil. It includes variables such as age, education level, transport type, reason for absence, and time absent (in hours), among others.

---

## 📈 Solución adoptada / Adopted solution

Se realizó un análisis exploratorio de los datos (EDA) para comprender las relaciones entre las variables y su influencia en el absentismo. Luego se construyeron modelos de regresión (Linear Regression, KNN, Random Forest, XGBoost y LightGBM) para predecir el tiempo de ausencia en horas.

La evaluación de los modelos se hizo utilizando validación cruzada y métricas como MAE, RMSE y R². Se probaron tanto versiones con como sin codificación one-hot para analizar su impacto en el rendimiento de los modelos.

---

An exploratory data analysis (EDA) was conducted to understand the relationships between variables and their influence on absenteeism. Regression models (Linear Regression, KNN, Random Forest, XGBoost, and LightGBM) were built to predict absence duration in hours.

Model evaluation used cross-validation and metrics such as MAE, RMSE, and R². Both encoded and non-encoded versions of the dataset were tested to assess the effect of categorical variable treatment.

---

## 📁 Estructura del repositorio / Repository structure
