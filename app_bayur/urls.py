
from django.urls import path
from app_bayur import views


urlpatterns = [
  path('', views.index, name='index'),
  path('sign_up/', views.sign_up, name='sign_up'),
  path('otp/', views.otp, name='otp'),
  path('sign_in/', views.sign_in, name='sign_in'),
  path('Logout/', views.Logout, name='Logout'),
  path('profial/', views.profial, name='profial'),
  path('seller/', views.seller, name='seller'),
  path('Bayur/', views.Bayur, name='Bayur'),
  path('seller_signup/', views.seller_signup, name='seller_signup'),
  path('seller_signin/', views.seller_signin, name='seller_signin'),
  path('seller_otp/', views.seller_otp, name='seller_otp'),
  path('seller_logout/', views.seller_logout, name='seller_logout'),
  path('Seller_Listing/', views.Seller_Listing, name='Seller_Listing'),
  path('Show_Listing/', views.Show_Listing, name='Show_Listing'),
  path('Seller_update_Listing/<int:ck>', views.Seller_update_Listing, name='Seller_update_Listing'),
  path('Seller_Delete_Listing/<int:ck>', views.Seller_Delete_Listing, name='Seller_Delete_Listing'),
  path('shop', views.shop, name='shop'),
  path('contact', views.contact, name='contact'),
  path('faq', views.faq, name='faq'),
  path('errer404', views.errer404, name='errer404'),
  path('singal_pruduct/<int:ck>', views.singal_pruduct, name='singal_pruduct'),
  path('singal_pruduct', views.singal_pruduct, name='singal_pruduct'),
  path('Add_cart/<int:ck>', views.Add_cart, name='Add_cart'),
  path('ERRER', views.ERRER, name='ERRER'),
  path('About', views.About, name='About'),
  path('Blog', views.Blog, name='Blog'),
  path('Blog_Details', views.Blog_Details, name='Blog_Details'),
  path('show_cart', views.show_cart, name='show_cart'),
  path('Remove_cart/<int:ck>', views.Remove_cart, name='Remove_cart'),
  path('continue_shoping', views.continue_shoping, name='continue_shoping'),
  path('Update_cart', views.Update_cart, name='Update_cart'),
  path('checkout', views.checkout, name='checkout'),
  path('CheckoutDetels', views.CheckoutDetels, name='CheckoutDetels'),
  path('Search_for_products', views.Search_for_products, name='Search_for_products'),
  path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
  path('Categary/<str:ck>', views.Categary, name='Categary'),
  path('Color/<str:ck>', views.Color, name='Color'),

  
]