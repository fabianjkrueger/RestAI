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


## Intermediate

Files derived from the raw data. These are intermediate, because not all
necessary data preparation and processing has been done already.

### `sleep_data_main_intermediate.csv`

Derived from `student_sleep_patterns.csv` by selecting relevant columns.

## Processed

Finalized data for training, evaluating and testing models.
