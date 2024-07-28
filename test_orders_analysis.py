import pandas as pd
import pytest
from orders_analysis import read_data, total_revenue_per_month, total_revenue_per_product, total_revenue_per_customer, top_10_customers

# Fixture to create sample data for testing
@pytest.fixture
def sample_data():
    # Define sample data as a dictionary
    data = {
        'order_id': [1, 2, 3, 4],
        'customer_id': [101, 102, 101, 103],
        'order_date': ['01-02-2021', '15-02-2021', '01-03-2021', '20-03-2021'],
        'product_id': [1001, 1002, 1003, 1001],
        'product_name': ['Product A', 'Product B', 'Product C', 'Product A'],
        'product_price': [10.0, 20.0, 30.0, 10.0],
        'quantity': [1, 2, 1, 3]
    }
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)
    # Convert 'order_date' column to datetime format
    df['order_date'] = pd.to_datetime(df['order_date'], format='%d-%m-%Y')
    return df

# Test function for total revenue per month
def test_total_revenue_per_month(sample_data):
    # Calculate the total revenue per month using the function
    result = total_revenue_per_month(sample_data)
    # Expected result as a Series with the correct index
    expected = pd.Series([50.0, 40.0], index=pd.PeriodIndex(['2021-02', '2021-03'], freq='M'))
    # Assert that the result matches the expected output
    pd.testing.assert_series_equal(result, expected)

# Test function for total revenue per product
def test_total_revenue_per_product(sample_data):
    # Calculate the total revenue per product using the function
    result = total_revenue_per_product(sample_data)
    # Expected result as a Series with the correct index
    expected = pd.Series([40.0, 40.0, 30.0], index=pd.Index(['Product A', 'Product B', 'Product C'], name='product_name'))
    # Assert that the result matches the expected output
    pd.testing.assert_series_equal(result, expected)

# Test function for total revenue per customer
def test_total_revenue_per_customer(sample_data):
    # Calculate the total revenue per customer using the function
    result = total_revenue_per_customer(sample_data)
    # Expected result as a Series with the correct index
    expected = pd.Series([40.0, 40.0, 10.0], index=pd.Index([101, 102, 103], name='customer_id'))
    # Assert that the result matches the expected output
    pd.testing.assert_series_equal(result, expected)

# Test function for identifying top 10 customers by revenue
def test_top_10_customers(sample_data):
    # First calculate the total revenue per customer
    revenue_per_customer = total_revenue_per_customer(sample_data)
    # Identify the top 10 customers by revenue using the function
    result = top_10_customers(revenue_per_customer)
    # Expected result as a Series with the correct index
    expected = pd.Series([40.0, 40.0, 10.0], index=pd.Index([101, 102, 103], name='customer_id'))
    # Assert that the result matches the expected output
    pd.testing.assert_series_equal(result, expected)
