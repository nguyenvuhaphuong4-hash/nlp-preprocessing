import nltk
import spacy
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Input text
sentences = [
    "I love learning natural language processing.",
    "This course is very interesting and useful.",
    "Python makes text processing easier."
]

# Initialize
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess_nltk(text):
    tokens = nltk.word_tokenize(text)
    
    lower = [word.lower() for word in tokens]
    
    no_stop = [word for word in lower if word not in stop_words]
    
    no_punct = [word for word in no_stop if word not in string.punctuation]
    
    stemmed = [stemmer.stem(word) for word in no_punct]
    
    return stemmed


def preprocess_spacy(text):
    doc = nlp(text)
    
    tokens = [token.text for token in doc]
    
    lower = [token.lower() for token in tokens]
    
    no_stop = [token for token in doc if not token.is_stop]
    
    no_punct = [token for token in no_stop if not token.is_punct]
    
    lemmas = [token.lemma_.lower() for token in no_punct]
    
    return lemmas


# Run preprocessing
print("=== NLTK ===")
for s in sentences:
    print(preprocess_nltk(s))

print("\n=== spaCy ===")
for s in sentences:
    print(preprocess_spacy(s))
gold = [
    ["love", "learn", "natural", "language", "processing"],
    ["course", "interesting", "useful"],
    ["python", "make", "text", "processing", "easy"]
]
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

def evaluate(predicted, gold):
    y_true = []
    y_pred = []

    for g, p in zip(gold, predicted):
        all_words = list(set(g + p))
        for word in all_words:
            y_true.append(1 if word in g else 0)
            y_pred.append(1 if word in p else 0)

    print("Accuracy:", accuracy_score(y_true, y_pred))
    print("Precision:", precision_score(y_true, y_pred))
    print("Recall:", recall_score(y_true, y_pred))
    print("F1-score:", f1_score(y_true, y_pred))


# Get predictions
nltk_pred = [preprocess_nltk(s) for s in sentences]
spacy_pred = [preprocess_spacy(s) for s in sentences]

print("\n=== NLTK Evaluation ===")
evaluate(nltk_pred, gold)

print("\n=== spaCy Evaluation ===")
evaluate(spacy_pred, gold)