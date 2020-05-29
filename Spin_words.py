def spin_words(sentence):
    res = []
    phrase = sentence.split(" ")
    for word in phrase:
        if len(word) >= 5:
            word = word[::-1]
            res.append(word)
        else:
            res.append(word)
    res = " ".join(res)
    return res


z = input("Enter a sentence: ")
print(spin_words(z))


