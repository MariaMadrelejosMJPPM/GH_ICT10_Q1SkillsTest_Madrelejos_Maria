# 1Q Skills test
from pyscript import display, document


def create_order(e):
    document.getElementById('VAT').innerHTML = " "
    document.getElementById('subtotal').innerHTML = " "
    document.getElementById('total').innerHTML = " "
    coffee = document.getElementById('drink')

    subtotal = float(coffee.value)
    VAT = subtotal * 12 / 100
    total = VAT + subtotal

    display(f'Subtotal: {subtotal}', target='subtotal')
    display(f'VAT: {VAT}', target='VAT')
    display(f'Total: {total}', target='total')