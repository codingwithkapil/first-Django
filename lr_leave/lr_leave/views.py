from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.views import View
from django.urls import reverse
from .models import  Add_client,Visiting_card, Broucher,id_card,entry_pass,invitation_card,pamplate,latter_head_box,envelope,payment,notes
from django.views.decorators.csrf import csrf_protect
from django.db import connection
import random
from django.contrib.auth.hashers import make_password
import math

def view_quotation(request):
    data=Visiting_card.objects.all()
    d={
        'data':data,
    }
    return render(request,'view_quotation.html',d)
def create_quotation(request):
    product={"1":visiting_card,"2":Id_card,"3":Entry_pass,"4":Invitation_card,"5":broucher,"6":Pamplate,"7":Latter_head_box,"8":Envelope}
    final_data=""
    if request.method=='POST':
        client_name=request.POST['clientname']
        item_name=request.POST['product']
        sub_item_name=request.POST['sub_product']
        qty=request.POST['qnty']
        s1=request.POST['box_height']
        s2=request.POST['box_width']
        maxbox=request.POST['maxbox']
        
        final_data=product[item_name](client_name,sub_item_name,qty,s1,s2,maxbox)
    return HttpResponseRedirect('/invoice/'+final_data+'/')

def Id_card(a,b,c,d,e,f):
    c_name=a
    s_item=b
    qty=c
    s1=int(d)
    s2=int(e)
    maxbox=int(f)
    x=int(qty)/maxbox
    qtys=int(math.ceil(x))
    
    product="id card"
    title=qty+" "+product+" "+str(s_item)+"/ "+str(s1)+"X"+str(s2)
    sheet=(qtys*8)+80
    sub_details1=str(s1)+"X"+str(s2)+" sheet 300gsm white mat card sheet"
    sub_details_price1=sheet*8
    
    qty1=str(sheet)
    rate1=str(8)
    
    
    sub_details2="Page Design"
    sub_details_price2=16*200
    qty2=str(16)
    rate2=str(200)

    sub_details3="Colour Printout"
    sub_details_price3=8*50
    qty3=str(8)
    rate3=str(50)

    sub_details4="Plate 19x26"
    a=(((sheet-80)*4)/1000)
    sub_details_price4=a*400
    
    qty4=str(a)
    rate4=str(400)

    sub_details5="Set Ptg"
    a=a/4
    sub_details_price5=a*1000
    
    qty5=str(a)
    rate5=str(1000)

    sub_details6="Mat Lamination"
    sub_details_price6=(sheet*s1*s2*2)*.00667
    
    qty6=str(sheet)+"x"+str(s1)+"x"+str(s2)+"x"+"2"
    rate6=".00667"

    sub_details7="UV output"
    sub_details_price7=qtys*.1
    
    qty7=str(qtys)
    rate7=".1"

    sub_details8="Front and Back UV Printing"
    sub_details_price8=sheet*1.5
    
    qty8=str(sheet)
    rate8="1.5"

    sub_details9="creasing"
    sub_details_price9=(qtys*2)*.2
    a=qtys*2
    qty9=str(a)
    rate9=".2"

    sub_details10="Book Binding"
    sub_details_price10=(qtys/2)*2
    a=(qtys/2)
    qty10=str(a)
    rate10=str(2)


    total=sub_details_price1+sub_details_price2+sub_details_price3+sub_details_price4+sub_details_price5+sub_details_price6+sub_details_price7+sub_details_price8+sub_details_price9+sub_details_price10
    c_detail=Add_client.objects.filter(c_name=c_name)
    random_value="ID"+str(random.randint(0,99999999999))
    
    c_name=""
    c_number=""
    c_address=""
    c_email=""
    for a in c_detail:
        c_name=a.c_name
        c_number=a.c_number
        c_address=a.c_address
        c_email=a.c_email
    brou=id_card(c_name=c_name,c_number=c_number,c_email=c_email,c_address=c_address,order_id=random_value,qty=qty,title=title,sub_details1=sub_details1,sub_details2=sub_details2,sub_details3=sub_details3,sub_details4=sub_details4,sub_details5=sub_details5,sub_details6=sub_details6,sub_details7=sub_details7,sub_details8=sub_details8,sub_details9=sub_details9,sub_details10=sub_details10,sub_detail_price1=sub_details_price1,sub_detail_price2=sub_details_price2,sub_detail_price3=sub_details_price3,sub_detail_price4=sub_details_price4,sub_detail_price5=sub_details_price5,sub_detail_price6=sub_details_price6,sub_detail_price7=sub_details_price7,sub_detail_price8=sub_details_price8,sub_detail_price9=sub_details_price9,sub_detail_price10=sub_details_price10,qty1=qty1,qty2=qty2,qty3=qty3,qty4=qty4,qty5=qty5,qty6=qty6,qty7=qty7,qty8=qty8,qty9=qty9,qty10=qty10,rate1=rate1,rate2=rate2,rate3=rate3,rate4=rate4,rate5=rate5,rate6=rate6,rate7=rate7,rate8=rate8,rate9=rate9,rate10=rate10,total=total)
    brou.save()
    
    return random_value

def Entry_pass(a,b,c,d,e,f):
    c_name=a
    s_item=b
    qty=c
    s1=int(d)
    s2=int(e)
    maxbox=int(f)
    x=int(qty)/maxbox
    qtys=int(math.ceil(x))
    
    product="entry_pass"
    title=qty+" "+product+" "+str(s_item)+"/ "+str(s1)+"X"+str(s2)
    sheet=(qtys*8)+80
    sub_details1=str(s1)+"X"+str(s2)+" sheet 300gsm white mat card sheet"
    sub_details_price1=sheet*8
    
    qty1=str(sheet)
    rate1=str(8)
    
    
    sub_details2="Page Design"
    sub_details_price2=16*200
    qty2=str(16)
    rate2=str(200)

    sub_details3="Colour Printout"
    sub_details_price3=8*50
    qty3=str(8)
    rate3=str(50)

    sub_details4="Plate 19x26"
    a=(((sheet-80)*4)/1000)
    sub_details_price4=a*400
    
    qty4=str(a)
    rate4=str(400)

    sub_details5="Set Ptg"
    a=a/4
    sub_details_price5=a*1000
    
    qty5=str(a)
    rate5=str(1000)

    sub_details6="Mat Lamination"
    sub_details_price6=(sheet*s1*s2*2)*.00667
    
    qty6=str(sheet)+"x"+str(s1)+"x"+str(s2)+"x"+"2"
    rate6=".00667"

    sub_details7="UV output"
    sub_details_price7=qtys*.1
    
    qty7=str(qtys)
    rate7=".1"

    sub_details8="Front and Back UV Printing"
    sub_details_price8=sheet*1.5
    
    qty8=str(sheet)
    rate8="1.5"

    sub_details9="creasing"
    sub_details_price9=(qtys*2)*.2
    a=qtys*2
    qty9=str(a)
    rate9=".2"

    sub_details10="Book Binding"
    sub_details_price10=(qtys/2)*2
    a=(qtys/2)
    qty10=str(a)
    rate10=str(2)


    total=sub_details_price1+sub_details_price2+sub_details_price3+sub_details_price4+sub_details_price5+sub_details_price6+sub_details_price7+sub_details_price8+sub_details_price9+sub_details_price10
    c_detail=Add_client.objects.filter(c_name=c_name)
    random_value="EP"+str(random.randint(0,99999999999))
    
    c_name=""
    c_number=""
    c_address=""
    c_email=""
    for a in c_detail:
        c_name=a.c_name
        c_number=a.c_number
        c_address=a.c_address
        c_email=a.c_email
    brou=entry_pass(c_name=c_name,c_number=c_number,c_email=c_email,c_address=c_address,order_id=random_value,qty=qty,title=title,sub_details1=sub_details1,sub_details2=sub_details2,sub_details3=sub_details3,sub_details4=sub_details4,sub_details5=sub_details5,sub_details6=sub_details6,sub_details7=sub_details7,sub_details8=sub_details8,sub_details9=sub_details9,sub_details10=sub_details10,sub_detail_price1=sub_details_price1,sub_detail_price2=sub_details_price2,sub_detail_price3=sub_details_price3,sub_detail_price4=sub_details_price4,sub_detail_price5=sub_details_price5,sub_detail_price6=sub_details_price6,sub_detail_price7=sub_details_price7,sub_detail_price8=sub_details_price8,sub_detail_price9=sub_details_price9,sub_detail_price10=sub_details_price10,qty1=qty1,qty2=qty2,qty3=qty3,qty4=qty4,qty5=qty5,qty6=qty6,qty7=qty7,qty8=qty8,qty9=qty9,qty10=qty10,rate1=rate1,rate2=rate2,rate3=rate3,rate4=rate4,rate5=rate5,rate6=rate6,rate7=rate7,rate8=rate8,rate9=rate9,rate10=rate10,total=total)
    brou.save()
    
    return random_value
   
def Invitation_card(a,b,c,d,e,f):
    c_name=a
    s_item=b
    qty=c
    s1=int(d)
    s2=int(e)
    maxbox=int(f)
    x=int(qty)/maxbox
    qtys=int(math.ceil(x))
    
    product="invitation card"
    title=qty+" "+product+" "+str(s_item)+"/ "+str(s1)+"X"+str(s2)
    sheet=(qtys*8)+80
    sub_details1=str(s1)+"X"+str(s2)+" sheet 300gsm white mat card sheet"
    sub_details_price1=sheet*8
    
    qty1=str(sheet)
    rate1=str(8)
    
    
    sub_details2="Page Design"
    sub_details_price2=16*200
    qty2=str(16)
    rate2=str(200)

    sub_details3="Colour Printout"
    sub_details_price3=8*50
    qty3=str(8)
    rate3=str(50)

    sub_details4="Plate 19x26"
    a=(((sheet-80)*4)/1000)
    sub_details_price4=a*400
    
    qty4=str(a)
    rate4=str(400)

    sub_details5="Set Ptg"
    a=a/4
    sub_details_price5=a*1000
    
    qty5=str(a)
    rate5=str(1000)

    sub_details6="Mat Lamination"
    sub_details_price6=(sheet*s1*s2*2)*.00667
    
    qty6=str(sheet)+"x"+str(s1)+"x"+str(s2)+"x"+"2"
    rate6=".00667"

    sub_details7="UV output"
    sub_details_price7=qtys*.1
    
    qty7=str(qtys)
    rate7=".1"

    sub_details8="Front and Back UV Printing"
    sub_details_price8=sheet*1.5
    
    qty8=str(sheet)
    rate8="1.5"

    sub_details9="creasing"
    sub_details_price9=(qtys*2)*.2
    a=qtys*2
    qty9=str(a)
    rate9=".2"

    sub_details10="Book Binding"
    sub_details_price10=(qtys/2)*2
    a=(qtys/2)
    qty10=str(a)
    rate10=str(2)


    total=sub_details_price1+sub_details_price2+sub_details_price3+sub_details_price4+sub_details_price5+sub_details_price6+sub_details_price7+sub_details_price8+sub_details_price9+sub_details_price10
    c_detail=Add_client.objects.filter(c_name=c_name)
    random_value="IN"+str(random.randint(0,99999999999))
    
    c_name=""
    c_number=""
    c_address=""
    c_email=""
    for a in c_detail:
        c_name=a.c_name
        c_number=a.c_number
        c_address=a.c_address
        c_email=a.c_email
    brou=invitation_card(c_name=c_name,c_number=c_number,c_email=c_email,c_address=c_address,order_id=random_value,qty=qty,title=title,sub_details1=sub_details1,sub_details2=sub_details2,sub_details3=sub_details3,sub_details4=sub_details4,sub_details5=sub_details5,sub_details6=sub_details6,sub_details7=sub_details7,sub_details8=sub_details8,sub_details9=sub_details9,sub_details10=sub_details10,sub_detail_price1=sub_details_price1,sub_detail_price2=sub_details_price2,sub_detail_price3=sub_details_price3,sub_detail_price4=sub_details_price4,sub_detail_price5=sub_details_price5,sub_detail_price6=sub_details_price6,sub_detail_price7=sub_details_price7,sub_detail_price8=sub_details_price8,sub_detail_price9=sub_details_price9,sub_detail_price10=sub_details_price10,qty1=qty1,qty2=qty2,qty3=qty3,qty4=qty4,qty5=qty5,qty6=qty6,qty7=qty7,qty8=qty8,qty9=qty9,qty10=qty10,rate1=rate1,rate2=rate2,rate3=rate3,rate4=rate4,rate5=rate5,rate6=rate6,rate7=rate7,rate8=rate8,rate9=rate9,rate10=rate10,total=total)
    brou.save()
    
    return random_value

def broucher(a,b,c,d,e,f):
    c_name=a
    s_item=b
    qty=c
    s1=int(d)
    s2=int(e)
    maxbox=int(f)
    x=int(qty)/maxbox
    qtys=int(math.ceil(x))
    
    product="Brochure"
    title=qty+" "+product+" "+str(s_item)+"/ "+str(s1)+"X"+str(s2)
    sheet=(qtys*8)+80
    sub_details1=str(s1)+"X"+str(s2)+" sheet 300gsm white mat card sheet"
    sub_details_price1=sheet*8
    
    qty1=str(sheet)
    rate1=str(8)
    
    
    sub_details2="Page Design"
    sub_details_price2=16*200
    qty2=str(16)
    rate2=str(200)

    sub_details3="Colour Printout"
    sub_details_price3=8*50
    qty3=str(8)
    rate3=str(50)

    sub_details4="Plate 19x26"
    a=(((sheet-80)*4)/1000)
    sub_details_price4=a*400
    
    qty4=str(a)
    rate4=str(400)

    sub_details5="Set Ptg"
    a=a/4
    sub_details_price5=a*1000
    
    qty5=str(a)
    rate5=str(1000)

    sub_details6="Mat Lamination"
    sub_details_price6=(sheet*s1*s2*2)*.00667
    
    qty6=str(sheet)+"x"+str(s1)+"x"+str(s2)+"x"+"2"
    rate6=".00667"

    sub_details7="UV output"
    sub_details_price7=qtys*.1
    
    qty7=str(qtys)
    rate7=".1"

    sub_details8="Front and Back UV Printing"
    sub_details_price8=sheet*1.5
    
    qty8=str(sheet)
    rate8="1.5"

    sub_details9="creasing"
    sub_details_price9=(qtys*2)*.2
    a=qtys*2
    qty9=str(a)
    rate9=".2"

    sub_details10="Book Binding"
    sub_details_price10=(qtys/2)*2
    a=(qtys/2)
    qty10=str(a)
    rate10=str(2)


    total=sub_details_price1+sub_details_price2+sub_details_price3+sub_details_price4+sub_details_price5+sub_details_price6+sub_details_price7+sub_details_price8+sub_details_price9+sub_details_price10
    c_detail=Add_client.objects.filter(c_name=c_name)
    random_value="BR"+str(random.randint(0,99999999999))
    
    c_name=""
    c_number=""
    c_address=""
    c_email=""
    for a in c_detail:
        c_name=a.c_name
        c_number=a.c_number
        c_address=a.c_address
        c_email=a.c_email
    brou=Broucher(c_name=c_name,c_number=c_number,c_email=c_email,c_address=c_address,order_id=random_value,qty=qty,title=title,sub_details1=sub_details1,sub_details2=sub_details2,sub_details3=sub_details3,sub_details4=sub_details4,sub_details5=sub_details5,sub_details6=sub_details6,sub_details7=sub_details7,sub_details8=sub_details8,sub_details9=sub_details9,sub_details10=sub_details10,sub_detail_price1=sub_details_price1,sub_detail_price2=sub_details_price2,sub_detail_price3=sub_details_price3,sub_detail_price4=sub_details_price4,sub_detail_price5=sub_details_price5,sub_detail_price6=sub_details_price6,sub_detail_price7=sub_details_price7,sub_detail_price8=sub_details_price8,sub_detail_price9=sub_details_price9,sub_detail_price10=sub_details_price10,qty1=qty1,qty2=qty2,qty3=qty3,qty4=qty4,qty5=qty5,qty6=qty6,qty7=qty7,qty8=qty8,qty9=qty9,qty10=qty10,rate1=rate1,rate2=rate2,rate3=rate3,rate4=rate4,rate5=rate5,rate6=rate6,rate7=rate7,rate8=rate8,rate9=rate9,rate10=rate10,total=total)
    brou.save()
    
    return random_value

def Pamplate(a,b,c,d,e,f):
    c_name=a
    s_item=b
    qty=c
    s1=int(d)
    s2=int(e)
    maxbox=int(f)
    x=int(qty)/maxbox
    qtys=int(math.ceil(x))
    
    product="pamplate"
    title=qty+" "+product+" "+str(s_item)+"/ "+str(s1)+"X"+str(s2)
    sheet=(qtys*8)+80
    sub_details1=str(s1)+"X"+str(s2)+" sheet 300gsm white mat card sheet"
    sub_details_price1=sheet*8
    
    qty1=str(sheet)
    rate1=str(8)
    
    
    sub_details2="Page Design"
    sub_details_price2=16*200
    qty2=str(16)
    rate2=str(200)

    sub_details3="Colour Printout"
    sub_details_price3=8*50
    qty3=str(8)
    rate3=str(50)

    sub_details4="Plate 19x26"
    a=(((sheet-80)*4)/1000)
    sub_details_price4=a*400
    
    qty4=str(a)
    rate4=str(400)

    sub_details5="Set Ptg"
    a=a/4
    sub_details_price5=a*1000
    
    qty5=str(a)
    rate5=str(1000)

    sub_details6="Mat Lamination"
    sub_details_price6=(sheet*s1*s2*2)*.00667
    
    qty6=str(sheet)+"x"+str(s1)+"x"+str(s2)+"x"+"2"
    rate6=".00667"

    sub_details7="UV output"
    sub_details_price7=qtys*.1
    
    qty7=str(qtys)
    rate7=".1"

    sub_details8="Front and Back UV Printing"
    sub_details_price8=sheet*1.5
    
    qty8=str(sheet)
    rate8="1.5"

    sub_details9="creasing"
    sub_details_price9=(qtys*2)*.2
    a=qtys*2
    qty9=str(a)
    rate9=".2"

    sub_details10="Book Binding"
    sub_details_price10=(qtys/2)*2
    a=(qtys/2)
    qty10=str(a)
    rate10=str(2)


    total=sub_details_price1+sub_details_price2+sub_details_price3+sub_details_price4+sub_details_price5+sub_details_price6+sub_details_price7+sub_details_price8+sub_details_price9+sub_details_price10
    c_detail=Add_client.objects.filter(c_name=c_name)
    random_value="PA"+str(random.randint(0,99999999999))
    
    c_name=""
    c_number=""
    c_address=""
    c_email=""
    for a in c_detail:
        c_name=a.c_name
        c_number=a.c_number
        c_address=a.c_address
        c_email=a.c_email
    brou=pamplate(c_name=c_name,c_number=c_number,c_email=c_email,c_address=c_address,order_id=random_value,qty=qty,title=title,sub_details1=sub_details1,sub_details2=sub_details2,sub_details3=sub_details3,sub_details4=sub_details4,sub_details5=sub_details5,sub_details6=sub_details6,sub_details7=sub_details7,sub_details8=sub_details8,sub_details9=sub_details9,sub_details10=sub_details10,sub_detail_price1=sub_details_price1,sub_detail_price2=sub_details_price2,sub_detail_price3=sub_details_price3,sub_detail_price4=sub_details_price4,sub_detail_price5=sub_details_price5,sub_detail_price6=sub_details_price6,sub_detail_price7=sub_details_price7,sub_detail_price8=sub_details_price8,sub_detail_price9=sub_details_price9,sub_detail_price10=sub_details_price10,qty1=qty1,qty2=qty2,qty3=qty3,qty4=qty4,qty5=qty5,qty6=qty6,qty7=qty7,qty8=qty8,qty9=qty9,qty10=qty10,rate1=rate1,rate2=rate2,rate3=rate3,rate4=rate4,rate5=rate5,rate6=rate6,rate7=rate7,rate8=rate8,rate9=rate9,rate10=rate10,total=total)
    brou.save()
    
    return random_value

def Latter_head_box(a,b,c,d,e,f):
    c_name=a
    s_item=b
    qty=c
    s1=int(d)
    s2=int(e)
    maxbox=int(f)
    x=int(qty)/maxbox
    qtys=int(math.ceil(x))
    
    product="latter head box"
    title=qty+" "+product+" "+str(s_item)+"/ "+str(s1)+"X"+str(s2)
    sheet=(qtys*8)+80
    sub_details1=str(s1)+"X"+str(s2)+" sheet 300gsm white mat card sheet"
    sub_details_price1=sheet*8
    
    qty1=str(sheet)
    rate1=str(8)
    
    
    sub_details2="Page Design"
    sub_details_price2=16*200
    qty2=str(16)
    rate2=str(200)

    sub_details3="Colour Printout"
    sub_details_price3=8*50
    qty3=str(8)
    rate3=str(50)

    sub_details4="Plate 19x26"
    a=(((sheet-80)*4)/1000)
    sub_details_price4=a*400
    
    qty4=str(a)
    rate4=str(400)

    sub_details5="Set Ptg"
    a=a/4
    sub_details_price5=a*1000
    
    qty5=str(a)
    rate5=str(1000)

    sub_details6="Mat Lamination"
    sub_details_price6=(sheet*s1*s2*2)*.00667
    
    qty6=str(sheet)+"x"+str(s1)+"x"+str(s2)+"x"+"2"
    rate6=".00667"

    sub_details7="UV output"
    sub_details_price7=qtys*.1
    
    qty7=str(qtys)
    rate7=".1"

    sub_details8="Front and Back UV Printing"
    sub_details_price8=sheet*1.5
    
    qty8=str(sheet)
    rate8="1.5"

    sub_details9="creasing"
    sub_details_price9=(qtys*2)*.2
    a=qtys*2
    qty9=str(a)
    rate9=".2"

    sub_details10="Book Binding"
    sub_details_price10=(qtys/2)*2
    a=(qtys/2)
    qty10=str(a)
    rate10=str(2)


    total=sub_details_price1+sub_details_price2+sub_details_price3+sub_details_price4+sub_details_price5+sub_details_price6+sub_details_price7+sub_details_price8+sub_details_price9+sub_details_price10
    c_detail=Add_client.objects.filter(c_name=c_name)
    random_value="LA"+str(random.randint(0,99999999999))
    
    c_name=""
    c_number=""
    c_address=""
    c_email=""
    for a in c_detail:
        c_name=a.c_name
        c_number=a.c_number
        c_address=a.c_address
        c_email=a.c_email
    brou=latter_head_box(c_name=c_name,c_number=c_number,c_email=c_email,c_address=c_address,order_id=random_value,qty=qty,title=title,sub_details1=sub_details1,sub_details2=sub_details2,sub_details3=sub_details3,sub_details4=sub_details4,sub_details5=sub_details5,sub_details6=sub_details6,sub_details7=sub_details7,sub_details8=sub_details8,sub_details9=sub_details9,sub_details10=sub_details10,sub_detail_price1=sub_details_price1,sub_detail_price2=sub_details_price2,sub_detail_price3=sub_details_price3,sub_detail_price4=sub_details_price4,sub_detail_price5=sub_details_price5,sub_detail_price6=sub_details_price6,sub_detail_price7=sub_details_price7,sub_detail_price8=sub_details_price8,sub_detail_price9=sub_details_price9,sub_detail_price10=sub_details_price10,qty1=qty1,qty2=qty2,qty3=qty3,qty4=qty4,qty5=qty5,qty6=qty6,qty7=qty7,qty8=qty8,qty9=qty9,qty10=qty10,rate1=rate1,rate2=rate2,rate3=rate3,rate4=rate4,rate5=rate5,rate6=rate6,rate7=rate7,rate8=rate8,rate9=rate9,rate10=rate10,total=total)
    brou.save()
    
    return random_value

def visiting_card(a,b,c,d,e,f):
    c_name=a
    s_item=b
    qty=c
    s1=int(d)
    s2=int(e)
    maxbox=int(f)
    x=int(qty)/maxbox
    qtys=int(math.ceil(x))
    product="Visiting Card"
    title=qty+" Pcs"+s_item+" "+product+" with Card name printing"
    sub_details1=qty+" "+s_item+" "+product
    sub_details_price1=qtys*maxbox
    abc=(qtys*maxbox)
    sub_details2=str(abc)+" Card name printing @.5"
    sub_details_price2=abc*.5
    total=sub_details_price1+sub_details_price2
    c_detail=Add_client.objects.filter(c_name=c_name)
    random_value="VC"+str(random.randint(0,99999999999))
    
    c_name=""
    c_number=""
    c_address=""
    c_email=""
    for a in c_detail:
        c_name=a.c_name
        c_number=a.c_number
        c_address=a.c_address
        c_email=a.c_email
    v_card=Visiting_card(c_name=c_name,c_number=c_number,c_email=c_email,c_address=c_address,order_id=random_value,qty=qty,title=title,sub_details1=sub_details1,sub_details2=sub_details2,sub_detail_price1=sub_details_price1,sub_detail_price2=sub_details_price2,total=total)
    v_card.save()
    return random_value
    
def Envelope(a,b,c,d,e,f):
    c_name=a
    s_item=b
    qty=c
    s1=int(d)
    s2=int(e)
    maxbox=int(f)
    x=int(qty)/maxbox
    qtys=int(math.ceil(x))
    
    product="envelope"
    title=qty+" "+product+" "+str(s_item)+"/ "+str(s1)+"X"+str(s2)
    sheet=(qtys*8)+80
    sub_details1=str(s1)+"X"+str(s2)+" sheet 300gsm white mat card sheet"
    sub_details_price1=sheet*8
    
    qty1=str(sheet)
    rate1=str(8)
    
    
    sub_details2="Page Design"
    sub_details_price2=16*200
    qty2=str(16)
    rate2=str(200)

    sub_details3="Colour Printout"
    sub_details_price3=8*50
    qty3=str(8)
    rate3=str(50)

    sub_details4="Plate 19x26"
    a=(((sheet-80)*4)/1000)
    sub_details_price4=a*400
    
    qty4=str(a)
    rate4=str(400)

    sub_details5="Set Ptg"
    a=a/4
    sub_details_price5=a*1000
    
    qty5=str(a)
    rate5=str(1000)

    sub_details6="Mat Lamination"
    sub_details_price6=(sheet*s1*s2*2)*.00667
    
    qty6=str(sheet)+"x"+str(s1)+"x"+str(s2)+"x"+"2"
    rate6=".00667"

    sub_details7="UV output"
    sub_details_price7=qtys*.1
    
    qty7=str(qtys)
    rate7=".1"

    sub_details8="Front and Back UV Printing"
    sub_details_price8=sheet*1.5
    
    qty8=str(sheet)
    rate8="1.5"

    sub_details9="creasing"
    sub_details_price9=(qtys*2)*.2
    a=qtys*2
    qty9=str(a)
    rate9=".2"

    sub_details10="Book Binding"
    sub_details_price10=(qtys/2)*2
    a=(qtys/2)
    qty10=str(a)
    rate10=str(2)


    total=sub_details_price1+sub_details_price2+sub_details_price3+sub_details_price4+sub_details_price5+sub_details_price6+sub_details_price7+sub_details_price8+sub_details_price9+sub_details_price10
    c_detail=Add_client.objects.filter(c_name=c_name)
    random_value="BR"+str(random.randint(0,99999999999))
    
    c_name=""
    c_number=""
    c_address=""
    c_email=""
    for a in c_detail:
        c_name=a.c_name
        c_number=a.c_number
        c_address=a.c_address
        c_email=a.c_email
    brou=envelope(c_name=c_name,c_number=c_number,c_email=c_email,c_address=c_address,order_id=random_value,qty=qty,title=title,sub_details1=sub_details1,sub_details2=sub_details2,sub_details3=sub_details3,sub_details4=sub_details4,sub_details5=sub_details5,sub_details6=sub_details6,sub_details7=sub_details7,sub_details8=sub_details8,sub_details9=sub_details9,sub_details10=sub_details10,sub_detail_price1=sub_details_price1,sub_detail_price2=sub_details_price2,sub_detail_price3=sub_details_price3,sub_detail_price4=sub_details_price4,sub_detail_price5=sub_details_price5,sub_detail_price6=sub_details_price6,sub_detail_price7=sub_details_price7,sub_detail_price8=sub_details_price8,sub_detail_price9=sub_details_price9,sub_detail_price10=sub_details_price10,qty1=qty1,qty2=qty2,qty3=qty3,qty4=qty4,qty5=qty5,qty6=qty6,qty7=qty7,qty8=qty8,qty9=qty9,qty10=qty10,rate1=rate1,rate2=rate2,rate3=rate3,rate4=rate4,rate5=rate5,rate6=rate6,rate7=rate7,rate8=rate8,rate9=rate9,rate10=rate10,total=total)
    brou.save()
    
    return random_value






def add_client(request):
    c_name=Add_client.objects.all()
    data={
        'data': c_name,
    }
    if request.method=='POST':
        name=request.POST['name']
        number=request.POST['number']
        email=request.POST['email']
        address=request.POST['address']
        pan=request.POST['pan']
        gst=request.POST['gst']
        save_details=Add_client(c_name=name,c_number=number,c_email=email,c_address=address,pan=pan,gst=gst)
        save_details.save()
        
    return render(request,'attendance.html',data)
    


def quotation(request):
    c_name=Add_client.objects.all()
    data={
        'data': c_name,
    }
    return render(request,'attendance.html',data)

def quot_add(request):
    qty=request.POST['quantity']
    size1=request.POST['size1']
    size2=request.POST['size2']
    size3=request.POST['size3']

    return render(request,'invoices.html')
def invoice(request,d):
    if(d[0:2]=="VC"):
        da=Visiting_card.objects.filter(order_id=d)
        dat=payment.objects.filter(order_id=d)
        dat1=notes.objects.filter(order_id=d)
        data={
            'data':da,
            'dataa':dat,
            'data1':dat1,
        }
    elif(d[0:2]=="BR"):
        dat1=notes.objects.filter(order_id=d)
        da=Broucher.objects.filter(order_id=d)
        dat=payment.objects.filter(order_id=d)
        data={
            'data':da,
            'dataa':dat,
            'data1':dat1,
        }
    elif(d[0:2]=="ID"):
        dat1=notes.objects.filter(order_id=d)
        da=id_card.objects.filter(order_id=d)
        dat=payment.objects.filter(order_id=d)
        data={
            'data':da,
            'dataa':dat,
            'data1':dat1,
        }
    elif(d[0:2]=="EP"):
        dat1=notes.objects.filter(order_id=d)
        da=entry_pass.objects.filter(order_id=d)
        dat=payment.objects.filter(order_id=d)
        data={
            'data':da,
            'dataa':dat,
            'data1':dat1,
        }
    elif(d[0:2]=="IN"):
        dat1=notes.objects.filter(order_id=d)
        da=invitation_card.objects.filter(order_id=d)
        dat=payment.objects.filter(order_id=d)
        data={
            'data':da,
            'dataa':dat,
            'data1':dat1,
        }
    elif(d[0:2]=="PA"):
        dat1=notes.objects.filter(order_id=d)
        da=pamplate.objects.filter(order_id=d)
        dat=payment.objects.filter(order_id=d)
        data={
            'data':da,
            'dataa':dat,
            'data1':dat1,
        }
    elif(d[0:2]=="LA"):
        dat1=notes.objects.filter(order_id=d)
        da=latter_head_box.objects.filter(order_id=d)
        dat=payment.objects.filter(order_id=d)
        data={
            'data':da,
            'dataa':dat,
            'data1':dat1,
        }
    elif(d[0:2]=="EN"):
        dat1=notes.objects.filter(order_id=d)
        da=envelope.objects.filter(order_id=d)
        dat=payment.objects.filter(order_id=d)
        data={
            'data':da,
            'dataa':dat,
            'data1':dat1,
        }
    else:
        data={
            
        }

    return render(request, 'invoices.html',data)

def index(request):
    return render(request, 'attendance.html')



def update(request):
    payment1=request.POST['amt_received']
    order_id=request.POST['order_id']
    payment_status=request.POST['payment_status']
    description=request.POST['description']
    save_payment=payment(payment=payment1,payment_status=payment_status,description=description,order_id=order_id)
    save_payment.save()

    return render(request,"attendance.html")
    
def view_invoice(request):
    d=request.POST['Id']
    if(d[0:2]=="VC"):
        da=Visiting_card.objects.filter(order_id=d)
        dat=payment.objects.filter(order_id=d)
        data={
            'data':da,
            'dataa':dat,
        }
    elif(d[0:2]=="BR"):
        da=Broucher.objects.filter(order_id=d)
        dat=payment.objects.filter(order_id=d)
        data={
            'data':da,
            'dataa':dat,
        }
    elif(d[0:2]=="ID"):
        da=id_card.objects.filter(order_id=d)
        dat=payment.objects.filter(order_id=d)
        data={
            'data':da,
            'dataa':dat,
        }
    elif(d[0:2]=="EP"):
        da=entry_pass.objects.filter(order_id=d)
        dat=payment.objects.filter(order_id=d)
        data={
            'data':da,
            'dataa':dat,
        }
    elif(d[0:2]=="IN"):
        da=invitation_card.objects.filter(order_id=d)
        dat=payment.objects.filter(order_id=d)
        data={
            'data':da,
            'dataa':dat,
        }
    elif(d[0:2]=="PA"):
        da=pamplate.objects.filter(order_id=d)
        dat=payment.objects.filter(order_id=d)
        data={
            'data':da,
            'dataa':dat,
        }
    elif(d[0:2]=="LA"):
        da=latter_head_box.objects.filter(order_id=d)
        dat=payment.objects.filter(order_id=d)
        data={
            'data':da,
            'dataa':dat,
        }
    elif(d[0:2]=="EN"):
        da=envelope.objects.filter(order_id=d)
        dat=payment.objects.filter(order_id=d)
        data={
            'data':da,
            'dataa':dat,
        }
    else:
        data={
            
        }

    return render(request, 'invoices.html',data)
 
def view_invoices(request):
    return render(request, 'view_invoices.html')

def create_quotation(request):
    da=Visiting_card.objects.all()
    da1=id_card.objects.all()
    da2=entry_pass.objects.all()
    da3=invitation_card.objects.all()
    da4=Broucher.objects.all()
    da5=pamplate.objects.all()
    da6=latter_head_box.objects.all()
    da7=envelope.objects.all()
    data={
        'data':da,
        'data1':da1,
        'data2':da2,
        'data3':da3,
        'data4':da4,
        'data5':da5,
        'data6':da6,
        'data7':da7,

    }
    return render(request, 'create_quotation.html',data)