# 📊 Sales Data Analysis with NumPy
A pure NumPy data analysis project — no Pandas, no Excel, just raw array manipulation.
## 📌 Overview

This project demonstrates data generation and analysis using only NumPy, showcasing fundamental data-processing skills without relying on higher-level libraries.

The dataset is synthetically generated and simulates sales transactions from a retail store.
You will find:

Transaction-level data

Category-level insights

Monthly sales breakdown

Top-performing products

Clean, efficient NumPy operations

This project is ideal for portfolios, interviews, and GitHub showcasing.

## 🛠 Tech Stack

Python 3.x

NumPy

## 📁 Project Structure
data_generator.py – Generates dataset

analysis.py – Runs full analysis

sales_data.npz – Saved NumPy dataset

README.md – Documentation             # Project documentation

## 📦 Dataset Description

Each generated record simulates a purchase transaction with:

Transaction ID:	Unique ID of the transaction\
Product ID:	ID of the purchased product\
Price:	Price of each unit\
Quantity:	How many units were bought\
Category:	Product category\
Date:	Purchase date

A total of 1000 records are created by default.

## 🔍 Features
### ✔️ Basic Analysis

Total number of transactions

Total revenue

Average transaction value

Highest & lowest transaction amounts

### ✔️ Category-Based Insights

For each category:

Number of transactions

Total sales amount

Average product price

### ✔️ Time-Based Analysis

Monthly revenue breakdown

Best-performing month

### ✔️ Advanced (Top Products)

Top 5 products by total revenue

## 🚀 How to Run
### 1️⃣ Generate dataset
python data_generator.py

### 2️⃣ Run the analysis
python analysis.py

### Output

The script prints all statistics directly to the console.

## 📸 Example Output
=== Basic Statistics ===\
Total transactions: 1000\
Total sales: 187325.13\
Average transaction value: 187.32\
Max transaction: 4890.00\
Min transaction: 5.00
