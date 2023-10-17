import pandas as pd

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
        
    def get_following_list(self, instaloader_service, path):
        time_service = TimeService()
        time_service.print_hello()
        df = pd.read_csv(path)
        
        columns = df.columns.tolist()
        lines = df.values.tolist()
        updated_lines = lines.copy()

        # last_time = time_service.get_current_time_in_minutes()
        # random_value = time_service.get_random_values(3, 5)

        control = 0
        change = time_service.get_random_values(5, 10)
        for element in lines:
            visited = str(element[2])
            index = lines.index(element)  
        
            if visited == "False":
                if control >= change:
                    control = 0
                    change = time_service.get_random_values(5, 10)
                    instaloader_service.change_session()

                user = element[1]
                status, following_list = instaloader_service.get_profile_data(user)
                updated_lines[index][2] = status

                if status == "True":
                    following_path = path.replace("followers.csv", "each_following/") + user + ".csv"
                    self.update_df(following_list, ['names'], following_path)

                self.update_df(updated_lines, columns, path)
                print(str(index) + ": " + user)

                sleep_time = time_service.get_random_values(10, 30)
                print("Dormindo por " + str(sleep_time) + " segundos.")
                time_service.sleep_in_seconds(sleep_time)

                control = control + 1

        return lines

