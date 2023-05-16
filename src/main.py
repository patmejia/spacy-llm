import spacy
import pytextrank
from pprint import pprint


def load_model():
    return spacy.load("en_core_web_sm")


def process_text(nlp, text):
    return nlp(text)


def process_text_returns_expected_tuples(nlp, text):
    doc = process_text(nlp, text)
    return [(token.text, token.pos_, token.dep_) for token in doc]


def extract_entities_returns_expected_entity_tuples(nlp, text):
    doc = process_text(nlp, text)
    return [(ent.text, ent.label_) for ent in doc.ents]


def summarize_text_returns_expected_summary(nlp, text):
    doc = process_text(nlp, text)
    if 'textrank' not in nlp.pipe_names:
        nlp.add_pipe("textrank")
    doc = nlp(text)
    return [str(sent) for sent in doc._.textrank.summary(limit_phrases=15, limit_sentences=5)]

        
def print_results(text, result, result_type, result_description):
    print("Text:\n")
    print(text)
    print("\nResult:\n")
    pprint(result[:5])
    print(f"\nEach element in the result is a {result_description}.")
    print(f'The text was processed into {len(result)} such {result_type}.\n\n')


def display_results(text):
    nlp = load_model()
    operations = {
        'tuples': {
            'function': process_text_returns_expected_tuples,
            'description': '3-tuple (token, part-of-speech tag, dependency tag)'
        },
        'entity tuples': {
            'function': extract_entities_returns_expected_entity_tuples,
            'description': '2-tuple (entity, entity type)'
        },
        'sentences': {
            'function': summarize_text_returns_expected_summary,
            'description': 'list of sentences that summarize the text'
        }
    }

    for result_type, operation in operations.items():
        result = operation['function'](nlp, text)
        print_results(text, result, result_type, operation['description'])


if __name__ == "__main__":
    butyrate_text = """Trivia: The bacterium Faecalibacterium prausnitzii in the human gut microbiome is responsible for producing butyrate, a short-chain fatty acid.
    Explanation: Faecalibacterium prausnitzii utilizes complex carbohydrates, such as dietary fiber, as its primary energy source. Through a fermentation process, it breaks down these carbohydrates into smaller molecules, including butyrate. Butyrate has beneficial effects on gut health, serving as an energy source for colon cells, promoting their growth, maintaining the gut barrier integrity, and reducing inflammation. Faecalibacterium prausnitzii's ability to produce butyrate highlights its importance in maintaining a healthy gut microbiome."""
    display_results(butyrate_text)
