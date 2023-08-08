"""
Find if a word, from a dictionary file, is a palindrome.
"""
import fileloader

word_list = fileloader.load('wordlist.txt')

def find_palindromes():
    """Add all palindromes from dictionary list to a new list.
    
    Arguments:
        Dictionary file name.
    
    Returns:
        List of strings.
    """
    palindrome_list = []

    for word in word_list:
        if len(word) > 1 and word == word[::-1]:
            palindrome_list.append(word)

    return palindrome_list

def print_palindromes(palindrome_list):
    """Print all palindromes from a list.

    Arguments:
        List of strings.
    """
    print(*palindrome_list, sep='\n')
    print(f'\nNumber of palindromes found: {len(palindrome_list)}')
    print(f'Proportion of words in text file that are palindromes: {len(palindrome_list) / len(word_list)}')

if __name__ == "__main__":
    list_of_palis = find_palindromes()
    print_palindromes(list_of_palis)
