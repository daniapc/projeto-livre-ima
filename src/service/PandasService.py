import pandas as pd

import service.InstaloaderService

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
        
    def get_following_list(self, instaloader_service, path):
        df = pd.read_csv(path)
        
        columns = df.columns.tolist()
        lines = df.values.tolist()
        updated_lines = lines.copy()

        for element in lines:
            visited = str(element[2])
            index = lines.index(element)
            
            if visited == "False":
                user = element[1]
                status, following_list = instaloader_service.get_profile_data(user)
                # private, n_following = 
                updated_lines[index][2] = status

                if status == "True":
                    following_path = path.replace("followers.csv", "each_following/") + user + ".csv"
                    self.update_df(following_list, ['names'], following_path)

                self.update_df(updated_lines, columns, path)

        return lines

