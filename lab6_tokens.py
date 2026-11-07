
import re
texts = [
    "Welcome to Python programming!",
    "I won't attend the class today.",
    "contact.student@outlook.com",
    "The subject code is CS4944.",
    "",
  "\u0622\u062c \u0645\u0648\u0633\u0645 \u0628\u06c1\u062a \u0627\u0686\u06be\u0627 \u06c1\u06d2"
]
for number, sentence in enumerate(texts, start=1):
    space_tokens = sentence.split()
    pattern_tokens = re.findall(
        r"\b\w+\b", sentence, re.UNICODE
    )
    print("\nExample", number)
    print("Text:", repr(sentence))
    print("Space Based Tokens:", space_tokens)
    print("Total Space Tokens:", len(space_tokens))
    print("Regex Based Tokens:", pattern_tokens)
    print("Total Regex Tokens:", len(pattern_tokens))
try:
    from sentence_transformers import SentenceTransformer
    encoder = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2",
        device="cpu"
    )
    english_texts = [
        "Welcome to Python programming!",
        "I won't attend the class today."
    ]
    print("\nPretrained Model Tokenization")
    for sentence in english_texts:
        pieces = encoder.tokenizer.tokenize(sentence)
        print("\nSentence:", sentence)
        print("Subword Pieces:", pieces)
        print("Number of Pieces:", len(pieces))
except Exception as error:
    print("\nModel tokenizer could not be loaded.")
    print("Error:", error)

