import fiction_dictionary
import argparse
#TODO
#Build out command line arguements
# Add interactive mode with loop for tab
#    Add command keywords to interactive mode
# used to build the command line arguments
def build_cmdline():
	pass


def main():
    option=None
    help_messages('about')
    while not option == 'quit':
    	option=input('Select an option: ')
    	print(option)
    	help_messages(option)





def help_messages(choice="about"):
    '''Print choice and a general help message 
    once choice is made return a function that does what is asked'''
    options_msg='Options: \'Create\' ,\' Add \' , \' Remove\', \'Edit\', \'Save\', \'Import\' \'Quit\''
    if choice =="about":
        print('Welcome, this program creates and saves fictional words and their definitions 	in a searchable form')
        print(options_msg)
        return None
    elif choice =='create':
    	print('If you do not have a current dictionary create one.')
    	print('create <dictionary name>')
    elif choice =='add':
    	print('add a word to the dictionary')
    	print('add <word> <definition>')
    elif choice =='remove':
    	print('delete a word from the dictionary')
    	print(' remove <word>')
    elif choice =='edit':
    	print('change the definition of a word already in the dictionary')
    	print('edit <word> <new definition>')
    elif choice =='save':
    	print('save the dictionary to a json file')
    	print('save')
    elif choice =='import':
    	print('If you do not have a current dictionary import an existing one.')
    	print('import <dictionary name>.json')
    elif choice=='test':
    	print('Run through all unit test in test folder')
    	print('test')
    else:
    	print('Command not found. ')
    	print(options_msg)


if __name__ == "__main__":
    main()