Information Retrieval
=====================

### Installation

```bash
sudo pip3 install -U numpy scipy scikit-learn
sudo pip3 install -U nltk
```

#### NLTK Ressources Installation:

```bash
python3
>>> import nltk
>>> nltk.download()
```

Models > punkt > Download

### Execution

```bash
python / python3 main.py
```

### Settings

In the main.py file, the configuration of the parse can be chosen:

```python
parser = Parser(ParserType.simple)
parser = Parser(ParserType.wordprocessing)
```

### Books

All books used during the implementation can be found here: https://github.com/alexlanz/information-retrieval/