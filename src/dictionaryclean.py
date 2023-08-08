"""Remove single letter words from text file, except for 'a' or 'i'"""
import fileloader

word_list = fileloader.load('wordlist.txt')

allowable = ('a', 'i')

def clean():
    """Remove single letters from given word list
    
    Arguments:
        Text file to work on

    Returns:
        Word list of omittted single letter words
    """
    word_list_clean = []
    for word in word_list:
        if len(word) > 1: 
            word_list_clean.append(word)
        elif len(word) == 1 and word in allowable:
            word_list_clean.append(word)
        else:
            continue
    return word_list_clean
