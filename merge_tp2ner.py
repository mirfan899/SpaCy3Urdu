import spacy
nlp = spacy.load("ur_model")
# nlp.remove_pipe("ner")
print(nlp.pipe_names)  # ['tagger', 'parser']

# nlp.remove_pipe("ner")
nlp_entity = spacy.load("ur_ner")
nlp_entity.replace_listeners("tok2vec", "ner", ["model.tok2vec"])

# Get the ner pipe from this model and add it to base model
# nlp.add_pipe("ner", source=nlp_entity)
nlp.add_pipe(
    "ner",
    name="ner_custom",
    source=nlp_entity,
    after="ner",
)
print(nlp.pipe_names)  # ['tagger', 'parser', 'ner']

nlp.to_disk("./ur_ner")
