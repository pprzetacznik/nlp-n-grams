# -*- coding: utf-8 -*-
#!/usr/bin/env python

import unittest
import numpy as np
from stats import cosine_distance, initialize_n_grams_list, clean, get_n_grams_from_string, count_n_grams, count_stat_for_document

class TestLogger(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_cosine_distance(self):
    print cosine_distance([1,2,3], [2,3,4])
    self.assertAlmostEqual(cosine_distance([3,4,5], [3,4,5]), 1)
    self.assertEqual(cosine_distance([1,2], [-2,1]), 0)

  def test_initialize_n_grams_list(self):
    print initialize_n_grams_list(1)
    # print initialize_n_grams_list(2)

  def test_clean(self):
    print clean("abecadło z pieca spadło123")

  def test_get_n_grams_from_string(self):
    print get_n_grams_from_string("string", 3)

  def test_count_n_grams(self):
    print count_n_grams("to jest testowy tekst".split(), 3)

  def test_count_stat_for_document(self):
    print count_stat_for_document('pjn_lab1/polski.txt')

if __name__ == '__main__':
  unittest.main()
