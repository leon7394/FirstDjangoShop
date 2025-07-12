from django import template

register = template.Library()

@register.filter(name='three_digits_currency')
def three_digits_currency(value:int):
    return '{:,}'.format(value) + ' تومان'

@register.simple_tag
def multiply(quantity, price, *args, **kwargs):
    return three_digits_currency(int(quantity) * int(price))