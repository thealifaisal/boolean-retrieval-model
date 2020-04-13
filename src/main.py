#################################################################
# -------------------  AUTHOR: ALI FAISAL -----------------------#
#################################################################
from src.indexing import Indexing
from src.utilities import *
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

    doc_list = []

    while True:

        query = input("Enter Query (F for stop): ")

        if query == "F":
            break

        query_type = identifyQuery(query)

        if query_type == "PO":
            print("\nQuery Type: " + query_type)
            doc_list = positionalSearch(query+" ", stop_list, dict_book)
            printResultSet(doc_list)

        elif query_type == "PR":  # after years /1
            print("\nQuery Type: " + query_type)
            q_l = query.split("/")  # ["after years", "1"]
            q = q_l[0]  # "after years "
            k = q_l[1]  # 1
            doc_list = proximitySearch(q+" ", stop_list, dict_book, int(k))
            printResultSet(doc_list)

        elif query_type == "B":
            print("\nQuery Type: " + query_type)
            doc_list = booleanSearch(query+" ", stop_list, dict_book)
            printResultSet(doc_list)

        elif query_type == "S":
            print("\nQuery Type: " + query_type)
            doc_list = positionalSingleSearch(query + " ", stop_list, dict_book)
            printResultSet(doc_list)

