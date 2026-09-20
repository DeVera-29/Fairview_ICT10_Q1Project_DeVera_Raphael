from pyscript import document, display

def generate_sku(e):

    category = document.getElementById('category').value
    product_name = document.getElementById('prod_name').value.strip()
    stock_qty = document.getElementById('stock_qty').value.strip()

    document.getElementById('sku_result').innerHTML = ''

    clean_name = product_name.replace(" ", "").upper()
    name_code = clean_name[:3] if len(clean_name) >= 3 else clean_name.ljust(3, 'X')

    try:
        qty_code = f"{int(stock_qty):03d}"
    except ValueError:
        qty_code = "000"


    sku = f"{category}-{name_code}-{qty_code}"
    display(f"SKU Code: {sku}", target='sku_result')