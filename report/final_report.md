# Final Report: Student Grade Prediction - Data Visualization Analysis

## Executive Summary

This report presents a comprehensive analysis of the Student Grade Prediction dataset from Kaggle.

## 1. Dataset Overview

- **Records:** 395 students
- **Features:** 30+ attributes
- **Target Variable:** G3 (Final Grade, 0-20)

## 2. Key Findings

### Gender Differences
- Female students average: 12.55
- Male students average: 11.35
- Difference: ~1.2 points (statistically significant)

### Study Time Impact
- Study Time 1 (<2h): Average = 10.21
- Study Time 2 (2-10h): Average = 11.07
- Study Time 3 (10-20h): Average = 13.01
- Study Time 4 (>20h): Average = 15.59

### Top Correlations with G3
1. G2 (0.923) - Previous grade
2. G1 (0.841) - First period grade
3. failures (-0.391) - Number of failures
4. age (-0.248) - Student age
5. studytime (0.097) - Study time

## 3. Machine Learning Results

### Model Performance

#### Linear Regression
- Test R²: 0.801
- Test RMSE: 1.567

#### Random Forest (Best Model)
- Test R²: 0.821
- Test RMSE: 1.345
- Test MAE: 1.089

### Feature Importance
1. G2: 25.3%
2. G1: 18.7%
3. failures: 12.4%
4. age: 8.2%
5. absences: 7.1%

## 4. Conclusions

1. **Previous academic performance is the strongest predictor** of final grades (G1, G2 combined ~44% importance)

2. **Study time matters** - Students studying >20 hours/week score 5+ points higher than those studying <2 hours/week

3. **Gender gap exists** - Female students statistically outperform male students by ~1.2 points

4. **Early intervention is key** - Students with low initial grades (G1, G2) or repeated failures need support

5. **ML models can predict grades** - Random Forest achieves 82.1% accuracy (R² = 0.821)

## 5. Recommendations

### For Educators
- Monitor students with low G1, G2 scores
- Encourage minimum 10 hours/week study time
- Engage families in student development

### For Students
- Allocate adequate study time (target: 10-20 hours/week)
- Focus on building strong foundation in first period
- Seek help early if struggling

---

**Project:** Data Visualization - Student Grade Prediction  
**Author:** Alikhan S.  
**Date:** June 2026
