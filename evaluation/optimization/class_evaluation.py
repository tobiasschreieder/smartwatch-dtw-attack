from evaluation.calculate_precisions import calculate_precision_combinations
from evaluation.calculate_ranks import get_realistic_ranks_combinations
from preprocessing.data_preparation import get_sensor_combinations
from preprocessing.data_preparation import load_dataset

from typing import Dict
import pandas as pd
import statistics


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
