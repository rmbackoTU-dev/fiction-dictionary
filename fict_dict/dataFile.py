import os, sys, datetime
from pathlib import Path
import json


# TODO
'''
For a list of dictionaries first check if the dictionary exist in the list before setting it
'''


class DataFile:

    # directory does not get to be choose by use
    topLevelDir = Path(os.path.dirname(os.path.abspath(__file__))).parent

    # context is the current dictionary that the program is writing to
    def __init__(self):
        self.temp_file = 'temp.json'
        self.temp_abs = os.path.join(self.topLevelDir, 'dictionaries', self.temp_file)
        self.currentContext = {}
        self.dict_collection = {}
        
    def set_filename(self, filename):
        self.temp_file = filename
        self.temp_abs = os.path.join(self.topLevelDir, 'dictionaries', self.temp_file)
    
    # This should only be done initially. it will overwrite the current context
    def set_new_dictionary(self, dict_of_list, dict_name):
        self.dict_collection[dict_name] = dict_of_list
        self.currentContext = dict_of_list

    # Update file dumps the current dictionary the user is writing to a temp file
    def update_file(self):
        pass

    # delete file deletes the current temp file, may attempt to call this after some condition automatically
    def delete_file(self):
        pass

    # create file creates a new temp file if one does not exist, assigns the context dictionary
    # to the file
    # if one exist set the context to the first item
    # Always should return a dictionary : including current context and Error passed if any
    def create_file(self):
        data_list = {"currentContext": self.currentContext}
        try:
            if os.path.isfile(self.temp_abs):
                with open(self.temp_abs, 'r') as f:
                    data_list=json.load(f)
                    # Get the first dictionary off the list and set it as the context if the file exist
                    self.currentContext = next(iter(data_list.values()))
                    return data_list
            else:
                raise FileNotFoundError
        except (FileNotFoundError, IOError): 
            print(": Creating a new temp file: ")
            try:
                if data_list["currentContext"]:
                    with open(self.temp_abs, 'a+') as f:
                        json.dump(data_list, f)
                        return data_list
                else:
                    raise ValueError
            except ValueError:
                val_error = "No default dictionary context was set create a populated dictionary first"
                data_list["Error0"] = val_error
                print(data_list["Error0"])
                return data_list

    # print dictionary which is pointed to by key
    def print_current(self, key):
        pass

    # set Context sets the current dictionary to the dictionary pointed to by the key
    def set_context(self, key):
        pass

    # Check to see if file contains a key
    def __contains__(self, key):
        try:
            found = False
            if not os.file.exists(self.temp_abs):
                return found
            else:
                with os.open(self.temp_abs, 'r') as temp:
                    file_dict = json.load(self.temp_abs)
                    for k in file_dict.keys():
                        if k == key:
                            found = True
                    temp.close()
                return found
        except IOError:
            print("Error while reading temporary file")
            return found




