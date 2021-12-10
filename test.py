import spacy
nlp = spacy.load("ur_model")

doc = nlp("اب آپ اردو ماڈل استمعال کر سکتے ہیں ")

for token in doc:
    print(token.text, token.pos_, token.dep_)
