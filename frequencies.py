import string_histogram as sh


def frequencies(histogram):
    frequency_array = []
    count_characters = sum(histogram.values())
    for i in range(0, 26):

        if histogram.get(chr(i + 97)) is None:
            frequency_array.append(0)
        else:
            frequency_array.append(1 / count_characters * histogram.get(chr(i + 97)))
    return frequency_array

