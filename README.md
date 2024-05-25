# Spacy-LLMs: Augmenting NLP Pipelines

<img width="514" alt="Screenshot 2023-05-16 at 11 31 42 AM" src="https://github.com/patmejia/spacy-llm/assets/92187562/af4ce21a-e872-4f5f-9d1b-cc464d812157">

Integration of spaCy's components with Large Language Models (LLMs) to boost text processing, entity extraction, NER, and summarization. Includes unit and integration tests, fixtures, and samples. Enables NLP pipelines with Large Language Models (LLMs), combining spaCy's supervised learning or rule-based components with LLM-powered features.

![process_text_foo](docs/process_text.gif)

![console-output](docs/console_screenshoot.png)

## Installation

The installation steps suit a specific configuration:

- macOS/OSX
- ARM/M1, -`conda`
- CPU
- Virtual environment
- English
- Efficiency

Refer to [spaCy Quickstart ⩩](https://spacy.io/usage#quickstart) for other configurations.

### Steps

Activate a virtual environment and install spaCy:

Terminal:
```shell
conda create -n venv
conda activate venv
conda install -c conda-forge spacy
python -m spacy download en_core_web_sm
python -m spacy validate
```

- `en_core_web_sm`: A small English model trained on web text.
- `en_core_web_trf`: For accuracy, use a transformer-based model.

To use the transformer-based model:
```shell
python -m spacy download en_core_web_trf
```

See [spaCy download method ⩩](https://spacy.io/api/cli#download) and [spaCy models ⩩](https://spacy.io/models/en#en_core_web_sm) for more details.

## 🏁 Start Run

```shell
pytest src/test.py
python src/main.py
python src/get_top_ranked_phrases.py
```

## Features

- **`load_model()`**: Loads the spaCy model. Returns the model. Example: `spacy.load("en_core_web_sm")`
- **`process_text_returns_expected_tuples(nlp, text)`**: Loads the spaCy model, processes text, and returns expected tuples. Example: `[(token, POS, dependency)]`
- **`extract_entities_returns_expected_entity_tuples(nlp, text)`**: Identifies named entities in text and returns expected entity tuples. Example: `[(entity, label)]`
- **`summarize_text_returns_expected_summary(nlp, text)`**: Generates a summary of text by extracting important phrases. Example: 'summary'
- **`get_top_ranked_phrases(text)`**: Extracts top-ranked phrases from text and returns expected phrases. Example: `[(phrase, rank)]`
- **`@pytest.fixture`**
- **`textrank`**
- **`pytextrank`**
- **`pytest`**

## Samples

### `butyrate_text`

```python
butyrate_text = """Trivia: The bacterium Faecalibacterium prausnitzii in the human gut microbiome is responsible for producing butyrate, a short-chain fatty acid.
Explanation: Faecalibacterium prausnitzii utilizes complex carbohydrates, such as dietary fiber, as its primary energy source. Through a fermentation process, it breaks down these carbohydrates into smaller molecules, including butyrate. Butyrate has beneficial effects on gut health, serving as an energy source for colon cells, promoting their growth, maintaining the gut barrier integrity, and reducing inflammation. Faecalibacterium prausnitzii's ability to produce butyrate highlights its importance in maintaining a healthy gut microbiome."""
```

### `geosynchronization_text`

```python
geosynchronization_text = """Trivia: The concept of geosynchronization was first postulated by Arthur C. Clarke.
Explanation: Geosynchronous orbits are orbits around Earth that have an orbital period matching Earth's rotation period. This results in the satellite appearing stationary with respect to a point on Earth's surface. This concept is crucial in space physics and geodesy, as it is used in various applications like communication satellites. Arthur C. Clarke, a British science fiction writer, was the first to postulate this concept, which is why geosynchronous orbits are sometimes referred to as Clarke orbits."""
```

## Roadmap

- Optimize LLM integration
- Extend models
- API development
- Testing
- Dockerization

## Contributing

To contribute, fork the repository, implement changes, run tests, and submit a pull request. We appreciate and support collaborations.

## Notes

- Forgetfulness
- Momentum
- Extraction
- Dependency parsing
- [spaCy evaluate](https://spacy.io/api/cli#evaluate)
- NER
- 🤗 Huggingface transformers
- 🦙 spaCy-LLM
- Memory
- Redis
- System stability

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgements

- [explosion_ai 💥](https://github.com/explosion)
- [@spacy_io 🪐](https://github.com/explosion/spacy-llm)
- [DerwenAI 🌲](https://github.com/DerwenAI)
- [spaCy-pytextrank ⩩](https://spacy.io/universe/project/spacy-pytextrank)
- [rada, tarau @ cs.unt.edu - textrank: bringing order into texts 🗄️](https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf)
