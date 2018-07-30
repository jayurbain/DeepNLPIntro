def sent_labels(sentences):
    dictionary = dict()
    with open("stanfordSentimentTreebank/dictionary.txt", "rt", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            splitted = line.split("|")
            dictionary[splitted[0].lower()] = int(splitted[1])

    labels = [0.5] * (max(dictionary.values()) + 1)
    with open("stanfordSentimentTreebank/sentiment_labels.txt", "rt", encoding="utf-8") as f:
        f.readline()
        for line in f:
            line = line.strip()
            if not line:
                continue
            splitted = line.split("|")
            labels[int(splitted[0])] = float(splitted[1])

    sent_labels = [0.5] * len(sentences)
    for i in range(len(sentences)):
        full_sent = sentences[i].replace("-lrb-", "(").replace("-rrb-", ")").replace("\\\\", "")
        try:
            sent_labels[i] = labels[dictionary[full_sent.lower()]]
        except KeyError:
            pass

    return sent_labels

if __name__ == "__main__":
    import pandas
    p = pandas.read_csv("stanfordSentimentTreebank/datasetSentences.txt", sep="\t")
    s = p["sentence"].tolist()
    a = sent_labels(s)
