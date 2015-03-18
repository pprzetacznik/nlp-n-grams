# -*- coding: utf-8 -*-
#!/usr/bin/env python

from __future__ import print_function
import numpy as np
import os
import sys
import re
from operator import itemgetter

def initialize_n_grams_list(n):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  n_grams_table = []
  if n == 1:
    for i in alphabet:
      n_grams_table.append(i)
    return n_grams_table
  else:
    n_grams_table = initialize_n_grams_list(n-1)
    n_grams_table2 = []
    for i in n_grams_table:
      for j in alphabet:
        n_grams_table2.append(i+j)
    return n_grams_table2

def cosine_distance(vec1, vec2):
  return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def clean(string):
  return re.sub("[^a-z\s]", "", string)

def get_n_grams_from_string(string, n_grams=3):
  n_grams_list = []
  for i in xrange(len(string)-n_grams+1):
    n_grams_list.append(string[i:i+n_grams])
  return n_grams_list

def count_n_grams(data, n_grams=3):
  n_grams_map = {}
  for word in data:
    for gram in get_n_grams_from_string(word, n_grams):
      if gram in n_grams_map:
        n_grams_map[gram] += 1
      else:
        n_grams_map[gram] = 1
  return n_grams_map

def count_stat_for_document(document):
  stat_list = []
  with open(document) as file:
    data = file.read()
    data2 = clean(data.lower()).split()
    stat_map = count_n_grams(data2, 3)
    for key in initialize_n_grams_list(3):
      if key not in stat_map:
        stat_list.append(0)
      else:
        stat_list.append(stat_map[key])
  return stat_list

def make_stats(directory):
  stat_map = {}
  for file in os.listdir(directory):
    if file.endswith(".txt"):
      print("Processing file: " + directory + "/" + file)
      stat_map[file] = count_stat_for_document(directory + "/" + file)
  return stat_map

def print_similarity_map(similarity_map):
  print("######## RECOMENDATIONS ###########")
  for item in sorted(similarity_map.items(), key=itemgetter(1), reverse=True):
    print(item[0], " : ", item[1])


if __name__ == '__main__':
  if len(sys.argv) == 4:
    dir = sys.argv[1]
    n_size = sys.argv[2]
    user_file = sys.argv[3]

    stats = make_stats(dir)
    user_stats = count_stat_for_document(user_file)

    similarity = {}
    for key in stats:
      similarity[key] = cosine_distance(stats[key], user_stats)
    print_similarity_map(similarity)

  else:
    print("python stats.py [directory] [n-grams] [user_file]")

