import pandas as pd

def input_test():
    print(pd.DataFrame({"TEST":["테스트"],"TEST2":["완료"]}))

def read_data():
    a=pd.read_excel('./file_test/test_file.xlsx',keep_default_na=False)
    print(a)