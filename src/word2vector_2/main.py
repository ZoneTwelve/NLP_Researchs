#!/usr/bin/env python
import os, time, json
from re import match
from tqdm import tqdm
from argparse import ArgumentParser
# https://dboyliao.medium.com/python-%E8%B6%85%E5%A5%BD%E7%94%A8%E6%A8%99%E6%BA%96%E5%87%BD%E5%BC%8F%E5%BA%AB-argparse-4eab2e9dcc69

argp = ArgumentParser()
argp.add_argument("-s", "--source", help="Data source", dest="datasource")
argp.add_argument("-p", "--pattern", help="Filtering with Regex", dest="pattern", default=".*")
argp.add_argument("-c", "--encoding", help="File encoding", dest="coded", default="utf-8")
# https://realpython.com/working-with-files-in-python/
args = argp.parse_args()
_rp = args.pattern
_ds = args.datasource
_coded = args.coded
dslist = os.listdir(_ds)

# filtering https://realpython.com/working-with-files-in-python/
# https://stackoverflow.com/questions/3640359/regular-expressions-search-in-list
# Testing https://regex101.com/
vocab = set()
keep = list(filter(lambda v: match(_rp, v), dslist))
for doc in tqdm(keep):
  doc_path = f'{_ds}/{doc}'
  # https://stackoverflow.com/questions/10971033/backporting-python-3-openencoding-utf-8-to-python-2
  tokens = open(doc_path, 'r', encoding=_coded, errors='replace').read()
  for token in tokens:
    vocab.add(token)
maps = {index:word for index, word in enumerate(vocab)}
# https://www.geeksforgeeks.org/get-current-timestamp-using-python/
output = open(f"_output/{time.time()}.out", "w")
output.write(json.dumps(maps))
