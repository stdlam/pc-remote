import pandas as pd
class HTML_Generator:
    def __init__(self):
        pass
    def html_table(dataframe):
        # print(dataframe)
        df = pd.DataFrame(dataframe['data'],columns=dataframe['columns'])
        html = df.to_html()
        return html
    def html_msg(self):
        pass
    def html_tree(self):
        pass
    def html_mail(self):
        pass