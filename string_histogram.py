def string_histogram(text):
    histogram = {}

    for character in text:
        char = character.lower()
        if character.isalpha():
            if histogram.get(char) is None:
                histogram[char] = 1
            else:
                histogram[char] += 1

    sortedKeys = list(histogram.keys())
    sortedKeys.sort()
    sortedHistogram = {i : histogram[i] for i in sortedKeys}

    return sortedHistogram






