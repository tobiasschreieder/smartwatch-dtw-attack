from evaluation.metrics.calculate_precisions import calculate_precision_combinations
from evaluation.metrics.calculate_ranks import get_realistic_ranks_combinations
from preprocessing.data_preparation import get_sensor_combinations
from preprocessing.data_preparation import get_subject_list

from typing import List, Dict


def bold_minimums(value, sensor: str, results) -> str:
    """
    Bold minimum scores for md-table
    :param value: Value to bold
    :param sensor: Specify sensor
    :param results: Dictionary with results
    :return: Bolded text
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


def bold_subject(subject: int, check_subject: int) -> str:
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


def create_md_distances(results, subject_id: int) -> str:
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


def create_md_ranks(overall_ranks, individual_ranks, subject_id) -> str:
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

    sensor_combinations = get_sensor_combinations()

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


def create_md_precision_rank_method(results: Dict[int, Dict[str, float]], best_rank_method: str,
                                    best_k_parameters: Dict[str, int]) -> str:
    """
    Create text for MD-file with results of rank-method evaluation
    :param results: Results with precision values
    :param best_rank_method: Specify best rank-method
    :param best_k_parameters: Specify best k parameters
    :return: String with MD text
    """
    text = "# Evaluation of Rank-Methods: \n"
    text += "* Preferred rank-method: '" + str(best_rank_method) + "' (decision based on smallest k) \n"

    text += "## Precision@k table: \n"
    text += "| k | rank | score | mean |" + "\n"
    text += "|---|---|---|---|" + "\n"

    for k in results:
        text += "| " + str(k) + " | " + str(results[k]["rank"]) + " | " + str(results[k]["score"]) + " | " + \
                str(results[k]["mean"]) + " |" + "\n"

    text += "| max@k | " + "k = " + str(best_k_parameters["rank"]) + " | " + "k = " + str(best_k_parameters["score"]) \
            + " | " + "k = " + str(best_k_parameters["mean"]) + " |" + "\n"

    return text


def create_md_precision_classes(rank_method: str, results: Dict[int, Dict[str, float]],
                                average_results: Dict[int, float], weighted_average_results: Dict[int, float],
                                best_class_method: str, best_k_parameters: Dict[str, int],
                                best_average_k_parameters: Dict[str, int]) -> str:
    """
    Create text for MD-file with results of class evaluation
    :param rank_method: Specify rank-method ("score" or "rank")
    :param results: Results with precision values per class
    :param average_results: Results with average precision values
    :param weighted_average_results: Results with weighted average precision values
    :param best_class_method: Specify best class-method
    :param best_k_parameters: Specify best k parameters
    :param best_average_k_parameters: Specify best average k parameters
    :return: String with MD text
    """
    text = "# Evaluation of Classes: \n"
    text += "* Calculated with rank-method: '" + str(rank_method) + "' \n"
    text += "* Preferred class averaging method: '" + str(best_class_method) + "' (decision based on smallest k) \n"

    text += "## Evaluation per Class: \n"
    text += "### Precision@k table: \n"
    text += "| k | baseline | amusement | stress |" + "\n"
    text += "|---|---|---|---|" + "\n"

    for k in results:
        text += "| " + str(k) + " | " + str(results[k]["baseline"]) + " | " + str(results[k]["amusement"]) + " | " + \
                str(results[k]["stress"]) + " |" + "\n"

    text += "| max@k | " + "k = " + str(best_k_parameters["baseline"]) + " | " + "k = " + \
            str(best_k_parameters["amusement"]) + " | " + "k = " + str(best_k_parameters["stress"]) + " |" + "\n"

    text += "## Overall Evaluation: \n"
    text += "### Precision@k table: \n"
    text += "| k | mean | weighted mean |" + "\n"
    text += "|---|---|---|" + "\n"

    for k in average_results:
        text += "| " + str(k) + " | " + str(average_results[k]) + " | " + str(weighted_average_results[k]) + " |" + "\n"

    text += "| max@k | " + "k = " + str(best_average_k_parameters["mean"]) + " | " + "k = " + \
            str(best_average_k_parameters["weighted-mean"]) + " |" + "\n"

    return text


def create_md_precision_sensors(rank_method: str, average_method: str, results: Dict[int, Dict[str, float]],
                                best_sensors: str) -> str:
    """
    Create text for MD-file with results of sensor-combination evaluation
    :param rank_method: Specify rank-method ("score" or "rank")
    :param average_method: Specify averaging-method ("mean" or "weighted-mean)
    :param results: Results with precision values per class
    :param best_sensors: Specify best sensor-combination
    :return: String with MD text
    """
    text = "# Evaluation of Sensor-Combinations: \n"
    text += "* Calculated with rank_method: '" + str(rank_method) + "' \n"
    text += "* Calculated with averaging-method: '" + str(average_method) + "' \n"
    text += "* Preferred sensor-combination: '" + str(best_sensors) + "' (decision based on smallest k) \n"

    text += "## Precision@k table: \n"
    text += "| k |"
    separator = "|---|"
    for sensor in results[list(results.keys())[0]]:
        text += str(sensor) + " | "
        separator += "---|"
    text += "\n"
    text += separator + "\n"

    for k in results:
        text += "| " + str(k) + " | "
        for sensor in results[k]:
            text += str(results[k][sensor]) + " | "
        text += "\n"

    return text


def create_md_precision_windows(rank_method: str, average_method: str, sensor_combination: str,
                                results: Dict[int, Dict[float, float]], best_window: float) -> str:
    """
    Create text for MD-file with results of window (test-proportion) evaluation
    :param rank_method: Specify rank-method ("score" or "rank")
    :param average_method: Specify averaging-method ("mean" or "weighted-mean)
    :param sensor_combination: Specify sensor-combination e.g. "acc+temp" (Choose best one)
    :param results: Results with precision values per class
    :param best_window: Specify best window
    :return: String with MD text
    """
    text = "# Evaluation of Windows: \n"
    text += "* Calculated with rank-method: '" + str(rank_method) + "' \n"
    text += "* Calculated with averaging-method: '" + str(average_method) + "' \n"
    text += "* Calculated with sensor-combination: '" + str(sensor_combination) + "' \n"
    text += "* Preferred window-size: '" + str(best_window) + "' (decision based on smallest k) \n"

    text += "## Precision@k table: \n"
    text += "| k |"
    separator = "|---|"
    for window in results[list(results.keys())[0]]:
        text += str(window) + " | "
        separator += "---|"
    text += "\n"
    text += separator + "\n"

    for k in results:
        text += "| " + str(k) + " | "
        for window in results[k]:
            text += str(results[k][window]) + " | "
        text += "\n"

    return text


def create_md_precision_overall(results: Dict[int, Dict[str, float]], rank_method: str, average_method: str,
                                sensor_combination: str, window: float,
                                weightings: Dict[str, Dict[int, List[Dict[str, float]]]]) -> str:
    """
    Create text for MD-file with results of overall evaluation and best sensor-weightings
    :param results: Results with precision values (DTW-results, maximum results, random guess results)
    :param rank_method: Specify rank-method ("score" or "rank")
    :param average_method: Specify averaging-method ("mean" or "weighted-mean)
    :param sensor_combination: Specify sensor-combination e.g. "acc+temp" (Choose best one)
    :param window: Specify best window-size
    :param weightings: Specify best sensor-weightings
    :return: String with MD text
    """
    text = "# Evaluation overall: \n"
    text += "* Calculated with rank-method: '" + str(rank_method) + "' \n"
    text += "* Calculated with averaging-method: '" + str(average_method) + "' \n"
    text += "* Calculated with sensor-combination: '" + str(sensor_combination) + "' \n"
    text += "* Calculated with window-size: '" + str(window) + "' \n"

    text += "## Precision@k table: \n"
    text += "| k | DTW-results | sensor weighted | random guess |" + "\n"
    text += "|---|---|---|---|" + "\n"
    for k in results:
        text += "| " + str(k) + " | " + str(results[k]["results"]) + " | " + str(results[k]["max"]) + " | " + \
                str(results[k]["random"]) + " |" + "\n"

    text += "## Sensor-weighting tables: \n"
    for method in weightings:
        text += "### Table for method: '" + str(method) + "': \n"
        text += "| k | acc | bvp | eda | temp | \n"
        text += "|---|---|---|---|---| \n"
        for k in weightings[method]:
            for weights in weightings[method][k]:
                text += "| " + str(k) + " | " + str(weights["acc"]) + " | " + str(weights["bvp"]) + " | " + \
                        str(weights["eda"]) + " | " + str(weights["temp"]) + " |" + "\n"

    return text
