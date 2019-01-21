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

  dtype_dict = {
    'hessen_man': float,
    'baden_man': float
  }
  df = pd.read_csv(input_csv_file_name, sep=';', encoding='ISO-8859-1', dtype=dtype_dict, na_values='-')
  print(df.head(10))
  print(df.dtypes)
finally:
  # input_csv_file.close()
  print('Finished')