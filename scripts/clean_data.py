import capstone
import os

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Clean CDC data.')
    parser.add_argument('-i','--in_dir', type=str, default=capstone.data_dir, help='name of directory containing all .txt files with mortality data')
    parser.add_argument('-o','--out_name', type=str, default='mort.csv', help='output name of cleaned .csv file')
    args = parser.parse_args()

    capstone.clean_data(args.in_dir,args.out_name)
