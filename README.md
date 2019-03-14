# Advanced Sentiment Analysis

This project compare different advances techniques for Sentiment Analysis in Spanish Tweets using data samples of [Sepln-TASS](http://www.sepln.org/workshops/tass/)

## TASS 2017 (Development)

|  Model | Macro F1 | Accuracy |
|--------|----------|----------|
|  CNN   |  0.330   | 0.77075  |
|  SIF   |  0.733   | 0.773    |
| ULMFit |	0.222	| 0.3837   |

## TASS 2018

### Test

|  Model |              Run             | Macro F1 | Accuracy | 
|--------|------------------------------|----------|----------|
|  CNN   | cnn-btf-2019_03_13-04_12_55  |  0.387   |   0.432  |
|  SIF   | SIF-M LP-2019_01_30-00_27_52 |  0.399   |   0.398  |
| ULMFit | md3-2019_03_12-06_37_15      |  0.270   |   0.299  |

### Development

|  Model |   Accuracy  | 
|--------|-------------|
|  CNN   |    0.755    |
|  SIF   |    0.602    |
| ULMFit |    0.309    |


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
