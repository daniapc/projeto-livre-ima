from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import hmine
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
from service.PandasService import PandasService
from service.TimeService import TimeService

import pandas as pd

class MlxtendService:
    def __init__(self, path):
        self.hello = "Hello mlxtend!"
        self.path = path

    def print_hello(self):
        print(self.hello)

    def execute_algorithm(self, algorithm, min_support):
        
        path = self.path

        print("Iniciando " + algorithm)

        dataset = PandasService.read_item_dataset(path)

        te = TransactionEncoder()
        te_ary = te.fit(dataset).transform(dataset)
        df = pd.DataFrame(te_ary, columns=te.columns_)

        tempo_inicial = TimeService.get_current_time_in_seconds()

        if (algorithm == 'hmine'):
            frequent_itemsets = hmine(df, min_support=min_support, use_colnames=True)
        elif (algorithm == 'fpgrowth'):
            frequent_itemsets = fpgrowth(df, min_support=min_support, use_colnames=True)
        else:
            frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)

        rules = association_rules(frequent_itemsets, metric="lift")
        
        # print(rules)

        df = pd.DataFrame(rules)

        columns = df.columns.tolist()
        rules_list = df.values.tolist()
        correct_list = rules_list.copy()

        for element in rules_list:
            i = rules_list.index(element)
            antecedent = str(element[0]).replace('frozenset(', '').replace(')', '')
            consequent = str(element[1]).replace('frozenset(', '').replace(')', '')

            correct_list[i][0] = antecedent
            correct_list[i][1] = consequent

        df = pd.DataFrame(correct_list, columns = columns)

        # saving the dataframe
        df.to_csv(path.replace('all_profiles', algorithm), index=False)

        tempo_final = TimeService.get_current_time_in_seconds()

        print('Algoritmo ' + algorithm + 
              ' finalizado. Tempo total: ' + str(round(tempo_final - tempo_inicial,3)) +
              ' segundos.')

