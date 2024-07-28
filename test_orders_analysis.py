import pandas as pd
import pytest
from orders_analysis import read_data, total_revenue_per_month, total_revenue_per_product, total_revenue_per_customer, top_10_customers

@pytest.fixture
def sample_data():
    data = {
        'order_id': [1, 2, 3, 4],
        'customer_id': [101, 102, 101, 103],
        'order_date': ['01-02-2021', '15-02-2021', '01-03-2021', '20-03-2021'],
        'product_id': [1001, 1002, 1003, 1001],
        'product_name': ['Product A', 'Product B', 'Product C', 'Product A'],
        'product_price': [10.0, 20.0, 30.0, 10.0],
        'quantity': [1, 2, 1, 3]
    }
    df = pd.DataFrame(data)
    df['order_date'] = pd.to_datetime(df['order_date'], format='%d-%m-%Y')
    return df

def test_total_revenue_per_month(sample_data):
    result = total_revenue_per_month(sample_data)
    expected = pd.Series([50.0, 40.0], index=pd.PeriodIndex(['2021-02', '2021-03'], freq='M'))
    pd.testing.assert_series_equal(result, expected)

def test_total_revenue_per_product(sample_data):
    result = total_revenue_per_product(sample_data)
    expected = pd.Series([40.0, 40.0, 30.0], index=pd.Index(['Product A', 'Product B', 'Product C'], name='product_name'))
    pd.testing.assert_series_equal(result, expected)

def test_total_revenue_per_customer(sample_data):
    result = total_revenue_per_customer(sample_data)
    expected = pd.Series([40.0, 40.0, 10.0], index=pd.Index([101, 102, 103], name='customer_id'))
    pd.testing.assert_series_equal(result, expected)

def test_top_10_customers(sample_data):
    revenue_per_customer = total_revenue_per_customer(sample_data)
    result = top_10_customers(revenue_per_customer)
    expected = pd.Series([40.0, 40.0, 10.0], index=pd.Index([101, 102, 103], name='customer_id'))
    pd.testing.assert_series_equal(result, expected)
