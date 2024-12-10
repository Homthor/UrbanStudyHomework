def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for i in range(len(other_words)):
        #other_words = list(other_words)          задумка на то чтобы не запутаться прописывать методы lower в проверках
        #other_words[i] = other_words[i].lower()  но тогда пострадает целостность изначальных данных
        if root_word in other_words[i].lower():
            same_words.append(other_words[i])
        elif other_words[i].lower() in root_word:
            same_words.append(other_words[i])
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)
