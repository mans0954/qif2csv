#!/usr/bin/python3

from quiffen import Qif, QifDataType
import argparse
import decimal

parser = argparse.ArgumentParser()
parser.add_argument("--input", default='input.qif', help="input QIF file")
parser.add_argument("--output", default='output.csv', help="output CSV file")

args, unknown_args = parser.parse_known_args()

print(args)

qif = Qif.parse(args.input, day_first=True)
df = qif.to_dataframe(data_type=QifDataType.TRANSACTIONS)
df.to_csv(args.output, index=False, columns=['date', 'payee', 'amount', 'line_number'])