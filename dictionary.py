d = {"eng-spa": {"yes":"si"}, "eng-deu":{"yes":"ja"}}
print (d["eng-deu"] ["yes"])
print(d["eng-spa"] ["yes"])

# for the key you normally use the string

punctuation2 = ",.;:!?'""[]{}/-*<>"
def common_words(file_name):
    fd = open(file_name, "r")
    d = {}
    for line in fd: #line by line reading - from now on do it for every linr of text in a file
        for c in punctuation2: #each carachter in punctuation2
            line = line.replace(c, " ") #result is a line of text without punctuation
        words = line.split() #why we need split? we are splitting by space each word
        for word in words: #going through each word one by one
            if word in d: #start with empty dictionary
                d[word] += 1 #if the word in dictionary? the key of first word + 1
            else:
                d[word] = 1 #the key of word appearing first time is always 1

        # d={"Harry":10, "Potter": 50} harry - key, 10 - value; created a list of these values.
    values = list(d.values()) #get the values from the dictionary - only takes the values
    values.sort(reverse=True) #sort from biggest to smallest

    # values = [50, 10]
    #we know the list, but don't know what are the keys to the 10 biggest values

    common = []
    for numbers in values[:10]: #first 10 elements from values - 0 to 9 - we are checking
        for keys in d: # is the value for this key 50? yes, it is Harry
            if d[keys] == numbers:
                common.append((keys, numbers))
    print("the most common words are:")
    for i in common:
        print(i[0], i[1], "times")
common_words("hp")

common_words("Moby")

# when you want to use someone else's code, use import. It becomes a module for you