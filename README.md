# LLMs in SpaCy: enables NLP pipelines

The advantages of incorporating Large Language Models (LLMs) in Natural Language Processing (NLP) tasks and demonstrates the synergistic combination of spaCy's components, which utilize supervised learning or rule-based methodologies, with LLM-powered components.

## Installation

Installation for macOS/OSX,ARM/M1,`conda`,CPU, virtual env, English, efficiency.

For other installation options, see [install spaCy ](https://spacy.io/usage#quickstart).

step1: env setup:

```
conda create --name spacy-llm
conda activate spacy-llm
```

step2: install commands:

```
conda install -c conda-forge spacy
python -m spacy download en_core_web_sm
```

> `en_core_web_sm` is a small English model pipeline trained on web text.

step3: test installation:

```
python -m spacy validate
```

## Usage

```
# ---- wip ----
2. Installation with extra models:

```

python -m spacy download en_core_web_sm en_core_web_md en_core_web_lg

```

3. Installation with extra dependencies:

```

pip install spacy[lookups,transformers]

```

4. Conda installation:

```

conda install -c conda-forge spacy

```

5. Upgrading spaCy:

```

pip install -U spacy
python -m spacy validate

```

6. Running spaCy with GPU:

```

pip install -U spacy[cuda113]
import spacy
spacy.prefer_gpu()
nlp = spacy.load("en_core_web_sm")

```

7. Compiling spaCy from source:

```

python -m pip install -U pip setuptools wheel
git clone https://github.com/explosion/spaCy
cd spaCy
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
pip install --no-build-isolation --editable .

```

8. Building an executable:

```

git clone https://github.com/explosion/spaCy
cd spaCy
make

```

9. Running tests:

```

python -m pytest --pyargs spacy
python -m pytest --pyargs spacy --slow

```

```
