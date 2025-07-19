# qif2csv
Python script converting QIF files to CSV.

An extremely simple wrapper around [quiffen](https://github.com/isaacharrisholt/quiffen).

```
python3 -m venv quiffen
source quiffen/bin/activate
pip install -r requirements.txt 
python3 qif2csv.py --input=money.qif --output=money.csv
```
