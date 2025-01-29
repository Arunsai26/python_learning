from collections import Counter
words = ["ad","bd","aaab","baa","badab"]
allowed = "ab"
count=0
freq=Counter(words)

for i in range(len(words)):
    if words[i] in allowed:
        count+=1
print(count)





