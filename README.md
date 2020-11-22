Natural Language Processing - n-grams statistics
===

Run:
```
pip install -r requirements.txt
python -m stats --train-dir train_corpus --n-gram 3 --test-file test_corpus/thewire.txt
```

Example run:
```
$ python -m stats --train-dir train_corpus --n-gram 3 --test-file test_corpus/thewire.txt
Processing file: train_corpus/2momm10.txt
Processing file: train_corpus/4momm10.txt
Processing file: train_corpus/54.txt
Processing file: train_corpus/5momm10.txt
Processing file: train_corpus/8momm10.txt
Processing file: train_corpus/finnish.txt
Processing file: train_corpus/finnish1.txt
Processing file: train_corpus/Harry Potter 1 Sorcerer's_Stone.txt
Processing file: train_corpus/Harry Potter 2 Chamber_of_Secrets.txt
Processing file: train_corpus/Harry Potter 3 Prisoner of Azkaban.txt
Processing file: train_corpus/Harry Potter 4 and the Goblet of Fire.txt
Processing file: train_corpus/polski.txt
Processing file: train_corpus/polski2.txt
Processing file: train_corpus/polski3.txt
Processing file: train_corpus/q.txt
Processing file: train_corpus/spanish.txt
Processing file: train_corpus/spanish1.txt
######## RECOMMENDATIONS ###########
Harry Potter 1 Sorcerer's_Stone.txt  :  0.8516218202150778
Harry Potter 4 and the Goblet of Fire.txt  :  0.8382954018753523
Harry Potter 3 Prisoner of Azkaban.txt  :  0.8297737283348564
Harry Potter 2 Chamber_of_Secrets.txt  :  0.8286664546220112
q.txt  :  0.2687367480112696
54.txt  :  0.2654665173972638
spanish1.txt  :  0.2157763828702334
8momm10.txt  :  0.20948116826277266
5momm10.txt  :  0.20088947556841405
4momm10.txt  :  0.20052011673047865
2momm10.txt  :  0.1900199333318412
spanish.txt  :  0.18425240798457684
finnish.txt  :  0.1749251467750644
finnish1.txt  :  0.17453271188273536
polski.txt  :  0.12179996712775056
polski3.txt  :  0.09870171027877826
polski2.txt  :  0.09401455065003979
```
