import pandas as pd

def addNewContactstoEmailList(constantContactsCsv, wvrecCsv):
    df1 = pd.read_csv(constantContactsCsv)
    ccEmails = df1["EMAIL"]

    df2 = pd.read_csv(f'./{wvrecCsv}')
    newEmails = df2["Email"]

    new_items = df2[~newEmails.isin(ccEmails)]

    new_items.to_csv(f'new_{wvrecCsv}', index=False)

# addNewContactstoEmailList('./constantcontact.csv', 'ActiveAssocBroker.csv')
# addNewContactstoEmailList('./constantcontact.csv', 'ActiveBroker.csv')
# addNewContactstoEmailList('./constantcontact.csv', 'ActiveSalespersons.csv')