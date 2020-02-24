class TextIO:
    def write(self, message, ai={'name': 'AVA'}):
        messages = message.split('\n')
        for mes in messages:
            print(ai['name'] + '> ' + mes)

    def read(self):
        message = input('> ').lower()
        return message
