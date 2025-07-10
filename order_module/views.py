from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from order_module.models import Order, OrderDetail
from product_module.models import Product


def add_product_to_order(request):
    product_id = request.GET.get('product_id')
    count = int(request.GET.get('count',1))

    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()
        if product:
            current_order, created  = Order.objects.get_or_create(user_id=request.user.id, is_paid=False)
            current_order_detail = current_order.order_details.filter(product_id=product_id).first()
            if current_order_detail:
                current_order_detail.count += count
                current_order_detail.save()
            else:
                new_detail = OrderDetail(order=current_order, product_id=product_id, count=count)
                new_detail.save()

            return JsonResponse({
                'status': 'success',
            })
        else:
            return JsonResponse({
                'status': 'NOT FOUND!',
            })
    else:
        return JsonResponse({
            'status': 'NOT_AUTHORIZED',
        })

    return JsonResponse({"0": "0"})
