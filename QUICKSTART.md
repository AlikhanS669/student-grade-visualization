# Quickstart Guide

## 🚀 Быстрый старт

### 1. Клонирование репозитория
```bash
git clone https://github.com/AlikhanS669/student-grade-visualization.git
cd student-grade-visualization
```

### 2. Установка окружения
```bash
# Создание виртуального окружения
python -m venv venv

# Активация (Windows)
venv\Scripts\activate

# Активация (macOS/Linux)
source venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt
```

### 3. Запуск Jupyter Notebooks
```bash
# Запуск Jupyter Lab
jupyter lab

# Или Jupyter Notebook
jupyter notebook

# Открыть нужный notebook из папки notebooks/
```

### 4. Запуск интерактивного дашборда
```bash
streamlit run app/streamlit_app.py
```

Дашборд откроется по адресу: `http://localhost:8501`

### 5. Использование модулей в Python
```python
from src.data_cleaning import load_data, clean_data
from src.visualization import plot_distribution, plot_correlation_matrix
from src.math_analysis import correlation_analysis, feature_statistics
from src.model import full_pipeline

# Загрузка данных
df = load_data('data/raw/student-grades.csv')

# Очистка данных
df_clean = clean_data('data/raw/student-grades.csv')

# Визуализация
fig = plot_distribution(df, 'G3')

# ML pipeline
results = full_pipeline(df, target_col='G3', model_type='rf')
```

---

## 📁 Структура проекта

```
student-grade-visualization/
├── data/
│   ├── raw/                 # Исходные данные
│   └── processed/           # Очищенные данные
├── notebooks/
│   ├── 01_eda.ipynb        # Exploratory Data Analysis
│   ├── 02_math_analysis.ipynb # Статистический анализ
│   └── 03_ml_model.ipynb   # ML-модели
├── src/
│   ├── __init__.py
│   ├── data_cleaning.py    # Очистка данных
│   ├── visualization.py    # Визуализация
│   ├── math_analysis.py    # Статистика
│   └── model.py            # ML-модели
├── app/
│   └── streamlit_app.py    # Интерактивный дашборд
├── report/
│   └── final_report.md     # Итоговый отчет
├── img/                    # Скриншоты и графики
├── README.md               # Основная документация
├── requirements.txt        # Зависимости
└── .gitignore
```

---

## 🔧 Решение проблем

### Проблема: ModuleNotFoundError
**Решение:** Убедитесь, что вы активировали виртуальное окружение и установили зависимости:
```bash
source venv/bin/activate  # или venv\Scripts\activate
pip install -r requirements.txt
```

### Проблема: Jupyter notebook не находит ��одули
**Решение:** Добавьте папку проекта в Python path:
```python
import sys
sys.path.append('/path/to/student-grade-visualization')
```

### Проблема: Streamlit не запускается
**Решение:** Убедитесь, что streamlit установлен:
```bash
pip install streamlit plotly
streamlit run app/streamlit_app.py
```

### Проблема: Нет данных в data/raw/
**Решение:** Скачайте датасет с Kaggle:
1. Перейдите на https://www.kaggle.com/datasets/dipam7/student-grade-prediction
2. Скачайте student-grades.csv
3. Поместите в папку data/raw/

---

## 📚 Основные функции

### Загрузка и очистка данных
```python
from src.data_cleaning import load_data, clean_data

df = load_data('data/raw/student-grades.csv')
df_clean = clean_data(
    'data/raw/student-grades.csv',
    remove_dupes=True,
    handle_missing=True,
    strategy='mean'
)
```

### Визуализация
```python
from src.visualization import (
    plot_distribution,
    plot_correlation_matrix,
    plot_boxplot,
    plot_bar
)

plot_distribution(df, 'G3')
plot_correlation_matrix(df)
plot_boxplot(df, 'G3', by='sex')
```

### Статистический анализ
```python
from src.math_analysis import (
    correlation_analysis,
    feature_statistics,
    print_statistical_report
)

corr = correlation_analysis(df, target_col='G3')
stats = feature_statistics(df)
print_statistical_report(df)
```

### Machine Learning
```python
from src.model import full_pipeline

results = full_pipeline(
    df,
    target_col='G3',
    model_type='rf',
    test_size=0.2,
    random_state=42
)

print(f"Test R²: {results['test_metrics']['R2']}")
print(f"Test RMSE: {results['test_metrics']['RMSE']}")
```

---

## 📖 Документация

- **README.md** - Основная документация проекта
- **API.md** - Полная документация всех функций
- **DEVELOPMENT.md** - Гайд для разработки
- **CONTRIBUTING.md** - Как внести вклад
- **report/final_report.md** - Финальный отчет

---

## 🎯 Следующие шаги

1. Скачайте датасет с Kaggle
2. Запустите notebooks для EDA
3. Изучите интерактивный дашборд
4. Ознакомьтесь с ML-результатами
5. Прочитайте финальный отч��т

**Happy analyzing!** 📊
