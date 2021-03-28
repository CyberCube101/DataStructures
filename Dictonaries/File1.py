' Create a Dictionary to count the frequency of words in a song'

myDict = {}


def lyrics_count(lyrics):
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict


song = ['she', 'loves', 'you', 'yeah', 'yeah', 'yeah']


def most_common(myDict):
    values = myDict.values()
    best = max(values)
    words = []
    for k in myDict:
        if myDict[k] == best:
            words.append(k)
    return (words, best)


if __name__ == '__main__':
    lyrics_count(song)
    print(most_common(myDict=myDict))
