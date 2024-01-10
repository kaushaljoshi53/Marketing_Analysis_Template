import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Function to generate random spend data
def generate_marketing_spend_data():
    spend_id = fake.uuid4()
    marketing_tactic = fake.random_element(elements=('Tactic1', 'Tactic2', 'Tactic3', 'Tactic4', 'Tactic5'))
    spend_month = (datetime.now() - timedelta(days=random.randint(1, 365))).replace(day=1).strftime('%Y-%m-%d')
    region = fake.random_element(elements=('UK', 'US', 'France', 'Canada'))
    amount = round(random.uniform(1000, 10000), 2)

    return {'spend_id': spend_id, 'marketing_tactic': marketing_tactic, 'spend_month': spend_month, 'region': region, 'amount': amount}

# Function to generate random leads data
def generate_leads_data(spend_data):
    lead_id = fake.uuid4()
    tactic = spend_data['marketing_tactic']
    enquiry_month = spend_data['spend_month']

    # Determine lead status randomly
    status = random.choice(['Closed-won', 'Open'])

    if status == 'Closed-won':
        closed_date = (datetime.strptime(enquiry_month, '%Y-%m-%d') + timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d')
        customer_id = fake.uuid4()
    else:
        closed_date = None
        customer_id = None

    region = spend_data['region']

    return {'lead_id': lead_id, 'tactic': tactic, 'enquiry_month': enquiry_month, 'status': status, 'closed_date': closed_date, 'customer_id': customer_id, 'region': region}

# Function to generate random customer cube data
def generate_customer_cube_data(customer_id, region, closed_date):
    if closed_date is None:
        return []  # No customer cube data for customers without a closed date

    products = [
        {'id': 1, 'name': 'Product1', 'recurring': 1},
        {'id': 2, 'name': 'Product2', 'recurring': 1},
        {'id': 3, 'name': 'Product3', 'recurring': 1},
        {'id': 4, 'name': 'Product4', 'recurring': 1},
        {'id': 5, 'name': 'Product5', 'recurring': 1},
        {'id': 6, 'name': 'Product6', 'recurring': 1},
        {'id': 7, 'name': 'Product7', 'recurring': 1},
        {'id': 8, 'name': 'Product8', 'recurring': 1},
        {'id': 9, 'name': 'Product9', 'recurring': 1},
        {'id': 10, 'name': 'Product10', 'recurring': 1},
        {'id': 11, 'name': 'Product11', 'recurring': 0},
        {'id': 12, 'name': 'Product12', 'recurring': 0},
        {'id': 13, 'name': 'Product13', 'recurring': 0},
        {'id': 14, 'name': 'Product14', 'recurring': 0},
        {'id': 15, 'name': 'Product15', 'recurring': 0},
    ]

    customer_cube_data = []

    for product in products:
        if product['recurring'] == 1:
            # For recurring products, generate records for each month with random bill start and end dates
            bill_start_date = closed_date + timedelta(days=random.randint(1, 365))
            bill_end_date = bill_start_date + timedelta(days=random.randint(30, 365))

            while bill_start_date < bill_end_date:
                bill_month = bill_start_date.strftime('%Y-%m-%d')
                bill_amount = round(random.uniform(50, 200), 2)
                recurring_flag = 1

                customer_cube_data.append({'customer_id': customer_id, 'region': region, 'bill_start_month': bill_start_date.strftime('%Y-%m-%d'), 'bill_end_month': bill_end_date.strftime('%Y-%m-%d'), 'product_id': product['id'], 'bill_amount': bill_amount, 'recurring_flag': recurring_flag, 'bill_month': bill_month})

                # Move to the next month
                bill_start_date = bill_start_date + timedelta(days=30)
        else:
            # For non-recurring products, generate a single record with random bill start date
            bill_start_date = closed_date + timedelta(days=random.randint(1, 365))
            bill_end_date = None
            bill_month = bill_start_date.strftime('%Y-%m-%d')
            bill_amount = round(random.uniform(50, 200), 2)
            recurring_flag = 0

            customer_cube_data.append({'customer_id': customer_id, 'region': region, 'bill_start_month': bill_start_date.strftime('%Y-%m-%d'), 'bill_end_month': None, 'product_id': product['id'], 'bill_amount': bill_amount, 'recurring_flag': recurring_flag, 'bill_month': bill_month})

    return customer_cube_data

if __name__ == '__main__':

    # Generate 100 rows of spend data
    spends_data = [generate_marketing_spend_data() for _ in range(100)]

    # Generate leads data based on spends data
    leads_data = [generate_leads_data(row) for row in spends_data]

    # Generate customer cube data based on leads data
    customer_cube_data = []

    for lead in leads_data:
        customer_id = lead['customer_id']
        region = lead['region']
        closed_date_str = lead['closed_date']
        closed_date = datetime.strptime(closed_date_str, '%Y-%m-%d') if closed_date_str else None

        customer_cube_data.extend(generate_customer_cube_data(customer_id, region, closed_date))

    # Generate data for customers not in leads table
    for _ in range(20):  # Assuming 20 customers not in leads table
        customer_id = fake.uuid4()
        region = fake.random_element(elements=('UK', 'US', 'France', 'Canada'))
        closed_date = None  # No closed date for customers not in leads table

        customer_cube_data.extend(generate_customer_cube_data(customer_id, region, closed_date))

    # Convert data to dataframes
    spends_df = pd.DataFrame(spends_data)
    leads_df = pd.DataFrame(leads_data)
    customer_cube_df = pd.DataFrame(customer_cube_data)

    # Save dataframes to CSV files
    spends_df.to_csv('spends_table.csv', index=False)
    leads_df.to_csv('leads_table.csv', index=False)
    customer_cube_df.to_csv('customer_cube_table.csv', index=False)
