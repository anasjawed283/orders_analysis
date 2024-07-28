import pandas as pd

# Function to read the data from a CSV file
def read_data(file_path):
    try:
        # Try to read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        # Print an error message if there is an issue reading the file
        print(f"Error reading the file: {e}")
        return None

# Function to compute total revenue per month
def total_revenue_per_month(df):
    # Convert 'order_date' column to datetime format, with day-first format
    df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce')
    
    # Drop rows where 'order_date' could not be converted and resulted in NaT (Not a Time)
    df.dropna(subset=['order_date'], inplace=True)
    
    # Create a new column 'month' that contains just the month and year from 'order_date'
    df['month'] = df['order_date'].dt.to_period('M')
    
    # Group the DataFrame by 'month' and sum the revenue (product_price * quantity) for each month
    revenue_per_month = df.groupby('month').apply(lambda x: (x['product_price'] * x['quantity']).sum())
    return revenue_per_month

# Function to compute total revenue per product
def total_revenue_per_product(df):
    # Group the DataFrame by 'product_name' and sum the revenue (product_price * quantity) for each product
    revenue_per_product = df.groupby('product_name').apply(lambda x: (x['product_price'] * x['quantity']).sum())
    return revenue_per_product

# Function to compute total revenue per customer
def total_revenue_per_customer(df):
    # Group the DataFrame by 'customer_id' and sum the revenue (product_price * quantity) for each customer
    revenue_per_customer = df.groupby('customer_id').apply(lambda x: (x['product_price'] * x['quantity']).sum())
    return revenue_per_customer

# Function to identify the top 10 customers by revenue
def top_10_customers(revenue_per_customer):
    # Use the nlargest function to get the top 10 customers by revenue
    top_customers = revenue_per_customer.nlargest(10)
    return top_customers

def main():
    # Define the path to the CSV file
    file_path = 'orders.csv'
    
    # Read the data from the CSV file
    df = read_data(file_path)

    # Check if the DataFrame is not None (file was read successfully)
    if df is not None:
        # Compute total revenue per month
        revenue_per_month = total_revenue_per_month(df)
        
        # Compute total revenue per product
        revenue_per_product = total_revenue_per_product(df)
        
        # Compute total revenue per customer
        revenue_per_customer = total_revenue_per_customer(df)
        
        # Identify the top 10 customers by revenue
        top_customers = top_10_customers(revenue_per_customer)

        # Print the results
        print("Total Revenue per Month:")
        print(revenue_per_month)
        print("\nTotal Revenue per Product:")
        print(revenue_per_product)
        print("\nTotal Revenue per Customer:")
        print(revenue_per_customer)
        print("\nTop 10 Customers by Revenue:")
        print(top_customers)

# Check if the script is being run directly (not imported)
if __name__ == "__main__":
    main()
