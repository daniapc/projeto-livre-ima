import pandas as pd
import os

class PandasService:
    def __init__(self):
        self.hello = "Hello pandas!"

    def print_hello(self):
        print(self.hello)

    def save_followers_list_csv(self, list):
        
        visited_column = self.get_visited_column(len(list))

        dict = {'follower': list, 'visited': visited_column}

        df = pd.DataFrame(dict)

        path = os.getcwd() + '/src/service/data_files/followers.csv'
        # saving the dataframe
        df.to_csv(path)

    def get_visited_column(self, size):
        column = size*["False"]

        return column
        

