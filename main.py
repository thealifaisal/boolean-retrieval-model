from pre_proc import Preprocessing


def removeWhitespaces(stop_list):
    for sw in stop_list:
        if sw.endswith(' '):
            stop_list.remove(sw)
            sw = sw.replace(' ', '')  # 'is ' => 'is'
            stop_list.append(sw)
    return stop_list


def dictionary(stem_list):
    book = {}
    stem_list_len = len(stem_list)
    for pos in range(0, stem_list_len):
        stem = stem_list[pos]
        if book.__contains__(stem):
            li = book[stem]
            li.append(pos)
            book[stem] = li
        else:
            li = [pos]
            book[stem] = li
    return book


if __name__ == '__main__':
    stop_file = open('Stopword-List.txt', "r")
    # stop_list when imported from file has whitespaces, they should be removed
    stop_list = removeWhitespaces(stop_file.read().split('\n'))
    # print(stop_list)

    doc_id = 0
    file = open('Trump Speechs/speech_' + str(doc_id) + ".txt", "r")
    file.readline()  # after reading the line, moves file ptr to next line to skip the title

    tokens = []
    stems = []

    pipe = Preprocessing()
    pipe.stop_word = stop_list

    tokens = pipe.tokenizer(file.read())
    # print(tokens)     # use of stop-list reduces overall char size from 53K to 42K from file speech_0
    stems = pipe.stemmer(tokens)
    print(stems)
    dict_book = dictionary(stems)
    # print(dict_book)
