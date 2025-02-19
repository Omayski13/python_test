from django.db import models
from django.core.validators import MinValueValidator
from python_tasks.mixins import ModifiedDataMixin


class Product_Category(ModifiedDataMixin):   #Python convention ProductCategory
    ProductCategoryID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    rowguid = models.CharField(max_length=50)


class Product_Subcategory(ModifiedDataMixin):    #Python convention ProductSubcategory
    ProductSubcategoryID = models.AutoField(primary_key=True)
    ProductCategory = models.ForeignKey(Product_Category, related_name='subcategories', on_delete=models.CASCADE)
    Name = models.CharField(max_length=255)
    rowguid = models.CharField(max_length=50)


class Product(ModifiedDataMixin):
    ProductID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, blank=True, null=True)
    ProductNumber = models.CharField(max_length=50,blank=True, null=True)
    MakeFlag = models.BooleanField(default=False,blank=True, null=True)
    FinishedGoodsFlag = models.BooleanField(default=False,blank=True, null=True)
    Color = models.CharField(max_length=50, blank=True, null=True)
    SafetyStockLevel = models.IntegerField(default=0,blank=True, null=True)
    ReorderPoint = models.IntegerField(default=0,blank=True, null=True)
    StandardCost = models.DecimalField(max_digits=10, decimal_places=4, default=0.0000,blank=True, null=True)
    ListPrice = models.DecimalField(max_digits=10, decimal_places=4, default=0.0000,blank=True, null=True)
    Size = models.IntegerField(null=True, blank=True)
    SizeUnitMeasureCode = models.CharField(max_length=50, blank=True, null=True)
    WeightUnitMeasureCode = models.CharField(max_length=50, blank=True, null=True)
    Weight = models.DecimalField(max_digits=5, decimal_places=2, default=0.00,blank=True, null=True)
    DaysToManufacture = models.IntegerField(default=0,blank=True, null=True)
    ProductLine = models.CharField(max_length=50, blank=True, null=True)
    Class = models.CharField(max_length=50, blank=True, null=True)
    Style = models.CharField(max_length=50, blank=True, null=True)
    ProductSubcategoryID = models.ForeignKey(Product_Subcategory, related_name="subcategory", on_delete=models.CASCADE,null=True, blank=True,)
    ProductModelID = models.IntegerField(null=True, blank=True)
    SellStartDate = models.DateTimeField(null=True, blank=True)
    SellEndDate = models.DateTimeField(null=True, blank=True)
    DiscontinuedDate = models.DateTimeField(null=True, blank=True)
    rowguid = models.CharField(max_length=50,null=True, blank=True)

class Territory(ModifiedDataMixin):
    TerritoryID = models.AutoField(primary_key=True)
    CountryName = models.CharField(max_length=50)
    CountryCapital = models.CharField(max_length=50)
    Population = models.IntegerField(validators=[MinValueValidator(0)])

class Sales(ModifiedDataMixin):
    SalesOrderID = models.AutoField(primary_key=True)
    RevisionNumber = models.IntegerField(null=True, blank=True)
    OrderDate = models.DateTimeField(null=True, blank=True)
    DueDate = models.DateTimeField(null=True, blank=True)
    ShipDate = models.DateTimeField(null=True, blank=True)
    Status = models.IntegerField(null=True, blank=True)
    OnlineOrderFlag = models.BooleanField(default=False,null=True, blank=True)
    SalesOrderNumber = models.CharField(max_length=50,null=True, blank=True)
    PurchaseOrderNumber = models.CharField(max_length=50,null=True, blank=True)
    AccountNumber = models.CharField(max_length=50,null=True, blank=True)
    CustomerID = models.IntegerField(null=True, blank=True)
    SalesPersonID = models.IntegerField(null=True, blank=True)
    TerritoryID = models.ForeignKey(Territory, on_delete=models.CASCADE, null=True, blank=True)
    BillToAddressID = models.IntegerField(null=True, blank=True)
    ShipToAddressID = models.IntegerField(null=True, blank=True)
    ShipMethodID = models.IntegerField(null=True, blank=True)
    CreditCardID = models.IntegerField(null=True, blank=True)
    CreditCardApprovalCode = models.CharField(max_length=50, null=True, blank=True)
    CurrencyRateID = models.IntegerField(null=True, blank=True)
    SubTotal = models.DecimalField(max_digits=18, decimal_places=4,null=True, blank=True)
    TaxAmt = models.DecimalField(max_digits=18, decimal_places=4,null=True, blank=True)
    Freight = models.DecimalField(max_digits=18, decimal_places=4,null=True, blank=True)
    TotalDue = models.DecimalField(max_digits=18, decimal_places=4,null=True, blank=True)
    Comment = models.TextField(null=True, blank=True)
    rowguid = models.CharField(max_length=50,null=True, blank=True)



class Special_Offer(ModifiedDataMixin):    #Python convention SpecialOffer
    SpecialOfferID = models.AutoField(primary_key=True)
    Description = models.CharField(max_length=255)
    DiscountPct = models.DecimalField(max_digits=5, decimal_places=2)  # Discount as a percentage
    Type = models.CharField(max_length=50)
    Category = models.CharField(max_length=50)
    StartDate = models.DateTimeField()
    EndDate = models.DateTimeField()
    MinQty = models.IntegerField()
    MaxQty = models.IntegerField(null=True, blank=True)  # MaxQty can be null
    rowguid = models.CharField(max_length=50)



class Sales_Details(ModifiedDataMixin):    #Python convention SalesDetails
    SalesOrderDetailID = models.AutoField(primary_key=True)
    SalesOrder = models.ForeignKey(Sales, on_delete=models.CASCADE, related_name='sales_orders',null=True, blank=True)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products',null=True, blank=True)
    SpecialOffer = models.ForeignKey(Special_Offer, on_delete=models.CASCADE, related_name='special_offers',null=True, blank=True)
    CarrierTrackingNumber = models.CharField(max_length=50,null=True, blank=True)
    OrderQty = models.IntegerField(null=True, blank=True)
    UnitPrice = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True)
    UnitPriceDiscount = models.DecimalField(max_digits=5, decimal_places=2, default=0,null=True, blank=True)
    LineTotal = models.DecimalField(max_digits=15, decimal_places=4,null=True, blank=True)
    rowguid = models.CharField(max_length=50,null=True, blank=True)




