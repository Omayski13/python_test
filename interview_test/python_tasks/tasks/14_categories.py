import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'interview_test.settings')
django.setup()

from python_tasks.models import Product_Category


def categories():
    #get query set wit all categories
    categories = Product_Category.objects.all()

    result = []
    category_results = []

    #iterate through every category to get the total sales, total discount and total orders and add them to category result list
    for category in categories:
        total_sales = 0
        total_discount = 0
        total_orders = 0

        for subcategory in category.subcategories.all():
            for product in subcategory.subcategory.all():
                for sales_detail in product.products.all():
                    total_sales += sales_detail.LineTotal or 0
                    total_discount += sales_detail.UnitPriceDiscount or 0
                    total_orders += 1

        category_results.append({
            'category': category.Name,
            'total_sales': total_sales,
            'total_discount': total_discount,
            'total_orders': total_orders
        })

    #iterate through category result and add the data to the result list
    for details in category_results:
        result.append(f'\nCategory: {details['category']}')
        result.append(f'Total Sales Amount: {details['total_sales']}')
        result.append(f'Total Discounted Amount: {details['total_discount']}')
        result.append(f'Total Number of Orders: {details['total_orders']}')

    #get the category with the highest sales and orders from the list using anonymos lambda function
    highest_sales_category = max(category_results, key=lambda x: x['total_sales'])
    result.append(f'\nProduct category with the highest sales amount: {highest_sales_category['category']}')

    highest_orders_category = max(category_results, key=lambda x: x['total_orders'])
    result.append(f'\nProduct category with the highest number of orders: {highest_orders_category['category']}')

    return '\n'.join(result)


print(categories())
