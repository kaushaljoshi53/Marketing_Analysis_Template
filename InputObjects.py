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

    def calculate_enquiry_age(self):
        self.data['enquiry_month'] = pd.to_datetime(self.data['enquiry_month'],format='%Y-%m-%d')
        self.data['closed_date'] = pd.to_datetime(self.data['closed_date'],format='%Y-%m-%d')
        self.data['enquiry_age'] = (self.data['closed_date'] - self.data['enquiry_month']).dt.days//30


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
        self.data: pd.DataFrame = data
        self.columns = data.columns

    def validate_columns(self):
        return all(column in self.columns for column in CustomerCube.required_columns)

    def calculate_tenure(self):
        self.data['bill_start_month'] = pd.to_datetime(self.data['bill_start_month'],format='%Y-%m-%d')
        self.data['bill_end_month'] = pd.to_datetime(self.data['bill_end_month'],format='%Y-%m-%d')
        grouped_data = self.data.groupby('customer_id').agg(
            cohort_month=('bill_start_month', 'min'),
            last_bill_month=('bill_end_month', 'max')
        ).reset_index()

        grouped_data['tenure'] = (grouped_data['last_bill_month'] - grouped_data['cohort_month']).dt.days // 30
        self.data = pd.merge(self.data, grouped_data[['customer_id', 'cohort_month', 'last_bill_month', 'tenure']],
                             on='customer_id', how='left')

