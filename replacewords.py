def word_replacement():
    str = "Moi, minun nimi on Ugyen Lama. "
    to_replace = input("Choose word to replace in the sentence: ")
    replace_with = input("Enter the word to replace with: ")
    print(str.replace(to_replace, replace_with))
    
word_replacement()
