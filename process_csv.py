import pandas as pd

input_csv_file_name = './csv/chinese_all.csv'
dates = []
berlin_man_number = []
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

  #######################################
  # select the chinese for studies
  #######################################
  print("index      date  berlin_man berlin_woman bayern_man bayern_woman")
  for index, row in df.iterrows():
    if (index % 13) == 4:
      dates.append(row['date'])
      berlin_man_number.append(row['berlin_man'])
      print(
        "{index:>3}  {date:>10} {berlin_man:>10} {berlin_woman:>10} {bayern_man:>10} {bayern_woman:>10}".format(
          index=index,
          date=row['date'],
          berlin_man=row['berlin_man'],
          berlin_woman=row['berlin_woman'],
          bayern_man = row['bayern_man'],
          bayern_woman = row['bayern_woman']
        )
      )

  #######################################
  # select the chinese with green cards
  #######################################
  print("index      date  berlin_man berlin_woman bayern_man bayern_woman")
  for index, row in df.iterrows():
    if (index % 13) == 2:
      print(
        "{index:>3}  {date:>10} {berlin_man:>10} {berlin_woman:>10} {bayern_man:>10} {bayern_woman:>10}".format(
          index=index,
          date=row['date'],
          berlin_man=row['berlin_man'],
          berlin_woman=row['berlin_woman'],
          bayern_man = row['bayern_man'],
          bayern_woman = row['bayern_woman']
        )
      )
      
  #######################################
  # select the chinese with time-limited visa 
  #######################################
  print("index      date  berlin_man berlin_woman bayern_man bayern_woman")
  for index, row in df.iterrows():
    if (index % 13) == 3:
      print(
        "{index:>3}  {date:>10} {berlin_man:>10} {berlin_woman:>10} {bayern_man:>10} {bayern_woman:>10}".format(
          index=index,
          date=row['date'],
          berlin_man=row['berlin_man'],
          berlin_woman=row['berlin_woman'],
          bayern_man = row['bayern_man'],
          bayern_woman = row['bayern_woman']
        )
      )

finally:
  # input_csv_file.close()
  print(dates)
  print(berlin_man_number)
  print('Finished')