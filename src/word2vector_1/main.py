#!/usr/bin/env python
from tqdm import tqdm

# idea come from https://ithelp.ithome.com.tw/articles/10269454
docs = [
          "he is a king",
          "she is a queen",
          "he is a man",
          "she is a woman",
        ]

vocab = set()

for doc in tqdm(docs):
  tokens = doc.split(" ")
  for token in tqdm(tokens):
    vocab.add(token)

maps = { index: word for index, word in enumerate(vocab) }
# https://www.geeksforgeeks.org/python-convert-a-set-into-dictionary/
# https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops

print(vocab)
print(maps)
# Output: 
#   {'queen', 'king', 'man', 'is', 'he', 'she', 'woman', 'a'}
#   {0: 'man', 1: 'king', 2: 'is', 3: 'queen', 4: 'woman', 5: 'she', 6: 'he', 7: 'a'}