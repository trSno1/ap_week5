#recatoring means to restructure cod3e without chanfinf its extermna; behavior this helps improve readibility and maintainability.
#importing the functions

from problem_set1 import problem
from problem_set3 import problem_set3
from problem_set4 import problem_set4

from advanced_slicing import advanced_slice





#call the functions
problem()

# an absrat representatation

# # Problem Set 1: Indexing and Slicing Strings
# # Basic Indexing:
# # Given the string magic = 'abracadabra',
# # a. Retrieve the 5th character.
# # b. Retrieve the second to last character.
# # c. Find the first occurrence of the letter 'c'.+
magic = "abracadabra"
fifth_char = magic[4]
second_to_last_char = magic[-2]
first_occurrence_c = magic.find('c')
print (first_occurrence_c) 


# # Advanced Slicing:
# # Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# # a. Extract the letters 'hij'.
# # b. Extract every second letter starting from 'a' to 'm'.
# # c. Reverse the entire string using slicing.

# # Problem Set 2: Extracting Information
# # From Descriptions:
# # Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
name = "John F. Kennedy"
print(name) 
# # Manipulating Words:
# # Given the string info = "Python is fun. Fun is good. Good is subjective.",
# # a. Extract the word 'subjective' without knowing its exact position.
# # b. Extract every third word.
# # c. Reverse the positions of the words, but keep the characters in each word in the same order.

# # Problem Set 3: String Methods
# # Upper & Lower:
# # Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
text = "MAY THE FORCE BE WITH YOU"
lowercase_text = text.lower()
print(lowercase_text)
# # String Joining and Splitting:
# # Given the list motto = ["Make", "haste", "slowly."],
# # a. Convert the list into a single string.
# # b. Now, split the string at every occurrence of the letter 'a'.
motto = ["Make", "haste", "slowly"]
motto_strong = ''.join(motto)
split_motto = motto_strong.split('a')
print = motto
 # Replacing Words:
# # Modify the sentence: "Life is what happens when you are busy making other plans."
# # a. Replace "busy" with "distracted".
# # b. Replace "plans" with "mistakes".

# # Problem Set 4: String Properties and Advanced Operations
# # Repetition:
# # Concatenate the word "Iteration" 7 times.
word = "Iteration"
result = word * 7
print(result)
# # Word Search:
# # Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

# # Length and Count:
# # a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# # b. Count the number of times the letter 'i' appears in the same word/phrase.
