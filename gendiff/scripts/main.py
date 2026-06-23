import argparse
import json

def main():
    parser = argparse.ArgumentParser(
                        prog='gendiff',
                        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        dest="format",
        default="json",
        help='set format of output')
    args = parser.parse_args()
    file_name1, file_name2 = args.first_file, args.second_file
    file_content1 = json.load(open(file_name1))
    file_content2 = json.load(open(file_name2))

if __name__ == "__main__":
    main()
