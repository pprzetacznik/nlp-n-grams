import os
import re
from argparse import Namespace, ArgumentParser
from typing import Dict, List, Union
from operator import itemgetter
import numpy as np


SimilarityMap = Dict[str, float]
NGramsVector = List[int]
NGramsList = List[str]
NGramsMap = Dict[str, int]


class NGrams:
    def __init__(
        self, n_size: int = 3, alphabet: Union[None, str] = None
    ) -> None:
        self.n_size = n_size
        if not alphabet:
            self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        else:
            self.alphabet = alphabet
        self.init_n_grams_list = self._initialize_n_grams_list(self.n_size)

    def get_vector_for_document(self, document: str) -> NGramsVector:
        stat_list = []
        with open(document, "r") as file:
            data = file.read()
            data2 = clean(data.lower()).split()
            stat_map = self._count_n_grams(data2, self.n_size)
            for key in self.init_n_grams_list:
                if key not in stat_map:
                    stat_list.append(0)
                else:
                    stat_list.append(stat_map[key])
        return stat_list

    def _initialize_n_grams_list(self, n_size: int) -> NGramsList:
        n_grams_table = []
        if n_size == 1:
            for i in self.alphabet:
                n_grams_table.append(i)
            return n_grams_table
        else:
            n_grams_table = self._initialize_n_grams_list(n_size - 1)
            n_grams_table2 = []
            for i in n_grams_table:
                for j in self.alphabet:
                    n_grams_table2.append(i + j)
            return n_grams_table2

    def _count_n_grams(self, data: List[str], n_grams: int) -> NGramsMap:
        n_grams_map: NGramsMap = {}
        for word in data:
            for gram in self._get_n_grams_from_string(word, n_grams):
                if gram in n_grams_map:
                    n_grams_map[gram] += 1
                else:
                    n_grams_map[gram] = 1
        return n_grams_map

    def _get_n_grams_from_string(
        self, string: str, n_grams: int
    ) -> NGramsList:
        return [
            string[i : i + n_grams] for i in range(len(string) - n_grams + 1)
        ]


def cosine_distance(vec1: NGramsVector, vec2: NGramsVector) -> float:
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


def clean(string: str) -> str:
    return re.sub(r"[^a-z\s]", "", string)


def n_grams_for_directory(
    ngrams: NGrams, directory: str, n_size: int = 3
) -> Dict[str, NGramsVector]:
    stat_map = {}
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            print(f"Processing file: {filepath}")
            stat_map[filename] = ngrams.get_vector_for_document(filepath)
    return stat_map


def print_similarity_map(similarity_map: SimilarityMap) -> None:
    print("######## RECOMMENDATIONS ###########")
    for file_name, score in sorted(
        similarity_map.items(), key=itemgetter(1), reverse=True
    ):
        print(f"{file_name} : {score}")


def parse_arguments() -> Namespace:
    parser = ArgumentParser(description="Calculate n-gram stats for a file")
    parser.add_argument(
        "--n-gram",
        type=int,
        default=3,
        help="number of chars in each n-gram",
        dest="n_size",
    )
    parser.add_argument(
        "--train-dir",
        default="train",
        help="directory of corpus dataset txt files used for training",
        dest="train_dir",
    )
    parser.add_argument(
        "--test-file",
        help="path to test txt file for which you want to calculate stats",
        dest="test_file",
    )
    return parser.parse_args()


def main(args: Namespace) -> None:
    ngrams = NGrams(args.n_size)
    corpus_n_grams_vectors = n_grams_for_directory(ngrams, args.train_dir)
    user_stats = ngrams.get_vector_for_document(args.test_file)

    similarity_map = {
        filename: cosine_distance(corpus_n_grams_vectors[filename], user_stats)
        for filename in corpus_n_grams_vectors
    }
    print_similarity_map(similarity_map)


if __name__ == "__main__":
    args = parse_arguments()
    main(args)
