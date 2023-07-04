from preprocessing.data_preparation import load_dataset, get_subject_list

from dtw import *
import pandas as pd
from typing import Dict, List, Tuple
import json
import os


MAIN_PATH = os.path.abspath(os.getcwd())
DATA_PATH = os.path.join(MAIN_PATH, "dataset")  # add /dataset to path


def create_full_subject_data() -> Dict[int, Dict[str, pd.DataFrame]]:
    """
    Create dictionary with all subjects and their sensor data as Dataframe
    :return: Dictionary with subject_data
    """
    data_dict = load_dataset()
    subject_data = dict()

    for subject in data_dict:

        sensor_data = {"bvp": data_dict[subject][["bvp"]],
                       "eda": data_dict[subject][["eda"]],
                       "acc_x": data_dict[subject][["acc_x"]],
                       "acc_y": data_dict[subject][["acc_y"]],
                       "acc_z": data_dict[subject][["acc_z"]],
                       "temp": data_dict[subject][["temp"]]}

        subject_data.setdefault(subject, sensor_data)

    return subject_data


def calculate_complete_subject_alignment(subject_id: int) \
        -> Tuple[Dict[int, Dict[str, float]], Dict[int, Dict[str, float]]]:
    """
    Calculate dtw-alignments for all sensors and subjects (no train-test split)
    :param subject_id: Specify subject-id
    :return: Tuple with Dictionaries of normalized and standard results
    """
    results_normalized = dict()
    results_standard = dict()
    subject_data = create_full_subject_data()

    for subject in subject_data:
        print("----Current subject: " + str(subject))
        results_normalized.setdefault(subject, dict())
        results_standard.setdefault(subject, dict())

        for sensor in subject_data[subject]:
            test = subject_data[subject_id][sensor]
            train = subject_data[subject][sensor]

            alignment = dtw(train, test, keep_internals=False)
            distance_normalized = alignment.normalizedDistance
            distance_standard = alignment.distance

            results_normalized[subject].setdefault(sensor, round(distance_normalized, 4))
            results_standard[subject].setdefault(sensor, round(distance_standard, 4))

    return results_normalized, results_standard


def run_dtw_alignments(subject_ids: List[int] = None):
    """
    Run DTW-Calculations with all given parameters and save results as json (no train-test split)
    :param subject_ids: List with all subjects that should be used as test subjects (int) -> None = all subjects
    """
    if subject_ids is None:
        subject_ids = get_subject_list()

    # Run DTW Calculations
    for subject_id in subject_ids:
        print("-Current id: " + str(subject_id))

        results_normalized, results_standard = calculate_complete_subject_alignment(subject_id=subject_id)

        # Save results as json
        try:
            path = os.path.join(MAIN_PATH, "/out")  # add /out to path
            path = os.path.join(path, "/alignments")  # add /alignments to path
            path = os.path.join(path, "complete")  # add /complete to path
            os.makedirs(path, exist_ok=True)

            path_string_normalized = "/SW-DTW_results_normalized_" + "complete_S" + str(subject_id) + ".json"
            path_string_standard = "/SW-DTW_results_standard_" + "complete_S" + str(subject_id) + ".json"

            with open(path + path_string_normalized, "w", encoding="utf-8") as outfile:
                json.dump(results_normalized, outfile)

            with open(path + path_string_standard, "w", encoding="utf-8") as outfile:
                json.dump(results_standard, outfile)

            print("SW-DTW results saved at: " + str(path))

        except FileNotFoundError:
            with open("/SW-DTW_results_normalized_" + "complete_S" + str(subject_id) + ".json", "w", encoding="utf-8") \
                    as outfile:
                json.dump(results_normalized, outfile)

            with open("/SW-DTW_results_standard_" + "complete_S" + str(subject_id) + ".json", "w", encoding="utf-8") \
                    as outfile:
                json.dump(results_standard, outfile)

            print("FileNotFoundError: results saved at working dir")
