import pandas as pd

input_csv_file_name = './csv/chinese_all.csv'
try:
  # input_csv_file = open(input_csv_file_name, mode='r', encoding='ISO-8859-1')
  # count = 0
  # for line in input_csv_file:
  #   cols = line.split(';')
  #   if count == 1:
  #     for index, col in enumerate(cols):
  #       if col == '17':
  #         print(col)
  #       if col == '33\n':
  #         print(col)
  #       print(str(col) + str(index))
  #   count += 1
  # print(count)
  df = pd.read_csv(input_csv_file_name, sep=';', encoding='ISO-8859-1')
  print(df.head(10))
finally:
  # input_csv_file.close()
  print('Finished')