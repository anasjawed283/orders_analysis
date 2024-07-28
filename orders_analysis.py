import pandas as pd

# Read the data
def read_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None

# Compute total revenue per month
def total_revenue_per_month(df):
    # Adjust the format for date parsing
    df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce')
    df.dropna(subset=['order_date'], inplace=True)  # Drop rows with invalid dates
    df['month'] = df['order_date'].dt.to_period('M')
    revenue_per_month = df.groupby('month').apply(lambda x: (x['product_price'] * x['quantity']).sum())
    return revenue_per_month

# Compute total revenue per product
def total_revenue_per_product(df):
    revenue_per_product = df.groupby('product_name').apply(lambda x: (x['product_price'] * x['quantity']).sum())
    return revenue_per_product

# Compute total revenue per customer
def total_revenue_per_customer(df):
    revenue_per_customer = df.groupby('customer_id').apply(lambda x: (x['product_price'] * x['quantity']).sum())
    return revenue_per_customer

# Identify top 10 customers by revenue
def top_10_customers(revenue_per_customer):
    top_customers = revenue_per_customer.nlargest(10)
    return top_customers

def main():
    file_path = 'orders.csv'
    df = read_data(file_path)

    if df is not None:
        revenue_per_month = total_revenue_per_month(df)
        revenue_per_product = total_revenue_per_product(df)
        revenue_per_customer = total_revenue_per_customer(df)
        top_customers = top_10_customers(revenue_per_customer)

        print("Total Revenue per Month:")
        print(revenue_per_month)
        print("\nTotal Revenue per Product:")
        print(revenue_per_product)
        print("\nTotal Revenue per Customer:")
        print(revenue_per_customer)
        print("\nTop 10 Customers by Revenue:")
        print(top_customers)

if __name__ == "__main__":
    main()
