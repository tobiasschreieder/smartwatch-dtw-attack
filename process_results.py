import json
import os
import statistics


# Specify path
MAIN_PATH = os.path.abspath(os.getcwd())
OUT_PATH = os.path.join(MAIN_PATH, "out")  # add /out to path
RESULT_PATH = os.path.join(OUT_PATH, "results")  # add /results to path


def load_results(subject_id: int, method: str, proportion_test: float, normalized_data: bool = True):
    """
    Load results from ../out/results/
    :param subject_id: Specify subject
    :param method: Specify method ("baseline", "amusement", "stress")
    :param proportion_test: Specify test-proportion
    :param normalized_data: True if normalized results should be used
    :return: Dictionary with results
    """
    try:
        path = os.path.join(RESULT_PATH, str(method))  # add /method to path
        path = os.path.join(path, "test=" + str(proportion_test))  # add /test=0.XX to path

        if normalized_data:
            path = path + "/SW-DTW_results_normalized_" + str(method) + "_" + str(proportion_test) + "_S" + str(
                subject_id) + ".json"
        else:
            path = path + "/SW-DTW_results_standard_" + str(method) + "_" + str(proportion_test) + "_S" + str(
                subject_id) + ".json"

        f = open(path, "r")
        results = json.loads(f.read())

    except FileNotFoundError:
        print("FileNotFoundError: no results with this configuration available")

    # Calculate mean of all 3 "ACC" Sensor distances
    for i in results:
        results[i].setdefault("acc", round(statistics.mean([results[i]["acc_x"], results[i]["acc_y"],
                                                            results[i]["acc_z"]]), 4))

    return results