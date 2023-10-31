from nltk.tokenize import word_tokenize

def calculate_jaccard_similarity(sentence1, sentence2):
    # Tokenize sentences into words
    words1 = set(word_tokenize(sentence1.lower()))
    words2 = set(word_tokenize(sentence2.lower()))

    # Calculate Jaccard similarity
    intersection = len(words1.intersection(words2))
    union = len(words1.union(words2))
    jaccard_similarity = intersection / union

    return jaccard_similarity

def calculate_length_ratio(sentence1, sentence2):
    # Calculate length ratio
    length1 = len(sentence1) / max(len(sentence1), len(sentence2))
    length2 = len(sentence2) / max(len(sentence1), len(sentence2))

    return length1, length2

# Read sentences from file
with open('DZDA.txt', 'r') as file:
    sentences = file.readlines()

# Clean and filter sentences
cleaned_sentences = []
for sentence1 in sentences:
    for sentence2 in sentences:
        if sentence1 != sentence2:
            jaccard_similarity = calculate_jaccard_similarity(sentence1, sentence2)
            length1, length2 = calculate_length_ratio(sentence1, sentence2)
            if jaccard_similarity > 0.5 and 0.3 <= length1 <= 3.0 and 0.3 <= length2 <= 3.0:
                cleaned_sentences.append(sentence1)

# Write cleaned sentences to a new file
with open('cleaned_sentences.txt', 'w') as file:
    for sentence in cleaned_sentences:
        file.write(sentence)
