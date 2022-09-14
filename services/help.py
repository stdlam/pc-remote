from .html_generator import HTML_Generator
commands = [
    ['MAC',
        ['MAC get'],
        ['Lấy địa chỉ MAC']
    ],
    ['APP',
        ['APP get','APP close <ID>'],
        ['Lấy danh sách app','Đóng app với ID']
    ],
    ['PROCESS',
        ['PROCESS get','PROCESS close <ID>'],
        ['Lấy danh sách process','Đóng process với ID']
    ],
    ['SCREEN',
        ['SCREEN get screenshot','SCREEN get record <seconds>'],
        ['Chụp màn hình','Quay phim màn hình trong khoảng thời gian']
    ],
    ['KEYLOGGER',
        ['KEYLOGGER get keypress <seconds>'],
        ['Lấy danh sách ký tự phím đã gõ trong 1 khoảng thời gian']
    ],
    ['REGISTRY',[
        'REGISTRY get value <key>',
        'REGISTRY edit value <value>',
        'REGISTRY delete value <key>',
        'REGISTRY get key <key>',
        'REGISTRY delete key <key>'
    ],
    [
        'Lấy giá trị registry theo key',
        'Sửa giá trị registry theo key',
        'Xoá giá trị registry theo key',
        'Lấy key registry',
        'Xoá key registry',
    ]
    ],
    ['EXPLORER',[
        'EXPLORER get',
        'EXPLORER copy file <path>',
        'EXPLORER move file <path> to <path>',
        'EXPLORER delete file <path>',
        'EXPLORER copy folder <path>',
        'EXPLORER move folder <path>',
        'EXPLORER delete folder <path>'
    ],
    [
        'Lấy danh sách thư mục',
        'Sao chép file',
        'Di chuyển file',
        'Xoá file',
        'Sao chép folder',
        'Di chuyển folder',
        'Xoá folder',
    ]
    ],
    ['SYSTEM',[
        'SYSTEM shutdown',
        'SYSTEM restart',
    ],
    [
        'Tắt máy',
        'Khởi động lại',
    ]
    ],
]

class Help:
    def __init__(self):
        pass
    def __help_df(self):
        return {
            'type': 'group',
            'columns': ['group command','command','desc'],
            'data': commands
        }
    def show_help(self):
        # html = HTML_Generator.html_table(self.__help_df())
        html = HTML_Generator.html_table(self.__help_df())
        return {
            'html': html,
            'data': None
        }