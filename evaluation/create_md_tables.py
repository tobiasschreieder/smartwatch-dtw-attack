from evaluation.calculate_precisions import calculate_precision_combinations
from evaluation.calculate_ranks import get_realistic_ranks_combinations
from preprocessing.data_preparation import get_subject_list

from typing import List


def bold_minimums(value, sensor: str, results):
    """
    Bold minimum scores for md-table
    :param value: Value to bold
    :param sensor: Specify sensor
    :param results:
    :return:
    """
    text = str(value)
    sensor_results = list()

    if sensor is not None:
        for i in results:
            sensor_results.append(results[i][sensor])
    else:
        for i in results:
            sensor_results.append(results[i])

    minimum = min(sensor_results)

    if value == minimum:
        text = "**" + str(value) + "**"

    return text


def bold_subject(subject: int, check_subject: int):
    """
    Bold subject with minimum score
    :param subject: subject to check if it should be bolded
    :param check_subject: chosen subject
    :return: String with bolded text
    """
    text = str(subject)

    if text == str(check_subject):
        text = "**" + str(subject) + "**"

    return text


def create_md_distances(results, subject_id: int):
    """
    Create md-table with results
    :param results: Dictionary with results
    :param subject_id: Current subject_id
    :return: String with text
    """
    text = "### Distance table for subject " + str(subject_id) + "\n"
    text += "| Subject | BVP | EDA | ACC | TEMP |" + "\n"
    text += "|---|---|---|---|---|" + "\n"

    for i in results:
        text += "| " + bold_subject(i, subject_id) + " | " + bold_minimums(results[i]["bvp"], "bvp",
                                                                           results) + " | " + bold_minimums(
            results[i]["eda"], "eda", results) + " | " + bold_minimums(results[i]["acc"], "acc",
                                                                       results) + " | " + bold_minimums(
            results[i]["temp"], "temp", results) + " |" + "\n"

    return text


def create_md_ranks(overall_ranks, individual_ranks, subject_id):
    """
    Create md-file for overall precision@k scores with methods "rank" and "score"
    :param overall_ranks:
    :param individual_ranks:
    :param subject_id:
    :return:
    """
    text = "### Rank table for subject " + str(subject_id) + "\n"
    text += "| Subject | BVP | EDA | ACC | TEMP | Overall |" + "\n"
    text += "|---|---|---|---|---|---|" + "\n"

    for i in individual_ranks:
        text += "| " + bold_subject(i, subject_id) + " | " + \
                bold_minimums(individual_ranks[i]["bvp"], "bvp", individual_ranks) + " | " + \
                bold_minimums(individual_ranks[i]["eda"], "eda", individual_ranks) + " | " + \
                bold_minimums(individual_ranks[i]["acc"], "acc", individual_ranks) + " | " + \
                bold_minimums(individual_ranks[i]["temp"], "temp", individual_ranks) + " | " + \
                bold_minimums(overall_ranks[i], None, overall_ranks) + " |" + "\n"

    return text


def bold_maximum_precision(precision_comb, value):
    """
    Bold maximum precision@k
    :param precision_comb:
    :param value:
    :return:
    """
    precision_list = list()
    for k, v in precision_comb.items():
        precision_list.append(v)

    text = str(value)
    if value == max(precision_list):
        text = "**" + str(value) + "**"

    return text


def create_md_precision_combinations(rank_method: str, method: str, proportion_test: float, max_k: int = 15,
                                     subject_ids: List[int] = None, k_list: List[int] = None) -> str:
    """
    Create text for md-file with precision@k scores for all sensor combinations
    :param rank_method: Specify ranking-method ("rank", "score")
    :param method: Specify method ("baseline", "amusement", "stress")
    :param proportion_test: Specify test-proportion
    :param max_k: Specify maximum k for precision@k
    :param subject_ids: List with subject-ids; if None: all subjects are used
    :param k_list: Specify k parameters in precision tables
    :return: String with MD text
    """
    if subject_ids is None:
        subject_ids = get_subject_list()

    sensor_combinations = [["bvp"], ["eda"], ["acc"], ["temp"], ["bvp", "eda"], ["bvp", "temp"], ["eda", "acc"],
                           ["eda", "temp"], ["acc", "temp"], ["bvp", "eda", "acc"], ["bvp", "eda", "temp"],
                           ["bvp", "acc", "temp"], ["eda", "acc", "temp"], ["bvp", "eda", "acc", "temp"]]

    text = "### Precision@k table combinations (method: " + rank_method + ")" + "\n"

    realistic_ranks_comb = get_realistic_ranks_combinations(rank_method=rank_method,
                                                            combinations=sensor_combinations, method=method,
                                                            proportion_test=proportion_test, subject_ids=subject_ids)
    precision_comb_1 = calculate_precision_combinations(realistic_ranks_comb=realistic_ranks_comb, k=1)

    text += "| Precision@k | "
    for i in precision_comb_1:
        text += i + " | "
    text += "\n"

    text += "|---|"
    for i in precision_comb_1:
        text += "---|"
    text += "\n"

    if k_list is None:
        for i in range(1, max_k + 1):
            precision_comb = calculate_precision_combinations(realistic_ranks_comb, i)
            text += "| k = " + str(i) + " | "
            for k, v in precision_comb.items():
                text += bold_maximum_precision(precision_comb, v) + " | "
            text += "\n"
    else:
        for i in k_list:
            precision_comb = calculate_precision_combinations(realistic_ranks_comb, i)
            text += "| k = " + str(i) + " | "
            for k, v in precision_comb.items():
                text += bold_maximum_precision(precision_comb, v) + " | "
            text += "\n"

    return text
