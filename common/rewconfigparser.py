import configparser

class Rewconfigparser(configparser.RawConfigParser):
    # def __init__(self,defaults=None):
    #     super().__init__(self,defaults=None)
    # def optionxform(self, optionstr):
    #     return optionstr

    def __init__(self, defaults=None):
        configparser.RawConfigParser.__init__(self, defaults=None)
    def optionxform(self, optionstr):
        return optionstr

# if __name__ == '__main':
#     rewconfigparser = rewconfigparser()
#     b=rewconfigparser.optionxform('Avb')
#     print(b)
