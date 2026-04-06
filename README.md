# NLP Text Preprocessing using NLTK and spaCy

## Project Description

This project demonstrates basic text preprocessing techniques using two popular NLP libraries: **NLTK** and **spaCy**.

The goal is to compare their performance in handling:

* Tokenization
* Lowercasing
* Stopword removal
* Punctuation removal
* Stemming (NLTK)
* Lemmatization (spaCy)

---

## Input Sentences

1. I love learning natural language processing.
2. This course is very interesting and useful.
3. Python makes text processing easier.

---

## Preprocessing Steps

* Tokenization
* Lowercasing
* Stopword Removal
* Punctuation Removal
* Stemming (NLTK)
* Lemmatization (spaCy)

---

## Results

### NLTK Output

```
['love', 'learn', 'natur', 'languag', 'process']
['cours', 'interest', 'use']
['python', 'make', 'text', 'process', 'easier']
```

### spaCy Output

```
['love', 'learn', 'natural', 'language', 'processing']
['course', 'interesting', 'useful']
['python', 'make', 'text', 'processing', 'easy']
```

---

## Evaluation Metrics

| Metric    | NLTK  | spaCy |
| --------- | ----- | ----- |
| Accuracy  | 0.238 | 0.857 |
| Precision | 0.385 | 0.923 |
| Recall    | 0.385 | 0.923 |
| F1-score  | 0.385 | 0.923 |

---

## Analysis

spaCy outperforms NLTK because it uses **lemmatization**, which produces meaningful base forms of words.
In contrast, NLTK uses **stemming**, which may truncate words incorrectly and reduce accuracy.

---

## Requirements

Install dependencies using:

```
pip install -r requirements.txt
```

---

## How to Run

```
python main.py
```

---

## Project Structure

```
├── main.py
├── requirements.txt
└── README.md
```

---

## Author

Student project for NLP course.
