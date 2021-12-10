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