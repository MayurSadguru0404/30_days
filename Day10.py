words=["eat","tea","tan","ate","nat","bat"]
anagram_groups={}
def Anangrams(li):
    for word in li:
        sorted_words="".join(sorted(word))
        if sorted_words in anagram_groups:
            anagram_groups[sorted_words].append(word)
        else:
            anagram_groups[sorted_words]=[word]
    return list(anagram_groups.values())

print(Anangrams(words))
