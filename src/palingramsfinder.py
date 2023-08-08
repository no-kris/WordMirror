"""Find palingrams from a wordlist textfile."""
import fileloader
import dictionaryclean

word_list = fileloader.load('wordlist.txt')
word_list_clean = dictionaryclean.clean()

def find_palingrams():
    """Find palingrams from a dictionary of single words.
    
    Returns:
        List of palingram pairs.
    """
    palingram_list = []
    words = set(word_list_clean)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        # Discard single letter words
        if end > 1:
            for i in range(end):
                # Check if the original word and its reverse are palindromes
                # on each iteration
                # and check if the substring of rev_word is in the word list
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    palingram_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words:
                    palingram_list.append((rev_word[:end-i], word))
    return palingram_list

def print_palingrams(palingrams):
    """Print all palingram words found from text file."""
    for first, second in palingrams:
        print(f'{first} {second}')
    print(f'Number of palingrams: {len(palingrams)}')
    print(f'Proportion of words in text file that are palingrams: {len(palingrams) / len(word_list_clean)}')

if __name__ == "__main__":
    palingrams_list = find_palingrams()

    sort_palingrams = sorted(palingrams_list)

    print_palingrams(palingrams_list)


