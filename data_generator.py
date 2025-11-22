import numpy as np

def generate_data(num_records=1000, seed=42):
    np.random.seed(seed)

    transaction_ids = np.arange(1, num_records + 1)

    product_ids = np.random.randint(100, 200, size=num_records)

    prices = np.round(np.random.uniform(5, 500, size=num_records), 2)

    quantities = np.random.randint(1, 10, size=num_records)

    categories = np.random.choice(
        ['Electronics', 'Clothing', 'Groceries', 'Toys', 'Books'],
        size=num_records
    )

    dates = np.random.choice(
        np.arange('2023-01', '2023-07', dtype='datetime64[D]'),
        size=num_records
    )

    return transaction_ids, product_ids, prices, quantities, categories, dates


def save_data(filename="sales_data.npz"):
    data = generate_data()

    np.savez(
        filename,
        transaction_ids=data[0],
        product_ids=data[1],
        prices=data[2],
        quantities=data[3],
        categories=data[4],
        dates=data[5]
    )

    print(f"Data saved to {filename}")


if __name__ == "__main__":
    save_data()
