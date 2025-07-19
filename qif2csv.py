#!/usr/bin/python3

from quiffen import Qif, QifDataType
import decimal

qif = Qif.parse('input.qif', day_first=True)
df = qif.to_dataframe(data_type=QifDataType.TRANSACTIONS)
df.to_csv('output.csv', index=False)