from service.InstaloaderService import InstaloaderService
from service.MlxtendService import MlxtendService
from service.PandasService import PandasService

instaloader_service = InstaloaderService()
instaloader_service.print_hello()

mlxtend_service = MlxtendService()
mlxtend_service.print_hello()

pandas_service = PandasService()
pandas_service.print_hello()