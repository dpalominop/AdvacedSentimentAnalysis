# Advanced Sentiment Analysis

This project compare different advances techniques for Sentiment Analysis in Spanish Tweets using data samples of [Sepln-TASS](http://www.sepln.org/workshops/tass/)

## Vocabulary Size

| Freq     | TASS 2017 | TASS 2018   |
| -------- | --------- | ----------- |
| 1        | 4227      | 3067        | 
| 2        | 1240      | 800         |
| 3        | 715       | 478         |

# Accuracy

## CNN

| Freq     | TASS 2017 | TASS 2018 |
| -------- | --------- | --------- |
| 1        | 77.86     | 76.11     | 
| 2        | 73.0      | 71.64     | 
| 3        | 74.6      | 70.64     | 


## SIF Embedding + SVD(C=0.8)

| Freq     | TASS 2017 | TASS 2018 |
| -------- | --------- | --------- |
| 1        | 73.10     | 70.10     | 
| 2        | 69.90     | 62.70     | 
| 3        | 64.30      | 58.20     |

## ULMFit

| Freq     | TASS 2017 | TASS 2018 |
| -------- | --------- | --------- |
| 1        | 70.93     | 70.64     | 
| 2        | 71.46     | 69.65     | 
| 3        | 73.6      | 63.13     | 


# Extras
## Word2Vec embeddings from SBWC

#### Embeddings
Links to the embeddings (#dimensions=300, #vectors=1000653) 
- [Vector format (.txt.bz2)](http://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/SBW-vectors-300-min5.txt.bz2) 
- [Binary format (.bin.gz)](http://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/SBW-vectors-300-min5.bin.gz) 

#### Algorithm
- Implementation: [Word2Vec with Skipgram by GenSim](https://radimrehurek.com/gensim/models/word2vec.html) 
- Parameters: For details on parameters please refer to the [SBWCE page](http://crscardellino.github.io/SBWCE/)
     
#### Corpus
- [Spanish Billion Word Corpus](http://crscardellino.github.io/SBWCE/) 
- Corpus Size: 1.4 billion words

#### Reference
Word embeddings were computed by [Cristian Cardellino](https://github.com/crscardellino). Please refer to the [SBWCE page](http://crscardellino.github.io/SBWCE/) if you want to use these vectors.
