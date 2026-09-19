from collections import Counter


def frequency_analysis(text):
    letters = [char.upper() for char in text if char.isalpha()]
    total = len(letters)

    if total == 0:
        return {}

    counts = Counter(letters)

    frequency = {}

    for letter in sorted(counts):
        frequency[letter] = round((counts[letter] / total) * 100, 2)

    return frequency
