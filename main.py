def main():
    
    #defines the path to the book and calls the get_book_text() function to set the text variable
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    #calls the word_count() and get_letter_counts() functions
    total_words = word_count(text)
    letter_counts = get_letter_counts(text)

    #prints the final analysis as a report
    print(f"--- Begin report of {book_path} ---")
    print(f"{total_words} words found in the document")
    print("")
    #this loop indexes the sorted list and prints a line for each with the letter and number values
    for i in range(0, len(letter_counts)):
        letter = letter_counts[i][0]
        number = letter_counts[i][1]
        print(f"The '{letter}' character was found {number} times")

#function as given in the project description to convert the entire book text into a single string variable 
def get_book_text(path):
    with open(path) as f:
        return f.read()

#splits the text string into individual words, returns the length of the resulting list as a word count value
def word_count(text):
    words = text.split()
    return len(words)

#function to count how many of each individual character appears in the given text and return a sorted list  
def get_letter_counts(text):

    #defines the variables used further down
    #alphabet restricts the characters being counted to just lower case letters
    #all_counts is an empty dictionary to contain the count results
    #lower_text is the source text converted to all lower case letters
    #sorted_counts is an empty list to hold the final sorted letter counts as tuples
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    all_counts = {}
    lower_text = text.lower()
    sorted_counts = [] 

    #iterates through each letter in the alphabet list and counts how many times it appears in the lowercase text
    for letter in alphabet:
        this_count = lower_text.count(letter)
        all_counts[letter] = this_count
    
    #sorts the previous output into a list sorted by values starting highest first
    for i in sorted(all_counts, key = all_counts.get, reverse = True):
        sorted_counts.append((i, all_counts[i]))
    return sorted_counts

main()