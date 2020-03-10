from pre_proc import Preprocessing
from indexing_dict import Indexing
from utility_funcs import removeWhitespaces


def identifyQuery(query):
    q_l = query.split()

    if q_l.__contains__("AND") or q_l.__contains__("OR") or q_l.__contains__("NOT") or q_l.__len__() == 1:
        return "B"
    elif query.__contains__("/"):
        return "PR"
    else:
        return "PO"


def positionalSearch(query, stop_list, dict_book):
    pipe = Preprocessing()
    pipe.stop_word = stop_list
    tokens = pipe.tokenizer(query)
    stems = pipe.stemmer(tokens)

    w1 = stems[0]
    w2 = stems[1]
    if dict_book.__contains__(w1) and dict_book.__contains__(w2):
        posting1 = dict_book[w1]  # set returned, {docID:[], ...}
        posting2 = dict_book[w2]
    else:
        return []

    # len_posting1 = len(posting1)
    # len_posting2 = len(posting2)

    doc_list = []

    for docI in posting1:
        for docJ in posting2:
            if docI == docJ:
                poslist1 = posting1[docI]
                poslist2 = posting2[docJ]
                match: bool = False
                for pos1 in poslist1:  # hilary
                    for pos2 in poslist2:  # clinton
                        if pos2 - pos1 <= 1:
                            doc_list.append(docI)
                            match = True
                            break
                    if match is True:
                        break
            match = False
    return doc_list


def proximitySearch(query, stop_list, dict_book, k):
    pipe = Preprocessing()
    pipe.stop_word = stop_list
    print(query)
    tokens = pipe.tokenizer(query)
    stems = pipe.stemmer(tokens)

    w1 = stems[0]
    w2 = stems[1]

    if dict_book.__contains__(w1) and dict_book.__contains__(w2):
        posting1: set = dict_book[w1]  # set returned, {docID:[], ...}
        posting2: set = dict_book[w2]
    else:
        return []

    # len_posting1 = len(posting1)
    # len_posting2 = len(posting2)

    doc_list = []

    for docI in posting1:
        for docJ in posting2:
            if docI == docJ:
                poslist1: list = posting1[docI]
                poslist2: list = posting2[docJ]
                match: bool = False
                for pos1 in poslist1:  # hilary
                    for pos2 in poslist2:  # clinton
                        if pos2 - pos1 <= k:
                            doc_list.append(docI)
                            match = True
                            break
                    if match is True:
                        break
            match = False
    return doc_list


def booleanSearch(query, stop_list, dict_book):
    pipe = Preprocessing()
    pipe.stop_word = stop_list
    # print(query)
    tokens = pipe.tokenizer(query)
    stems = pipe.stemmer(tokens)

    if dict_book.__contains__(stems):
        posting: set = dict_book[stems]
    else:
        return []

    doc_list = []

    for i in posting:
        doc_list.append(i)

    return doc_list
