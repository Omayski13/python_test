import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'interview_test.settings')
django.setup()

from python_tasks.models import Sales_Details
from django.db.models import Sum


def most_sold_products() -> str:
    most_sold_products_list = list(
        Sales_Details.objects.values('Product').annotate(
            sold_quantity=Sum('OrderQty')
        ).order_by('-sold_quantity')[:10]
    )



    most_sold_products = Sales_Details.objects.values('Product').annotate(sold_quantity=Sum('OrderQty')).order_by('-sold_quantity')[:10]
    print(most_sold_products)


    result = ['\nMost Sold Products:']

    for product in most_sold_products_list:
        result.append(f"Product ID: {product['Product']}, sold quantity: {product['sold_quantity']}")

    if most_sold_products_list:
        most_sold_product = most_sold_products_list[0]
        least_sold_product = most_sold_products_list[-1]

        result.append('\nMost sold product:')
        result.append(f"Product ID: {most_sold_product['Product']}, sold quantity: {most_sold_product['sold_quantity']}")

        result.append('\nLeast sold product:')
        result.append(f"Product ID: {least_sold_product['Product']}, sold quantity: {least_sold_product['sold_quantity']}")

    return '\n'.join(result)


print(most_sold_products())

