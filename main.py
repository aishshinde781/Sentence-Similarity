# Create a list of punctuations to compare and discard these stopwords from the sentence
punctuations = {".", ",", "!", "'"}
# Create a list of english stopwords to compare and discard these stopwords from the sentence
stopwords = {"i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
             "yourselves", "you'll", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
             "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
             "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
             "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until",
             "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during",
             "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under",
             "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both",
             "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so",
             "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"}


# function to parse the original sentence after removing punctuations and stopwords to have a better similarity score
def filter_sentences(s):
    # Create an empty set to store the final tokenized words from the sentence after all pre-processing
    new_sent = set()
    s = s.strip()
    # words tokenization
    words = s.split(" ")
    for w in words:
        # lowercase all the texts
        w = w.lower()
        tmp = ""
        for ch in w:
            if ch not in punctuations:
                tmp += ch
        if tmp not in stopwords:
            new_sent.add(tmp)
    return new_sent


def check_similarity(sentence1, sentence2):
    # Implementing Jaccard algorithm for calculating similarity scores between two texts
    sentence_intersection = sentence1.intersection(sentence2)
    sentence_union = sentence1.union(sentence2)

    similarity_score = len(sentence_intersection) / len(sentence_union)
    return similarity_score


if __name__ == "__main__":

    s1 = input("Enter first sentence:  \n")
    print()
    s2 = input("Enter second sentence:  \n")
    print()

    parsed_sentence1 = filter_sentences(s1)
    parsed_sentence2 = filter_sentences(s2)

    score1 = check_similarity(parsed_sentence1, parsed_sentence2)

    print("Similarity score for first & second sentence: ", score1)

    print()



