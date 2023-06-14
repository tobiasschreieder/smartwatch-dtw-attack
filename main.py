from exploratory_data_analysis import plot_subject_data
from data_preparation import preprocess_data
from evaluation import run_calculate_max_precision, subject_evaluation


subject_evaluation(methods=["baseline", "amusement", "stress"], proportions_test=[0.01, 0.02, 0.05, 0.1])



