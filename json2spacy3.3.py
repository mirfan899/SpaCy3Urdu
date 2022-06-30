import spacy
from spacy.tokens import DocBin
import pickle

nlp = spacy.blank("fa")
with open('ner/urdu_ner_dataset.txt', 'rb') as fp:
    training_data = pickle.load(fp)
# the DocBin will store the example documents
db = DocBin()
validation = int(len(training_data)*.2)
for text, annotations in training_data[validation:]:
    doc = nlp(text)
    ents = []
    for start, end, label in annotations["entities"]:
        span = doc.char_span(start, end, label=label)
        ents.append(span)
    doc.ents = ents
    db.add(doc)
db.to_disk("corpus/dev.spacy")


for text, annotations in training_data[:validation]:
    doc = nlp(text)
    ents = []
    for start, end, label in annotations["entities"]:
        span = doc.char_span(start, end, label=label)
        ents.append(span)
    doc.ents = ents
    db.add(doc)
db.to_disk("corpus/train.spacy")
