import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'interview_test.settings')
django.setup()

from python_tasks.models import Product, Product_Category, Product_Subcategory, Sales, Sales_Details, Special_Offer

#create function to count total records in every table, by default count fucntion is on the primary keys
def count_table_records():

    result = []

    result.append(f'Product total records: {Product.objects.count()}')
    result.append(f'Product Category total records: {Product_Category.objects.count()}')
    result.append(f'Product Subcategory total records: {Product_Subcategory.objects.count()}')
    result.append(f'Sales total records: {Sales.objects.count()}')
    # could not import the data for sales details so this answer is valid only for the project, but not for task 4
    result.append('*' * 20)
    result.append(f'Sales Details total records: {Sales_Details.objects.count()}')
    result.append('*' * 20)
    result.append(f'Special Offer total records: {Special_Offer.objects.count()}')


    return '\n'.join(result)

print(count_table_records())