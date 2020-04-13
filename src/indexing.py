# I created a class Indexing to encapsulate the methods related to dictionary
class Indexing:
    # dictionary struct: {"stem":{"docID", [positions, ...]}}
    def dictionary(self, stem_list, book: dict, doc_id):
        stem_list_len = len(stem_list)
        for pos in range(0, stem_list_len):
            stem = stem_list[pos]
            if book.keys().__contains__(stem):
                posting_list: dict = book[stem]
                if posting_list.keys().__contains__(doc_id):
                    position_list: list = posting_list[doc_id]
                    position_list.append(pos)
                    posting_list[doc_id] = position_list
                else:
                    position_list = [pos]
                    posting_list[doc_id] = position_list
                book[stem] = posting_list
            else:
                posting_list = {}  # posting_list struct: {"docID":[positions, ...], ...}
                position_list = [pos]
                posting_list[doc_id] = position_list
                book[stem] = posting_list
        return book

    # prints dict on terminal and write to file
    def printDictBook(self, dict_book):
        log_file = open("dict-log.txt", "w")
        for i in dict_book:
            log_file.write(i + " => " + str(dict_book[i]) + "\n")
            print(i + " => " + str(dict_book[i]))
        return
