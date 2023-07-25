from collections import Counter
if __name__ == '__main__':
    N = int(input())
    words = []
    while N > 0:
        words.append(str(input()))
        N -= 1
    word_frequency = Counter(words)
    frequency = []
    for word_count , count in word_frequency.items():
        frequency.append(count)
    print(len(frequency))
    print (frequency)