from data_preparation import load_dataset

import os
import matplotlib.pyplot as plt


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



