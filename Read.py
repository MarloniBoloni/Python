f = open("readin.txt", "r+")  #Draws the file in 
print(f.read())             #Prints the file
def word_count(str):
    counts = dict()         #Counting Words in a String
    words = str.split()     #Spliting the words in that String 

    for word in words:
        if word in counts:
            counts[word] += 1     #For each word repeated, increment the number after 1
        else:
            counts[word] = 1      #For each word, number it 1

    return counts                 #Return the results
print (word_count ('Three Tomatoes were walking down the street. Mama Tomato, Papa Tomato and Baby Tomato. Baby Tomato was lacking behind. Papa Tomato went back to Baby Tomato and squished him. And said "ketchup".'))
