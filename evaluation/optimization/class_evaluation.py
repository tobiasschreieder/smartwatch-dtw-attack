from alignments.dtw_calculations import get_classes, get_proportions
from evaluation.calculate_precisions import calculate_precision_combinations
from evaluation.calculate_ranks import get_realistic_ranks_combinations
from evaluation.create_md_tables import create_md_precision_classes
from preprocessing.data_preparation import get_sensor_combinations, get_subject_list
from preprocessing.data_preparation import load_dataset

from typing import Dict, List, Tuple
import pandas as pd
import statistics
import os
import random


MAIN_PATH = os.path.abspath(os.getcwd())
OUT_PATH = os.path.join(MAIN_PATH, "out")  # add /out to path
EVALUATIONS_PATH = os.path.join(OUT_PATH, "evaluations")  # add /evaluations to path


def get_class_distribution() -> Dict[str, float]:
    """
    Get proportions of baseline, stress and amusement data (mean over all subjects)
    :return: Dictionary with proportions
    """
    data_dict = load_dataset()

    amusement_proportions = list()
    baseline_proportions = list()
    stress_proportions = list()

    for subject in data_dict:
        data = pd.DataFrame(data_dict[subject]["label"])
        subject_length = data.shape[0]

        amusement_length = data[data.label == 0.5].shape[0]
        baseline_length = data[data.label == 0].shape[0]
        stress_length = data[data.label == 1].shape[0]

        amusement_proportions.append(round(amusement_length / subject_length, 2))
        baseline_proportions.append(round(baseline_length / subject_length, 2))
        stress_proportions.append(round(stress_length / subject_length, 2))

    amusement_proportion = round(statistics.mean(amusement_proportions), 2)
    baseline_proportion = round(statistics.mean(baseline_proportions), 2)
    stress_proportion = round(statistics.mean(stress_proportions), 2)

    return {"amusement": amusement_proportion, "baseline": baseline_proportion, "stress": stress_proportion}


def calculate_class_precisions(rank_method: str = "score", subject_ids: List = None) -> Dict[int, Dict[str, float]]:
    """
    Calculate precisions per class ("baseline", "amusement", "stress"), mean over sensors and test-proportions
    :param rank_method: Specify rank-method "score" or "rank" (use beste rank-method)
    :param subject_ids: Specify subject-ids, if None: all subjects are used
    :return: Dictionary with results
    """
    sensor_combinations = get_sensor_combinations()  # Get all sensor-combinations
    classes = get_classes()  # Get all classes
    proportions_test = get_proportions()  # Get all test-proportions
    k_list = [1, 3, 5]  # List with all k for precision@k that should be considered

    if subject_ids is None:
        subject_ids = get_subject_list()

    proportion_results_dict = dict()
    for proportion_test in proportions_test:
        results_sensor = dict()
        for k in k_list:
            results_sensor.setdefault(k, dict())
            for method in classes:
                # Calculate realistic ranks with specified rank-method
                realistic_ranks_comb = get_realistic_ranks_combinations(rank_method=rank_method,
                                                                        combinations=sensor_combinations,
                                                                        method=method,
                                                                        proportion_test=proportion_test,
                                                                        subject_ids=subject_ids)
                # Calculate precision values with specified rank-method
                precision_comb = calculate_precision_combinations(realistic_ranks_comb=realistic_ranks_comb, k=k)

                # Calculate mean over precision-values per sensor-combinations for specified rank-method
                sensor_combined_precision = statistics.mean(precision_comb.values())

                # Save results in dictionary
                results_sensor[k].setdefault(method, sensor_combined_precision)

        proportion_results_dict.setdefault(proportion_test, results_sensor)

    # Calculate mean over test-proportions
    results = dict()
    for method in classes:
        for k in k_list:
            results.setdefault(k, dict())
            precision_k_list = list()
            for proportion in proportion_results_dict:
                precision_k_list.append(proportion_results_dict[proportion][k][method])
            results[k].setdefault(method, round(statistics.mean(precision_k_list), 3))

    return results


def calculate_average_class_precisions(rank_method: str = "score", subject_ids: List = None) \
        -> Tuple[Dict[int, float], Dict[int, int]]:
    """
    Calculate average class precision values (mean and weighted mean over classes)
    :param rank_method: Specify rank-method "score" or "rank" (use beste rank-method)
    :param subject_ids: Specify subject-ids, if None: all subjects are used
    :return: Tuple with result dictionaries
    """
    results = calculate_class_precisions(rank_method=rank_method, subject_ids=subject_ids)
    class_distribution = get_class_distribution()

    average_results = dict()
    weighted_average_results = dict()
    for k in results:
        average_results.setdefault(k, 0)
        weighted_average_results.setdefault(k, 0)
        average_precision_list = list()
        weighted_average_precision = 0
        for method in results[k]:
            average_precision_list.append(results[k][method])
            weighted_average_precision += results[k][method] * class_distribution[method]
        average_results[k] = round(statistics.mean(average_precision_list), 3)
        weighted_average_results[k] = round(weighted_average_precision, 3)

    return average_results, weighted_average_results


def get_best_class_configuration(average_res: Dict[int, float], weighted_average_res: Dict[int, float]) -> str:
    """
    Calculate best class configuration "mean" or "weighted-mean" from given results
    :param average_res: Dictionary with averaged results
    :param weighted_average_res: Dictionary with weighted averaged results
    :return: String with best class-configuration
    """
    best_class_method = str()
    for dec_k in average_res:
        if average_res[dec_k] > weighted_average_res[dec_k]:
            best_class_method = "mean"
            break
        elif average_res[dec_k] < weighted_average_res[dec_k]:
            best_class_method = "weighted-mean"
            break
        else:
            best_class_method = random.choice(["mean", "weighted-mean"])

    return best_class_method


def run_class_evaluation(rank_method: str = "score"):
    """
    Run and save evaluation for classes
    :param rank_method: Specify rank-method "score" or "rank" (use best performing method)
    """
    results = calculate_class_precisions(rank_method=rank_method)
    average_results, weighted_average_results = calculate_average_class_precisions(rank_method=rank_method)
    best_class_method = get_best_class_configuration(average_res=average_results,
                                                     weighted_average_res=weighted_average_results)

    text = [create_md_precision_classes(rank_method=rank_method, results=results, average_results=average_results,
                                        weighted_average_results=weighted_average_results,
                                        best_class_method=best_class_method)]

    # Save MD-File
    os.makedirs(EVALUATIONS_PATH, exist_ok=True)

    path_string = "/SW-DTW_evaluation_classes.md"
    with open(EVALUATIONS_PATH + path_string, 'w') as outfile:
        for item in text:
            outfile.write("%s\n" % item)

    print("SW-DTW evaluation for classes saved at: " + str(EVALUATIONS_PATH))
