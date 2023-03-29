#!/usr/bin/env python3

import random
import json
from os.path import exists
import tarfile
import sys

class BrainWorms():
    def __init__(self):

        base_name = 'markov_2gram_riks'
        self.archive_name = base_name+'.tar.bz2'
        self.json_name = base_name+'.json'

        good_exit = self.handle_files()
        if not good_exit:
            return sys.exit(1)

        self.terminators = ('.', ',', '!', '?')

        with open(self.json_name, 'r') as f:
            self.dict = json.load(f)
    
    def handle_files(self):
        """Makes sure that the files are in place. Expects a 'markov_2gram_riks'
        file of type 'tar.bz2' or 'json' in the present folder."""
        if exists(self.archive_name) and not exists(self.json_name):
            with tarfile.open(self.archive_name) as archive_file:
                archive_file.extractall()
            if not exists(self.json_name):
                print('Something went wrong. No json file detected after extraction.')
                return False
        if not exists(self.archive_name) and not exists(self.json_name):
            print('No json or archive file found.')
            print("This project should have come with a file named 'markov_2gram_riks.tar.bz2', please put it in the present folder.")
            return False
        return True

    def generate_comment(self):
        """Generates a string containing a comment."""
        # self.dict has the structure of:
        # self.dict = {'word1': {'word2': ['list', 'of', 'words'], ...}, ...}
        # specifying 'word1' and 'word2' hence provide a list from which
        # we can select the next word in the chain.

        # There are two special tokens, '[START]' and '[END]'. To start
        # a chain we select a random word among the keys of the dictionary
        # that corresponds to the keyword '[START]':
        current_word = '[START]'
        next_word = random.choice(list(self.dict[current_word].keys()))
        # and the randomly chosen starting word 'next_word' helps us select
        # the next word:
        final_word = random.choice(self.dict[current_word][next_word])

        # To avoid some starts have no chance of being diverse, we shuffle
        # the word selection for a bit
        while len(self.dict[current_word][next_word]) < 2 or len(self.dict[current_word].keys()) < 2 or final_word == '[END]':
            next_word = random.choice(list(self.dict[current_word].keys()))
            final_word = random.choice(self.dict[current_word][next_word])
        
        # We store the comment we are building here:
        new_comment = ''

        # Start generating the comment
        while True:
            # Since we start on the special token '[START]', we begin
            # by shifting the actual first word of the comment to be 
            # the current word, hence also preparing for the next step
            current_word, next_word = next_word, final_word

            # Handle some special cases when the chain breaks or
            # terminates. We will assist it in terminating properly by
            # adding the selecting the special token '[END]'.
            final_word = self.dict.get(current_word)
            if final_word is None:
                final_word = ['[END]']
            else:
                final_word = final_word.get(next_word)
                if final_word is None:
                    final_word = ['[END]']
            final_word = random.choice(final_word)

            # Add the current word to the comment
            new_comment += current_word

            # Looking forward, if the next word is not a terminator, e.g. 
            # '.', it is a word, and we should add a space.
            if not next_word in (*self.terminators, '[END]'):
                new_comment += ' '

            # If the next word is the special token to end the chain, we
            # will terminate
            if next_word == '[END]':
                break

        return new_comment

if __name__ == '__main__':
    n = 0
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if not arg.isdigit():
            print("Usage: brainworms.py [n]\n\n Args:\n\tn: Number of comments to print. Zero gives unlimited comments, interactively. Default: 0.")
            sys.exit(0)
        else:
            n = int(arg)

    brain_worms = BrainWorms()
    if n > 0:
        print('\n----------------------------------------\n')
        for _ in range(n):
            comment = brain_worms.generate_comment()
            print(comment)
            print('\n----------------------------------------\n')
    else:
        print('\n----------------------------------------\n')
        while True:
            comment = brain_worms.generate_comment()
            print(comment)
            rep = input('\n--- [Enter] för nästa, "a" för Avbryt --\n')
            if rep == 'a':
                break
    
