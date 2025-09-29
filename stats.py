
def count_words(filepath):
    count = 0
    with open(filepath) as file:
        content = file.read()
        content = str(content)
        words = content.split()
        
    count = len(words)
    return count

def count_carackters(filepath):
    count_dict = {}
    with open(filepath) as file:
        content = file.read()
        content = str(content)
        words = content.split()
        for word in words:
            for i in range(len(word)):
                
                if word[i].lower() in count_dict:
                    new_count = count_dict[word[i].lower()] + 1
                    count_dict[word[i].lower()] = new_count
                else:
                    count_dict.update({word[i].lower(): 1})
    return count_dict