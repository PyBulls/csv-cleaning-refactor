import pandas

infile = open(r"loansData.csv")

claimframe = pandas.read_csv(infile)


#Debt.To.Income.Ratio,Employment.Length,Loan.Purpose,
#Loan.Length,Amount.Requested,State,Interest.Rate,Monthly.Income,
#Open.CREDIT.Lines,Amount.Funded.By.InvestorsB,Amount.Funded.By.InvestorsA

for col in claimframe.columns:
    print col
    if len(claimframe[col].unique()) < 100:
        print claimframe[col].unique()
    print "---"
