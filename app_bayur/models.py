from django.db import models

# Create your models here.
class User(models.Model):
    firstname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50,unique=True)
    password=models.CharField(max_length=1000)
    image=models.FileField(upload_to='media/',default='/abc.jpg')
    
    def __str__(self):
        return self.firstname
     
class Seller_User(models.Model):
    Seller_firstname=models.CharField(max_length=50)
    Seller_email=models.EmailField(max_length=50,unique=True)
    Seller_password=models.CharField(max_length=1000)
    Seller_image=models.FileField(upload_to='media/',default='media/abc.jpg')
    
    def __str__(self):
        return self.Seller_firstname

class Listing_Product(models.Model):
    # user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True) # authentication
    Listing_immage=models.FileField(upload_to='Listing/',default="/abc.jpg")
    P_name=models.CharField(max_length=100)
    P_Price=models.IntegerField(default=0)
    P_sellprice=models.CharField(max_length=100)
    P_Quntity=models.IntegerField(default=0)
    
    Color = [('Black', 'Black'),('White', 'White'),('Red', 'Red'),('Blue', 'Blue'),('Green', 'Green')]
    P_Color=models.CharField(choices=Color,max_length=100, blank=True )
    P_Description=models.CharField(max_length=500)
    P_Categary=models.CharField(max_length=50,null=True)
    seller_id=models.ForeignKey(Seller_User,on_delete=models.CASCADE)

    def __str__(self):
        return self.P_name 
    
class Cart(models.Model):
    Product_id=models.ForeignKey(Listing_Product,on_delete=models.CASCADE)
    Bayer_id=models.ForeignKey(User,on_delete=models.CASCADE) 
    Quntity=models.IntegerField(default=0)
    product_color=models.CharField(max_length=50)
    Total=models.IntegerField(default=0)
    status=models.BooleanField(default=True)



    def __str__(self):
        return str(self.Product_id)
    
class CheckoutDetals(models.Model):
    firstname=models.CharField(max_length=50)  
    lastname=models.CharField(max_length=50)  
    email=models.EmailField(max_length=20)
    mobile_no=models.IntegerField(default=0)
    address1=models.CharField(max_length=1000)
    address2=models.CharField(max_length=1000)
    City=models.CharField(max_length=50)
    State=models.CharField(max_length=50)  
    Country=models.CharField(max_length=50)
    ZIPCode=models.IntegerField(default=0)
    bayer_detials=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    order_id=models.CharField(max_length=50)
        
    def __str__(self):
        return self.firstname  
        
        