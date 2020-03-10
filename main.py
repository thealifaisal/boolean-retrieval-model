from nltk.stem import PorterStemmer


def tokenizer(file_buffer='U.S.A. has '):  # file_buffer is a string
    tokens = []
    file_len = len(file_buffer)
    string = ""
    c = 0  # indicated no chars in a word before end of sentence, period (.), space ( ), colon (:)
    i = 0
    while i < file_len:
        if ord(file_buffer[i]) in range(65, 91):  # ASCII[65-90] => [A-Z]
            string += chr(ord(file_buffer[i]) + 32)  # A => a, .., Z => z
            c += 1  # inc the no chars read
        elif ord(file_buffer[i]) in range(97, 123):  # ASCII[97-122] => [a-z]
            string += file_buffer[i]
            c += 1
        elif ord(file_buffer[i]) in range(48, 58):  # ASCII[48-57] => [0-9]
            while file_buffer[i] not in [" ", ":", "!", "?"]:
                if file_buffer[i] in [".", ","] and ord(file_buffer[i+1]) not in range(48, 58):  # '234,Now'
                    break
                string += file_buffer[i]
                i += 1
            tokens.append(string)
            string = ""
            c = 0  # reset the counter of chars when end of word
        else:
            if file_buffer[i] in [" ", ":", ",", "!", "?"] and c != 0:  # indicates end of word
                tokens.append(string)
                string = ""
                c = 0  # reset the counter of chars when end of word
            elif file_buffer[i] == ".":
                # if no of chars before . are more than 1 then this is not an abbr but end of sentence/word
                # e.g: Thousands.
                if c > 1:
                    tokens.append(string)
                    string = ""
                else:
                    if file_buffer[i + 2] not in [" ", ".", ":", ",", "!", "?"]:  # not abbr, e.g:'U.S.A.Something '
                        tokens.append(string)
                        string = ""
                # else if no of chars before . is 1 then it is probably an abbr, so do not append in list now
                # e.g: U.
                c = 0  # reset the counter of chars before .
            elif file_buffer[i] == "'":  # if char is apostrophe (`)
                tokens.append(string)  # add the string to list
                string = ""
                c = 0
                i += 1
                while file_buffer[i] not in [" ", ":", ",", "!", "?", "."]:
                    i += 1
            elif file_buffer[i] == "[":
                if c != 0:
                    tokens.append(string)  # add the string to list
                    string = ""
                    c = 0
                i += 1
                while file_buffer[i] not in ["]"]:
                    i += 1

        i += 1
    return tokens


if __name__ == '__main__':
    file = open('Trump Speechs/speech_' + str(0) + ".txt", "r")
    file.readline()  # after reading the line, moves file ptr to next line to skip the title

    # tokensM = tokenizer()
    tokensM = tokenizer(file.read())

    print(tokensM)
