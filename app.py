from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample product data
products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Smartphone", "price": 20000},
    {"id": 3, "name": "Headphones", "price": 2000}
]

# Home page - product listing
@app.route('/')
def index():
    return render_template('index.html', products=products)

# Add to cart
@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(product_id)
    return redirect(url_for('index'))

# View cart
@app.route('/cart')
def cart():
    if 'cart' not in session or len(session['cart']) == 0:
        return render_template('cart.html', items=[], total=0)
    cart_items = []
    total = 0
    for pid in session['cart']:
        for product in products:
            if product['id'] == pid:
                cart_items.append(product)
                total += product['price']
    return render_template('cart.html', items=cart_items, total=total)

# Checkout
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Simulate payment success
        session.pop('cart', None)
        return redirect(url_for('success'))
    if 'cart' not in session or len(session['cart']) == 0:
        return redirect(url_for('cart'))
    return render_template('checkout.html')

# Payment success page
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
