class DuplicateWord(Exception):

    '''
    Raised when a key (word) entry is already present in the dictionary
    '''

    def __init__(self, word, message=None):
        if not message:
            self.message='{0} was already found in the dictionary, please modify the current entry'.format(word)
        else:
            self.message=message

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        if value is None:
            raise ValueError('Exception message was not set')
        self._message=value

