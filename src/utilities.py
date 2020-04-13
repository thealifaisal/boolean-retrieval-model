# stop_list when imported from file has whitespaces, they should be removed
def removeWhitespaces(stop_list):
    for sw in stop_list:
        if sw.endswith(' '):
            stop_list.remove(sw)
            sw = sw.replace(' ', '')  # 'is ' => 'is'
            stop_list.append(sw)
    return stop_list


def printResultSet(doc_list):
    result_string = "{ "
    result_count = 0

    for doc in doc_list:
        result_string += str(doc)+", "
        result_count += 1

    result_string += "}"

    print("Result-Set Length: " + str(result_count))
    print("Result-Set: " + result_string + "\n")
