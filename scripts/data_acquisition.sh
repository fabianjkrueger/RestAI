#!/bin/bash

# download data sets

# `student_sleep_patterns.csv`
kaggle datasets download --unzip arsalanjamal002/student-sleep-patterns --path ./data/raw

# `wearable_tech_sleep_quality_1.csv`
kaggle datasets download --unzip uom190346a/sleep-and-health-metrics --path ./data/raw

# `Sleep_Efficiency.csv`
kaggle datasets download --unzip equilibriumm/sleep-efficiency --path ./data/raw

# `Sleep_health_and_lifestyle_dataset.csv`
kaggle datasets download --unzip uom190346a/sleep-health-and-lifestyle-dataset --path ./data/raw
