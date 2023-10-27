import pandas as pd
import os

# from service.InstaloaderService import InstaloaderService
from service.TimeService import TimeService

class PandasService:
    def __init__(self):
        self.hello = "Hello pandas!"

    def print_hello(self):
        print(self.hello)

    def save_followers_list_csv(self, list, path):
        
        visited_column = self.get_visited_column(len(list))

        dict = {'follower': list, 'visited': visited_column}

        df = pd.DataFrame(dict)

        # saving the dataframe
        df.to_csv(path)

    def get_visited_column(self, size):
        column = size*["False"]

        return column
    
    def update_df(self, lines, columns, path):
        df = pd.DataFrame(lines, columns=columns)

        # saving the dataframe
        df.to_csv(path, index=False)

    def get_df_size(self, path):
        df = pd.read_csv(path)
        lines = df.values.tolist()
        return len(lines)
    
    def get_df_to_list(self, path):
        if not os.path.isfile(path):
            return None
        df = pd.read_csv(path)
        lines = df.values.tolist()
        return lines

    def get_following_list(self, instaloader_service, path):
        time_service = TimeService()
        df = pd.read_csv(path)
        
        columns = df.columns.tolist()
        lines = df.values.tolist()
        updated_lines = lines.copy()

        following_size = len(lines)

        for iterator in range(following_size):
            random = time_service.get_random_values(0, 12484)
            element = lines[random]
            visited = str(element[2])
            index = lines.index(element)  
        
            if visited == "False":
                user = element[1]
                try:
                    status, following_list = instaloader_service.get_profile_data(user)
                except Exception as ex:
                    TimeService.notifica_erro(str(ex))
                    exit()
                updated_lines[index][2] = status

                if status == "True":
                    following_path = path.replace("followers.csv", "each_following/") + user + ".csv"
                    self.update_df(following_list, ['names'], following_path)

                self.update_df(updated_lines, columns, path)
                print(str(index) + ": " + user + " - " + status)

        return lines
    
    # Quando dá algum erro em que a lista é salva vazia, chama a função de limpeza
    def clean_followers(self, path):
        df = pd.read_csv(path)
        
        columns = df.columns.tolist()
        lines = df.values.tolist()
        updated_lines = lines.copy()

        for element in lines:
            visited = str(element[2])
            index = lines.index(element)  

            # if visited == "True":
            user = element[1]
            following_path = path.replace("followers.csv", "each_following/") + user + ".csv"
            following_list = self.get_df_to_list(following_path)
            if following_list != None and len(following_list) == 0:
                self.update_df(updated_lines, columns, path)
                os.remove(following_path)

                updated_lines[index][2] = "False"
                self.update_df(updated_lines, columns, path)
