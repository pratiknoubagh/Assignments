def count_word_occurrence(sentence):
    word_counts = {}
    words = sentence.split()

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

# Example usage
sentence = input("Enter a sentence")
occurrences = count_word_occurrence(sentence)
print("Word occurrences:")
for word, count in occurrences.items():
    print(f"{word}: {count}")