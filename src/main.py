from service.InstaloaderService import InstaloaderService
from service.MlxtendService import MlxtendService
from service.PandasService import PandasService

if __name__ == "__main__":
    instaloader_service = InstaloaderService()
    instaloader_service.print_hello()

    followers_list = instaloader_service.get_followers_list("ladien.cup", "utfpr.curitiba")

    pandas_service = PandasService()
    pandas_service.print_hello()

    pandas_service.save_followers_list_csv(followers_list)

    mlxtend_service = MlxtendService()
    mlxtend_service.print_hello()
