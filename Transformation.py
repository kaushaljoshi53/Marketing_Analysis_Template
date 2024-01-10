import pandas as pd
import InputObjects

if __name__ == '__main__':

    marketing_spends = pd.read_csv("Input Files/spends_table.csv")
    marketing_spends_obj = InputObjects.MarketingSpends(marketing_spends)
    print(marketing_spends_obj.validate_columns())

    leads = pd.read_csv("Input Files/leads_table.csv")
    leads_obj = InputObjects.LeadsTable(leads)
    print(leads_obj.validate_columns())

    customer_cube = pd.read_csv("Input Files/customer_cube_table.csv")
    customer_cube_obj = InputObjects.CustomerCube(customer_cube)
    print(customer_cube_obj.validate_columns())
