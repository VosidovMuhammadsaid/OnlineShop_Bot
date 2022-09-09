import telebot
from telebot import types
import config
import pymysql

API_TOKEN = '5568683213:AAHpwRncT7DZ29YYzif-eMTf3O9hXnMIlKY'

bot = telebot.TeleBot(API_TOKEN)

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="default_name",
)

def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

# command /start
print("Starting.....")
@bot.message_handler(commands=['start'])
def send_welcome(message):
    #pipeline 0
    update_post_description = """UPDATE on_time SET pipeline = "{pipeline}" WHERE username="{username}" """.format(pipeline=0,username="admin")
    execute_query(connection,  update_post_description)
    connection.commit()

    markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    my_product = types.KeyboardButton(config.my_product)
    add_product = types.KeyboardButton(config.add_product)
    edit_product = types.KeyboardButton(config.edit_product)
    orders=types.KeyboardButton(config.orders)
    markup.row(my_product)
    markup.row(add_product,edit_product)
    markup.row(orders)
    bot.send_message(message.chat.id, config.menu_admin,reply_markup=markup)

# category part
def category(message):
    #pipeline 1
    update_post_description = """UPDATE on_time SET pipeline = "{pipeline}" WHERE username="{username}" """.format(pipeline=1,username="admin")
    execute_query(connection,  update_post_description)
    connection.commit()

    markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    back=types.KeyboardButton(config.back_home)
    tort=types.KeyboardButton(config.tort)
    desert=types.KeyboardButton(config.desert)
    hot_soda=types.KeyboardButton(config.hot_soda)
    cold_soda=types.KeyboardButton(config.cold_soda)
    markup.add(back)
    markup.add(tort,desert,hot_soda,cold_soda)
    bot.send_message(message.chat.id,config.category,reply_markup=markup)

# into menu
def into_menu(message):
    #pipeline 2
    update_post_description = """UPDATE on_time SET pipeline = "{pipeline}" WHERE username="{username}" """.format(pipeline=2,username="admin")
    execute_query(connection,  update_post_description)
    connection.commit()

    with connection.cursor() as cursor:
        select_all_rows_c = "SELECT * FROM `products`"
        cursor.execute(select_all_rows_c)
        rows = cursor.fetchall()

    markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    back = types.KeyboardButton(config.back_home)
    markup.row(back)

    for row in rows:
        if message.text == row[1]:
            buttons_prod =types.KeyboardButton(f"{row[2]}")
            markup.add(buttons_prod)
    bot.send_message(message.from_user.id,message.text,reply_markup=markup)

# edit into menu
def edit_into_menu(message):
    #pipeline 2
    update_post_description = """UPDATE on_time SET pipeline = "{pipeline}" WHERE username="{username}" """.format(pipeline=5,username="admin")
    execute_query(connection,  update_post_description)
    connection.commit()

    with connection.cursor() as cursor:
        select_all_rows_c = "SELECT * FROM `products`"
        cursor.execute(select_all_rows_c)
        rows = cursor.fetchall()

    markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    back = types.KeyboardButton(config.back_home)
    markup.row(back)

    for row in rows:
        if message.text == row[1]:
            buttons_prod =types.KeyboardButton(f"{row[2]}")
            markup.add(buttons_prod)
    bot.send_message(message.from_user.id,message.text,reply_markup=markup)


# into products
def my_into_product(message):
    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `products`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

    for row in rows:
        if message.text == row[2]:
            product_info=f'<a href="{row[4]}">&#8205;</a><b>{row[2]}</b>\n\n<i>{row[5]}</i>\n\n1 шт. = {row[3]} сомони\n\n<b>Общее количество: </b>{row[6]} штук'
            bot.send_message(message.chat.id,product_info, parse_mode='html')

# edit into products
def edit_into_product(message):
    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `products`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

    for row in rows:
        if message.text == row[2]:
            # update table "admin"
            update_post_description = """UPDATE on_time SET product = "{product}" WHERE username="{username}" """.format(product=message.text,username="admin")
            execute_query(connection,  update_post_description)
            connection.commit()

            # buttons create
            markup=types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
            back=types.KeyboardButton(config.back_home)
            edit_name=types.KeyboardButton(config.edit_name)
            edit_description=types.KeyboardButton(config.edit_description)
            edit_price=types.KeyboardButton(config.edit_price)
            edit_photo=types.KeyboardButton(config.edit_photo)
            edit_amount=types.KeyboardButton(config.edit_amount)
            delete_product=types.KeyboardButton(config.delete_product)
            markup.add(back,edit_name,edit_description,edit_price,edit_photo,edit_amount,delete_product)
            # send message
            product_info=f'<a href="{row[4]}">&#8205;</a><b>{row[2]}</b>\n\n<i>{row[5]}</i>\n\n1 шт. = {row[3]} сомони\n\n<b>Общее количество: </b>{row[6]} штук'
            bot.send_message(message.chat.id,product_info, parse_mode='html',reply_markup=markup)

def delete_product_text(message):
    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `on_time`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

    for row in rows:
        if row[2] == "admin":
            print(row[5])
            delete_comment = """DELETE FROM products WHERE name="{name_product}" """.format(name_product=str(row[5]))     
            execute_query(connection, delete_comment)
            connection.commit()
# add category name
def add_category_prod():
    #pipeline 1
    update_post_description = """UPDATE on_time SET pipeline = "{pipeline}" WHERE username="{username}" """.format(pipeline=1,username="admin")
    execute_query(connection,  update_post_description)
    connection.commit()

    markup=types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    back=types.KeyboardButton(config.back_home)
    tort=types.KeyboardButton(config.tort)
    desert=types.KeyboardButton(config.desert)
    hot_soda=types.KeyboardButton(config.hot_soda)
    cold_soda=types.KeyboardButton(config.cold_soda)
    markup.row(back)
    markup.add(tort,desert,hot_soda,cold_soda)
    return markup

# edit category name
def edit_category_prod(message):
    #pipeline 4
    update_post_description = """UPDATE on_time SET pipeline = "{pipeline}" WHERE username="{username}" """.format(pipeline=4,username="admin")
    execute_query(connection,  update_post_description)
    connection.commit()

    markup=types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    back=types.KeyboardButton(config.back_home)
    tort=types.KeyboardButton(config.tort)
    desert=types.KeyboardButton(config.desert)
    hot_soda=types.KeyboardButton(config.hot_soda)
    cold_soda=types.KeyboardButton(config.cold_soda)
    markup.row(back)
    markup.add(tort,desert,hot_soda,cold_soda)
    bot.send_message(message.chat.id,config.category,reply_markup=markup)

def add_product_category(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
    cancel = types.KeyboardButton(config.cancel)
    markup.row(cancel)

    if message.text!=config.cancel:
        global add_category 
        add_category=message.text
        bot.send_message(message.from_user.id,"Название продукта в категории <b><i>{message}</i></b>".format(message=message.text),reply_markup=markup,parse_mode='html')
        bot.register_next_step_handler(message,add_product_name)

def add_product_name(message):
    if message.text!=config.cancel:
        global add_name 
        add_name=message.text
        bot.send_message(message.from_user.id,"Введите цену продукта <b><i>{message}</i></b>".format(message=message.text),parse_mode='html')
        bot.register_next_step_handler(message,add_product_price)

def add_product_price(message):
    if message.text!=config.cancel:
        global add_price
        add_price=message.text
        bot.send_message(message.from_user.id,"Отправьте ссылку на фотографию <b><i>{message}</i></b>".format(message=add_name),parse_mode='html')
        bot.register_next_step_handler(message,add_product_photo)

def add_product_photo(message):
    if message.text!=config.cancel:
        global add_photo
        add_photo=message.text
        bot.send_message(message.from_user.id,"Отправьте описание продукта <b><i>{message}</i></b>".format(message=add_name),parse_mode='html')
        bot.register_next_step_handler(message,add_product_description)

def add_product_description(message):
    if message.text!=config.cancel:
        global add_description
        add_description=message.text
        bot.send_message(message.from_user.id,"Общее количество продукта <b><i>{message}</i></b>".format(message=add_name),parse_mode='html')
        bot.register_next_step_handler(message,add_product_total)

def add_product_total(message):
    if message.text!=config.cancel:
        global add_total
        add_total=message.text

        with connection.cursor() as cursor:
            insert_query = "INSERT INTO `products` (category, name,price,photo,description,general_product) VALUES (%s, %s,%s,%s,%s,%s);"
            cursor.execute(insert_query, (add_category, add_name,add_price,add_photo,add_description,add_total))
            connection.commit()
        bot.send_message(message.from_user.id,"Спасибо. Ваш продукт добавлен! \n\nНазвание продукта: <b>{name}</b>\nКатегория: <b>{category}</b>\nСтоимость: <b>{price}</b>\nСсылка на фото: <b>{photo}</b>\nОписание продукта: <b>{description}</b> \nОбщий количество продукта в кафе: <b>{total}</b>".format(name=add_name,category=add_category,price=add_price,photo=add_photo,description=add_description,total=add_total),parse_mode='html',reply_markup=send_welcome(message))

# edit name product
def edit_name_text(message):
    if message.text!=config.cancel:
        global edit_name_text
        edit_name_text=message.text
        bot.send_message(message.chat.id,"OK")
        bot.register_next_step_handler(message,send_welcome)

        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `on_time`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

        for row in rows:
            if row[2] == "admin":
                update_post_description = """UPDATE products SET name = "{edit_name}" WHERE name="{name_product}" """.format(edit_name=edit_name_text,name_product=row[5]) 
                execute_query(connection,update_post_description)
                connection.commit()

# edit description product
def edit_description_text(message):
    if message.text!=config.cancel:
        global edit_description_text
        edit_description_text=message.text
        bot.send_message(message.chat.id,"OK")
        bot.register_next_step_handler(message,send_welcome)

        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `on_time`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

        for row in rows:
            if row[2] == "admin":
                update_post_description = """UPDATE products SET description = "{edit_description}" WHERE name="{name_product}" """.format(edit_description=edit_description_text,name_product=row[5]) 
                execute_query(connection,update_post_description)
                connection.commit()

# edit price product
def edit_price_text(message):
    if message.text!=config.cancel:
        global edit_price_text
        edit_price_text=message.text
        bot.send_message(message.chat.id,"OK")
        bot.register_next_step_handler(message,send_welcome)

        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `on_time`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

        for row in rows:
            if row[2] == "admin":
                update_post_description = """UPDATE products SET price = "{edit_price}" WHERE name="{name_product}" """.format(edit_price=edit_price_text,name_product=row[5]) 
                execute_query(connection,update_post_description)
                connection.commit()

# edit photo product
def edit_photo_text(message):
    if message.text!=config.cancel:
        global edit_photo_text
        edit_photo_text=message.text
        bot.send_message(message.chat.id,"OK")
        bot.register_next_step_handler(message,send_welcome)

        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `on_time`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

        for row in rows:
            if row[2] == "admin":
                update_post_description = """UPDATE products SET photo = "{edit_photo}" WHERE name="{name_product}" """.format(edit_photo=edit_photo_text,name_product=row[5]) 
                execute_query(connection,update_post_description)
                connection.commit()

# edit amount product
def edit_amount_text(message):
    if message.text!=config.cancel:
        global edit_amount_text
        edit_amount_text=message.text
        bot.send_message(message.chat.id,"OK")
        bot.register_next_step_handler(message,send_welcome)

        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `on_time`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

        for row in rows:
            if row[2] == "admin":
                update_post_description = """UPDATE products SET general_product = "{edit_amount}" WHERE name="{name_product}" """.format(edit_amount=edit_amount_text,name_product=row[5]) 
                execute_query(connection,update_post_description)
                connection.commit()

#orders list
def orders_list(message):
    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `orders`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

    for row in rows:
        orders_info=f'<b>id: </b>{row[0]}\n<b>user_id: </b>{row[1]}\n\n<b>username: </b>@{row[2]}\n<b>ФИО: </b>{row[3]}\n<b>Телефон: </b>{row[4]}\n<b>Адрес: </b>{row[5]}\n\n<b>Продукты: </b>\n{row[6]}\n<b>Итого: </b>{row[7]} сомони\n\n<b>Дата: </b>{row[8]}'
        bot.send_message(message.chat.id,orders_info,parse_mode='html')
# messages 
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Main buttons
    if message.text==config.my_product:
        bot.send_message(message.chat.id,reply_markup=category(message))

    # catogory scene buttons
    # into products menu
    if message.text==config.tort or message.text==config.desert or message.text==config.hot_soda or message.text==config.cold_soda:
        print("yes")
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `on_time`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

        #pipeline 1
        for row in rows:
            if row[2] == "admin" and row[3]==1:
                bot.send_message(message.chat.id,reply_markup=into_menu(message))

    # edit into products menu
    if message.text==config.tort or message.text==config.desert or message.text==config.hot_soda or message.text==config.cold_soda:
        print("yes")
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `on_time`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

        #pipeline 1
        for row in rows:
            if row[2] == "admin" and row[3]==4:
                bot.send_message(message.chat.id,reply_markup=edit_into_menu(message))
    # edit product category scene
    if message.text==config.edit_product:
        bot.send_message(message.chat.id,reply_markup=edit_category_prod(message))
    
    # products info scene
    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `products`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

    for row in rows:
        if message.text==row[2]:
            print("yes")
            with connection.cursor() as cursor:
                select_all_rows = "SELECT * FROM `on_time`"
                cursor.execute(select_all_rows)
                rows = cursor.fetchall()

            #pipeline 2
            for row in rows:
                if row[2] == "admin" and row[3]==2:
                    bot.send_message(message.chat.id,reply_markup=my_into_product(message))
                if row[2] == "admin" and row[3]==5:
                    bot.send_message(message.chat.id,reply_markup=edit_into_product(message))

    # add_product_categoty
    if message.text==config.add_product:
        bot.send_message(message.from_user.id,config.send_menu,reply_markup=add_category_prod())
        bot.register_next_step_handler(message,add_product_category)

    # cancel button
    if message.text==config.cancel:
        bot.send_message(message.chat.id,reply_markup=send_welcome(message))

    # edit product name scene
    if message.text==config.edit_name:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
        cancel=types.KeyboardButton(config.cancel)
        markup.row(cancel)
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `on_time`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

        for row in rows:
            if row[2] == "admin":
                bot.send_message(message.from_user.id,f"Введите название {row[5]}",reply_markup=markup)
                bot.register_next_step_handler(message,edit_name_text)

    # edit product description scene
    if message.text==config.edit_description:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
        cancel=types.KeyboardButton(config.cancel)
        markup.row(cancel)
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `on_time`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

        for row in rows:
            if row[2] == "admin":
                bot.send_message(message.from_user.id,f"Введите описание {row[5]}",reply_markup=markup)
                bot.register_next_step_handler(message,edit_description_text)

    # edit product price scene
    if message.text==config.edit_price:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
        cancel=types.KeyboardButton(config.cancel)
        markup.row(cancel)
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `on_time`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

        for row in rows:
            if row[2] == "admin":
                bot.send_message(message.from_user.id,f"Введите цену {row[5]}",reply_markup=markup)
                bot.register_next_step_handler(message,edit_price_text)

    # edit product photo scene
    if message.text==config.edit_photo:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
        cancel=types.KeyboardButton(config.cancel)
        markup.row(cancel)
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `on_time`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

        for row in rows:
            if row[2] == "admin":
                bot.send_message(message.from_user.id,f"Введите ссылку фото {row[5]}",reply_markup=markup)
                bot.register_next_step_handler(message,edit_photo_text)

    # edit product amount scene
    if message.text==config.edit_amount:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
        cancel=types.KeyboardButton(config.cancel)
        markup.row(cancel)
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `on_time`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

        for row in rows:
            if row[2] == "admin":
                bot.send_message(message.from_user.id,f"Введите общее количество продукта {row[5]}",reply_markup=markup)
                bot.register_next_step_handler(message,edit_amount_text)

    # delete product from table
    if message.text==config.delete_product:
        bot.send_message(message.from_user.id,f"Ваш продукт удален",reply_markup=delete_product_text(message))

    # orders list
    if message.text==config.orders:
        print("yes")
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `on_time`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

        #pipeline 1
        for row in rows:
            if row[2] == "admin" and row[3]==0:
                bot.send_message(message.chat.id,reply_markup=orders_list(message))

    # back button
    if message.text==config.back_home:
        print("yes")
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `on_time`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

        #pipeline 1
        for row in rows:
            if row[2] == "admin" and row[3]==1:
                bot.send_message(message.chat.id,reply_markup=send_welcome(message))
            if row[2] == "admin" and row[3]==2:
                bot.send_message(message.chat.id,reply_markup=category(message))
            if row[2]=="admin" and row[3]==4:
                bot.send_message(message.chat.id,reply_markup=send_welcome(message))
            if row[2]=="admin" and row[3]==5:
                bot.send_message(message.chat.id,reply_markup=edit_category_prod(message))
bot.infinity_polling()
