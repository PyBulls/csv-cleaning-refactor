import csv


def clean_loan_length(ll):
    ll_lut = {
        "36 months": 36,
        "60 months": 60,
    }
    return ll_lut[ll]


def clean_employment_length(el):
    el_lut = {
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
    }
    return el_lut[el]


def clean_FICO_range(fr):
    low, hi = fr.split("-")
    hi = hi.strip()
    return ((int(hi) - int(low)) / 2) + int(low)


def clean_percent(p):
    return p.replace("%", "")


if __name__ == "__main__":
    outfile = open(r"loansData_clean.csv", "w")
    infile = open(r"loansData.csv")
    reader = csv.DictReader(infile)

    cnt = 0
    for aline in reader:
        if cnt == 0:
            outfile.write(",".join(aline.keys()) + "\n")

        aline["FICO.Range"] = clean_FICO_range(aline["FICO.Range"])
        aline["Interest.Rate"] = clean_percent(aline["Interest.Rate"])
        aline["Debt.To.Income.Ratio"] = clean_percent(aline["Debt.To.Income.Ratio"])
        aline["Employment.Length"] = clean_employment_length(aline["Employment.Length"])
        aline["Loan.Length"] = clean_loan_length(aline["Loan.Length"])

        outfile.write(",".join(["{}".format(aline[k]) for k in aline.keys()]))
        outfile.write("\n")
        cnt += 1
