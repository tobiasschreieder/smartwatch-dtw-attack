from alignments.dtw_attack import run_calculations
from evaluation.analysis.exploratory_data_analysis import plot_subject_data
from evaluation.evaluation import subject_evaluation, precision_evaluation, run_optimization_evaluation
from evaluation.optimization.class_evaluation import run_class_evaluation
from evaluation.optimization.rank_method_evaluation import run_rank_method_evaluation
from evaluation.optimization.sensor_evaluation import run_sensor_evaluation
from evaluation.optimization.window_evaluation import run_window_evaluation
from preprocessing.data_preparation import preprocess_data
from evaluation.optimization.overall_evaluation import run_overall_evaluation


import getopt
import sys


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

"""5. Evaluation DTW-alignment results overall mit precision@k; save MD-tables with precision values"""
# precision_evaluation(methods=["baseline", "amusement", "stress"], proportions_test=[0.01, 0.02, 0.05, 0.1],
#                      k_list=[1, 3, 5])

"""6. Evaluation of rank-method; save precision@k values as MD-table"""
# run_rank_method_evaluation()

"""7. Evaluation of classes, save precision@k values as MD-table"""
# run_class_evaluation(rank_method="score")

"""8. Evaluation of sensor-combinations, save precision@k values as MD-table"""
# run_sensor_evaluation(rank_method="score", average_method="weighted-mean")

"""9. Evaluation of windows, save precision@k values as MD-table"""
# run_window_evaluation(rank_method="score", average_method="weighted-mean", sensor_combination=[["acc", "temp"]])

"""10. Complete optimization evaluation, save precision@k values as MD-table"""
# run_optimization_evaluation()

"""11. Overall evaluation with (DTW-results, maximum results, random guess results), save precision@k values as 
MD-table"""
# run_overall_evaluation()


"""
Main for input arguments
------------------------------------------------------------------------------------------------------------------------
"""


def main(argv):
    subject_ids = list()
    try:
        opts, args = getopt.getopt(argv, 's:', ['subject_ids='])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-s", "--subject_ids"):
            subject_ids = int(arg)
    run_calculations(proportions=[0.001, 0.005], subject_ids=[subject_ids])


if __name__ == "__main__":
    main(sys.argv[1:])