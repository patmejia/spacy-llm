import spacy
from pprint import pprint

def process_text(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    result = []
    for token in doc:
        result.append((token.text, token.pos_, token.dep_))
    return result

text = """Trivia: The gut microbiome plays a crucial role in the production of short-chain fatty acids (SCFAs), such as butyrate, through the activity of a bacterium called Faecalibacterium prausnitzii.

Explanation: Faecalibacterium prausnitzii is a commensal bacterium found in the human gut. It is known for its ability to produce significant amounts of butyrate, a short-chain fatty acid. Butyrate is a vital energy source for the cells lining the colon and has been associated with various health benefits.

The production of butyrate by Faecalibacterium prausnitzii is achieved through a fermentation process. This bacterium utilizes complex carbohydrates, such as dietary fiber, as its primary substrate. Through enzymatic reactions, it breaks down these carbohydrates into smaller molecules, including acetate, propionate, and butyrate.

Within the gut, Faecalibacterium prausnitzii possesses specialized enzymes, such as glycoside hydrolases and acetate kinase, which enable it to efficiently metabolize complex carbohydrates. This metabolic pathway ultimately leads to the synthesis of butyrate.

Butyrate has numerous beneficial effects on the gut and overall health. It serves as an energy source for colonocytes, promoting their growth and maintenance. Additionally, butyrate has anti-inflammatory properties and helps to maintain the integrity of the gut barrier. Studies have suggested that a decreased abundance of Faecalibacterium prausnitzii and reduced levels of butyrate production are associated with certain gut disorders, such as inflammatory bowel disease.

Hence, the intricate ability of Faecalibacterium prausnitzii to utilize dietary fiber and produce butyrate highlights its significance in maintaining gut health and underscores the importance of a diverse and balanced gut microbiome."""

result = process_text(text)
print("Text:\n")
print(text)
print("\nResult:\n")
pprint(result[:10])  # Print only the first 10 elements for brevity
print("\nEach element in the result is a 3-tuple (token, part of speech, dependency).")
print(f'The text was processed into {len(result)} such tuples.')



