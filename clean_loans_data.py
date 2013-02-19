#!/usr/local/bin/python
import csv


INFILENAME = 'loansData.csv'
OUTFILENAME = 'loansData_clean.csv'


def clean_loan_length(ll):
    return {
        "36 months": 36,
        "60 months": 60,
    }[ll]


def clean_employment_length(el):
    return {
        "< 1 year": 0,
        "2 years": 2,
        "5 years": 5,
        "9 years": 9,
        "3 years": 3,
        "10+ years": 10,
        "8 years": 8,
        "6 years": 6,
        "1 year": 1,
        "7 years": 7,
        "4 years": 4,
        "n/a": 0,
    }[el]


def clean_fico_range(fico_range):
    low, hi = fico_range.split("-")
    low, hi = int(low), int(hi)
    return (hi - low) / 2 + low


def clean_percent(p):
    return p.replace("%", "")


def clean_line(line):
    line["FICO.Range"] = clean_fico_range(line["FICO.Range"])
    line["Interest.Rate"] = clean_percent(line["Interest.Rate"])
    line["Debt.To.Income.Ratio"] = clean_percent(line["Debt.To.Income.Ratio"])
    line["Employment.Length"] = clean_employment_length(line["Employment.Length"])
    line["Loan.Length"] = clean_loan_length(line["Loan.Length"])
    return line


def main(infilename=INFILENAME, outfilename=OUTFILENAME):
    infile = open(outfilename)
    outfile = open(infilename, "w")
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, reader.fieldnames)

    for aline in reader:
        writer.writeline(clean_line(aline))


if __name__ == "__main__":
    main()
