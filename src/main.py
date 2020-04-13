#################################################################
# -------------------  AUTHOR: ALI FAISAL -----------------------#
#################################################################
from src.indexing import Indexing
from src.utilities import removeWhitespaces
from src.search import *

if __name__ == '__main__':

    stop_file = open('../resource/stopword-list.txt', "r")
    # stop_list when imported from file has whitespaces, they should be removed
    stop_list = removeWhitespaces(stop_file.read().split('\n'))
    # print(stop_list)
    stop_file.close()

    dict_book = {}

    for i in range(0, 55):
        doc_id = i
        file = open('../resource/trump-speeches/speech_' + str(doc_id) + ".txt", "r")
        file.readline()  # after reading the line, moves file ptr to next line to skip the title

        pipe = Preprocessing()
        pipe.stop_word = stop_list

        tokens = pipe.tokenizer(file.read())
        # print(tokens)     # use of stop-list reduces overall char size from 53K to 42K from file speech_0
        stems = pipe.stemmer(tokens)
        dict_obj = Indexing()  # creating a object of Indexing class
        dict_book = dict_obj.dictionary(stems, dict_book, doc_id)

    # dict_obj.printDictBook(dict_book)  # prints dict on terminal and write to file

    # ----------------- INDEXING DONE ------------------

    while True:
        query = input("Enter Query (F for stop): ")

        if query == "F":
            break

        v = identifyQuery(query)

        if v == "PO":
            print("Query Type: " + v)
            doc_list1 = positionalSearch(query+" ", stop_list, dict_book)
            print("Relevant Documents: \n")
            for i in doc_list1:
                print('Trump Speechs/speech_' + str(i) + '.txt')
        elif v == "PR":  # after years /1
            print("Query Type: " + v)
            q_l = query.split("/")  # ["after years", "1"]
            q = q_l[0]  # "after years "
            k = q_l[1]  # 1
            doc_list2 = proximitySearch(q+" ", stop_list, dict_book, int(k))
            print("Relevant Documents: \n")
            for i in doc_list2:
                print('Trump Speechs/speech_' + str(i) + '.txt')
        elif v == "B":
            print("Query Type: " + v)
            doc_list3 = booleanSearch(query+" ", stop_list, dict_book)
            print("Relevant Documents: \n")
            for i in doc_list3:
                print('Trump Speechs/speech_' + str(i) + '.txt')
        elif v == "S":
            print("Query Type: " + v)
            doc_list3 = positionalSingleSearch(query + " ", stop_list, dict_book)
            print("Relevant Documents: \n")
            for i in doc_list3:
                print('Trump Speechs/speech_' + str(i) + '.txt')
