### Project setup
run command to setup assets(dataset from UD)
```shell
spacy project assets
```
It uses `project.yml` file and download the data from UD GitHub repository.

### Download vectors
Download fasttext vectors
```shell
wget https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.ur.300.vec.gz 
```

Use these vectors to prune it so that model size is reduced. I'm currently using 100000 vectors for training the model.
```shell
mkdir vectors
python -m spacy init vectors ur cc.ur.300.vec.gz  ./vectors --truncate 100000 --name ur_model.vectors
```

### Preprocessing
Replace Other with O to train a better model.
```shell
sed -i 's/Other/O/g' ner/100000.txt 
```

convert tsv to json
```shell
python tsv_to_json.py
```
Now convert json to spacy pickle format.
```shell
python json_to_spacy.py -i ner/urdu_ner_dataset.json -o ner/urdu_ner_dataset.txt
```

Now convert to spacy .spacy binary format.

```shell
python json2spacy3.3.py
```
### Train the model
Now run the command to train the tagger and parser for Urdu language.
```shell
spacy project run all
```

It will train the tagger and parser model on cpu. You can specify gpu in `project.yml` file.

### Install the model
After training, you can install and use the model.

```shell
pip install ur_model-0.0.0.tar.gz 
```

There is a script `test.py` on how to use the model.


### Spacy 3.3
Create config.cfg from base_config.cfg

```shell
python -m spacy init fill-config base_config.cfg config.cfg
```

Train two models i.e. one for tagger, parser etc and second for ner.
To train tagger and parser run
```shell
spacy project assets
spacy project run all
```
Train ner model
```shell
spacy train configs/config.cfg --output ./ner3 --paths.train corpus/train.spacy --paths.dev corpus/dev.spacy
```


Install both models
```shell
pip install location/ur_model.xxxx.tar.gz
pip install location/ur_ner.xxxx.tar.gz
```
Now Merge two trained models.
```shell
python merge_tp2ner.py
```

Now uninstall these models
```shell
pip uninstall ur_model
pip uninstall ur_ner
```

Now package merged model
```shell
# create packages directory if get error
spacy package ur_ner packages --name "ner" --version "0.0.0" --force
```

Now install it
```shell
pip install location/ur_ner.xxx.tar.gz
```
