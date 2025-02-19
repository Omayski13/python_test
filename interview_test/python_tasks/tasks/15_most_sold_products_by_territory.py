import os
import django
from openpyxl import Workbook

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'interview_test.settings')
django.setup()

from python_tasks.models import Product, Sales, Sales_Details, Territory
from django.db.models import Count


def product_profit(product_name, sold_units):
    product = Product.objects.filter(Name=product_name).first()

    if not product:
        return f'Product with the name {product_name} does not exist in the database.'

    profit = product.ListPrice - product.StandardCost
    total_profit = sold_units * profit
    return profit, total_profit


def territory_with_most_orders():
    territory_with_most_orders = Sales.objects.values('TerritoryID').annotate(order_count=Count('SalesOrderID')).order_by('-order_count').first()

    if not territory_with_most_orders:
        return 'No territories found with sales orders.'

    return territory_with_most_orders['TerritoryID']


def most_sold_products_by_territory(territory_id):
    most_sold_products_by_territory = Sales_Details.objects.filter(SalesOrder__TerritoryID=territory_id).values(
        'Product__Name').annotate(sales_count=Count('SalesOrderDetailID')).order_by('-sales_count')[:3]

    data = []

    territory = Territory.objects.filter(TerritoryID=territory_id).first()
    country_name = territory.CountryName

    for product in most_sold_products_by_territory:
        product_name = product['Product__Name']
        sold_units = product['sales_count']
        profit, total_profit = product_profit(product_name, sold_units)

        data.append([country_name, product_name, profit, total_profit])

    wb = Workbook()
    ws = wb.active
    ws.title = 'Profit Data'

    ws.append(['Country Name', 'Product Name', 'Profit Per Unit', 'Total Profit'])

    for row in data:
        ws.append(row)

    wb.save('Insights.xlsx')
    print("Excel file has been created successfully!")


most_sold_products_by_territory(territory_with_most_orders())
