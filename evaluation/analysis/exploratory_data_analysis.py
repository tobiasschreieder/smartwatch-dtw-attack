from preprocessing.data_preparation import load_dataset, get_subject_list
from preprocessing.process_results import load_complete_alignment_results

import os
import matplotlib.pyplot as plt
import numpy as np


MAIN_PATH = os.path.abspath(os.getcwd())
EDA_PATH = os.path.join(MAIN_PATH, "out")  # add /out to path
EDA_PATH = os.path.join(EDA_PATH, "eda")  # add /eda to path


def plot_subject_data():
    """
    Plot sensor-value distribution for all subjects
    :return:
    """
    data_dict = load_dataset()  # read data_dict

    for subject in data_dict:
        plt.plot(data_dict[subject])
        plt.legend(data_dict[subject].keys(), loc="center left")
        plt.title(label="Sensor-value distribution for subject: " + str(subject), loc="center")
        plt.ylabel('normalized sensor values (label=1: stress)')
        plt.xlabel('index | time')

        try:
            plt.savefig(fname=EDA_PATH + "/eda_plot_S" + str(subject) + ".png")

        except FileNotFoundError:
            print("FileNotFoundError: Invalid directory structure!")

        plt.close()


def plot_alignment_heatmap(normalized_data: bool = True):
    """
    Plot complete subject alignments as heatmap
    :param normalized_data: If True -> use normalized results
    """
    subject_ids = get_subject_list()
    data = dict()
    data_array = list()
    for subject_id in subject_ids:
        results = load_complete_alignment_results(subject_id=subject_id, normalized_data=normalized_data)
        data.setdefault(subject_id, list(results.values()))

    for subject_id in data:
        data_array.append(data[subject_id])

    data_array = np.array(data_array)

    fig, ax = plt.subplots()
    im = ax.imshow(data_array)
    ax.set_xticks(np.arange(len(subject_ids)), labels=subject_ids)
    ax.set_yticks(np.arange(len(subject_ids)), labels=subject_ids)

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    for i in range(len(subject_ids)):
        for j in range(len(subject_ids)):
            text = ax.text(j, i, data_array[i, j], ha="center", va="center", color="w")

    ax.set_title("DTW-Alignment: subject distance heatmap")
    fig.tight_layout()

    try:
        plt.savefig(fname=EDA_PATH + "/eda_dtw_alignment_heatmap.png", dpi=2000)

    except FileNotFoundError:
        print("FileNotFoundError: Invalid directory structure!")
