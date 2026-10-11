import csv 

def calculate_sales(file_path="data/sales.csv"):
    total_sales = 0
    sales_by_product = {}
    with open("data/sales.csv", "r", newline="", encoding="utf-8") as file:
      report = csv.DictReader(file)

      for row in report:
              quantity = int(row["Quantity"])
              price = int(row["Price"])
              print(f"product: {row['Product']}, Quantity: {quantity}, Price: {price}")
              amount = quantity * price
              total_sales += amount
              
              product = row["Product"]
              
              if product in sales_by_product:
                sales_by_product[product] += amount
              else:
                sales_by_product[product] = amount
      return total_sales, sales_by_product