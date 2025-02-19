import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'interview_test.settings')
django.setup()

from python_tasks.models import Sales_Details
from django.db.models import F, ExpressionWrapper, DecimalField, Prefetch

# get the details from db using prefetc related to optimize performance
def calculate_discounts():
    sales_details = Sales_Details.objects.prefetch_related(
        Prefetch('Product')
    ).annotate(
        unit_discount=ExpressionWrapper(
            F('UnitPrice') * (F('UnitPriceDiscount') / 100),
            output_field=DecimalField(max_digits=10, decimal_places=4)
        ),
        total_discount=ExpressionWrapper(
            F('OrderQty') * F('UnitPrice') * (F('UnitPriceDiscount') / 100),
            output_field=DecimalField(max_digits=15, decimal_places=4)
        ),
        original_total=ExpressionWrapper(
            F('UnitPrice') * F('OrderQty'),
            output_field=DecimalField(max_digits=15, decimal_places=4)
        ),
        discounted_total=ExpressionWrapper(
            (F('UnitPrice') * F('OrderQty')) - (F('OrderQty') * F('UnitPrice') * (F('UnitPriceDiscount') / 100)),
            output_field=DecimalField(max_digits=15, decimal_places=4)
        )
    )

    #iterate through sales records, round the to the second decimal and add to the result list
    for sale in sales_details:
        unit_discount = round(sale.unit_discount, 2)
        total_discount = round(sale.total_discount, 2)

        print(f'Sales Order ID: {sale.SalesOrderDetailID}')
        print(f'Product ID: {sale.Product.ProductID}')
        print(f'Unit Price: {sale.UnitPrice:.2f}')
        print(f'Unit Discount: {unit_discount}')
        print(f'Total Discount: {total_discount}')
        print(f'Original Total Price: {sale.original_total:.2f}')
        print(f'Discounted Total Price: {sale.discounted_total:.2f}\n')


calculate_discounts()
