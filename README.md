# LLMs in SpaCy: enables NLP pipelines

The advantages of incorporating Large Language Models (LLMs) in Natural Language Processing (NLP) tasks and demonstrates the synergistic combination of spaCy's components, which utilize supervised learning or rule-based methodologies, with LLM-powered components.

## Installation

Install given configuration: macOS/OSX,ARM/M1,`conda`,CPU, virtual env, English, efficiency.

For other installation options, see [install spaCy ](https://spacy.io/usage#quickstart).

### step1: env setup:\*\*

```
conda create --name spacy-llm
conda activate spacy-llm
```

### step2: install commands:\_\*\*

```
conda install -c conda-forge spacy
```

python -m spacy download en_core_web_sm # or en_core_web_trf for transformer-based model

> `en_core_web_sm` is a small English model pipeline trained on web text.

> for accurary use `python -m spacy download en_core_web_trf` for transformer-based model`

For more details, see the [models](https://spacy.io/models/en#en_core_web_sm).

**_step3: test installation:_**

```
python -m spacy validate
```

## Usage

```shell
python src/test.py
python src/main.py
```

## Components

`process_text(text)`
Extracts `(token, POS, dependency)`: tokens, part-of-speech tags, and dependency tags using Spacy.

**input**

- `text` (str): The text to process.

**output**

- A list of tuples: `(token, POS, dependency)`

**\*example**

```python
text = "This is an example sentence."
processed_text = process_text(text)
print(processed_text)
```

Output:

```
[('This', 'DET', 'nsubj'), ('is', 'VERB', 'ROOT'), ('an', 'DET', 'det'), ('example', 'NOUN', 'attr'), ('sentence', 'NOUN', 'pobj'), ('.', 'PUNCT', 'punct')]
```
