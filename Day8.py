def reverse_str(s):
    words=s.strip().split()
    reverse_word=words[::-1]
    return " ".join(reverse_word)

print(reverse_str("the sky is blue"))
print(reverse_str("hello world"))