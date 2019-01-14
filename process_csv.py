output_man_file_name = 'baden_man.csv'
output_woman_file_name = 'baden_woman.csv'
try:
  input_csv_file = open('/Users/lvsun/Downloads/chineseInGermany/baden.csv', mode='r', encoding='ISO-8859-1')
  output_man_csv_file = open(output_man_file_name, mode='w')
  output_woman_csv_file = open(output_woman_file_name, mode='w')

  count = 0
  for line in input_csv_file:
    cols = line.split(';')
    if count == 1:
      for index, col in enumerate(cols):
        if col == '17':
          print(col)
        if col == '33\n':
          print(col)
        print(str(col) + str(index))
    count += 1

  print(count)
finally:
  input_csv_file.close()
  output_man_csv_file.close()
  output_woman_csv_file.close()