import numpy as np

data = np.load("sales_data.npz", allow_pickle=True)

transaction_ids = data["transaction_ids"]
product_ids = data["product_ids"]
prices = data["prices"]
quantities = data["quantities"]
categories = data["categories"]
dates = data["dates"]

total_sales = prices * quantities

# ----------- Basic Stats ---------------
print("=== Basic Statistics ===")
print("Total transactions:", len(transaction_ids))
print("Total sales:", total_sales.sum())
print("Average transaction value:", total_sales.mean())
print("Max transaction:", total_sales.max())
print("Min transaction:", total_sales.min())

# ----------- Category Analysis ---------------
print("\n=== Category Analysis ===")
unique_cats = np.unique(categories)

for cat in unique_cats:
    mask = categories == cat
    cat_sales = total_sales[mask]
    cat_prices = prices[mask]

    print(f"\nCategory: {cat}")
    print(" Transactions:", mask.sum())
    print(" Total sales:", cat_sales.sum())
    print(" Average price:", cat_prices.mean())

# ----------- Monthly Sales ---------------
print("\n=== Monthly Sales ===")
months = np.array([str(d)[:7] for d in dates])
unique_months = np.unique(months)

for m in unique_months:
    m_mask = months == m
    print(f" {m}: {total_sales[m_mask].sum()}")

# ----------- Top 5 products ---------------
print("\n=== Top 5 Products by Revenue ===")
unique_products = np.unique(product_ids)
revenues = []

for p in unique_products:
    mask = product_ids == p
    revenues.append((p, total_sales[mask].sum()))

top5 = sorted(revenues, key=lambda x: x[1], reverse=True)[:5]

for prod, rev in top5:
    print(f" Product {prod}: Revenue = {rev}")
