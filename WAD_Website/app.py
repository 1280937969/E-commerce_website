import flask
from flask import Flask, render_template, request, \
    flash, session, redirect, g, url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
#配置数据库的地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/flask_sql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = '/static/picture'
db = SQLAlchemy(app)
#数据库模型需要继承db.Model
class User(db.Model):
    # 定义表名和字段
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(10), default="user")
    email = db.Column(db.String(32), unique=True,nullable=False)
    password = db.Column(db.String(32),nullable=False)
    address = db.Column(db.String(255))
    phone_number = db.Column(db.String(20))
    cart = db.relationship("Cart", backref=db.backref("user", uselist=False))
    orders = db.relationship("Order", backref="user")
    messages = db.relationship("Message", backref="user")
    comments = db.relationship("Comment", backref="user")
    items = db.relationship("Item", backref="user")
class Cart(db.Model):
    __tablename__ = 'cart'
    cart_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    quantity = db.Column(db.Integer)
    total_price = db.Column(db.Integer)
    items = db.relationship("Item", backref="cart")
class Order(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.cart_id'))
    total_price = db.Column(db.Float)
    time = db.Column(db.db.String(255))
    items = db.relationship("Item", backref="order")
class Comment(db.Model):
    __tablename__ = 'comment'
    comment_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    item_id = db.Column(db.Integer, db.ForeignKey('item.item_id'))
    comment_details = db.Column(db.Text)
    name = db.Column(db.Text)
    mark = db.Column(db.Integer)
    comment_time = db.Column(db.DateTime,default=datetime.now)
class Message(db.Model):
    __tablename__ = 'message'
    message_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    item_id = db.Column(db.Integer, db.ForeignKey('item.item_id'))
    recipient = db.Column(db.Integer)
    content = db.Column(db.Text)
    time = db.Column(db.DateTime,default=datetime.now)
class Item(db.Model):
    __tablename__ = 'item'
    item_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.cart_id'))
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'))
    item_name = db.Column(db.String(20),nullable=False)
    photo = db.Column(db.String(255))
    address = db.Column(db.String(255),default="Merchant did not publish origin")
    item_details = db.Column(db.String(255),default="The merchant did not publish detailed details")
    price = db.Column(db.Float,nullable=False)
    duration = db.Column(db.String(255))
    discount_limit = db.Column(db.Float,default=1)
    liked_quantity = db.Column(db.Integer,default=0)
    disliked_quantity = db.Column(db.Integer, default=0)
    messages = db.relationship("Message", backref="item")
    comments = db.relationship("Comment",backref="item")
    interactions = db.relationship("UserItemInteraction", backref="item")
class Category(db.Model):
    __tablename__ = 'category'
    category_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    category_name = db.Column(db.String(20))
    #添加关系
    #表示和Item模型发生关联，增加了一个items属性
    #backref='category'反引用
    items = db.relationship("Item",backref="category")

class UserItemInteraction(db.Model):
    __tablename__ = 'user_item_interaction'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    item_id = db.Column(db.Integer, db.ForeignKey('item.item_id'))
    liked = db.Column(db.Boolean, default=False)
    disliked = db.Column(db.Boolean, default=False)

with app.app_context():
    db.drop_all()
    db.create_all()
def add_category():
    # Create a list of categories
    categories = ["women's clothing", "menswear", "cosmetics", "toy", "digital product", "snack"]
    # Create and add each category
    for category_name in categories:
        category = Category(category_name=category_name)
        db.session.add(category)
    # Commit all changes at once
    db.session.commit()
    # Close session
    db.session.close()
def add_item():
    item1 = Item(item_name="Trousers",photo="../static/picture/menswear5.jpg",address="china",
                item_details="Black trousers",price=96.2,duration= "2023/5/19",
                discount_limit=0.3,liked_quantity= 16)
    item2 = Item(item_name="Phone", photo="../static/picture/digital product2.jpg", address="USA",
                 item_details="Huawei Mobile phone", price=100.0, duration="2023/5/20",
                 discount_limit=0.3, liked_quantity=20)
    item3 = Item(item_name="T-shirt", photo="../static/picture/menswear2.jpg", address="USA",
                 item_details="Black T-shirt", price=120.0, duration="2023/5/20",
                 discount_limit=0.9, liked_quantity=3)
    item4 = Item(item_name="Bird toys", photo="../static/picture/toy1.jpg", address="USA",
                 item_details="Cute Little Bird Toys", price=200.0, duration="2023/5/30",
                 discount_limit=0.4, liked_quantity=100)
    item5 = Item(item_name="Little Bear Toys", photo="../static/picture/toy.jpg", address="china",
                 item_details="Cute little bear toy", price=180.0, duration="2023/5/20",
                 discount_limit=1, liked_quantity=19)
    item6 = Item(item_name="face cream", photo="../static/picture/cosmetics3.jpg", address="UK",
                 item_details="L'oreal", price=400.0, duration="2023/5/30",
                 discount_limit=1, liked_quantity=80)
    item7 = Item(item_name="Women's skirt", photo="../static/picture/women's wear3.jpg", address="UK",
                 item_details="A beautiful skirt", price=130.0, duration="2023/5/30",
                 discount_limit=0.5, liked_quantity=80)
    item8 = Item(item_name="Dress", photo="../static/picture/women's wear1.jpg", address="UK",
                 item_details="Cheap skirt", price=80.0, duration="2023/5/30",
                 discount_limit=0.9, liked_quantity=80)
    item9 = Item(item_name="Cookie", photo="../static/picture/snack2.jpg", address="UK",
                 item_details="delicious", price=80.0, duration="2023/5/30",
                 discount_limit=0.9, liked_quantity=80)
    item1.category = Category.query.filter_by(category_name="menswear").first()
    item2.category = Category.query.filter_by(category_name="digital product").first()
    item3.category = Category.query.filter_by(category_name="menswear").first()
    item4.category = Category.query.filter_by(category_name="toy").first()
    item5.category = Category.query.filter_by(category_name="toy").first()
    item6.category = Category.query.filter_by(category_name="cosmetics").first()
    item7.category = Category.query.filter_by(category_name="women's clothing").first()
    item8.category = Category.query.filter_by(category_name="women's clothing").first()
    item9.category = Category.query.filter_by(category_name="snack").first()
    db.session.add_all([item1,item2,item3,item4,item5,item6,item7,item8,item9])
    db.session.commit()
with app.app_context():
    add_category()
    add_item()
'''实现一个简单的登录逻辑处理
1.路由需要get和post两种请求方式-->判断请求方式
2.获取请求的参数
3.判断这个参数是否填写，密码是否相同
4.判断没问题，返回succeed'''
'''
给模板传递消息
flash-->需要对内容加密，因此需要设置secret_key
'''
app.secret_key = 'coursework'
@app.route('/register',methods =['GET', 'POST'])
def register():
    #request:请求对象-->获取请求方式，数据
    if request.method == 'POST':
        #2.获取请求的参数
        username = request.values.get('username')
        password = request.values.get('password')
        password2 = request.values.get('password2')
        #3.判断这个参数是否填写，密码是否相同
        if not all([username,password,password2]):
            #闪现消息
            flash('The input box cannot be empty')
        elif password != password2:
            flash('Entered passwords differ')
        elif password == username:
            flash('Password and account cannot be consistent')
        elif username.find("@")==-1:
            flash("The account needs to be in email format")
        elif username.find(".com")==-1:
            flash("账户需要是邮The account needs to be in email format箱格式")
        elif not 7 < len(username) < 20:
            flash("The username length needs to be greater than 7 and less than 20")
        else:
            user = User.query.filter_by(email=username).first()
            if user:
                flash("User already exists, please re-enter")
            else:
                user = User(password=password, email=username)
                db.session.add(user)
                db.session.commit()
                message = Message(recipient=user.user_id,content = "Welcome to the e-commerce website!")
                db.session.add(message)
                db.session.commit()
                cart = Cart(user_id = user.user_id)
                db.session.add(cart)
                db.session.commit()
                return redirect("/login")
    return render_template('register.html')
@app.route('/login',methods =['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')
        if not all([username, password]):
            # 闪现消息
            flash('The input box cannot be empty')
        elif username.find("@") == -1:
            flash("The account needs to be in email format")
        elif username.find(".com") == -1:
            flash("The account needs to be in email format")
        elif not 7 < len(username) < 20:
            flash("The username length needs to be greater than 7 and less than 20")
        else:
            user = User.query.filter_by(email=username).first()
            if user and user.password == password:  # 假设密码已经被加密保存
                session['user_id'] = user.user_id
                return redirect("/")
            else:
                flash("Incorrect username or password")
    return render_template('login.html')
@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")

@app.before_request
def before_request():
    user_id = session.get("user_id")
    if user_id:
        user = User.query.get(user_id)
        setattr(g,"user",user)
    else:
        setattr(g, "user", None)

@app.context_processor#所有模板可使用的对象
def context_processor():
    return {"user": g.user}

@app.route('/',methods =['GET', 'POST'])
def homepage():
    items = Item.query.all()
    return render_template('homePage.html',items=items)

@app.route('/goodsBrowsingInterface', methods=['GET', 'POST'])
# categories = ["women's clothing", "menswear", "cosmetics", "toy", "digital product", "snack"]
def goodsBrowsing():
    category1 = Category.query.filter_by(category_name="cosmetics").first()
    items_category1 = Item.query.filter_by(category=category1).all()

    category2 = Category.query.filter_by(category_name="menswear").first()
    items_category2 = Item.query.filter_by(category=category2).all()

    category3 = Category.query.filter_by(category_name="women's clothing").first()
    items_category3 = Item.query.filter_by(category=category3).all()

    category4 = Category.query.filter_by(category_name="toy").first()
    items_category4 = Item.query.filter_by(category=category4).all()

    category5 = Category.query.filter_by(category_name="digital product").first()
    items_category5 = Item.query.filter_by(category=category5).all()

    category6 = Category.query.filter_by(category_name="snack").first()
    items_category6 = Item.query.filter_by(category=category6).all()

    return render_template('goodsBrowsingInterface.html',
                           items_category1=items_category1,
                           items_category2=items_category2,
                           items_category3=items_category3,
                           items_category4=items_category4,
                           items_category5=items_category5,
                           items_category6=items_category6)

@app.route('/goodsInterface/<int:id>', methods=['GET', 'POST'])
def goodsInterface(id):
    item = Item.query.get(id)
    comment_detail = request.values.get('comment')
    mark = request.values.get('mark')
    if request.method == 'POST':
        comment = Comment(item_id=item.item_id,comment_details=comment_detail, mark=mark,name=g.user.name)
        db.session.add(comment)
        db.session.commit()
        if g.user:  # check if user is logged in
            item.cart_id = g.user.user_id
            db.session.add(item)
            db.session.commit()
        return redirect(url_for('goodsInterface', id=id))  # redirect back to the same page
    return render_template('goodsInterface.html', item=item)

@app.route('/like_item/<int:id>', methods=['POST'])
def like_item(id):
    item = Item.query.get(id)
    if item:
        interaction = UserItemInteraction.query.filter_by(user_id=g.user.user_id, item_id=id).first()
        if interaction:
            if not interaction.liked:
                interaction.liked = True
                interaction.disliked = False
                item.liked_quantity += 1
                item.disliked_quantity -= (item.disliked_quantity > 0)
        else:
            interaction = UserItemInteraction(user_id=g.user.user_id, item_id=id, liked=True)
            item.liked_quantity += 1
            db.session.add(interaction)
        db.session.commit()
    return redirect(url_for('goodsInterface', id=id))

@app.route('/dislike_item/<int:id>', methods=['POST'])
def dislike_item(id):
    item = Item.query.get(id)
    if item:
        interaction = UserItemInteraction.query.filter_by(user_id=g.user.user_id, item_id=id).first()
        if interaction:
            if not interaction.disliked:
                interaction.disliked = True
                interaction.liked = False
                item.disliked_quantity += 1
                item.liked_quantity -= (item.liked_quantity > 0) # decrease liked_quantity if it's more than 0
        else:
            interaction = UserItemInteraction(user_id=g.user.user_id, item_id=id, disliked=True)
            item.disliked_quantity += 1
            db.session.add(interaction)
        db.session.commit()
    return redirect(url_for('goodsInterface', id=id))


@app.route('/personInterface/<int:id>', methods=['GET', 'POST'])
def personInterface(id):
    information = User.query.get(id)
    if request.method == 'POST':
        name = request.values.get('name')
        address = request.values.get('address')
        email = request.values.get('email')
        phone = request.values.get('phone')
        # Update user's information
        information.name = name or information.name
        information.address = address or information.address
        information.email = email or information.email
        information.phone_number = phone or information.phone_number
        # Save the changes to the database
        db.session.commit()
    return render_template('personInterface.html', information = information)

@app.route('/delete_item/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
    return redirect(url_for('personInterface', id=g.user.user_id))  # redirect back to the personInterface page

@app.route('/publicItem/<int:id>', methods=['GET', 'POST'])
def publicItem(id):
    user = User.query.get(id)
    if request.method == 'POST':
        name = request.values.get('name')
        category_name = request.values.get('category')
        address = request.values.get('location')
        details = request.values.get('description')
        discount = request.values.get('discount')
        price = request.values.get('price')
        duration = request.values.get('duration')
        photo = "../static/picture/"+request.values.get('photo')+".jpg"
        category = Category.query.filter_by(category_name=category_name).first()
        item = Item(item_name=name, category_id=category.category_id,address=address, item_details=details, price=price,
                    discount_limit=discount,duration=duration,user_id=user.user_id,photo=photo)

        db.session.add(item)
        db.session.commit()
        return redirect(url_for('personInterface', id=id))
    return render_template('goodsPublicInterface.html', user = user)

@app.route('/cart/<int:id>', methods=['GET', 'POST'])
def cart(id):
    cart_items = Item.query.filter_by(cart_id=id).all()
    return render_template('cartInterface.html', items=cart_items)

@app.route('/payment/<int:id>', methods=['GET', 'POST'])
def pay(id):
    cart = Cart.query.filter_by(cart_id = id).first()
    return render_template('paymentInterface.html',cart = cart)

@app.route('/cart/update/<int:id>', methods=['POST'])
def update_cart(id):
    data = request.get_json()
    total_price = data.get('total_price')
    quantity = data.get('quantity')

    cart = Cart.query.get(id)
    if cart:
        cart.total_price = total_price
        cart.quantity = quantity
        db.session.commit()
    else:
        return jsonify({'error': 'Cart not found'}), 404

    return jsonify({'message': 'Cart updated successfully'}), 200

@app.route('/wechatPayment', methods=['GET', 'POST'])
def wechatPayment():
    return render_template('wechatPaymentPage.html')

@app.route('/alipayPayment', methods=['GET', 'POST'])
def ailipayPayment():
    return render_template('alipayPaymentPage.html')


@app.route('/paymentSuccess/<int:id>', methods=['GET', 'POST'])
def paymentSucessed(id):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cart = Cart.query.filter_by(cart_id=id).first()
    items = Item.query.filter_by(cart_id=id).all()
    order = Order(user_id=g.user.user_id, cart_id=id, total_price=cart.total_price, time=current_time)
    db.session.add(order)
    for item in items:
        message = Message(recipient=item.user_id, content="Your item has been purchased, please ship it as soon as possible!"+" Buyer ID:"
                                                          +str(g.user.user_id)+" Purchased items:"+item.item_name)
        db.session.add(message)
        db.session.commit()
    message = Message(recipient=g.user.user_id, content="Your order has been completed, completion time: " + order.time + " Total expenses: " + str(order.total_price), time=current_time)
    db.session.add(message)
    db.session.commit()
    @flask.after_this_request
    def remove_items(response):
        for item in items:
            item.cart_id = None
        db.session.commit()
        return response

    return render_template('paymentSuccessInterface.html', cart=cart, items=items, time=current_time)

@app.route('/message/<int:id>', methods=['GET', 'POST'])
def message(id):
    sent_messages = Message.query.filter_by(user_id=id).all()
    all_messages = Message.query.all()
    recipient = request.values.get('recipient_id')
    content = request.values.get('content')
    if request.method == 'POST':
        new_message = Message(recipient=recipient,content=content,user_id=id)
        db.session.add(new_message)
        db.session.commit()
    return render_template('messageInterface.html',message=all_messages,sent_messages =sent_messages)

if __name__ == '__main__':
    app.run(debug=True)
