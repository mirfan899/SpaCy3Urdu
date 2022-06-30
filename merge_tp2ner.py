import spacy
nlp = spacy.load("ur_model")
# nlp.remove_pipe("ner")
print(nlp.pipe_names)  # ['tagger', 'parser']

nlp_entity = spacy.load("ur_ner")
# Get the ner pipe from this model and add it to base model
nlp.add_pipe("ner", source=nlp_entity)
print(nlp.pipe_names)  # ['tagger', 'parser', 'ner']

nlp.to_disk("./ur_ner")
