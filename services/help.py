from .html_generator import HTML_Generator
commands = [
    ['MAC',['MAC get']],
    ['APP',['APP get','APP close <ID>']],
    ['PROCESS',['PROCESS get','PROCESS close <ID>']],
    ['SCREEN',['SCREEN screenshot','SCREEN record']],
    ['KEYLOGGER',['KEYLOGGER get']],
    ['REGISTRY',[
        'REGISTRY get value',
        'REGISTRY edit value',
        'REGISTRY delete value',
        'REGISTRY get key',
        'REGISTRY delete key'
    ]],
    ['EXPLORER',[
        'EXPLORER get',
        'EXPLORER copy file',
        'EXPLORER move file',
        'EXPLORER delete file',
        'EXPLORER copy folder',
        'EXPLORER move folder',
        'EXPLORER delete folder'
    ]],
    ['SYSTEM',[
        'SYSTEM shutdown',
        'SYSTEM restart',
    ]],
]

class Help:
    def __init__(self):
        pass
    def __help_df(self):
        return {
            'type': 'group',
            'columns': ['group','command'],
            'data': commands
        }
    def show_help(self):
        html = HTML_Generator.html_table(self.__help_df())
        return {
            'html': html,
            'data': None
        }