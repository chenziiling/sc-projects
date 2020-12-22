"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
words = []                    # A global list store all words in dictionary
ans_list = []                 # count how many vocabulary you find in anagram


def main():
    global ans_list
    read_dictionary()
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        user = input('Find anagrams for: ')
        if user == EXIT:
            break
        else:
            user = user.lower()
            find_anagrams(user)
            print(ans_list)  # correct from kelly
            print(len(ans_list))  # correct from kelly
            ans_list = []  # correct from kelly # clear the list to search the next word


def read_dictionary():
    global words
    with open(FILE, 'r') as f:
        for line in f:
            w = line.split()
            word = w[0].strip()
            words.append(word)


def find_anagrams(s):
    """
    :param s:string, user's word
    :return:every vocabulary that consist of letters from s
    """
    find_anagrams_helper(s, [])


def find_anagrams_helper(s, current):
    global ans_list  # correct from kelly
    if len(current) == len(s):
        new_w = ''
        for j in range(len(s)):
            new_w += s[current[j]]
            if not has_prefix(new_w):
                j = len(s)
            if new_w in words and new_w not in ans_list and len(new_w) >= len(s):  # correct from kelly
                ans_list.append(new_w)
                print('Found: ', new_w)
                print('Searching...')
    else:
        for i in range(len(s)):
            if i not in current:
                # choose
                current.append(i)
                # explore
                find_anagrams_helper(s, current)
                # un-choose
                current.pop()


def has_prefix(sub_s):
    """
    :param sub_s:string, to be check if sub_s is the beginning of the vocabulary in words or not
    :return:boolean, to check if sub_s is the beginning of the vocabulary in words or not
    """
    for w in words:
        if w.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
