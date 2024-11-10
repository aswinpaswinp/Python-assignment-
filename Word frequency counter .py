import string

def count_word_frequency(text):
    # Convert the text to lowercase to ensure the counting is case-insensitive
    text = text.lower()
    
    # Remove punctuation using str.translate() and string.punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Split the text into words (split by spaces)
    words = text.split()
    
    # Create a dictionary to store the frequency of each word
    word_frequency = {}
    
    # Loop through the words and count the frequency
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_fr
