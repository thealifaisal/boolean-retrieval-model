from nltk.stem import PorterStemmer


# only imported the Porter Stemmer

# I created a class Preprocessing to encapsulate the token and stemming-wrapper methods
class Preprocessing:
    stop_word = []

    # a linear time function created which takes a file-buffer and performs the tokenizing
    def tokenizer(self, file_buffer):  # file_buffer is a string
        tokens_l = []
        file_len = len(file_buffer)
        string = ""
        c = 0  # indicated no chars in a word before end of sentence, period (.), space ( ), colon (:)
        i = 0
        while i < file_len:  # linear time operation
            if ord(file_buffer[i]) in range(65, 91):  # ASCII[65-90] => [A-Z]
                string += chr(ord(file_buffer[i]) + 32)  # A => a, .., Z => z
                c += 1  # inc the no chars read
            elif ord(file_buffer[i]) in range(97, 123):  # ASCII[97-122] => [a-z]
                string += file_buffer[i]
                c += 1
                # when 'refugeeExcept' occurs
                if ord(file_buffer[i + 1]) in range(65, 91):
                    # if string not in self.stop_word:
                    tokens_l.append(string)
                    string = ""
                    c = 0  # reset the counter of chars when end of word
            elif ord(file_buffer[i]) in range(48, 58):  # ASCII[48-57] => [0-9]
                while file_buffer[i] not in [" ", ":", "!", "?", "-"] and i < file_len:  # read the numbers until
                    # if decimal or comma occurs but after that there is no number
                    if file_buffer[i] in [".", ","] and ord(file_buffer[i + 1]) not in range(48, 58):  # '234,Now'
                        break
                    string += file_buffer[i]  # append the numbers together
                    i += 1
                # if string not in self.stop_word:
                tokens_l.append(string)
                string = ""
                c = 0  # reset the counter of chars when end of word
            else:
                if file_buffer[i] in [" ", ":", ",", "!", "?", "-", "—"] and c != 0:  # indicates end of word
                    # if string not in self.stop_word:
                    tokens_l.append(string)
                    string = ""
                    c = 0  # reset the counter of chars when end of word
                elif file_buffer[i] == ".":
                    # if no of chars before . are more than 1 then this is not an abbr but end of sentence/word
                    # e.g: Thousands.
                    if c > 1:
                        # if string not in self.stop_word:
                        tokens_l.append(string)
                        string = ""
                    else:
                        # not abbr, e.g:'U.S.A.Something '
                        if file_buffer[i + 2] not in [" ", ".", ":", ",", "!", "?", "-", "—"]:
                            # if string not in self.stop_word:
                            tokens_l.append(string)
                            string = ""
                    # else if no of chars before . is 1 then it is probably an abbr, so do not append in list now
                    # e.g: U.
                    c = 0  # reset the counter of chars before .
                elif file_buffer[i] == "'":  # if char is apostrophe (`)
                    # if string not in self.stop_word:
                    tokens_l.append(string)  # add the string to list, if grammar is correct then will be c > 1
                    string = ""
                    c = 0
                    i += 1  # move the ptr to next char possibly [s, re, ..]
                    while file_buffer[i] not in [" ", ":", ",", "!", "?", ".", "—"] and i < file_len:
                        i += 1  # ignore everything after apostrophe until the list above
                elif file_buffer[i] == "[":  # when this occurs, ignore in the inside of brackets, e.g: [applause]
                    if c != 0:  # this also marks the end of word, so if read char count > 1
                        # if string not in self.stop_word:
                        tokens_l.append(string)  # add the string to list
                        string = ""
                        c = 0
                    i += 1  # move the ptr inside the brackets [...
                    while file_buffer[i] not in ["]"] and i < file_len:  # read until ]
                        i += 1  # ignore everything inside
            i += 1
        # tokens_L.remove('') - token list returned has empty strings in multiple indexes
        # remove these before performing indexing
        return tokens_l  # returns a prepared list of tokens

    def stemmer(self, tokens_list):
        stems_list = []
        ps = PorterStemmer()  # imported from nltk library
        for tk in tokens_list:  # pass token from token list in stem function and add stems in list
            stem = ps.stem(tk)
            stems_list.append(stem)
        return stems_list  # returns a list of stems
