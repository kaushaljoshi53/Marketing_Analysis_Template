
import pandas as pd

class MarketingSpends:

    requiredColumns = [
        "spend_id",
        "marketing_tactic",
        "region",
        "spend_month",
        "amount"
    ]

    def __init__(self, data:pd.DataFrame):
        self.data = data
        self.columns = data.columns

    def validateColumns(self):

        print(self.columns,"Self")
        print(MarketingSpends.requiredColumns,"Marketing Spends")

        return all(item in self.columns for item in MarketingSpends.requiredColumns)


class LeadsTable:

    required_columns = [
        "lead_Id",
        "tactic",
        "enquiry_month",
        "status",
        "closed_date",
        "customer_id",
        "region"
    ]

    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.columns = data.columns

    def validate_columns(self):
        return all(column in self.columns for column in LeadsTable.required_columns)


class CustomerCube:

    required_columns = [
        "Customer Id",
        "Region",
        "Bill Id",
        "Bill Start Date",
        "Bill End Date",
        "Product Id",
        "Bill Amount",
        "Recurring Flag",
        "Bill Month"
    ]

    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.columns = data.columns

    def validate_columns(self):
        return all(column in self.columns for column in CustomerCube.required_columns)

