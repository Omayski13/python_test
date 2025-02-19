import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'interview_test.settings')
django.setup()

from python_tasks.models import Sales_Details
from django.db.models import Sum

# good code don't need comments :)
def most_sold_products() -> str:
    sold_products_list = list(Sales_Details.objects.values('Product').annotate(sold_quantity=Sum('OrderQty')).order_by('-sold_quantity'))

    result = ['Products:']
    total_sold = 0

    # itterating through every product to add it into the result list and sum total sales
    for product in sold_products_list:
        result.append(f"Product ID: {product['Product']}, sold quantity: {product['sold_quantity']}")
        total_sold += product['sold_quantity']

    # if there are products in the list get the most sold and leas sold products and append them to the result list with total sales
    if sold_products_list:
        most_sold_product = sold_products_list[0]
        least_sold_product = sold_products_list[-1]

        result.append('\nMost sold product:')
        result.append(f'Product ID: {most_sold_product['Product']}, sold quantity: {most_sold_product['sold_quantity']}')

        result.append('\nLeast sold product:')
        result.append(f'Product ID: {least_sold_product['Product']}, sold quantity: {least_sold_product['sold_quantity']}')

        result.append(f'\nTotal sold items: {total_sold}')

    return '\n'.join(result)


print(most_sold_products())

