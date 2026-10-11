from sales import calculate_sales
from excel_report import create_excel_report

def main():
    total_sales, sales_by_product = calculate_sales()

    create_excel_report(total_sales, sales_by_product)

    print("Sales report generated successfully!")
    print("Total Sales:", total_sales)
    print("Saved as: sales_report.xlsx")


if __name__ == "__main__":
    main()