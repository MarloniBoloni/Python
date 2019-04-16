f = open("readin.txt", "r+")  #Draws the file in 
print(f.read())             #Prints the file
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
print (word_count ('Three Tomatoes were walking down the street. Mama Tomato, Papa Tomato and Baby Tomato. Baby Tomato was lacking behind. Papa Tomato went back to Baby Tomato and squished him. And said "ketchup".'))
