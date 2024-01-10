import pandas as pd
import RequiredObject



if __name__ == '__main__':

    marketing_spends = pd.read_csv("spends_table.csv")

    marketing_spends_obj = RequiredObject.MarketingSpends(marketing_spends)
    print(marketing_spends_obj.validateColumns())

    leads = pd.read_csv("leads_table.csv")

    leads_obj = RequiredObject.LeadsTable(leads)
    print(leads_obj.validate_columns())