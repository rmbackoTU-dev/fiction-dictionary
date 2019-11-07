from fict_dict.client import  fict_dict_cli_access
import argparse
#TODO
#Build out command line arguements and parameters
#map to fict_dict_cli_access
#run each flag and parameter at least once

def main():

    cliClient=fict_dict_cli_access()
    parser=argparse.ArgumentParser(description="Fiction dictionary allows users to create custom dictionaries"
                                               +" using JSON files \n The basic syntax is:"+
                                                "fictdictCli <option> [option parameters]" )
    subparsers=parser.add_subparsers(title="commands", dest='command')
    #Use sub parsers to parser arguments for each command
    create_subparser=subparsers.add_parser("create", help="Creates a new dictionary with the name specified.\n"+
                                       "Syntax: fictdictCli create <dictionary name>  <destination file>")
    create_subparser.add_argument('dictionary_name', action='store', type=str)
    create_subparser.add_argument('destination_file', action='store', type=str)
    insert_subparser=subparsers.add_parser('insert',  help="Inserts a word into the dictionary file specified.\n"+
                        "Syntax: fictdictCli insert <destination file> <word> <definition>")
    insert_subparser.add_argument('destination_file', action='store', type=str)
    insert_subparser.add_argument('word', action='store', type=str)
    insert_subparser.add_argument('definition', action='store', type=str)
    delete_subparser=subparsers.add_parser("delete",  help="Deletes a word from the dictionary file specified \n "+
                        "Syntax: fictdictCli delete <destination file> <word>")
    delete_subparser.add_argument('destination_file', action='store', type=str)
    delete_subparser.add_argument('word', action='store', type=str)
    edit_subparser=subparsers.add_parser("edit",  help="Edits the definition of the word specified from the dictionary file specifed \n"+
                        "Syntax: fictdictCli edit <destination file> <word> <definition>")
    edit_subparser.add_argument('destination_file', action='store', type=str)
    edit_subparser.add_argument('word', action='store', type=str)
    edit_subparser.add_argument('definition', action='store', type=str)
    add_subparser=subparsers.add_parser("add",  help="Adds two dictionary files dictionary content together, and save them in the destination file"+
                               "specified.\n  Syntax: fictDictCli add <destination file> <source file>")
    add_subparser.add_argument('source_file', action='store', type=str)
    add_subparser.add_argument('destination_file', action='store', type=str)
    diff_subparser=subparsers.add_parser("diff",  help="Takes the difference of two dictionary files, and saves them in the destination file"+
                        "specified. \n Syntax: fictDictCli diff <destination file> <source <file>")
    diff_subparser.add_argument('source_file', action='store', type=str)
    diff_subparser.add_argument('destination_file', action='store', type=str)
    copy_subparser=subparsers.add_parser("copy", help="Copies a dictionary from the source dictionary file specified into the destination dictionary"
                                "file.\n  Syntax: fictDictCli copy <destination file> <source file> ")
    copy_subparser.add_argument('source_file', action='store', type=str)
    copy_subparser.add_argument('destination_file', action='store', type=str)

    '''
    Print options
    Print word
    Print Dictionary
    '''
    print_subparser=subparsers.add_parser("print", help="Prints a word specified from the file specified, or"
                                 "prints te whole dictionary from the source file specified\n" +
                                 "Syntax: fictDictCli print <source file> [word] ")
    print_subparser.add_argument('source_file', action='store', type=str)
    print_subparser.add_argument('word', action='store', nargs='?', type=str, default='')

    '''
    Search Options
    Search regular,
    left-to-right, 
    right-to-left
     print definitions
    '''
    search_subparser=subparsers.add_parser("search", help="Search a dictionary file using a left-to-right search"+
                         "right-to-left search, or both for a specified word or grouping of letters.\n"+
                         "-l left-to-right search\n"+
                         "-r right-to-left search \n"+
                         "-b use both left-to-right, and right-to-left (b is assumed by default)\n"+
                         "-pd print the definitions of the results\n"+
                         "Syntax: fictDictCli search <-l|-r|-b> [-p]  <source file> <search_term>")
    choices=search_subparser.add_mutually_exclusive_group()
    choices.add_argument('--left-to-right','-l', action='store_true')
    choices.add_argument('--right-to-left','-r', action='store_true')
    choices.add_argument('--both','-b', action='store_true', default=True)
    search_subparser.add_argument('source_file', action='store', type=str)
    search_subparser.add_argument('search_term', action='store', type=str)
    search_subparser.add_argument('-p', action='store_true', required=False)
    args=parser.parse_args()
    if args.command == "create":
        if (args.dictionary_name is None or args.destination_file is None):
            parser.error("Arguments for create have not been correctly specified.")
        else:
            dictName=args.dictionary_name
            destFile=args.destination_file
            print("Creating dictionary " +dictName+ " at file "+destFile)
            cliClient.createDictionary(dictName, destFile)

    elif args.command == "insert":
        if(args.destination_file is None or args.word is None or args.definition is None):
            parser.error("Arguments for insert have not been correctly specified.")
        else:
            destFile=args.destination_file
            word=args.word
            definition=args.definition
            print("Inserting "+word+" defined as "+ definition+ " into dictionary located at "+
                  destFile)
            cliClient.addWord(destFile, word, definition)
    elif args.command == "delete":
        if(args.destination_file is None or args.word is None):
            parser.error("Arguments for delete have not been correctly specified.")
        else:
            destFile=args.destination_file
            word=args.word
            print("Deleting "+word+" from the dictionary file "+destFile)
            cliClient.deleteWord(destFile, word)
    elif args.command == 'edit':
        if(args.destination_file is None or args.word is None or args.definition is None):
            parser.error("Arguments for edit have not been correctly specified.")
        else:
            destFile=args.destination_file
            word=args.word
            definition=args.definition
            print("Editting the word "+word+", and changing the definition to "+definition+
                  " in the dictionary file "+destFile)
            cliClient.editDictionary(destFile, word, definition)
    elif args.command == 'add':
        if(args.destination_file is None or args.source_file is None):
            parser.error("Arguments for add have not been correctly specified")
        else:
            destFile=args.destination_file
            srcFile=args.source_file
            print("Adding the dictionary located at"+srcFile+" to "+destFile)
            cliClient.addDictionaries(destFile, srcFile)
    elif args.command == 'diff':
        if(args.destination_file is None or args.source_file is None):
            parser.error("Arguments for differentiate have not been correctly specified")
        else:
            destFile=args.destination_file
            srcFile=args.source_file
            print("Storing the difference between "+destFile+" and "+srcFile+" in "+destFile)
            cliClient.diffDictionaries(destFile, srcFile)
    elif args.command == 'copy':
        if(args.destination_file is None or args.source_file is None):
            parser.error("Arguments for copy have not been correctly specified")
        else:
            destFile=args.destination_file
            srcFile=args.source_file
            print("Copying the dictionary from"+srcFile+" to "+destFile)
            cliClient.copyDictionaries(destFile, srcFile)
    elif args.command == 'print':
        if(args.source_file is None):
            parser.error("Arguments for print have not been correctly specified")
        else:
            destFile=args.source_file
            if(args.word != ''):
                word=args.word
                print('Printing the definition of '+word+ ' from '+destFile)
                word_to_print=cliClient.get_word_Str(destFile, word)
                print(word_to_print)
            else:
                print('Printing dictionary found in '+destFile)
                dict_to_print=cliClient.get_dict_Str(destFile)
                print(dict_to_print)
    elif args.command == 'search':
        if(args.source_file is None or args.search_term is None):
            parser.error("Specify a dictionary file to search from")
        else:
            dictFile=args.source_file
            search_term=args.search_term
            if(args.left_to_right):
                search_method='left_to_right'
            elif (args.right_to_left):
                search_method='right_to_left'
            else:
                search_method='both'
            print("Searching for "+search_term+" using "+search_method+" on "+dictFile)
            if (args.p):
                print("Printing out search matchs and definitions...")
                print_list=[]
                if(search_term == 'left_to_right'):
                    printList=cliClient.searchDictLeftDef(dictFile, search_term)
                elif(search_term == 'right_to_left'):
                    printList=cliClient.searchDictRightDef(dictFile, search_term)
                else:
                    printList=cliClient.searchDictWithDef(dictFile, search_term)
                for i in printList:
                    print(i)
            else:
                print("Printing out search matchs")
                if(search_term == 'left_to_right'):
                    printList=cliClient.searchLeftDict(dictFile, search_term)
                elif(search_term == 'right_to_left'):
                    printList=cliClient.searchRightDict(dictFile, search_term)
                else:
                    printList=cliClient.searchDict(dictFile, search_term)
                for i in printList:
                    print(i)
    else:
        parser.print_help()


    
if __name__ == "__main__":
    main()