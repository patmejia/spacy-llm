# spacy-llms: augmenting nlp pipelines

Enabling NLP pipelines with Large Language Models (LLMs), combining spaCy's supervised learning or rule-based components with LLM-powered features.
![process_text_foo](docs/process_text.gif)

## Installation

The provided installation steps suit a configuration:

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
pytest src/test.py
```

```shell
python src/main.py
```

```shell
✗ python src/get_top_ranked_phrases.py
```

## Features

`process_text(text)` extracts `(token, POS, dependency)` from text.

`extract_entities(text)` identifies named entities in text. [entites ⩩](https://spacy.io/api/annotation#named-entities).

`get_top_ranked_phrases(text)` extracts top ranked phrases from text.`

`summarize_text_returns_expected_summary(nlp, geosynchronization_text)`

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

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Notes

- Dependency parsing is instrumental in information extraction and gains additional power when complemented with named entity recognition.

- Proper testing ensures reliability of NLP pipeline, enhancing predictability and stability of the system.

- Refer to [entities](https://spacy.io/usage/linguistic-features#named-entities) for comprehensive details on the entity recognition feature utilized in our project.
