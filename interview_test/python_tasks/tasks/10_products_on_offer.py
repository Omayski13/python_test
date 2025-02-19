import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'interview_test.settings')
django.setup()

from python_tasks.models import Sales_Details
from django.db.models import Sum


def products_on_offer():
    products_on_sale = Sales_Details.objects.filter(SpecialOffer__isnull=False).values('Product__Name').annotate(total_sales=Sum('OrderQty')).order_by('-total_sales')[:10]

    most_sold_product_on_sale = products_on_sale[0]

    result = ['Details for products on sale:\n']

    for product in products_on_sale:
        result.append(f'Product: {product['Product__Name']}, Sold quantity: {product['total_sales']}')
    result.append(f'\nMost sold product on sale: {products_on_sale[0]['Product__Name']}, sold quantity: {products_on_sale[0]['total_sales']}')

    return '\n'.join(result)


print(products_on_offer())
