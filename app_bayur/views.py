from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
import random
import datetime
import time
from datetime import datetime
from app_bayur.models import *
from django.contrib.auth.hashers import make_password,check_password 
from django.shortcuts import redirect
from django.db.models import Q
from django.core.paginator import Paginator
import razorpay 



def login_required_custom(view_func):     # define Decorators
    def wrapper(request, *args, **kwargs):
        try:
            request.session["email"]    # user email
        except:
            return redirect("ERRER")      # Replace 'login' with the URL name of your login page
        return view_func(request, *args, **kwargs)
    return wrapper 

def ERRER(request):
    return render (request,'404.html')
 
# Create your views here.
def index(request):
    try: 
        all_num=Cart.objects.all().count() 
        carrent_login=User.objects.get(email=request.session["Email"])
        all_num=Cart.objects.filter(Q(Bayer_id=carrent_login.id) & Q(status=True)).count() 
        user_data=User.objects.get(email=request.session["email"])
        all_product=Listing_Product.objects.all() 
        return render (request,'index.html',{'msg':user_data.firstname,'msg2':user_data.email,'all_num':all_num,'user_data':user_data,'all_product':all_product,'carrent_login':carrent_login})
    except:  
      all_product=Listing_Product.objects.all() 
      return render (request ,'index.html',{'all_product':all_product})
    
  
def checkemail(view_func):     # define Decorators
    def wrapper(request, *args, **kwargs):
        try:
            request.POST["Email"]    # user email
        except:
           return render (request,'sign_up.html',{'msg':'User allreddy ragistrd please sign in '})      # 
        return view_func(request, *args, **kwargs)
    return wrapper 


def About(request):
    return render(request,'about.html')

def Blog(request):
    return render(request,'blog.html')

def Blog_Details(request):
    return render(request,'blog-details.html')

# @checkemail
# def sign_up(request):
#     global temp,user_otp,start_time
#     all_data=User.objects.all()
#     if request.method == 'POST':
#         if request.POST["password"] == request.POST["cpassword"]:
#                 user_otp=random.randint(10000,99999)
#                 start_time= datetime.now().time()  
#                 subject = 'OTP VERIFICATIONS PROCESS Dukamarkect'
#                 message = f'Verification code Please use the verification code below to sign in. \n\n {user_otp}\n\nfrom django.utils.translation import ungettextIf you didn''t request this,\n you can ignore this email.\n\n Thanks,\n The Dukamarkect team '
#                 email_from = settings.EMAIL_HOST_USER
#                 recipient_list = [request.POST['email'], ]
#                 send_mail(subject, message, email_from, recipient_list )
#                 temp={
#                         "firstname":request.POST['firstname'],
#                         "email":request.POST['email'],
#                         "password":request.POST['password'] 
#                     }
#                 return render (request,'otp.html',{'msg1':'otp valid  120 secound'}) 
#                 # return render (request,'sign_up.html',{'msg':'User allreddy ragistrd please sign in '})  
#         else:   
#             return render (request,'Sign_up.html',{'msg':'password and canfirm password are not match'})              
#     else:
#         return render (request,'Sign_up.html')     


     
def sign_up(request):
    global temp,user_otp,start_time
    if request.method == 'POST':
        if request.POST["password"] == request.POST["cpassword"]:
            try:
                carrent_login = User.objects.get(email=request.POST['email'])
                if request.POST['email'] == carrent_login:
                    return render (request,'sign_up.html',{'msg':'User allreddy ragistrd please sign in ',"carrent_login":carrent_login})
                else:
                    pass
                return render (request,'sign_up.html',{'msg':'User allreddy ragistrd please sign in ',"carrent_login":carrent_login})
            except:
                    user_otp=random.randint(10000,99999)
                    start_time= datetime.now().time()  
                    subject = 'OTP VERIFICATIONS PROCESS Dukamarkect'
                    message = f'Verification code Please use the verification code below to sign in. \n\n {user_otp}\n\nfrom django.utils.translation import ungettextIf you didn''t request this,\n you can ignore this email.\n\n Thanks,\n The Dukamarkect team '
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [request.POST['email'], ]
                    send_mail(subject, message, email_from, recipient_list)
                    temp={
                            "firstname":request.POST['firstname'],
                            "email":request.POST['email'],
                            "password":request.POST['password'] 
                        } 
                    return render (request,'otp.html',{'msg1':'otp valid secound'})   
        else:   
            return render (request,'Sign_up.html',{'msg':'password and canfirm password are not match'})              
    else:
        return render (request,'Sign_up.html')     
@login_required_custom 
def Search_for_products(request):
    carrent_login=User.objects.get(email=request.session["Email"])
    all_num=Cart.objects.filter(Q(Bayer_id=carrent_login.id) & Q(status=True))
    if request.method == 'POST':
        quary=request.POST['search']
        all_product=Listing_Product.objects.filter(Q(P_name__icontains=quary) | Q(P_Description__icontains=quary)) 
        if all_product.count()==0:  # product count
            return render (request,"product.html",{"msg":"sorry product not found.."})
        else:
            return render (request,"product.html",{'all_product':all_product,'carrent_login':carrent_login}) 
 
       
def otp(request):
    if request.method == "POST": 
        if user_otp == int(request.POST["otp"]):
            end_time = datetime.now().time()
            time_diff = datetime.combine(datetime.today(),end_time) - datetime.combine(datetime.today(), start_time)   
            second_diff= time_diff.total_seconds() 
            if second_diff < 120:  
                User.objects.create(
                firstname=temp['firstname'],
                email=temp['email'],
                password=make_password(temp["password"])
            )
                return render (request,'Sign_up.html',{'msg1':'Register is successfully'})
            else:
                return render (request,"Sign_up.html",{"msg1":"your OTP has expired"})
        else:
            return render (request,'otp.html',{'msg1':'otp is not match'})      
    else:
        return render (request,'otp.html')
 

def sign_in(request):
    if request.method == 'POST':
        carrent_login=User.objects.get(email=request.POST["Email"])      
        try:
            if check_password(request.POST["password"],carrent_login.password):
                request.session["Email"] = request.POST["Email"]
                return render(request,'index.html',{'msg1':carrent_login.email,"carrent_login":carrent_login})
            else:
                return render(request,'sign_in.html',{'msg1':'Your Information  Not Match TRY AGEAN '})
        except:
            return render(request,'sign_in.html',{'msg1':'User Not Exist Plese Registration'})
    else:
        return render(request,'sign_in.html') 
        
   
def Logout(request):
    del request.session['Email']
    return render (request,'sign_in.html',{'msg1':'user logout successfully'})


def profial(request):  
    carrent_login=User.objects.get(email=request.session["Email"])
    all_num=Cart.objects.filter(Q(Bayer_id=carrent_login.id) & Q(status=True))
    if request.method=='POST':
        carrent_login=User.objects.get(email=request.session["Email"])
        try:
            profile_im=request.FILES["immage"] 
        except:
            profile_im=carrent_login.image   
        if request.POST['oldpassword']:
            if (check_password(request.POST['oldpassword'],carrent_login.password)):
                if request.POST['newpassword'] == request.POST['canfirmpassword']:
                    carrent_login.firstname=request.POST['firstname']
                    carrent_login.image=profile_im 
                    carrent_login.password=make_password(request.POST['newpassword'])
                    carrent_login.save()
                    return render(request, 'profial.html', {'carrent_login':carrent_login,'msg3':carrent_login.email,'msg' : 'profial update is sucessfully'})
                else:
                    return render(request, 'profial.html', {'carrent_login':carrent_login,'msg3':carrent_login.email,'msg' : 'New Password and Confirm New Password Not Matching'})
            else:
                return render (request,'profial.html',{'carrent_login':carrent_login,'msg3':carrent_login.email,"msg":'old password are not match'})
        else:
            carrent_login.firstname=request.POST['firstname']
            carrent_login.image=profile_im
            carrent_login.save()
            carrent_login=User.objects.get(email=request.session["Email"])
            return render (request,'profial.html',{'carrent_login':carrent_login,'msg3':carrent_login.email,"msg":'profial update is successfully '})
    else:
        return render (request,'profial.html',{'carrent_login':carrent_login,'all_num':all_num})
     
# =======================================================================================================
def contact(request):
    return render(request,'contact.html')

def errer404(request):
    return render(request,'404.html')


def faq(request):
    return render(request,'faq.html')

def seller(request):
    return render (request,'seller_index.html')

def Bayur(request):
    return render (request,'index.html')

def seller_signup(request):
    if request.method == 'POST':
        global temp,seller_otp,start_time
    if request.method == 'POST':
        if request.POST["Seller_password"] == request.POST["Seller_cpassword"]:
            try:
                seller_login = User.objects.get(email=request.POST['Seller_email'])
                if request.POST['Seller_email'] == seller_login:
                    return render (request,'seller_signup.html',{'msg':'User allreddy ragistrd please sign in ',"seller_login":seller_login})
            except:
                    list1=['c','t','4','q','o','4','0','a','1']
                    a=random.choices(list1,k=5)
                    seller_otp=''.join(a)
                    print(seller_otp)  
                    subject = 'OTP VERIFICATIONS PROCESS Dukamarkect'
                    message = f'Verification code Please use the verification code below to sign in. \n\n {seller_otp}\n\nfrom django.utils.translation import ungettextIf you didn''t request this,\n you can ignore this email.\n\n Thanks,\n The Dukamarkect team '
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [request.POST['Seller_email']]
                    send_mail(subject,message, email_from, recipient_list)
                    temp={
                            "Seller_firstname":request.POST['Seller_firstname'],
                            "Seller_email":request.POST['Seller_email'],
                            "Seller_password":request.POST['Seller_password'] 
                        } 
                    return render (request,'seller_otp.html',{'msg1':'otp valid secound'})   
        else:   
            return render (request,'seller_signup.html',{'msg':'password and canfirm password are not match'})              
    else:
        return render (request,'seller_signup.html') 

def seller_otp(request):
    if request.method == "POST": 
        if seller_otp == (request.POST["otp"]):
            Seller_User.objects.create(
            Seller_firstname=temp['Seller_firstname'],
            Seller_email=temp['Seller_email'],
            Seller_password=make_password(temp["Seller_password"])
        )
            return render (request,'seller_signup.html',{'msg1':'Register is successfully'})
        else:
            return render (request,'seller_otp.html',{'msg1':'otp is not match'})      
    else:
        return render (request,'seller_otp.html')


def seller_signin(request):
    if request.method == 'POST': 
        try:
            seller_login=Seller_User.objects.get(Seller_email=request.POST["Seller_email"])      
            if check_password(request.POST["Seller_password"],seller_login.Seller_password):
                request.session["Seller_email"] = request.POST["Seller_email"] 
                return render(request,'seller_index.html',{'msg2':seller_login.Seller_email,"seller_login":seller_login})
            else:
                return render(request,'seller_signin.html',{'msg1':'Your password are not match '})
        except:
            return render(request,'seller_signin.html',{'msg1':'User not exist plese registration'})
    else:
        return render(request,'seller_signin.html') 


def seller_logout(request):
    del request.session["Seller_email"]
    return render (request,'seller_signin.html',{'msg1':'User logout is successfully'})


def Seller_Listing(request):
    seller_login=Seller_User.objects.get(Seller_email=request.session["Seller_email"])      
    if request.method == 'POST':
        Selected_color=request.POST.getlist('P_Color')
        Selected_color_str=",".join(Selected_color) 
        try:
            request.FILES['Listing_immage'] 
            Listing_Product.objects.create(
                Listing_immage=request.FILES['Listing_immage'],
                P_name=request.POST['P_name'],
                P_Price=request.POST['P_Price'],
                P_sellprice=request.POST['P_sellprice'], 
                P_Quntity=request.POST['P_Quntity'],
                P_Color=Selected_color_str,
                P_Categary=request.POST['P_Categary'],
                P_Description=request.POST['P_Description'],
                seller_id=seller_login  
                )
            return render(request,'seller_listing.html',{'msg':'Data add is successfully...','seller_login':seller_login})  
        except:
             Listing_Product.objects.create(
                Listing_immage=request.FILES['Listing_immage'],
                P_name=request.POST['P_name'],
                P_Price=request.POST['P_Price'],
                P_sellprice=request.POST['P_sellprice'], 
                P_Quntity=request.POST['P_Quntity'],
                P_Color=Selected_color_str,
                P_Categary=request.POST['P_Categary'],
                P_Description=request.POST['P_Description'],
                seller_id=seller_login  
             )
             return render(request,'seller_listing.html',{'msg':'Data add is successfully...','seller_login':seller_login})  
    else:
         color=Listing_Product.Color
         return render (request,'seller_listing.html',{"color":color})


def Show_Listing(request):
    seller_login=Seller_User.objects.get(Seller_email=request.session["Seller_email"])      
    alldata=Listing_Product.objects.all()
    return render (request,'seller_Listing_Table.html',{'seller_login':seller_login,'alldata':alldata})


def Seller_update_Listing(request,ck):
    seller_login=Seller_User.objects.get(Seller_email=request.session["Seller_email"]) 
    Singal_data=Listing_Product.objects.get(id=ck)
    if request.method == 'POST':
        Selected_choice_color=request.POST.getlist('P_Color')
        Selected_choice_color_str=",".join( Selected_choice_color)
        Singal_data=Listing_Product.objects.get(id=ck)
        try:
             listing_im=request.FILES['Listing_immage']
        except:
            listing_im=Singal_data.Listing_immage
                              
        Singal_data.Listing_immage=listing_im
        Singal_data.P_name=request.POST['P_name']
        Singal_data.P_Price=request.POST['P_Price']
        Singal_data.P_sellprice=request.POST['P_sellprice'] 
        Singal_data.P_Quntity=request.POST['P_Quntity'] 
        Singal_data.P_Color=Selected_choice_color_str 
        Singal_data.P_Categary=request.POST['P_Categary']
        Singal_data.P_Description=request.POST['P_Description']
        Singal_data.save() 
        return Show_Listing(request)  
    else:
        color=Listing_Product.Color
        Singal_data=Listing_Product.objects.get(id=ck)
        list_color=Singal_data.P_Color.split(",")
        return render(request,'Seller_update_listing.html',{'seller_login':seller_login,"Singal_data":Singal_data,'color':color,'list_color':list_color})
    
    
def Seller_Delete_Listing(request,ck):
    seller_login=Seller_User.objects.get(Seller_email=request.session["Seller_email"])      
    Singal_data=Listing_Product.objects.get(id=ck)
    Singal_data.delete()
    return Show_Listing(request) 


def shop(request):
    carrent_login=User.objects.get(email=request.session["Email"])
    all_num=Cart.objects.filter(Q(Bayer_id=carrent_login.id) & Q(status=True)).count()       
    all_product=Listing_Product.objects.all()
    return render(request,"product.html",{'all_product':all_product,'all_num':all_num})

          
def singal_pruduct(request,ck):
    carrent_login=User.objects.get(email=request.session["Email"])
    all_num=Cart.objects.filter(Q(Bayer_id=carrent_login.id) & Q(status=True))         
    one_product=Listing_Product.objects.get(id=ck)
    return render(request,'product-details.html',{"one_product":one_product,"colors":one_product.P_Color.split(","),'all_num':all_num})
    

def Add_cart(request,ck):
    Current_Login=User.objects.get(email=request.session['Email'])
    # if request.method == 'POST':
    try:
        Product=Listing_Product.objects.get(id=ck)
        allredy_data=Cart.objects.get(Q(Product_id=ck) & Q(Bayer_id=Current_Login.id)) 
        allredy_data.Quntity+=1  
        allredy_data.Total=allredy_data.Quntity * allredy_data.Product_id.P_Price
        allredy_data.save() 
        return show_cart(request)  
    except:
        Product=Listing_Product.objects.get(id=ck)
        Cart.objects.create(
            Product_id=Product,
            Bayer_id=Current_Login,
            Quntity=1,
            Total=Product.P_Price,
        )
        return show_cart(request)  
 
              
def show_cart(request):
    carrent_login=User.objects.get(email=request.session["Email"])
    all_cart=Cart.objects.filter(Q(Bayer_id=carrent_login.id) & Q(status=True))
    all_num=Cart.objects.filter(Q(Bayer_id=carrent_login.id) & Q(status=True)).count()
    sub_total=0
    Net_amount=0
    if all_cart:
        for i in all_cart:
            sub_total=sub_total+i.Total
            Net_amount=sub_total       
    return render (request,'cart.html',{'carrent_login':carrent_login,'all_cart':all_cart,'sub_total':sub_total,'Net_amount':Net_amount,'all_num':all_num})


def Remove_cart(request,ck):
    Cart_data=Cart.objects.get(id=ck)
    Cart_data.delete()
    return redirect ('show_cart')

   
def continue_shoping(request):
    carrent_login=User.objects.get(email=request.session["Email"])
    return shop (request)
    
 
def Update_cart(request):
    if request.method == 'POST':
        try:
            carrent_login=User.objects.get(email=request.session["Email"])
            user_cart=Cart.objects.filter(Q(Bayer_id=carrent_login.id) & Q(status=True)) 
            list_data = request.POST.getlist("UpdateQuntity")
            if len(list_data) == user_cart.count():
                for i, j in zip(user_cart, list_data):
                    i.Quntity = int(j)
                    i.Total = int(j) * i.Product_id.P_Price
                    i.save()
                return redirect('show_cart')
            else:
                return redirect('show_cart')
        except:
            return redirect('show_cart')
    else:
        return redirect('show_cart')  

    
def checkout(request):
    carrent_login=User.objects.get(email=request.session["Email"])
    all_num=Cart.objects.filter(Q(Bayer_id=carrent_login.id) & Q(status=True)).count()
    all_cart=Cart.objects.filter(Bayer_id=carrent_login.id)
    sub_total=0
    Net_amount=0
    if all_cart:
        for i in all_cart:
            sub_total=sub_total+i.Total
            Net_amount=sub_total     
        print ("all cart",all_cart,"sub total ",sub_total,'net amount',Net_amount )
    carrent_login=User.objects.get(email=request.session["Email"])
    return render (request,'checkout.html',{'carrent_login':carrent_login,'all_cart':all_cart,'sub_total':sub_total,'Net_amount':Net_amount,'all_num':all_num})


def CheckoutDetels(request):
    carrent_login=User.objects.get(email=request.session["Email"])
    all_num=Cart.objects.filter(Q(Bayer_id=carrent_login.id) & Q(status=True)).count()
    list1=['c','q','r','r','x','t' ,'_','5','6','9','9']
    a=random.choices(list1,k=10) 
    user_order="".join(a)  
    if request.method == 'POST':
            CheckoutDetals.objects.create(
                firstname=request.POST['firstname'],
                lastname=request.POST['lastname'],
                email=request.POST['email'],
                mobile_no=request.POST['C_number'],
                address1=request.POST['address1'],
                address2=request.POST['address2'],
                City=request.POST['city'],
                ZIPCode=request.POST['zipcode'],
                order_id=user_order,
                bayer_detials=carrent_login
            )
            one_data=CheckoutDetals.objects.get(bayer_detials=carrent_login)
            all_cart=Cart.objects.filter(Q(Bayer_id=carrent_login.id) & Q(status=True))
            for i in all_cart:
                i.Details_id=one_data
                i.save()
                return render (request,'checkout.html',{'one_data':one_data,'all_cart':all_cart,'msg':'data add is successflly '})
    else:  
        return render (request,'checkout.html')
    
    
from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest


# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))





# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):

	# only accept POST request.
	if request.method == "POST":
		try:
		
			# get the required parameters from post request.
			payment_id = request.POST.get('razorpay_payment_id', '')
			razorpay_order_id = request.POST.get('razorpay_order_id', '')
			signature = request.POST.get('razorpay_signature', '')
			params_dict = {
				'razorpay_order_id': razorpay_order_id,
				'razorpay_payment_id': payment_id,
				'razorpay_signature': signature
			}

			# verify the payment signature.
			result = razorpay_client.utility.verify_payment_signature(
				params_dict)
			if result is not None:
				amount = 20000 # Rs. 200
				try:

					# capture the payemt
					razorpay_client.payment.capture(payment_id, amount)

					# render success page on successful caputre of payment
					return render(request, 'paymentsuccess.html')
				except:

					# if there is an error while capturing payment.
					return render(request, 'paymentfail.html')
			else:

				# if signature verification fails.
				return render(request, 'paymentfail.html')
		except:

			# if we don't find the required parameters in POST data
			return HttpResponseBadRequest()
	else:
	# if other than POST request is made.
		return HttpResponseBadRequest()

      
def all_delete(request):

    Current_Login=User.objects.get(email=request.session["email"])
    all_cart=Cart.objects.filter(Q(Bayer_id=Current_Login.id) & Q(status=True))
    for i in all_cart:
        one_data=Listing_Product.objects.get(id=i.Product_id.id)
        one_data.P_Quntity=int(one_data.P_Quntity)-i.Quntity
        i.status=False    # data cart in remove
        i.save()
        one_data.save()
    # all_cart.delete()
    # return render(request,"payment_success.html")
    return shop(request)    

def Categary(request,ck):
    carrent_login=User.objects.get(email=request.session["Email"])  
    all_product=Listing_Product.objects.filter(P_Categary=ck)  
    if all_product.count() == 0:
            return render (request,'product.html',{'msg4':'Product Not Found'})
    
    return render (request,'product.html',{'carrent_login':carrent_login,'all_product':all_product})     
     
    

def Color(request,ck):
    carrent_login=User.objects.get(email=request.session["Email"])  
    all_product=Listing_Product.objects.filter(P_Color=ck)  
    if all_product.count() == 0:
            return render (request,'product.html')
    
    return render (request,'product.html')     
     
