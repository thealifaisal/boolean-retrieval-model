# stop_list when imported from file has whitespaces, they should be removed
def removeWhitespaces(stop_list):
    for sw in stop_list:
        if sw.endswith(' '):
            stop_list.remove(sw)
            sw = sw.replace(' ', '')  # 'is ' => 'is'
            stop_list.append(sw)
    return stop_list