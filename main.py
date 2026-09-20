from pyscript import document, display

def calculate_total(e):
    receipt_div = document.getElementById('receipt')
    if receipt_div:
        receipt_div.innerHTML = ''

    subtotal = 0.00
    if document.getElementById('item1').checked:
        subtotal += 540
    if document.getElementById('item2').checked:
        subtotal += 200
    if document.getElementById('item3').checked:
        subtotal += 1000
    if document.getElementById('item4').checked:
        subtotal += 560
    if document.getElementById('item5').checked:
        subtotal += 2100

    VAT = subtotal * 0.12
    total = subtotal + VAT

    display(f'Subtotal: Php {subtotal:.2f}', target='receipt')
    display(f'VAT: Php {VAT:.2f}', target='receipt')
    display(f'Total: Php {total:.2f}', target='receipt')