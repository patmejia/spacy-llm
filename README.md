# LLMs in SpaCy: enables NLP pipelines

The advantages of incorporating Large Language Models (LLMs) in Natural Language Processing (NLP) tasks and demonstrates the synergistic combination of spaCy's components, which utilize supervised learning or rule-based methodologies, with LLM-powered components.

## Installation

Install given configuration: macOS/OSX,ARM/M1,`conda`,CPU, virtual env, English, efficiency.

For other installation options, see [install spaCy ](https://spacy.io/usage#quickstart).

step1: env setup:

```
conda create --name spacy-llm
conda activate spacy-llm
```

step2: install commands:

```
conda install -c conda-forge spacy
```

python -m spacy download en_core_web_sm # or en_core_web_trf for transformer-based model

> `en_core_web_sm` is a small English model pipeline trained on web text.

> for accurary use `python -m spacy download en_core_web_trf` for transformer-based model`

For more details, see the [models](https://spacy.io/models/en#en_core_web_sm).

step3: test installation:

```
python -m spacy validate
```

## Usage

```shell
python src/test.py
python src/main.py
```

# -------wip ----------

### 1. LLM-powered components

#### 1.1 Tokenizer

```
import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("This is a sentence.")
for token in doc:
    print(token.text)
```

#### 1.2 Part-of-speech tagger

```
import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("This is a sentence.")
for token in doc:
    print(token.text, token.pos_)
```

#### 1.3 Dependency parser

```
import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("This is a sentence.")
for token in doc:
    print(token.text, token.pos_, token.dep_)
```

#### 1.4 Named entity recognizer

```
import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
```

#### 1.5 Text classifier

```
import spacy
nlp = spacy.load("en_core_web_sm")
textcat = nlp.create_pipe("textcat", config={"exclusive_classes": True, "architecture": "simple_cnn"})
nlp.add_pipe(textcat)
textcat.add_label("POSITIVE")
textcat.add_label("NEGATIVE")
doc = nlp("This movie sucked")
print(doc.cats)
```

#### 1.6 Rule-based matcher

```
import spacy
from spacy.matcher import Matcher
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)
pattern = [{"LOWER": "hello"}, {"IS_PUNCT": True}, {"LOWER": "world"}]
matcher.add("HelloWorld", [pattern])
doc = nlp("Hello, world! Hello world!")
matches = matcher(doc)
for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]  # Get string representation
    span = doc[start:end]  # The matched span
    print(match_id, string_id, start, end, span.text)
```
