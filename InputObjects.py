import pandas as pd


class MarketingSpends:

    required_columns = [
        "spend_id",
        "marketing_tactic",
        "region",
        "spend_month",
        "amount"
    ]

    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.columns = data.columns

    def validate_columns(self):
        return all(item in self.columns for item in MarketingSpends.required_columns)


class LeadsTable:

    required_columns = [
        "lead_id",
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
        "customer_id",
        "region",
        "bill_start_month",
        "bill_end_month",
        "product_id",
        "bill_amount",
        "recurring_flag",
        "bill_month"
    ]

    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.columns = data.columns

    def validate_columns(self):
        return all(column in self.columns for column in CustomerCube.required_columns)

