from service.InstaloaderService import InstaloaderService
from service.MlxtendService import MlxtendService
from service.PandasService import PandasService

import sys
import os

if __name__ == "__main__":

    used_account = "augustopires.png" if len(sys.argv) <= 2 else sys.argv[1]
    used_password = "meesqueci" if len(sys.argv) <= 2 else sys.argv[2]

    # CARREGA O INSTALOADER
    instaloader_service = InstaloaderService(used_account, used_password, False)
    instaloader_service.print_hello()

    followers_list = instaloader_service.get_followers_list(used_account, "utfpr.curitiba")

    pandas_service = PandasService()
    pandas_service.print_hello()

    path = os.getcwd() + '/data_files/followers.csv'
    pandas_service.save_followers_list_csv(followers_list, path)
    # size = pandas_service.get_df_size(path)

    # pandas_service.clean_followers(path)

    # followers_list = pandas_service.get_df_to_list(path)
    # data_list = pandas_service.get_df_to_list(os.getcwd() + '/data_files/each_following/ulas_no_insta.csv')

    pandas_service.get_following_list(instaloader_service, path)

    pandas_service.collect_each_following('./data_files/each_following')

    # items = PandasService.read_item_dataset('./data_files/all_profiles.csv')

    mlxtend_service = MlxtendService('./data_files/all_filtered_profiles.csv')
    mlxtend_service.print_hello()

    ## PEGA OS ITENS MAIS FREQUENTES COM MÍNIMO SUPORTE DE 1% E FILTRA NO DATASET DE ALL PROFILES
    mlxtend_service.most_frequent()
    pandas_service.filter_each_following('./data_files/')

    ## EXECUTA CADA ALGORITMO
    mlxtend_service.execute_algorithm('apriori', min_support=0.02, min_threshold=0.01)
    mlxtend_service.execute_algorithm('fpgrowth', min_support=0.01, min_threshold=0.01)
    mlxtend_service.execute_algorithm('hmine', min_support=0.01, min_threshold=0.01)

    pandas_service.group_arules('./data_files/', 'hmine')

    from service.TimeService import TimeService
    TimeService.notifica_erro("Programa acabou")
