# Bike Sales – EDA, Limpieza y Análisis

Este proyecto incluye:
1. Un **EDA inicial** para detectar problemas en los datos.
2. Un **Data Quality Log** donde se documentan nulos, duplicados, ruido textual, columnas redundantes e incoherencias.
3. Un **pipeline de limpieza** con Pandas para normalizar texto, corregir fechas, gestionar nulos, tratar duplicados y generar un dataset fiable.
4. Un **análisis básico de negocio** (KPIs y visualizaciones) centrado en las ventas de diciembre.

## Archivos principales
- `eda_inicial.ipynb` — EDA + Data Quality Log.  
- `data_cleaning.ipynb` — Limpieza completa y exportación del dataset.  
- `datasets/bikesales.xlsx` — Datos originales.  
- `datasets/bikesales_clean.xlsx` — Datos limpios generados.

## Objetivo
Obtener un dataset limpio y coherente para analizar la **campaña de navidad**, identificando:
- productos más vendidos,  
- países con mayor revenue,  
- distribución del ticket medio,  
- evolución diaria de ventas.