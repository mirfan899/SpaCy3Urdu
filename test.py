import spacy
nlp = spacy.load("./ur_ner")
('کہ بھارت ، یورپ اور امریکا نے گناہوں کو آرٹ بنا دیا', {'entities': [(3, 8, 'Location'), (11, 15, 'Location'), (20, 26, 'Location')]})
doc = nlp("کہ بھارت ، یورپ اور امریکا نے گناہوں کو آرٹ بنا دیا")

for token in doc:
    print(token.text, token.pos_, token.ent_type_, token.dep_)
