import pandas as pd
import os
from os.path import abspath
import sys
import functools

def get_directory_structure(root_dir):
    """
    Creates a nested dictionary that represents the folder structure of root_dir
    """
    dir = {}
    root_dir = root_dir.rstrip(os.sep)
    start = root_dir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(root_dir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = functools.reduce(dict.get, folders[:-1], dir)
        parent[folders[-1]] = subdir
    return dir
def recurse_html(dir_dict):
    html = ""
    num_of_recursions = 1
    recursion_limit = sys.getrecursionlimit()
    if recursion_limit == num_of_recursions - 2:
        sys.setrecursionlimit(recursion_limit + 1)
    num_of_recursions += 1
    html += '<ul>'
    for i,file_or_folder in enumerate(dir_dict.keys()):
        if dir_dict[file_or_folder] is not None:
            html += '<p>[_] ' + file_or_folder + '</p>'
            html += recurse_html(dir_dict[file_or_folder])
        else:
            html += '<p>'+('└──' if len(dir_dict.keys())-1 == i else '├──')+ file_or_folder + '</p>'
    html += '</ul>'
    return html

class HTML_Generator:
    def __init__(self):
        pass
   
    def html_table(dataframe):
        html = None
        if(dataframe['type'] == 'group'):
            html = "<table border='2'>"
            table_head = "<thead>"
            for colName in dataframe['columns']:
                table_head += "<th>"+colName+"</th>"
            table_head += "</thead>"
            table_body = "<tbody>"
            for rowGroup in dataframe['data']:
                table_body += "<tr><td rowSpan='"+str(len(rowGroup[1])+1)+"'>"+rowGroup[0]+"</td></tr>"
                for i,commmandRow in enumerate(rowGroup[1]):
                    table_body += "<tr><td>"+commmandRow+"</td><td>"+rowGroup[2][i]+"</td></tr>"
            table_body += "</tbody>"
            html += table_head
            html += table_body
            html += "</table>"
        else:
            df = pd.DataFrame(dataframe['data'],columns=dataframe['columns'])
            html = df.to_html()
        return html
    def html_msg(msg,status,bold_all):
        html = ""
        color = "black"
        if(status == True): color = "green"
        if(status == False): color = "red"
        if(bold_all): html = '<b style="color:'+color+'">'+msg+'</b>'
        else: html = '<p style="color:'+color+'">'+msg+'</p>'
        return html
    def html_tree(path):
        dir_struct = get_directory_structure(path)

        html = recurse_html(dir_struct)
        return html
    def html_mail(request = "",content = ""):
        html = "<div>"
        html += "<h2>"+request+"</h2>"
        html += "<div>"+content+"</div>"
        html += "</div>"
        return html
