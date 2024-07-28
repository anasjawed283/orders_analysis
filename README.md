# Orders Analysis

This project analyzes customer orders from an online store. It computes various revenue metrics and identifies top customers based on the revenue generated.

## Features

- Compute total revenue generated by the online store for each month.
- Compute total revenue generated by each product.
- Compute total revenue generated by each customer.
- Identify the top 10 customers by revenue generated.

## Requirements

- Docker
- Docker Compose

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/anasjawed283/orders_analysis_tanX.git
    cd orders_analysis_tanX
    ```

2. Ensure Docker and Docker Compose are installed and running on your machine.

## Building and Running

### Build the Containers

To build the Docker containers for the application and tests, run:

```bash
docker-compose build
