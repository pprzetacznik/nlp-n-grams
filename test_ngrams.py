from unittest import TestCase, main
from ngrams import NGrams, cosine_distance, clean


class TestNGrams(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_cosine_distance(self):
        print(cosine_distance([1, 2, 3], [2, 3, 4]))
        self.assertAlmostEqual(cosine_distance([3, 4, 5], [3, 4, 5]), 1)
        self.assertEqual(cosine_distance([1, 2], [-2, 1]), 0)

    def test_clean(self):
        print(clean("abecadło z pieca spadło123"))

    def test_count_stat_for_document(self):
        ngrams = NGrams(3)
        print(ngrams.count_stat_for_document("train_corpus/polski.txt"))


if __name__ == "__main__":
    main()
