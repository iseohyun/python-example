### arg parsing ###
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)

# 입력 예:
# python script.py file1.txt file2.txt -l 5

# 출력 예:
# Namespace(filenames=['file1.txt', 'file2.txt'], lines=5)

