from service.InstaloaderService import InstaloaderService
from service.MlxtendService import MlxtendService
from service.PandasService import PandasService

from service.TimeService import TimeService

import sys
import os

if __name__ == "__main__":
    used_account = sys.argv[1] if len(sys.argv) > 1 else "umanosemlixo.seminar"
    used_password = sys.argv[2] if len(sys.argv) > 2 else ""

    instaloader_service = InstaloaderService(used_account, used_password)
    instaloader_service.print_hello()

    # followers_list = instaloader_service.get_followers_list(used_account, "utfpr.curitiba")

    # instaloader_service.get_profile_data("dani.apc")

    pandas_service = PandasService()
    pandas_service.print_hello()

    path = os.getcwd() + '/data_files/followers.csv'
    # pandas_service.save_followers_list_csv(followers_list, path)
    size = pandas_service.get_df_size(path)
    
    for index in range(size):
        try:
            pandas_service.get_following_list(instaloader_service, path)
        except:
            TimeService.sleep_in_seconds(None, 900)
            instaloader_service.recreate_session(used_account, used_password)

    mlxtend_service = MlxtendService()
    mlxtend_service.print_hello()
