from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import order,productListedInOrder

# Create your views here.

def list(request):
	address = {
		'building':'C.P. Tower',
		'detail':'313 Silom Road, Bangrak, Bangkok 10500 Thailand',
		'tel':'+662 625 7000',
	}
	customerContact = {
		'type':'Retailer',
		'name':'Tom',
		'status':'Pending'
	}
	product1 = {
		'sku':'00000001',
		'description':'Luxary watch',
		'brand':'Rolex',
		'price':'5000',
		'discount':'10',
		'netPrice':'4500',
		'qty':'10',
		'total':'45000'
	}
	product2 = {
		'sku':'00000002',
		'description':'Great Shoes',
		'brand':'Nike',
		'price':'4000',
		'discount':'10',
		'netPrice':'3600',
		'qty':'10',
		'total':'36000'
	}
	shippingDetails = {
		'estimatedDeliveryTime':'21-05-2017',
		'sub-total':'81000',
		'shippingCost':'500',
		'specialDiscount':'0',
		'tax':'5670',
		'total': '57330'
	}
	template = loader.get_template('order/list.html')
	context = {
		'address':address,
		'customerContact':customerContact,
		'product1':product1,
		'product2':product2,
		'shippingDetails':shippingDetails
		}
	return HttpResponse(template.render(context, request))

def getItemsList(eachOrder):
	productsListed = productListedInOrder.objects.filter(order__slug=eachOrder.slug)
	return productsListed