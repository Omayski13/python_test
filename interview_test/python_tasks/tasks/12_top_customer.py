import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'interview_test.settings')
django.setup()

from django.db.models import Count, Sum
from python_tasks.models import Sales


def top_customers():
    #get the 20 customers with most orders made in case is not only one and no data is missed
    top_customers = Sales.objects.values('CustomerID').annotate(total_purchases=Count('SalesOrderID'),total_due=Sum('TotalDue')).order_by('-total_purchases','-total_due')[:20]

    #get the count of the customers with most orders
    most_orders_by_customer = top_customers[0]['total_purchases']

    result = [f'Most orders made by customer: {most_orders_by_customer}\n','Customers with most orders:']

    #created so the result output will look more detailed
    customers_count = 0

    # itterating through every customer from the query set, check if they orders are equal to the count of customer with most orders
    for customer in top_customers:
        if customer['total_purchases'] == most_orders_by_customer:
            result.append(f'Customer ID: {customer['CustomerID']}')
            customers_count += 1
    result.append(f'Total customers with {most_orders_by_customer} orders - {customers_count} customers')

    return '\n'.join(result)


print(top_customers())



