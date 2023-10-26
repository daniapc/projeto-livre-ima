from service.InstaloaderService import InstaloaderService
from service.MlxtendService import MlxtendService
from service.PandasService import PandasService

import sys
import os

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        exit()

    used_account = sys.argv[1]
    used_password = sys.argv[2]

    instaloader_service = InstaloaderService(used_account, used_password)
    instaloader_service.print_hello()

    # followers_list = instaloader_service.get_followers_list(used_account, "utfpr.curitiba")

    # instaloader_service.get_profile_data("dani.apc")

    pandas_service = PandasService()
    pandas_service.print_hello()

    path = os.getcwd() + '/data_files/followers.csv'
    # pandas_service.save_followers_list_csv(followers_list, path)
    size = pandas_service.get_df_size(path)
    
    pandas_service.clean_followers(path)
    # followers_list = pandas_service.get_df_to_list(path)
    # data_list = pandas_service.get_df_to_list(os.getcwd() + '/data_files/each_following/ulas_no_insta.csv')

    pandas_service.get_following_list(instaloader_service, path)

    mlxtend_service = MlxtendService()
    mlxtend_service.print_hello()
