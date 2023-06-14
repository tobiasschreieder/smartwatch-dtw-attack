from evaluation.calculate_precisions import calculate_max_precision
from evaluation.calculate_ranks import run_calculate_ranks
from preprocessing.data_preparation import get_subject_list
from evaluation.create_md_tables import create_md_distances, create_md_ranks
from preprocessing.process_results import load_results

from typing import List
import os


MAIN_PATH = os.path.abspath(os.getcwd())
OUT_PATH = os.path.join(MAIN_PATH, "../out")  # add /out to path
SUBJECT_PLOT_PATH = os.path.join(OUT_PATH, "subject-plots")


def run_calculate_max_precision(k_list: List[int], methods: List[str], proportions_test: List[float],
                                step_width: float = 0.1):
    """
    Run calculations of maximum-precisions for specified k's, methods and test-proportions
    :param k_list: List with all k parameter
    :param methods: List with all methods ("baseline", "amusement", "stress")
    :param proportions_test: List with all test_proportions
    :param step_width: Specify step-width for weights
    """
    for k in k_list:
        for method in methods:
            for proportion_test in proportions_test:
                calculate_max_precision(k=k, step_width=step_width, method=method, proportion_test=proportion_test)


def subject_evaluation(methods: List[str], proportions_test: List[float], subject_list=None):
    """
    Create distance and rank-table for each subject
    :param methods: List with methods ("baseline", "amusement", "stress")
    :param proportions_test: List with test-proportions
    :param subject_list: Specify subject-ids if None: all subjects are used
    """
    if subject_list is None:
        subject_list = get_subject_list()

    for method in methods:
        for proportion_test in proportions_test:
            text = list()
            text.append("# Subject Rank and Distance Table")
            text.append("* method: " + str(method))
            text.append("* test-proportion: " + str(proportion_test))

            for subject in subject_list:
                results = load_results(subject_id=subject, method=method, proportion_test=proportion_test)
                overall_ranks_rank, individual_ranks_rank = run_calculate_ranks(results=results, method="rank")
                overall_ranks_score, individual_ranks_score = run_calculate_ranks(results=results, method="score")

                text_distances = create_md_distances(results=results, subject_id=subject)
                text_ranks_rank = create_md_ranks(overall_ranks=overall_ranks_rank,
                                                  individual_ranks=individual_ranks_rank, subject_id=subject)
                text_ranks_score = create_md_ranks(overall_ranks=overall_ranks_score,
                                                   individual_ranks=individual_ranks_score, subject_id=subject)

                text.append("## Subject: " + str(subject))
                text.append(text_distances)
                text.append(text_ranks_rank)
                text.append(text_ranks_score)

            # Save MD-File
            path = os.path.join(SUBJECT_PLOT_PATH, method)
            path = os.path.join(path, "test=" + str(proportion_test))
            os.makedirs(path, exist_ok=True)

            path_string = "/SW-DTW_subject-plot_" + str(method) + "_" + str(proportion_test) + ".md"
            with open(path + path_string, 'w') as outfile:
                for item in text:
                    outfile.write("%s\n" % item)

            print("SW-DTW subject-plot for method = " + str(method) + "and test-proportion = " + str(proportion_test) +
                  " saved at: " + str(path))




