from flask import Flask, render_template, request, redirect, url_for
from Model.management import Management

app = Flask(__name__)

global management
management = Management()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        management.the_user = None
    return render_template("index.html", office=management)


@app.route('/about')
def about():
    return render_template("about.html", office=management)


@app.route('/contact')
def contact():
    return render_template("contact.html", office=management)


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    msg = ""
    if request.method == 'POST':
        msg = management.sign_in(str(request.form["email"]), str(request.form["password"]))
        if msg == "":
            return redirect(url_for('home'))
    return render_template("sign in.html", office=management, msg=msg)


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ""
    if request.method == 'POST':
        msg = management.register(str(request.form["email"]), str(request.form["password"]))
    return render_template("register.html", office=management, msg=msg)


@app.route('/products_order_by_<sort_option>')
def show_all_products(sort_option):
    if sort_option == "name":
        return render_template("products/all products.html", office=management, products_list=management.all_products_sorted_by_name ,sort_option=sort_option)
    elif sort_option == "price":
        return render_template("products/all products.html", office=management, products_list=management.all_products_sorted_by_price, sort_option=sort_option)
    else:
        return render_template("products/all products.html", office=management, products_list=management.all_products, sort_option=sort_option)


@app.route('/platforms_<platform_name>_order_by_<sort_option>')
def show_all_platforms(platform_name, sort_option):
    platform_name = platform_name.replace("_", " ")
    if sort_option == "name":
        if platform_name == "All":
            return render_template("products/platforms.html", office=management, platforms_list=management.get_all_products_from_one_type('Platform', 'name'), platform_name=platform_name, sort_option=sort_option)
        else:
            return render_template("products/platforms.html", office=management, platforms_list=management.get_all_products_from_one_type_and_same_platform('Platform', 'name', platform_name), platform_name=platform_name, sort_option=sort_option)
    elif sort_option == "price":
        if platform_name == "All":
            return render_template("products/platforms.html", office=management, platforms_list=management.get_all_products_from_one_type('Platform', 'price'), platform_name=platform_name, sort_option=sort_option)
        else:
            return render_template("products/platforms.html", office=management, platforms_list=management.get_all_products_from_one_type_and_same_platform('Platform', 'price', platform_name), platform_name=platform_name, sort_option=sort_option)
    else:
        if platform_name == "All":
            return render_template("products/platforms.html", office=management, platforms_list=management.get_all_products_from_one_type('Platform', ''), platform_name=platform_name, sort_option=sort_option)
        else:
            return render_template("products/platforms.html", office=management, platforms_list=management.get_all_products_from_one_type_and_same_platform('Platform', '', platform_name), platform_name=platform_name, sort_option=sort_option)


@app.route('/games_<platform_name>_order_by_<sort_option>')
def show_all_games(platform_name, sort_option):
    platform_name = platform_name.replace("_", " ")
    if sort_option == "name":
        if platform_name == "All":
            return render_template("products/games.html", office=management, games_list=management.get_all_products_from_one_type('Game', 'name'), platform_name=platform_name, sort_option=sort_option)
        else:
            return render_template("products/games.html", office=management, games_list=management.get_all_products_from_one_type_and_same_platform('Game', 'name', platform_name), platform_name=platform_name, sort_option=sort_option)
    elif sort_option == "price":
        if platform_name == "All":
            return render_template("products/games.html", office=management, games_list=management.get_all_products_from_one_type('Game', 'price'), platform_name=platform_name, sort_option=sort_option)
        else:
            return render_template("products/games.html", office=management, games_list=management.get_all_products_from_one_type_and_same_platform('Game', 'price', platform_name), platform_name=platform_name, sort_option=sort_option)
    else:
        if platform_name == "All":
            return render_template("products/games.html", office=management, games_list=management.get_all_products_from_one_type('Game', ''), platform_name=platform_name, sort_option=sort_option)
        else:
            return render_template("products/games.html", office=management, games_list=management.get_all_products_from_one_type_and_same_platform('Game', '', platform_name), platform_name=platform_name, sort_option=sort_option)


@app.route('/accessories_<platform_name>_order_by_<sort_option>')
def show_all_accessories(platform_name, sort_option):
    platform_name = platform_name.replace("_", " ")
    if sort_option == "name":
        if platform_name == "All":
            return render_template("products/accessories.html", office=management, accessories_list=management.get_all_products_from_one_type('Accessory', 'name'), platform_name=platform_name, sort_option=sort_option)
        else:
            return render_template("products/accessories.html", office=management, accessories_list=management.get_all_products_from_one_type_and_same_platform('Accessory', 'name', platform_name), platform_name=platform_name, sort_option=sort_option)
    elif sort_option == "price":
        if platform_name == "All":
            return render_template("products/accessories.html", office=management, accessories_list=management.get_all_products_from_one_type('Accessory', 'price'), platform_name=platform_name, sort_option=sort_option)
        else:
            return render_template("products/accessories.html", office=management, accessories_list=management.get_all_products_from_one_type_and_same_platform('Accessory', 'price', platform_name), platform_name=platform_name, sort_option=sort_option)
    else:
        if platform_name == "All":
            return render_template("products/accessories.html", office=management, accessories_list=management.get_all_products_from_one_type('Accessory', ''), platform_name=platform_name, sort_option=sort_option)
        else:
            return render_template("products/accessories.html", office=management, accessories_list=management.get_all_products_from_one_type_and_same_platform('Accessory', '', platform_name), platform_name=platform_name, sort_option=sort_option)


@app.route('/<operation>_cart_<product_name>')
def cart_operations(product_name, operation):
    management.cart_operations(product_name, operation)
    return redirect(url_for('cart'))


@app.route('/cart')
def cart():
    return render_template("cart.html", office=management)


@app.route('/product_<product_name>')
def product_page(product_name):
    product_name = product_name.replace('_', ' ')
    product = management.search_by_name_product(product_name)
    return render_template("products/product.html", office=management, product=product)


@app.route('/order_form', methods=['GET', 'POST'])
def order_form():
    msg = ""
    if request.method == 'POST':
        msg = management.order_form(str(request.form["first_name"]), str(request.form["last_name"]), str(request.form["city"]), str(request.form["address"]))
        if msg == "":
            return redirect(url_for('my_orders'))
    return render_template("orders/order form.html", office=management, msg=msg)


@app.route('/my_orders')
def my_orders():
    return render_template("orders/my orders.html", office=management)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search = str(request.form["search"])
        arr = management.search_navbar(search)
        if len(arr) == 0:
            arr = "We did not find a product with a similar name!"
    return render_template("search.html", office=management, options=arr, search=search)


if __name__ == "__main__":
    app.run(debug=True)