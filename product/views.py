from django.http.response import HttpResponse, JsonResponse, FileResponse
import os

product = {
    'name' : 'test',
    'quantity' : 10,
    'price' : 2000,
}

def product_info_json(request):
    return JsonResponse(product)

def product_info_pdf(request):
    file = os.path.join("C:/Users/mhmmd/Documents/checks/1.pdf")
    return FileResponse(open(file, 'rb'), as_attachment= True)

def buy_product(request, quantity):
    if quantity> product['quantity']:
        return HttpResponse(f"we only have {product['quantity']}")
    else:
        return HttpResponse(f"it cost{product['price']* quantity}")
    
    