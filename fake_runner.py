import csv

from iris_example import action, begin

if __name__ == '__main__':
  begin()

  with open('iris_test_unlabled.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    with open('iris_test_labled.csv', 'w') as csvfile_out:
      for row in csvreader:
        for prediction in action(row):
          csvfile_out.write(f'{row},{prediction}\n')
