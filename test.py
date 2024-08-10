import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")

# List of predefined words to recognize
predefined_words = {"broken", "high", "low", "rust"}

def analyze_text(text):
    # Process the text
    doc = nlp(text)

    # Tokenization
    tokens = [token.text.lower() for token in doc]  # Convert to lower case for matching
    # print("Tokens:", tokens)

    # Part-of-speech tagging
    pos_tags = [(token.text, token.pos_) for token in doc]
    # print("Parts of Speech:", pos_tags)

    # Named Entity Recognition
    named_entities = [(ent.text, ent.label_) for ent in doc.ents]
    # print("Named Entities:", named_entities)

    # Dependency Parsing
    dependencies = [(token.text, token.dep_, token.head.text) for token in doc]
    # print("Dependencies:", dependencies)

    # Noun Chunks
    noun_chunks = [chunk.text for chunk in doc.noun_chunks]
    print("Noun Chunks:", noun_chunks)

    # Check for predefined words and prompt actions
    found_words = {word for word in predefined_words if word in tokens}
    if found_words:
        print("Predefined Words Found:", found_words)
        for word in found_words:
            prompt_action(word)

def prompt_action(word):
    # Define actions based on recognized words
    actions = {
        "broken": "Action: Inspect the component for damage and replacement.",
        "high": "Action: Check the levels and ensure they are within normal ranges.",
        "low": "Action: Refill or adjust to the correct levels.",
        "rust": "Action: Clean the rusted area and check for further damage."
    }
    # Print the corresponding action for the word
    action = actions.get(word, "No specific action defined.")
    print(f"Prompt for '{word}': {action}")

# Example usage
inspection_text = "The left front tire of the CAT 730 truck shows significant rust and low pressure."
analyze_text(inspection_text)