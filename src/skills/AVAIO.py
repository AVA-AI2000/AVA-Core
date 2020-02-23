class TextIO:
    def write(self, message):
        print('AVA> ' + message)

    def read(self):
        message = input('> ').lower()
        return message
