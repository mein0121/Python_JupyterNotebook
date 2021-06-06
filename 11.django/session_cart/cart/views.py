from django.shortcuts import render, redirect
from django.urls import reverse

#  장바구니 처리
# 요청파라미터로 제품이름을 받아서 이것을 cart(딕셔너리)에 저장. key:제품명, value:개수
def cart(request):
    # 요청파라미터 값 조회: get: request.GET
    #                     post: request.POST
    # .get(name), ["name"] => 하나의 값을 조회
    # .getlist(name) => name으로 넘어온 값들을 List로 묶어서 반환. => 같은이름으로 여러개의 값이 넘어올때 사용.
    item_list = request.POST.getlist('item') 
    # 요청파라미터 검증 - 선택안하고 요청한 경우
    if not item_list:
        return render(request, 'cart/shopping_list.html', 
                      {"error_message":"상품을 선택하세요."})
    # session에 "cart"이름으로 저장된 객체(딕셔너리)를 조회
    cart = request.session.get('cart')
    if not cart: # cart이름으로 저장된 값이 없으면 dictionary를 만들어서 session에 저장.
        cart = {}
        request.session['cart']=cart
    # 요청파라미터로 넘어온 값들을 cart 딕셔너리에 저장.
    for item in item_list:
        cnt = cart.get(item)
        if cnt: # 있으면 기존값 +1
            cart[item]=cnt+1
            print('=================',type(cart[item]), cart[item], item)
        else: # 없으면 추가.
            cart[item]=1
    return redirect(reverse('cart:cart_list'))

def order(request):
    del request.session['cart']
    return redirect(reverse('cart:shopping_list'))