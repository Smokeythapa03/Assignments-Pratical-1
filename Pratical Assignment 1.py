# Define a function to count word frequency in a given text
def count_word_frequency(text):
    # Initialize an empty dictionary to store word frequencies
    word_frequency = {}
    # Split the input text into individual words using space as a delimiter
    words = text.split()
    # Iterate through each word in the list of words     
    for word in words:
        # Check if the word is already in word_frequency dictionary
        if word in word_frequency:
            # If it's in the dictionary, increment its count by 1
            word_frequency[word] += 1
        else:
            # If it's not in the dictionary, add it with a count of one
            word_frequency[word] = 1
    # Return the dictionary containing word frequencies    
    return word_frequency

# Example usage: Count word frequency in a given text
text = "My name is Leela Thapa"
frequency = count_word_frequency(text)
print(frequency)
