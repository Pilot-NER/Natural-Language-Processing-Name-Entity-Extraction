# NLP-Approach
Using Natural Language Processing NLTK library to extract information 

Typical information extraction architecture works as follows:

1. **Segment the body** — split the text into an array of sentences
2. **Tokenize** — split each sentence into an array of words
3. **Part of Speech Tagging (POS)** — tag each word with a grammatical label
4. **Chunking** — group and label multi-token sequences

--- 

Applicability of the Information Extraction Architecture
1. We don't really have to segment the body because the text is just a sentence.
2. We need to tokenize the sentence but the sentence is not a complete sentence – it doesn't have a grammatical structure.
3. Similar to the concerns with step 2, the sentence does not have any grammatical structure.
4. Very important in order to extract vendors' names and location.

---

### Approach 1: Named-Entity Recognition
