import json, sys
class fiction_dictionary:
    
    '''
    Library used to provide quick shortcut searchable dictionary using JSON to store and find words
    commonly found in fantasy and sci-fi books, which are only used in the context of the book, but not in the
    books native lanuage
    '''
    # initiate the class with the name of the dictionary and the dictionary itself.
    # If not passed, pass an empty dictionary.
    def __init__(self, dict_name, fict_dict=None):
        self.dict_name=dict_name
        if fict_dict == None:
            self.fict_dict={}
        else:
            self.fict_dict=fict_dict

    def write_dict_to_json():
        filename=self.dict_name+'.json'
        with open(filename, 'w') as fw:
            json.dump(self.file_dict, fw)
        
    def add_word(word, definition):
        self.fict_dict[word]=definition

    def remove_word(word):
        del self.fict_dict[word]

    def import_json_dict(json_file):
        pass
   
    def set_definition(word, new_def):
        if not self.fict_dict[word]:
            print('The word', word, 'is not in the fiction dictionary!')
        else:
            self.fict_dict[word]=new_def

    def search_word(word_iterator):
        pass
