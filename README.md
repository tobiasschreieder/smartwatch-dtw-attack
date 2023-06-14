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

4. Evaluate DTW-alignment results per subject; save MD-tables with distance and rank results to /out/subject-plots
* subject_evaluation(methods=["baseline", "amusement", "stress"], proportions_test=[0.01, 0.02, 0.05, 0.1])
