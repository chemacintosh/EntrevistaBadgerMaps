from tabnanny import check
import pandas as pd

df = pd.read_csv("./data/sample test file - Sheet1.csv",
                 parse_dates=["Last Check-In Date"])
print(df)


def customerOlderChIn():
    print("Getting older checked-in customer...")
    checkIn = df[["First Name", "Last Name", "Last Check-In Date"]]
    retRow = checkIn.loc[checkIn["Last Check-In Date"].idxmin()]
    print("Customer: " + retRow["First Name"] + " " +
          retRow["Last Name"] + ", on date: " + str(retRow["Last Check-In Date"]))


def customerNewerChIn():
    print("Getting newer checked-in customer...")
    checkIn = df[["First Name", "Last Name", "Last Check-In Date"]]
    retRow = checkIn.loc[checkIn["Last Check-In Date"].idxmax()]
    print("Customer: " + retRow["First Name"] + " " +
          retRow["Last Name"] + ", on date: " + str(retRow["Last Check-In Date"]))


def alphaOrderLN():
    print("Geting Full Name table ordered by Last Name alphabetical order...")
    dfCopy = df
    dfCopy.sort_values(by=["Last Name"], ascending=False)
    print(dfCopy.sort_values(by=["Last Name"], ascending=True)[
        ["Last Name", "First Name"]])


def alphaOrderFN():
    print("Geting Full Name table ordered by First Name alphabetical order...")
    dfCopy = df
    dfCopy.sort_values(by=["Last Name"], ascending=False)
    print(dfCopy.sort_values(by=["Last Name"], ascending=True)[
          ["First Name", "Last Name"]])


customerOlderChIn()
customerNewerChIn()
alphaOrderLN()
alphaOrderFN()
