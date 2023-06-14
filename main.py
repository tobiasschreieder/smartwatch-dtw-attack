from evaluation.exploratory_data_analysis import plot_subject_data
from preprocessing.data_preparation import preprocess_data
from alignments.dtw_calculations import run_calculations
from evaluation.evaluation import subject_evaluation


"""
Example Calculations
------------------------------------------------------------------------------------------------------------------------
"""

"""1. Preprocess WESAD dataset and save dataset as data_dict.pickle to /dataset"""
# preprocess_data()

"""2. Plot exploratory data analysis to /out/eda"""
# plot_subject_data()

"""3. Calculate DTW-alignments and save results to /out/alignments"""
# run_calculations(methods=["baseline", "amusement", "stress"], proportions=[0.15])

"""4. Evaluate DTW-alignment results per subject; save MD-tables with distance and rank results and realistic-rank-plots
to /out/subject-plots"""
# subject_evaluation(methods=["baseline", "amusement", "stress"], proportions_test=[0.01, 0.02, 0.05, 0.1])
