# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.
text = "abracadabra"
result = text
print(result[4])
# b. Retrieve the second to last character.
print (result [-2])
# c. Find the first occurrence of the letter 'c'.
print (text.find('c'))
# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
#                              01234567891234567891234567
# a. Extract the letters 'hij'.
alphabet = 'abcdefghijklmnopqrstuvwxyz'
substring = text.find('hij')
print(substring)
substring = alphabet[7:9]
# b. Extract every second letter starting from 'a' to 'm'.
substring1 = alphabet[:13]
result1= substring1 [::2]
print (result1)
# c. Reverse the entire string using slicing.
print (result[::-1])
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
string = "Ask not what your country can do for you — ask what you can do for your country. - John f. Kennedy"
1234567
print (string [83:98])
# Manipulating Words
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
info = "Python is fun. Fun is good. Good is subjective."
print (info.find ('subjective'))
# b. Extract every third word.
words = info.split()
every_third_word = words[2::3]
print("Every third word:", every_third_word)

# c. Reverse the positions of the words, but keep the characters in each word in the same order.
words = info.split()
reversed_words = words[::-1]
reversed_sentence = ' '.join(reversed_words)
print("Reversed words:", reversed_sentence)

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
text = "MAY THE FORCE BE WITH YOU."
lowercase_text = text.lower()
print(lowercase_text)

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
motto = ["Make", "haste", "slowly."]
single_string = ' '.join(motto)
print(single_string)

# b. Now, split the string at every occurrence of the letter 'a'.
split_string = single_string.split('a')
print("Joined String:", single_string)
print("Split String:", split_string)
 
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
yes = "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
modified_sentence = yes.replace("busy", "distracted")
print (modified_sentence)
# b. Replace "plans" with "mistakes".
modified_sentence_two = modified_sentence.replace("plans", "mistakes" )
print (modified_sentence_two)

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
ok = "Iteration "
result = ok * 7
print(result)

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
no = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
print (no.find ("moonlight"))
# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
phrase = "Supercalifragilisticexpialidocious"
#         1234567890123456789012345678901234
number_of_characters = len(phrase)
print("Number of characters:", number_of_characters)

# b. Count the number of times the letter 'i' appears in the same word/phrase.
characters = phrase.count("i")
print ("Number of i's is: ",  characters)