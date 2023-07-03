# Smartwatch-DTW-Attack

## Dataset:
Please download the WESAD dataset from https://uni-siegen.sciebo.de/s/HGdUkoNlW1Ub0Gx and save it unzipped under /dataset/WESAD

## Code example calculations
1. Preprocess WESAD dataset and save dataset as data_dict.pickle to /dataset
* preprocess_data()

2. Plot exploratory data analysis to /out/eda
* plot_subject_data()

3. Calculate DTW-alignments and save results to /out/alignments
* run_calculations(methods=["baseline", "amusement", "stress"], proportions=[0.15])

4. Evaluate DTW-alignment results per subject; save MD-tables with distance and rank results and realistic-rank-plots to /out/subject-plots
* subject_evaluation()

5. Evaluation DTW-alignment results overall mit precision@k; save MD-tables with precision values
* precision_evaluation(k_list=[1, 3, 5])

6. Evaluation of rank-method; save precision@k values as MD-table
* run_rank_method_evaluation()

7. Evaluation of classes, save precision@k values as MD-table
* run_class_evaluation(rank_method="score")

8. Evaluation of sensor-combinations, save precision@k values as MD-table
* run_sensor_evaluation(rank_method="score", average_method="weighted-mean")

9. Evaluation of windows, save precision@k values as MD-table
* run_window_evaluation(rank_method="score", average_method="weighted-mean", sensor_combination=[["acc", "temp"]])

10. Complete optimization evaluation, save precision@k values as MD-table 
* run_optimization_evaluation()

11. Calculate maximum precisions, save precision@k values as json file
* run_calculate_max_precision(k_list=[1, 3, 5])

12. Overall evaluation with (DTW-results, maximum results, random guess results), save precision@k values as MD-table
* run_overall_evaluation()