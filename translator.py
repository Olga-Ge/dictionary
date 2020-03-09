import rus_dictionary
print (rus_dictionary.d)
text = "cat"

translate = ""
words = text.split()
for w in words:
    translate = translate + " "+ rus_dictionary.d(w)
print(translate)




