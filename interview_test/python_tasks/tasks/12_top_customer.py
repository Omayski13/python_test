import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'interview_test.settings')
django.setup()

from django.db.models import Count
from python_tasks.models import Sales


def top_customers():
    top_customers = Sales.objects.values('CustomerID').annotate(total_purchases=Count('SalesOrderID')).order_by('-total_purchases')[:20]
    most_orders_by_customer = top_customers[0]['total_purchases']

    result = [f'Most orders made by customer: {most_orders_by_customer}\n','Customers with most orders:']

    customers_count = 0

    for customer in top_customers:
        if customer['total_purchases'] == most_orders_by_customer:
            result.append(f'Customer ID: {customer['CustomerID']}')
            customers_count += 1
    result.append(f'Total customers with {most_orders_by_customer} orders - {customers_count} customers')

    return '\n'.join(result)


print(top_customers())



