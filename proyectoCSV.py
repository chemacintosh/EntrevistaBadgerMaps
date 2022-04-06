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


customerOlderChIn()
customerNewerChIn()
