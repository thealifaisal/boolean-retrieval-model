from pre_proc import Preprocessing


if __name__ == '__main__':
    file = open('Trump Speechs/speech_' + str(0) + ".txt", "r")
    file.readline()  # after reading the line, moves file ptr to next line to skip the title

    pipe = Preprocessing()
    tokens = pipe.tokenizer(file.read())
    stems = pipe.stemmer(tokens)
    # print(stems)


