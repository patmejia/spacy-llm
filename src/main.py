import spacy
from pprint import pprint

# Load the Spacy model globally so it only needs to be loaded once
nlp = spacy.load("en_core_web_sm")

def process_text(text):
    doc = nlp(text)
    return [(token.text, token.pos_, token.dep_) for token in doc]


text = """Trivia: The bacterium Faecalibacterium prausnitzii in the human gut microbiome is responsible for producing butyrate, a short-chain fatty acid.

Explanation: Faecalibacterium prausnitzii utilizes complex carbohydrates, such as dietary fiber, as its primary energy source. Through a fermentation process, it breaks down these carbohydrates into smaller molecules, including butyrate. Butyrate has beneficial effects on gut health, serving as an energy source for colon cells, promoting their growth, maintaining the gut barrier integrity, and reducing inflammation. Faecalibacterium prausnitzii's ability to produce butyrate highlights its importance in maintaining a healthy gut microbiome."""

result = process_text(text)
print("Text:\n")
print(text)
print("\nResult:\n")
pprint(result[:3])  # print upper 3 elements
print("\nEach element in the result is a 3-tuple (token, part of speech, dependency).")
print(f'The text was processed into {len(result)} such tuples.')



