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