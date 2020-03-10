from pre_proc import Preprocessing
from indexing_dict import Indexing
from utility_funcs import removeWhitespaces

if __name__ == '__main__':
    stop_file = open('Stopword-List.txt', "r")
    # stop_list when imported from file has whitespaces, they should be removed
    stop_list = removeWhitespaces(stop_file.read().split('\n'))
    # print(stop_list)
    stop_file.close()

    dict_book = {}

    for i in range(0, 2):
        doc_id = i
        file = open('Trump Speechs/speech_' + str(doc_id) + ".txt", "r")
        file.readline()  # after reading the line, moves file ptr to next line to skip the title

        pipe = Preprocessing()
        pipe.stop_word = stop_list

        tokens = pipe.tokenizer(file.read())
        # print(tokens)     # use of stop-list reduces overall char size from 53K to 42K from file speech_0
        stems = pipe.stemmer(tokens)
        # print(stems)
        dict_obj = Indexing()  # creating a object of Indexing class
        dict_book = dict_obj.dictionary(stems, dict_book, doc_id)

    dict_obj.printDictBook(dict_book)  # prints dict on terminal and write to file
