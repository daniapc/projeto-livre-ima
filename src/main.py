from service.InstaloaderService import InstaloaderService
from service.MlxtendService import MlxtendService
from service.PandasService import PandasService
import os

if __name__ == "__main__":
    instaloader_service = InstaloaderService("umanosemlixo.seminar")
    # instaloader_service = InstaloaderService("ladien.cup")
    instaloader_service.print_hello()

    # followers_list = instaloader_service.get_followers_list("ladien.cup", "utfpr.curitiba")

    # instaloader_service.get_profile_data("dani.apc")

    pandas_service = PandasService()
    pandas_service.print_hello()

    path = os.getcwd() + '/src/service/data_files/followers.csv'
    # pandas_service.save_followers_list_csv(followers_list, path)
    
    pandas_service.get_following_list(instaloader_service, path)

    mlxtend_service = MlxtendService()
    mlxtend_service.print_hello()
