from tabnanny import check
import pandas as pd
import numpy as np

df = pd.read_csv("./data/sample test file - Sheet1.csv",
                 parse_dates=["Last Check-In Date"])
print(df)
print("\n/////////////////////////////////////////////////\n")

print("Do you want to remove rows with any required value (zip, city, Last Check-In Date, Company) being NaN? (y/n)")

if input() == "y" or input() == "yes":
    df = df.dropna(subset=["Zip", "City", "Last Check-In Date", "Company"])


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


print("Welcome, which query do you wish to realize? ")
while True:
    print("Oldest Checked-in Customer: 1")
    print("Newer Checked-in Customer: 2")
    print("Full name table ordered by Last name alphabetical order: 3")
    print("Full name table ordered by First name alphabetical order: 4")
    print("Write here the option number: ")
    opc = input()
    if opc == "1":
        customerOlderChIn()
    elif opc == "2":
        customerNewerChIn()
    elif opc == "3":
        alphaOrderLN()
    elif opc == "4":
        alphaOrderFN()

    print("Do you wish to realize any other query? (y/n):")
    resp = input()
    if resp == "n" or resp == "no":
        break
