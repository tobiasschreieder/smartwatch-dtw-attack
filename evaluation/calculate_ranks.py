from preprocessing.data_preparation import get_subject_list
from preprocessing.process_results import load_results

import statistics
import math
import copy


SUBJECT_LIST = get_subject_list()


def calculate_ranks_1(results):
    """
    Calculate unique ranks by averaging individual ranks
    :param results:
    :return:
    """
    result_lists = dict()
    for i in results:
        for j in results[i]:
            if j not in result_lists:
                result_lists.setdefault(j, list())
            result_lists[j].append(results[i][j])

    ranks = dict()
    for i in result_lists:
        ranks.setdefault(i, [sorted(result_lists[i]).index(x) for x in result_lists[i]])

    rank_results = copy.deepcopy(results)
    for i in ranks:
        for j in range(len(ranks[i])):
            rank_results[str(SUBJECT_LIST[j])][i] = ranks[i][j]

    final_ranks = dict()
    for i in rank_results:
        final_ranks.setdefault(i, round(statistics.mean(
            [rank_results[i]["bvp"], rank_results[i]["eda"], rank_results[i]["acc"], rank_results[i]["temp"]])))

    items = list(final_ranks.values())
    final_rank_list = [sorted(items).index(x) for x in items]

    overall_ranks = copy.deepcopy(final_ranks)
    for i in range(len(final_rank_list)):
        overall_ranks[str(SUBJECT_LIST[int(i)])] = final_rank_list[i]

    return overall_ranks, rank_results


def calculate_ranks_2(results):
    """
    Calculate unique ranks by averaging calculated scores
    :param results:
    :return:
    """
    result_lists = dict()
    for i in results:
        mean_score = statistics.mean([results[i]["bvp"], results[i]["eda"], results[i]["acc"], results[i]["temp"]])
        result_lists.setdefault(i, mean_score)

    items = list(result_lists.values())
    final_rank_list = [sorted(items).index(x) for x in items]

    overall_ranks = copy.deepcopy(result_lists)
    for i in range(len(final_rank_list)):
        overall_ranks[str(SUBJECT_LIST[int(i)])] = final_rank_list[i]

    result_lists = dict()
    for i in results:
        for j in results[i]:
            if j not in result_lists:
                result_lists.setdefault(j, list())
            result_lists[j].append(results[i][j])

    ranks = dict()
    for i in result_lists:
        ranks.setdefault(i, [sorted(result_lists[i]).index(x) for x in result_lists[i]])

    rank_results = copy.deepcopy(results)
    for i in ranks:
        for j in range(len(ranks[i])):
            rank_results[str(SUBJECT_LIST[j])][i] = ranks[i][j]

    return overall_ranks, rank_results


def run_calculate_ranks(results, method):
    """
    Method to calculate unique scores with specified averaging method
    :param results:
    :param method:
    :return:
    """
    # Calculate ranks
    overall_ranks = dict()
    rank_results = dict()

    if method == "rank":
        overall_ranks, rank_results = calculate_ranks_1(results)
    elif method == "score":
        overall_ranks, rank_results = calculate_ranks_2(results)

    return overall_ranks, rank_results


def realistic_rank(overall_ranks, subject_id):
    """
    Calculate Realistic rank (if no clear decision possible, then pessimistic rank is used)
    :param overall_ranks:
    :param subject_id:
    :return:
    """
    subject_rank = overall_ranks[str(subject_id)]
    smaller_ranks = dict()
    equal_ranks = dict()

    for k, v in overall_ranks.items():
        if v < subject_rank:
            smaller_ranks.setdefault(k, v)
        elif v == subject_rank:
            equal_ranks.setdefault(k, v)

    optimistic_rank = len(smaller_ranks)
    pessimistic_rank = len(smaller_ranks) + len(equal_ranks) - 1
    realistic_rank = math.ceil((optimistic_rank + pessimistic_rank) / 2)

    return realistic_rank


def get_realistic_ranks(subject_ids, rank_method, results):
    """
    Get list with sorted realistic ranks
    :param subject_ids: List with subject-ids
    :param rank_method: Specify ranking method ("rank" or "score")
    :param results: Dictionary with results
    :return: List with sorted realistic ranks
    """
    real_ranks = list()
    for i in subject_ids:
        overall_ranks, individual_ranks = run_calculate_ranks(results, rank_method)

        real_rank = realistic_rank(overall_ranks, i)
        real_ranks.append(real_rank)

    return sorted(real_ranks)


def calculate_ranks_combinations_1(results, combination):
    """
    Calculate ranks for all sensor combinations with method "rank"
    :param results: Dictionary with results
    :param combination: Sensor combination
    :return: Dictionary with rank results
    """
    result_lists = dict()
    for i in results:
        for j in results[i]:
            if j in combination:
                if j not in result_lists:
                    result_lists.setdefault(j, list())
                result_lists[j].append(results[i][j])

    ranks = dict()
    for i in result_lists:
        ranks.setdefault(i, [sorted(result_lists[i]).index(x) for x in result_lists[i]])

    rank_results_all = copy.deepcopy(results)
    for i in ranks:
        for j in range(len(ranks[i])):
            rank_results_all[str(SUBJECT_LIST[j])][i] = ranks[i][j]

    rank_results = copy.deepcopy(rank_results_all)
    for i in rank_results_all:
        for j in rank_results_all[i]:
            if j not in combination:
                del (rank_results[i][j])

    final_ranks = dict()
    for i in rank_results:
        mean_score = 0
        for j in combination:
            mean_score += rank_results[i][j]
        mean_score = mean_score / len(combination)
        final_ranks.setdefault(i, round(mean_score))

    items = list(final_ranks.values())
    final_rank_list = [sorted(items).index(x) for x in items]

    overall_ranks = copy.deepcopy(final_ranks)
    for i in range(len(final_rank_list)):
        overall_ranks[str(SUBJECT_LIST[int(i)])] = final_rank_list[i]

    return overall_ranks


def calculate_ranks_combinations_2(results, combination):
    """
    Calculate ranks for all sensor combinations with method "score"
    :param results: Dictionary with results
    :param combination: Sensor combinations
    :return: Dictionary with rank results
    """
    result_lists = dict()
    for i in results:
        mean_score = 0
        for j in combination:
            mean_score += results[i][j]
        mean_score = mean_score / len(combination)
        result_lists.setdefault(i, mean_score)

    items = list(result_lists.values())
    final_rank_list = [sorted(items).index(x) for x in items]

    overall_ranks = copy.deepcopy(result_lists)
    for i in range(len(final_rank_list)):
        overall_ranks[str(SUBJECT_LIST[int(i)])] = final_rank_list[i]

    return overall_ranks


def calculate_ranks_combinations_3(results, combination, weights):
    """
    Calculate weighted ranks for all sensor combinations with method "score"
    :param results: Dictionary with results
    :param combination: Sensor combinations
    :param weights: List with weights
    :return: Dictionary with rank results
    """
    result_lists = dict()
    for i in results:
        weighted_score = 0
        for j in combination:
            weighted_score += results[i][j] * weights[j]
        result_lists.setdefault(i, weighted_score)

    items = list(result_lists.values())
    final_rank_list = [sorted(items).index(x) for x in items]

    overall_ranks = copy.deepcopy(result_lists)
    for i in range(len(final_rank_list)):
        overall_ranks[str(SUBJECT_LIST[int(i)])] = final_rank_list[i]

    return overall_ranks


def run_calculate_ranks_combinations(results, rank_method, combinations, weights=None):
    """
    Run calculation of rank combinations for one individual subject
    :param results: Dictionary with results
    :param rank_method: Specify ranking method
    :param combinations: Sensor combinations ("rank", "score", "max")
    :param weights: Specify weights for ranking method "max"
    :return: Dictionary with ranking results
    """
    def list_to_string(input_list):
        """
        Get string for possible sensor-name combinations
        :param input_list: List to be transformed
        :return: String with text
        """
        text = str()
        for i in input_list:
            text += i
            text += "+"
        text = text[:-1]
        return text

    if weights is None:
        weights = dict()

    overall_ranks_comb = dict()
    for comb in combinations:
        if rank_method == "rank":
            overall_ranks_comb.setdefault(list_to_string(comb), calculate_ranks_combinations_1(results, comb))
        elif rank_method == "score":
            overall_ranks_comb.setdefault(list_to_string(comb), calculate_ranks_combinations_2(results, comb))
        elif rank_method == "max":
            overall_ranks_comb.setdefault(list_to_string(comb), calculate_ranks_combinations_3(results, comb, weights))

    return overall_ranks_comb


def get_realistic_ranks_combinations(rank_method, combinations, method, proportion_test, subject_ids=None, weights=None):
    """
    Get realistic ranks for sensor combination results
    :param rank_method: Choose ranking method ("rank", "score", "max")
    :param combinations: Specify sensor combinations
    :param method: Specify DTW-method ("baseline", "amusement", "stress")
    :param proportion_test: Specify test-proportion
    :param subject_ids: Specify subjects if needed; ignore if all subjects should be used
    :param weights: Specify weights
    :return: Dictionary with realistic ranks for subjects
    """
    if weights is None:
        weights = dict()
    if subject_ids is None:
        subject_ids = SUBJECT_LIST

    realistic_ranks_comb = dict()
    for subject_id in subject_ids:
        results = load_results(subject_id=subject_id, method=method, proportion_test=proportion_test,
                               normalized_data=True)
        overall_ranks_comb = run_calculate_ranks_combinations(results=results, rank_method=rank_method,
                                                              combinations=combinations, weights=weights)

        for k, v in overall_ranks_comb.items():
            if k not in realistic_ranks_comb:
                realistic_ranks_comb.setdefault(k, list())
            realistic_ranks_comb[k].append(realistic_rank(v, subject_id))
    return realistic_ranks_comb
