from pre_proc import Preprocessing


def printDictBook(dict_book):
    log_file = open("dict-log.txt", "w")
    for i in dict_book:
        log_file.write(i+" => "+str(dict_book[i])+"\n")
        print(i+" => "+str(dict_book[i]))

def removeWhitespaces(stop_list):
    for sw in stop_list:
        if sw.endswith(' '):
            stop_list.remove(sw)
            sw = sw.replace(' ', '')  # 'is ' => 'is'
            stop_list.append(sw)
    return stop_list


# dictionary struct: {"stem":{"docID", [positions, ...]}}
def dictionary(stem_list, book, doc_id):
    stem_list_len = len(stem_list)
    for pos in range(0, stem_list_len):
        stem = stem_list[pos]
        if book.__contains__(stem):
            posting_list = book[stem]
            if posting_list.__contains__(doc_id):
                position_list = posting_list[doc_id]
                position_list.append(pos)
                posting_list[doc_id] = position_list
            else:
                position_list.append(pos)
                posting_list[doc_id] = position_list
            book[stem] = posting_list
        else:
            posting_list = {}  # posting_list struct: {"docID":[positions, ...], ...}
            position_list = [pos]
            posting_list[doc_id] = position_list
            book[stem] = posting_list
    return book


if __name__ == '__main__':
    stop_file = open('Stopword-List.txt', "r")
    # stop_list when imported from file has whitespaces, they should be removed
    stop_list = removeWhitespaces(stop_file.read().split('\n'))
    # print(stop_list)
    stop_file.close()

    dict_book = {}

    doc_id = 0
    file = open('Trump Speechs/speech_' + str(doc_id) + ".txt", "r")
    file.readline()  # after reading the line, moves file ptr to next line to skip the title

    pipe = Preprocessing()
    pipe.stop_word = stop_list

    tokens = pipe.tokenizer(file.read())
    # print(tokens)     # use of stop-list reduces overall char size from 53K to 42K from file speech_0
    stems = pipe.stemmer(tokens)
    # print(stems)
    dict_book = dictionary(stems, dict_book, doc_id)

    printDictBook(dict_book)    # prints dict on terminal and write to file

