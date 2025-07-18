from .models import Cart,CartItem
from .views import _cart_id



def counter(request):
    print("Counter function called")  # Debug print
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart_id = _cart_id(request)
            print(f"Cart ID: {cart_id}")  # Debug print
            cart = Cart.objects.get(cart_id=cart_id)
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
            for cart_item in cart_items:
                cart_count += cart_item.quantity
            print(f"Cart count: {cart_count}")  # Debug print
        except Cart.DoesNotExist:
            cart_count = 0
            print("Cart does not exist")  # Debug print
        except Exception as e:
            cart_count = 0
            print(f"Exception: {e}")  # Debug print
    return dict(cart_count=cart_count)