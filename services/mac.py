import os, re
from .html_generator import HTML_Generator
class Mac:
    def __init__(self):
        pass
    def __mac(self):
        result = os.popen("ipconfig /all")
        text = result.read()
        mac_address = re.findall('Physical Address.+', text)[-1]
        mac_address = mac_address.split(":")[-1].strip()
        return mac_address
    def get_mac(self):
        html = HTML_Generator.html_msg("Địa chỉ Mac server là: "+self.__mac(),None,True)
        return {
            'html': html,
            'data': None
        }