import spacy
from pprint import pprint


def load_model():
    return spacy.load("en_core_web_sm")


def process_text_returns_expected_tuples(nlp, text):
    doc = nlp(text)
    return [(token.text, token.pos_, token.dep_) for token in doc]


def extract_entities_returns_expected_entity_tuples(nlp, text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]


def display_results(text):
    nlp = load_model()
    result = process_text_returns_expected_tuples(nlp, text)
    print("Text:\n")
    print(text)
    print("\nResult:\n")
    pprint(result[:3])  
    print("\nEach element in the result is a 3-tuple (token, part-of-speech tag, dependency tag).")
    print(f'The text was processed into {len(result)} such tuples.')
    print("\n\n")
    result = extract_entities_returns_expected_entity_tuples(nlp, text)
    print("Text:\n")
    print(text)
    print("\nResult:\n")
    pprint(result[:5])
    print("\nEach element in the result is a 2-tuple (entity, entity type).")
    print(f'The text was processed into {len(result)} such tuples.')
    print("\n\n")


if __name__ == "__main__":
    butyrate_text = """Trivia: The bacterium Faecalibacterium prausnitzii in the human gut microbiome is responsible for producing butyrate, a short-chain fatty acid.
    Explanation: Faecalibacterium prausnitzii utilizes complex carbohydrates, such as dietary fiber, as its primary energy source. Through a fermentation process, it breaks down these carbohydrates into smaller molecules, including butyrate. Butyrate has beneficial effects on gut health, serving as an energy source for colon cells, promoting their growth, maintaining the gut barrier integrity, and reducing inflammation. Faecalibacterium prausnitzii's ability to produce butyrate highlights its importance in maintaining a healthy gut microbiome."""
    display_results(butyrate_text)
