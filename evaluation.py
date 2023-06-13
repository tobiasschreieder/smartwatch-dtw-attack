from calculate_precisions import calculate_max_precision

from typing import List


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


