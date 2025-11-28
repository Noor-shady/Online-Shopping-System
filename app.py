from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, User, Product, CartItem
import os
import webbrowser
from threading import Timer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# --- Routes ---

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        action = request.form.get('action')

        if action == 'register':
            if User.query.filter_by(username=username).first():
                flash('Username exists.')
                return redirect(url_for('login'))
            new_user = User(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('index'))

        else:
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash('Invalid credentials')

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/add/<int:product_id>')
@login_required
def add_to_cart(product_id):
    existing_item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()

    if existing_item:
        existing_item.quantity += 1
    else:
        new_item = CartItem(user_id=current_user.id, product_id=product_id, quantity=1)
        db.session.add(new_item)

    db.session.commit()
    flash('Item added to cart!')
    return redirect(url_for('index'))


@app.route('/cart')
@login_required
def cart():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render_template('cart.html', cart=cart_items, total=total)


@app.route('/checkout')
@login_required
def checkout():
    CartItem.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()
    flash('Thank you for your purchase! Your order has been placed.')
    return redirect(url_for('index'))


# --- Database Seeding ---
def seed_data():
    if not Product.query.first():
        items = [
            Product(name="Mechanical Keyboard", price=120.00, description="Clicky and tactical.",
                    image_url="https://placehold.co/300x200?text=Keyboard"),
            Product(name="Gaming Mouse", price=60.50, description="High DPI precision.",
                    image_url="https://placehold.co/300x200?text=Mouse"),
            Product(name="4K Monitor", price=350.00, description="Crystal clear display.",
                    image_url="https://placehold.co/300x200?text=Monitor"),
            Product(name="Headset", price=80.00, description="Noise cancelling.",
                    image_url="https://placehold.co/300x200?text=Headset"),
        ]
        db.session.bulk_save_objects(items)
        db.session.commit()
        print("Database seeded.")

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_data()

    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        Timer(1, open_browser).start()

    app.run(debug=True)
