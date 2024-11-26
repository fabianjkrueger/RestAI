# Data

## Raw

The unchanged and unprocessed data downloaded from the original source they were
accessed from. In the case of this project, this is Kaggle.

Technically, this may not truly be 'raw' data, as data sets uploaded to Kaggle
are typically processed in some way already. Here, it is regarded as raw though.

In this project, raw data is considered immutable. This means it will not be
changed in any way, and all data derived from it will be stored in dedicated
files.

### `student_sleep_patterns.csv`

Source: https://www.kaggle.com/datasets/arsalanjamal002/student-sleep-patterns

### `wearable_tech_sleep_quality_1.csv`

Source: https://www.kaggle.com/datasets/uom190346a/sleep-and-health-metrics

### `Sleep_Efficiency.csv`

Source: https://www.kaggle.com/datasets/equilibriumm/sleep-efficiency/data

### `Sleep_health_and_lifestyle_dataset.csv`

Source: https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset

## Processed

Finalized and solit data for training, evaluating and testing models.
Each subdirectory contains four files.
Here is what they represent:

|**file**|**represents**|
|-|-|
|`.*test_features.csv`|`X_test`|
|`.*test_labels.csv`|`y_test`|
|`.*train_features.csv`|`X_train`|
|`.*train_labels.csv`|`y_train`|

All four files were generated in the notebook
`01-data_preparation.ipynb`.

### Main

This is the main data set of this project.
It was used to train the final model.
It proved to be the most useful for the task of sleep prediction.
It is derived from `student_sleep_patterns.csv` by 
selecting and processing relevant columns.

### Integrated

An experimental data set resulting by integrating four
individual data sets about sleep quality.
In the end, this experimental approach didn't prove to be
useful, so the data was not used to train the final model.
