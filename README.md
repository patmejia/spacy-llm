# spacy-llms: augmenting nlp pipelines

Enabling NLP pipelines with Large Language Models (LLMs), combining spaCy's supervised learning or rule-based components with LLM-powered features.
![process_text_foo](docs/process_text.gif)

## Installation

Follow these steps for installation:

- macOS/OSX
- ARM/M1
- `conda`
- CPU
- virtual env
- English
- efficiency

For other setups, refer to [spaCy's installation guide](https://spacy.io/usage#quickstart).

### Step 1: Environment setup

```
conda create --name spacy-llm
conda activate spacy-llm
```

### Step 2: Install spaCy

```
conda install -c conda-forge spacy
```

To download the small English model trained on web text:

```
python -m spacy download en_core_web_sm
```

For better accuracy, use a transformer-based model:

```
python -m spacy download en_core_web_trf
```

See [spaCy's models](https://spacy.io/models/en#en_core_web_sm) for more details.

### Step 3: Test installation

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
Extracts `(token, POS, dependency)`: tokens, part-of-speech tags, and dependency tags using spaCy.

**Input**

- `text` (str): The text to process.

**Output**

- A list of tuples: `(token, POS, dependency)`

**Example**

```python
text = "This is an example sentence."
processed_text = process_text(text)
print(processed_text)
```

Output:

```
[('This', 'DET', 'nsubj'), ('is', 'VERB', 'ROOT'), ('an', 'DET', 'det'), ('example', 'NOUN', 'attr'), ('sentence', 'NOUN', 'pobj'), ('.', 'PUNCT', 'punct')]
```

## Roadmap

1. **Optimize LLM Integration**: Enhance Large Language Model integration.
2. **Extend Models**: Incorporate sentiment analysis.
3. **API Development**: Design a REST API for external usage.
4. **Testing**: Expand unit and integration tests.
5. **Dockerization**: Containerize application for portability.

## Contributing

To contribute, fork the repository, implement changes, run tests ✓, and submit a pull request We appreciate your help!

## Acknowledgements

- [explosion_ai 💥](https://github.com/explosion)
- [@spacy_io 🪐](https://github.com/explosion/spacy-llm)
