import telebot
from telebot import types
import config
import config_taj


import time
import datetime

today = datetime.datetime.today()


API_TOKEN_BOT = '5036770261:AAFcKk_Te1gPZ_cn2Ch0TewM1w1RYf4rHnU'
API_TOKEN_ADMIN='5568683213:AAHpwRncT7DZ29YYzif-eMTf3O9hXnMIlKY'

bot = telebot.TeleBot(API_TOKEN_BOT)
bot_admin=telebot.TeleBot(API_TOKEN_ADMIN)

# pipeline 0 - /start
# pipeline 1 - category
# pipeline 2 - into_menu
# pipeline 3 - into product
# pipeline 4 - into amount product
# pipeline 5 - adding products in table shopping_list
# pipeline 6 - oformit_zakaz
# pipeline 7 - oplata zakaz
# pipeline 8 - nalichie
# pipelint 9 - edit profile

 #!/usr/bin/env python3
import MySQLdb

connection = MySQLdb.connect(
     host="host",
     user="user",
     passwd="pass",
     db="db_name",
     port=3306 
)

def execute_query(connection, query):
     cursor = connection.cursor()
     try:
         cursor.execute(query)
         connection.commit()
         print("Query executed successfully")
     except Error as e:
         print(f"The error '{e}' occurred")

# message /start ________________________________________________________________________________________________________________
print("Starting....")
@bot.message_handler(commands=['start'])
def send_welcome(message):

    # create table on_table
    with connection.cursor() as cursor:
        select_all_rows = """SELECT * FROM `on_time` WHERE user_id="{message}" """.format(message=message.from_user.id)
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

        if rows:
            print("Yes")
        else:
            print("No")
            with connection.cursor() as cursor:
                insert_query = "INSERT INTO `on_time` (user_id,username, pipeline,language,product,price,amount) VALUES (%s,%s, %s,%s,%s,%s,%s);"
                cursor.execute(insert_query, (message.from_user.id,message.from_user.username, 0,"config_ru","-",0,0))
                connection.commit()

    # update table pipeline 0 _______________________________________________________________________________________
    update_post_description = """UPDATE on_time SET pipeline = "{pipeline}" WHERE username="{username}" """.format(pipeline=0,username=message.from_user.username)
    execute_query(connection,  update_post_description)
    connection.commit()

    # profile create username
    with connection.cursor() as cursor:
        select_all_rows = """SELECT * FROM `profiles` WHERE user_id="{message}" """.format(message=message.from_user.id)
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

        if rows:
            print("Yes")
        else:
            print("No")
            with connection.cursor() as cursor:
                insert_query = "INSERT INTO `profiles` (user_id,username_telegram, fio, address, phone) VALUES (%s, %s, %s, %s,%s);"
                cursor.execute(insert_query, (message.from_user.id,message.from_user.username, "-", "-", "-"))
                connection.commit()

    #create main buttons
    # button active /start
    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `on_time`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

    for row in rows:
        if row[1] == str(message.from_user.id):
            if row[4]=="config_ru":
                markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
                start_order = types.KeyboardButton(config.start_order)
                my_profile = types.KeyboardButton(config.my_profile)
                my_order = types.KeyboardButton(config.my_order)
                language=types.KeyboardButton(config.language)
                consultant=types.KeyboardButton(config.consultant)
                comments=types.KeyboardButton(config.comments)
                markup.row(start_order)
                markup.row(my_profile,my_order)
                markup.row(language,consultant)
                markup.row(comments)
                bot.send_message(message.chat.id, config.start_welcome, reply_markup=markup)
            else:
                markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
                start_order = types.KeyboardButton(config_taj.start_order)
                my_profile = types.KeyboardButton(config_taj.my_profile)
                my_order = types.KeyboardButton(config_taj.my_order)
                language=types.KeyboardButton(config_taj.language)
                consultant=types.KeyboardButton(config_taj.consultant)
                comments=types.KeyboardButton(config_taj.comments)
                markup.row(start_order)
                markup.row(my_profile,my_order)
                markup.row(language,consultant)
                markup.row(comments)
                bot.send_message(message.chat.id, config_taj.start_welcome, reply_markup=markup)

# Oformit zalaz _____________________________________________________________________________________________________________
def oformit_zakaz(message):
    update_post_description = """UPDATE on_time SET pipeline = "{pipeline}" WHERE user_id="{username}" """.format(pipeline=6,username=message.from_user.id)
    execute_query(connection,  update_post_description)
    connection.commit()

    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `on_time`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

    for row in rows:
        if row[1] == str(message.from_user.id):
            if row[4]=="config_ru":            
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                promokod=types.KeyboardButton(config.promokod)
                oplata_zakaz=types.KeyboardButton(config.oplata_zakaz)
                back_home=types.KeyboardButton(config.back_home)
                markup.row(promokod)
                markup.row(oplata_zakaz)
                markup.row(back_home)
                bot.send_message(message.from_user.id,"Вы можете оформить заказ:",reply_markup=markup)
            else:
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                promokod=types.KeyboardButton(config_taj.promokod)
                oplata_zakaz=types.KeyboardButton(config_taj.oplata_zakaz)
                back_home=types.KeyboardButton(config_taj.back_home)
                markup.row(promokod)
                markup.row(oplata_zakaz)
                markup.row(back_home)
                bot.send_message(message.from_user.id,"Шумо метавонед фармоиш диҳед:",reply_markup=markup)

    shopping_info = "Товары на корзине\n\n"
    total_list_sum = 0
    markup=types.InlineKeyboardMarkup(row_width=3)

    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `shopping_list`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

    for row in rows:
        if row[1] == str(message.from_user.id):
            product_sum = row[5]*row[4]
            shopping_info = shopping_info + "🔹 " + row[3] + " - " + str(row[4])+" сомони\n└ "+str(row[5])+" x "+str(row[4])+" = "+str(product_sum) + " сомони\n\n"
            total_list_sum = total_list_sum + product_sum

    if total_list_sum == 0:
        shopping_cart_text = config.cart_empty
    else:
        shopping_cart_text = f'{shopping_info}Продукты: <b>{total_list_sum} сомони</b> \nДоставка: <b>Отсутствует</b>\nДля оплаты: <b>{total_list_sum} сомони</b> '
    bot.send_message(message.from_user.id, shopping_cart_text, parse_mode='html', reply_markup=markup)


# category scene _____________________________________________________________________________________________________________
def category_prod(message):
    update_post_description = """UPDATE on_time SET pipeline = "{pipeline}" WHERE user_id="{username}" """.format(pipeline=1,username=message.from_user.id)
    execute_query(connection, update_post_description)
    connection.commit()

    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `on_time`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

    for row in rows:
        if row[1] == str(message.from_user.id):
            if row[4]=="config_ru":
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
                back = types.KeyboardButton(config.back_home)
                cart = types.KeyboardButton(config.cart)
                tort=types.KeyboardButton(config.tort)
                desert=types.KeyboardButton(config.desert)
                hot_soda=types.KeyboardButton(config.hot_soda)
                cold_soda=types.KeyboardButton(config.cold_soda)
                markup.row(back,cart)
                markup.row(tort,desert)
                markup.row(hot_soda,cold_soda)
                bot.send_message(message.chat.id,config.send_menu, reply_markup=markup)
            else:
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
                back = types.KeyboardButton(config_taj.back_home)
                cart = types.KeyboardButton(config_taj.cart)
                tort=types.KeyboardButton(config.tort)
                desert=types.KeyboardButton(config.desert)
                hot_soda=types.KeyboardButton(config.hot_soda)
                cold_soda=types.KeyboardButton(config.cold_soda)
                markup.row(back,cart)
                markup.row(tort,desert)
                markup.row(hot_soda,cold_soda)
                bot.send_message(message.chat.id,config_taj.send_menu, reply_markup=markup)

# INTO MENU PRODUCTS _____________________________________________________________________________________________________
def into_menu(message):
    update_post_description = """UPDATE on_time SET pipeline = "{pipeline}" WHERE user_id="{username}" """.format(pipeline=2,username=message.from_user.id)
    execute_query(connection,  update_post_description)
    connection.commit()

    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `on_time`"
        cursor.execute(select_all_rows)
        rows_c = cursor.fetchall()

    for row_c in rows_c:
        if row_c[1] == str(message.from_user.id):
            if row_c[4]=="config_ru":
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
                back = types.KeyboardButton(config.back_home)
                cart = types.KeyboardButton(config.cart)
                markup.row(back,cart)
            else:
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
                back = types.KeyboardButton(config_taj.back_home)
                cart = types.KeyboardButton(config_taj.cart)
                markup.row(back,cart)

    with connection.cursor() as cursor:
        select_all_rows_c = "SELECT * FROM `products`"
        cursor.execute(select_all_rows_c)
        rows = cursor.fetchall()

    for row in rows:
        if message.text == row[1]:
            buttons_prod =types.KeyboardButton(f"{row[2]}")
            markup.add(buttons_prod)
    bot.send_message(message.from_user.id,message.text,reply_markup=markup)

# into product _____________________________________________________________________________________________________________
def into_product(message):
    update_post_description = """UPDATE on_time SET pipeline = "{pipeline}" WHERE user_id="{username}" """.format(pipeline=3,username=message.from_user.id)
    execute_query(connection,  update_post_description)
    connection.commit()

    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `on_time`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

    for row in rows:
        if row[1] == str(message.from_user.id):
            if row[4]=="config_ru":
                #into_product -> into_amount_product
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
                back = types.KeyboardButton(config.to_menu)
                cart = types.KeyboardButton(config.cart)
                markup.row(back,cart)
            else:
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
                back = types.KeyboardButton(config_taj.to_menu)
                cart = types.KeyboardButton(config_taj.cart)
                markup.row(back,cart)

    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `products`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

    for row in rows:
        if message.text == row[2]:
            # update table on_time PRODUCT
            update_post_description = """UPDATE on_time SET product = "{product}" WHERE user_id="{username}" """.format(product=str(row[2]),username=str(message.from_user.id))
            execute_query(connection, update_post_description)
            connection.commit()

            update_post_description1 = """UPDATE on_time SET price = "{price}" WHERE user_id="{username}" """.format(price=str(row[3]),username=str(message.from_user.id))
            execute_query(connection, update_post_description1)
            connection.commit()

            buttons_prod =types.KeyboardButton(f"1 шт. - {row[3]} сомони")
            markup.add(buttons_prod)
            info = row[2]+"\n"
            bot.send_message(message.from_user.id, f'<a href="{row[4]}">&#8205;</a>{info}\n<i>{row[5]}</i>', parse_mode='html', reply_markup=markup)

def into_amount_product(message):
    update_post_description = """UPDATE on_time SET pipeline = "{pipeline}" WHERE user_id="{username}" """.format(pipeline=4,username=message.from_user.id)
    execute_query(connection,  update_post_description)
    connection.commit()

    #into_product -> into_amount_product
    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `on_time`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

    for row in rows:
        if row[1] == str(message.from_user.id):
            if row[4]=="config_ru":
                #into_product -> into_amount_product
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
                back = types.KeyboardButton(config.to_menu)
                cart = types.KeyboardButton(config.cart)
                markup.row(back,cart)
            else:
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
                back = types.KeyboardButton(config_taj.to_menu)
                cart = types.KeyboardButton(config_taj.cart)
                markup.row(back,cart)

    one = types.KeyboardButton("1")
    two = types.KeyboardButton("2")
    three = types.KeyboardButton("3")
    four = types.KeyboardButton("4")
    five = types.KeyboardButton("5")
    six = types.KeyboardButton("6")
    seven = types.KeyboardButton("7")
    eight = types.KeyboardButton("8")
    nine = types.KeyboardButton("9")
    markup.row(one,two,three)
    markup.row(four,five,six)
    markup.row(seven,eight,nine)

    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `on_time`"
        cursor.execute(select_all_rows)
        rows_c = cursor.fetchall()

    for row_c in rows_c:
        if row_c[1] == str(message.from_user.id):
            if message.text == f"1 шт. - {row_c[6]} сомони" or message.text==f"1 дона - {row_c[6]} сомон":
                break
    info = row_c[5]+" - 1 шт.\n\n1 шт. = "
    instuction = " сомони\n\nСколько вы хотите заказать, используйте кнопки ниже или пишите."
    
    bot.send_message(message.from_user.id, f'<a href="{row[4]}">&#8205;</a>{info}{row_c[6]}{instuction}', parse_mode='html', reply_markup=markup)

# add to shopping cart and uploading on table shopping_list
def add_to_shoping_cart(message):
    update_post_description = """UPDATE on_time SET pipeline = "{pipeline}" WHERE user_id="{username}" """.format(pipeline=5,username=message.from_user.id)
    execute_query(connection,  update_post_description)
    connection.commit()

    #into_amount_product -> add_to_shoping_cart ###need to see if shopping card should accept from pipeline 10

    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `products`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

    for row in rows:
        break
    product = row[2]
    amount = message.text
    price = row[3]
    username = message.from_user.username

    #update amount product in on_table
    update_post_description = """UPDATE on_time SET amount = "{amount}" WHERE user_id="{username}" """.format(amount=message.text,username=message.from_user.id)
    execute_query(connection,  update_post_description)
    connection.commit()
    #uploading to DB
    

    #here the problem is that when user added one product 2 times, it gets as different products
    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `on_time`"
        cursor.execute(select_all_rows)
        rows_c = cursor.fetchall()

    for row_c in rows_c:
        if row_c[1] == str(message.from_user.id):
            with connection.cursor() as cursor:
                insert_query = "INSERT INTO `shopping_list` (user_id,username, product, price, amount) VALUES (%s,%s, %s, %s, %s);"
                cursor.execute(insert_query, (str(message.from_user.id),message.from_user.username, str(row_c[5]), int(row_c[6]), amount))
                connection.commit()
            if row_c[4]=="config_ru":
                bot.send_message(message.from_user.id, f'✅ <b>{str(row_c[5])}</b> - {amount} {config.added_in_cart}<i>{config.instruction_after_adding}</i>', parse_mode='html',reply_markup=category_prod(message))
            else:
                bot.send_message(message.from_user.id, f'✅ <b>{str(row_c[5])}</b> - {amount} {config_taj.added_in_cart}<i>{config_taj.instruction_after_adding}</i>', parse_mode='html',reply_markup=category_prod(message))
                
                

   
# CART LIST
def into_shopping_cart(message):
    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `on_time`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

    for row in rows:
        if row[1] == str(message.from_user.id):
            if row[4]=="config_ru":
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                oformit=types.KeyboardButton(config.start_oformit_order)
                to_menu=types.KeyboardButton(config.to_menu)
                markup.row(oformit)
                markup.row(to_menu)
                bot.send_message(message.from_user.id, config.cart_send, reply_markup=markup)
            else:
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                oformit=types.KeyboardButton(config_taj.start_oformit_order)
                to_menu=types.KeyboardButton(config_taj.to_menu)
                markup.row(oformit)
                markup.row(to_menu)
                bot.send_message(message.from_user.id, config_taj.cart_send, reply_markup=markup)
                
    shopping_info = "Товары в корзине\n\n"
    total_list_sum = 0
    markup=types.InlineKeyboardMarkup(row_width=3)
    
    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `shopping_list`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

    for row in rows:
        if row[1] == str(message.from_user.id):
            product_sum = row[5]*row[4]
            shopping_info = shopping_info + "🔹 " + row[3] + " - " + str(row[4])+" сомони\n└ "+str(row[5])+" x "+str(row[4])+" = "+str(product_sum) + " сомони\n\n"
            total_list_sum = total_list_sum + product_sum
            minus=types.InlineKeyboardButton("➖", callback_data='decrease'+str(row[0]))
            cancel=types.InlineKeyboardButton("❌", callback_data='remove'+str(row[0]))
            plus=types.InlineKeyboardButton("➕", callback_data='increase'+str(row[0]))
            markup.add(minus,cancel,plus)


    if total_list_sum == 0:
        shopping_cart_text = config.cart_empty
    else:
        shopping_cart_text = f'{shopping_info}Итого: <b>{total_list_sum} сомони</b>'
    bot.send_message(message.from_user.id, shopping_cart_text, parse_mode='html', reply_markup=markup)

#EDIT PRODUCT IN SHOPPING CART
def edit_shopping_cart(message):

    shopping_info = "Товары в корзине\n\n"
    total_list_sum = 0
    markup=types.InlineKeyboardMarkup(row_width=3)

    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `shopping_list`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

    for row in rows:
        if row[1] == str(message.from_user.id):
            product_sum = row[5]*row[4]
            shopping_info = shopping_info + "🔹 " + row[3] + " - " + str(row[4])+" сомони\n└ "+str(row[5])+" x "+str(row[4])+" = "+str(product_sum) + " сомони\n\n"
            total_list_sum = total_list_sum + product_sum
            minus=types.InlineKeyboardButton("➖", callback_data='decrease'+str(row[0]))
            cancel=types.InlineKeyboardButton("❌", callback_data='remove'+str(row[0]))
            plus=types.InlineKeyboardButton("➕", callback_data='increase'+str(row[0]))
            markup.add(minus,cancel,plus)

    if total_list_sum == 0:
        shopping_cart_text = config.cart_empty
    else:
        shopping_cart_text = f'{shopping_info}Итого: <b>{total_list_sum} сомони</b>'
    bot.send_message(message.from_user.id, shopping_cart_text, parse_mode='html', reply_markup=markup)


# edit_profile button and back
def profile_button(message):
    update_post_description = """UPDATE on_time SET pipeline = "{pipeline}" WHERE username="{username}" """.format(pipeline=1,username=message.from_user.username)
    execute_query(connection,  update_post_description)
    connection.commit()

    with connection.cursor() as cursor:
        select_all_rows = """SELECT * FROM `profiles` WHERE user_id="{message}" """.format(message=message.from_user.id)
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

        for row in rows:
            if rows:
                with connection.cursor() as cursor:
                    select_all_rows = "SELECT * FROM `on_time`"
                    cursor.execute(select_all_rows)
                    rows_c = cursor.fetchall()

                for row_c in rows_c:
                    if row_c[1] == str(message.from_user.id):
                        if row_c[4]=="config_ru":
                            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                            edit_profile=types.KeyboardButton(config.edit_profile)
                            back=types.KeyboardButton(config.back_home)
                            markup.add(edit_profile,back)
                            bot.send_message(message.from_user.id,"Ваш профиль: \n\nФИО: <b>{fio}</b>\nАдрес: <b>{address}</b>\nТелефон: <b>{phone}</b>".format(fio=row[3],address=row[4],phone=row[5]), parse_mode='html',reply_markup=markup)
                        else:
                            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                            edit_profile=types.KeyboardButton(config_taj.edit_profile)
                            back=types.KeyboardButton(config_taj.back_home)
                            markup.add(edit_profile,back)
                            bot.send_message(message.from_user.id,"Профили шумо: \n\nНоми пурра: <b>{fio}</b>\nСурога: <b>{address}</b>\nРаками телефон: <b>{phone}</b>".format(fio=row[3],address=row[4],phone=row[5]), parse_mode='html',reply_markup=markup)

def edit_profiles(message):
    update_post_description = """UPDATE on_time SET pipeline = "{pipeline}" WHERE user_id="{username}" """.format(pipeline=13,username=message.from_user.id)
    execute_query(connection,  update_post_description)
    connection.commit()

    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `on_time`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

    for row in rows:
        if row[1] == str(message.from_user.id):
            if row[4]=="config_ru":
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                back=types.KeyboardButton(config.back_home)
                edit_name=types.KeyboardButton(config.edit_fio)
                edit_address=types.KeyboardButton(config.edit_address)
                edit_phone=types.KeyboardButton(config.edit_phone)
                markup.row(back,edit_name)
                markup.row(edit_address)
                markup.row(edit_phone)
                bot.send_message(message.from_user.id,config.edit_profile_buuton,reply_markup=markup)
            else:
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                back=types.KeyboardButton(config_taj.back_home)
                edit_name=types.KeyboardButton(config_taj.edit_fio)
                edit_address=types.KeyboardButton(config_taj.edit_address)
                edit_phone=types.KeyboardButton(config_taj.edit_phone)
                markup.row(back,edit_name)
                markup.row(edit_address)
                markup.row(edit_phone)
                bot.send_message(message.from_user.id,config_taj.edit_profile_buuton,reply_markup=markup)


# BUTTON Language
def language(message):
    update_post_description = """UPDATE on_time SET pipeline = "{pipeline}" WHERE user_id="{username}" """.format(pipeline=1,username=message.from_user.id)
    execute_query(connection,  update_post_description)
    connection.commit()

    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `on_time`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

    for row in rows:
        if row[1] == str(message.from_user.id):
            if row[4]=="config_ru":
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                back=types.KeyboardButton(config.back_home)
                rus=types.KeyboardButton(config.rus_keyboard)
                taj=types.KeyboardButton(config.taj_keyboard)
                markup.add(back)
                markup.add(rus,taj)
                bot.send_message(message.from_user.id,"Выберите желаемый язык \n\nЗабони худро интихоб кунед",reply_markup=markup)
            else:
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                back=types.KeyboardButton(config_taj.back_home)
                rus=types.KeyboardButton(config.rus_keyboard)
                taj=types.KeyboardButton(config.taj_keyboard)
                markup.add(back)
                markup.add(rus,taj)
                bot.send_message(message.from_user.id,"Выберите желаемый язык \n\nЗабони худро интихоб кунед",reply_markup=markup)

#actions in shopping list
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    #try:
    if call.message:
        if call.data == "rus":
            update_post_description = """UPDATE on_time SET language = "{pipeline}" WHERE user_id="{username}" """.format(pipeline="config_ru",username=call.from_user.id)
            execute_query(connection,  update_post_description)
            connection.commit()
            bot.send_message(call.from_user.id,reply_markup=send_welcome(message))
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `shopping_list`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

        for row in rows:
            if call.data == 'remove'+str(row[0]):
                #delete product
                with connection.cursor() as cursor:
                    delete_query = "DELETE FROM `shopping_list` WHERE id = %s;"
                    cursor.execute(delete_query, row[0])
                    connection.commit()

                #bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text= shopping_info, reply_markup=markup)
                #bot.send_message(call.message.chat.id, "heellooo!!!")

                #bot.delete_message(chat_id = call.message.chat.id, message_id = call.message.id, reply_markup=into_shopping_cart(call))
                bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                bot.send_message(call.message.chat.id,reply_markup=edit_shopping_cart(call))
                break
            
            if call.data == 'increase'+str(row[0]):

                total=int(row[5])
                total+=1
                #update amount
                print(total)

                update_post_description = """
                UPDATE
                shopping_list
                SET
                amount = "{amount}"
                WHERE
                product="{row}"
                """.format(amount=total,row=row[3])

                execute_query(connection,  update_post_description)
                connection.commit()

                bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                bot.send_message(call.message.chat.id,reply_markup=edit_shopping_cart(call))

            if call.data == 'decrease'+str(row[0]):
                if row[5]==0:
                    with connection.cursor() as cursor:
                        delete_query = "DELETE FROM `shopping_list` WHERE id = %s;"
                        cursor.execute(delete_query, row[0])
                        connection.commit()
                else:
                    total=int(row[5])
                    total-=1
                    #update amount
                    print(total)

                    update_post_description = """
                    UPDATE
                    shopping_list
                    SET
                    amount = "{amount}"
                    WHERE
                    product="{row}"
                    """.format(amount=total,row=row[3])

                    execute_query(connection,  update_post_description)
                    connection.commit()

                    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                    bot.send_message(call.message.chat.id,reply_markup=edit_shopping_cart(call))
# Oplata zakaz
def oplata_zakaza(message):
    update_post_description = """UPDATE on_time SET pipeline = "{pipeline}" WHERE user_id="{username}" """.format(pipeline=7,username=message.from_user.id)
    execute_query(connection,  update_post_description)
    connection.commit()

    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `on_time`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

    for row in rows:
        if row[1] == str(message.from_user.id):
            if row[4]=="config_ru":
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                nalichie=types.KeyboardButton(config.nalichie)
                back_home=types.KeyboardButton(config.back_home)
                markup.add(nalichie)
                markup.add(back_home)
                bot.send_message(message.from_user.id,"Каким способом вы хотите оплатить заказ ? \n\n<i>Выберите один из следующих.</i>",parse_mode='html', reply_markup=markup)
            else:
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                nalichie=types.KeyboardButton(config_taj.nalichie)
                back_home=types.KeyboardButton(config_taj.back_home)
                markup.add(nalichie)
                markup.add(back_home)
                bot.send_message(message.from_user.id,"Чӣ тавр шумо мехоҳед фармоишро пардохт кунед? \n\n<i>Яке аз зеринро интихоб кунед.</i>",parse_mode='html', reply_markup=markup)

#Nalichie
def order(message):
    
    update_post_description = """UPDATE on_time SET pipeline = "{pipeline}" WHERE user_id="{username}" """.format(pipeline=8,username=message.from_user.id)
    execute_query(connection,  update_post_description)
    connection.commit()

    shopping_info=""
    total_list_sum = 0

    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `shopping_list`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

    for row in rows:
        if row[1] == str(message.from_user.id):
            product_sum = row[5]*row[4]
            shopping_info = shopping_info + row[3]+" - " + str(row[5])+"шт. x "+str(row[4])+" = "+str(product_sum) + " сомони\n"
            total_list_sum = total_list_sum + product_sum
    
    with connection.cursor() as cursor:
        select_all_rows = """SELECT * FROM `profiles` WHERE username_telegram="{message}" """.format(message=message.from_user.username)
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

        for row in rows:
            if rows:
                data=today.strftime("%Y-%m-%d %H.%M.%S")
                insert_query = "INSERT INTO `orders` (user_id,username_telegram, username, phone, address,products,price,data) VALUES (%s,%s, %s, %s, %s,%s,%s,%s);"
                cursor.execute(insert_query, (message.from_user.id,message.from_user.username, row[3], row[4], row[5],shopping_info,total_list_sum,data))
                connection.commit()

    if total_list_sum == 0:
        shopping_cart_text = config.cart_empty
    else:
        shopping_cart_text = f'{shopping_info}Продукты: <b>{total_list_sum} сомони</b> \nДоставка: <b>Отсутствует</b>\nДля оплаты: <b>{total_list_sum} сомони</b> '
    
    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `on_time`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

    for row in rows:
        if row[1] == str(message.from_user.id):
            if row[4]=="config_ru":
                bot.send_message(message.from_user.id, f"Заказ принят и отправлен на рассмотрение модераторам.", parse_mode='html', reply_markup=send_welcome(message))
            else:
                bot.send_message(message.from_user.id, f"Фармоиш гирифта ва фиристода шуд ба баррасии модератор.", parse_mode='html', reply_markup=send_welcome(message))

    with connection.cursor() as cursor:
        delete_query = "DELETE FROM `shopping_list` WHERE user_id = %s;"
        cursor.execute(delete_query, row[1])
        connection.commit()


#edit fio
def edit_names(message):

    if message.text==config.back_home or message.text==config_taj.back_home:
        bot.send_message(message.from_user.id,reply_markup=edit_profiles(message))
    else:
        global edit_name
        edit_name=message.text

        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `on_time`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

        for row in rows:
            if row[1] == str(message.from_user.id):
                if row[4]=="config_ru":
                    bot.send_message(message.from_user.id,config.thank_edit_fio)
                else:
                    bot.send_message(message.from_user.id,config_taj.thank_edit_fio)

        update_post_description = """UPDATE profiles SET fio = "{edit_fio}" WHERE user_id="{username_telegram}" """.format(edit_fio=edit_name,username_telegram=message.from_user.id)
        execute_query(connection, update_post_description)
        connection.commit()

#edit address
def edit_address(message):
    if message.text==config.back_home or message.text==config_taj.back_home:
        bot.send_message(message.from_user.id,reply_markup=edit_profiles(message))
    else:
        global edit_address
        edit_address=message.text
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `on_time`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

        for row in rows:
            if row[1] == str(message.from_user.id):
                if row[4]=="config_ru":
                    bot.send_message(message.from_user.id,config.thank_edit_address)
                else:
                    bot.send_message(message.from_user.id,config_taj.thank_edit_address)
        update_post_description = """UPDATE profiles SET address = "{edit_address}" WHERE user_id="{username_telegram}" """.format(edit_address=edit_address,username_telegram=message.from_user.id)
        execute_query(connection, update_post_description)
        connection.commit()

#edit address
def edit_phone(message):
    if message.text==config.back_home or message.text==config_taj.back_home:
        bot.send_message(message.from_user.id,reply_markup=edit_profiles(message))
    else:
        global edit_phone
        edit_phone=message.text

        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `on_time`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

        for row in rows:
            if row[1] == str(message.from_user.id):
                if row[4]=="config_ru":
                    bot.send_message(message.from_user.id,config.thank_edit_phone)
                else:
                    bot.send_message(message.from_user.id,config_taj.thank_edit_phone)

        update_post_description = """UPDATE profiles SET phone = "{edit_phone}" WHERE user_id="{username_telegram}" """.format(edit_phone=edit_phone,username_telegram=message.from_user.id)
        execute_query(connection,  update_post_description)
        connection.commit()

# my products
def my_products(message):
    with connection.cursor() as cursor:
        select_all_rows = """SELECT * FROM `orders` WHERE user_id="{message}" """.format(message=message.from_user.id)
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

        for row in rows:
            if rows:
                with connection.cursor() as cursor:
                    select_all_rows = "SELECT * FROM `on_time`"
                    cursor.execute(select_all_rows)
                    rows_c = cursor.fetchall()

                for row_c in rows_c:
                    if row_c[1] == str(message.from_user.id):
                        if row_c[4]=="config_ru":
                            my_products_list=f"номер заказа: <b>{row[0]}</b>\nСтатус: <b>Заказан</b>\nДата: <b>{row[8]}</b>\n\n🔹{row[6]}\nСпособ оплаты: <b>💰 Наличные</b>\n\nДля продукта: <b>{row[7]} сомони</b>\n\nСкидка: <b>0 сомони</b>\nИтого: <b>{row[7]} сомони</b>"
                            bot.send_message(message.from_user.id,my_products_list, parse_mode='html')
                        else:
                            my_products_list=f"Рақами супоришдода: <b>{row[0]}</b>\nҲолат: <b>Фармон дода шудааст</b>\nСана: <b>{row[8]}</b>\n\n🔹{row[6]}\nНамуди пардохт: <b>💰 Пули накд</b>\n\nБарои маҳсулот: <b>{row[7]} сомон</b>\n\nТахфиф: <b>0 сомон</b>\nУмуми: <b>{row[7]} сомон</b>"
                            bot.send_message(message.from_user.id,my_products_list, parse_mode='html')

# Button Contacts
def contacts(message):
    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `on_time`"
        cursor.execute(select_all_rows)
        rows_c = cursor.fetchall()

    for row_c in rows_c:
        if row_c[1] == str(message.from_user.id):
            if row_c[4]=="config_ru":
                bot.send_message(message.from_user.id,f"📍 Наш адрес: \n 📌 - \n📱 Телефон: <b>+992400084277</b>\n📪 Почта: vosidovmuhammadsaid2007@gmail.com",parse_mode='html')
            else:
                bot.send_message(message.from_user.id,f"📍 Сурогаи мо: \n 📌 - \n📱 Ракам барои тамос: <b>+992400084277</b>\n📪 Почтаи электрони: vosidovmuhammadsaid2007@gmail.com",parse_mode='html')

#comments 
def leave_comments(message):
    if message.text==config.back_home or message.text==config_taj.back_home:
        print("to_home")
        bot.send_message(message.from_user.id,reply_markup=send_welcome(message))
    else:
        global comment  
        comment=message.text  
        
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `on_time`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

        for row in rows:
            if row[1] == str(message.from_user.id):
                if row[4]=="config_ru":
                    bot.send_message(message.from_user.id,config.thank_comment)
                    bot.register_next_step_handler(message,thanks_comment)
                else:
                    bot.send_message(message.from_user.id,config_taj.thank_comment)
                    bot.register_next_step_handler(message,thanks_comment)
        with connection.cursor() as cursor:
            insert_query = "INSERT INTO `comments` (username, text) VALUES (%s, %s);"
            cursor.execute(insert_query, (message.from_user.username, comment))
            connection.commit()

def thanks_comment(message):
    bot.send_message(message.from_user.id,reply_markup=send_welcome(message))
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # profile edit FIO
    if message.text==config.edit_fio or message.text==config_taj.edit_fio:
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `on_time`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

        for row in rows:
            if row[1] == str(message.from_user.id):
                if row[4]=="config_ru":
                    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                    back_home=types.KeyboardButton(config.back_home)
                    markup.row(back_home)
                    bot.send_message(message.from_user.id,config.your_fio,reply_markup=markup)
                else:
                    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                    back_home=types.KeyboardButton(config_taj.back_home)
                    markup.row(back_home)
                    bot.send_message(message.from_user.id,config_taj.your_fio,reply_markup=markup)
        bot.register_next_step_handler(message,edit_names)

    # profile edit ADDRESS
    if message.text==config.edit_address or message.text==config_taj.edit_address:
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `on_time`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

        for row in rows:
            if row[1] == str(message.from_user.id):
                if row[4]=="config_ru":
                    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                    back_home=types.KeyboardButton(config.back_home)
                    markup.row(back_home)
                    bot.send_message(message.from_user.id,config.your_address,reply_markup=markup)
                else:
                    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                    back_home=types.KeyboardButton(config.back_home)
                    markup.row(back_home)
                    bot.send_message(message.from_user.id,config_taj.your_address,reply_markup=markup)
        bot.register_next_step_handler(message,edit_address)

    # profile edit ADDRESS
    if message.text==config.edit_phone or message.text==config_taj.edit_phone:
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `on_time`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

        for row in rows:
            if row[1] == str(message.from_user.id):
                if row[4]=="config_ru":
                    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                    back_home=types.KeyboardButton(config.back_home)
                    markup.row(back_home)
                    bot.send_message(message.from_user.id,config.your_phone,reply_markup=markup)
                else:
                    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                    back_home=types.KeyboardButton(config.back_home)
                    markup.row(back_home)
                    bot.send_message(message.from_user.id,config_taj.your_phone,reply_markup=markup)
        bot.register_next_step_handler(message,edit_phone)

    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `on_time`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

        #pipeline 1
    for row in rows:
        if row[1] == str(message.from_user.id) and row[3]==13:
            if message.text==config.back_home or message.text==config_taj.back_home:
                bot.send_message(message.from_user.id, reply_markup=profile_button(message))

    # CART CALLS
    if message.text==config.cart or message.text==config_taj.cart:
        bot.send_message(message.from_user.id,reply_markup=into_shopping_cart(message))
    # menu scene calls 
    if message.text==config.to_menu or message.text==config_taj.to_menu:
        bot.send_message(message.from_user.id,reply_markup=category_prod(message))
    # pipeline 0 _________________________________________________________________________________________________________

    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `on_time`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

        #pipeline 1
    for row in rows:
        if row[1] == str(message.from_user.id) and row[3]==0:
            if message.text==config.start_order or message.text==config_taj.start_order:
                bot.send_message(message.from_user.id,reply_markup=category_prod(message))
            if message.text==config.language or message.text==config_taj.language:
                bot.send_message(message.from_user.id,reply_markup=language(message))

            if message.text==config.comments or message.text==config_taj.comments:
                with connection.cursor() as cursor:
                    select_all_rows = "SELECT * FROM `on_time`"
                    cursor.execute(select_all_rows)
                    rows = cursor.fetchall()

                for row in rows:
                    if row[1] == str(message.from_user.id):
                        if row[4]=="config_ru":
                            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                            back=types.KeyboardButton(config.back_home)
                            markup.row(back)
                            bot.send_message(message.from_user.id, config.comment_text,reply_markup=markup)
                            bot.register_next_step_handler(message,leave_comments)
                        else:
                            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                            back=types.KeyboardButton(config_taj.back_home)
                            markup.row(back)
                            bot.send_message(message.from_user.id, config_taj.comment_text,reply_markup=markup)
                            bot.register_next_step_handler(message,leave_comments)
    # pipeline 1 _________________________________________________________________________________________________________
    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `on_time`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

        #pipeline 1
    for row in rows:
        if row[1] == str(message.from_user.id) and row[3]==1:
            if message.text==config.tort or message.text==config.desert or message.text==config.hot_soda or message.text==config.cold_soda or message.text==config_taj.tort or message.text==config_taj.desert or message.text==config_taj.hot_soda or message.text==config_taj.cold_soda:
                bot.send_message(message.chat.id,reply_markup=into_menu(message))
            if message.text==config.back_home or message.text==config_taj.back_home:
                bot.send_message(message.chat.id,reply_markup=send_welcome(message))

    #pipeline 2 __________________________________________________________________________________________________________
    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `on_time`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

        #pipeline 1
    for row in rows:
        if row[1] == str(message.from_user.id) and row[3]==2:
            if message.text==config.tort or message.text==config.desert or message.text==config.hot_soda or message.text==config.cold_soda or message.text==config_taj.tort or message.text==config_taj.desert or message.text==config_taj.hot_soda or message.text==config_taj.cold_soda:
                bot.send_message(message.chat.id,reply_markup=into_menu(message))

            if message.text==config.back_home or message.text==config_taj.back_home:
                bot.send_message(message.chat.id,reply_markup=category_prod(message))

            with connection.cursor() as cursor:
                select_all_rows_c = "SELECT * FROM `products`"
                cursor.execute(select_all_rows_c)
                rows_c = cursor.fetchall()

            for row_c in rows_c:
                if message.text == row_c[2]:
                    bot.send_message(message.from_user.id, reply_markup=into_product(message))
                    break

    # pipeline 11 _________________________________________________________________________________________________________
    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `on_time`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

        #pipeline 1
    for row in rows:
        if row[1] == str(message.from_user.id) and row[3]==0:
            if message.text==config.back_home or message.text==config_taj.back_home:
                bot.send_message(message.from_user.id,reply_markup=into_shopping_cart(message))

    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `products`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

        for row in rows:
            if message.text == f"1 шт. - {row[3]} сомони" or message.text==f"1 дона - {row[3]} сомон":
                # update table on_time PRODUCT
                bot.send_message(message.from_user.id, reply_markup=into_amount_product(message))

    # pipeline 6 _________________________________________________________________________________________________________
    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `on_time`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

        #pipeline 1
    for row in rows:
        if row[1] == str(message.from_user.id) and row[3]==6:
            if message.text==config.back_home or message.text==config_taj.back_home:
                bot.send_message(message.chat.id,reply_markup=into_shopping_cart(message))

            if message.text==config.oplata_zakaz or message.text==config_taj.oplata_zakaz:
                bot.send_message(message.from_user.id,reply_markup=oplata_zakaza(message))

    # pipeline 7 _________________________________________________________________________________________________________
    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `on_time`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

        #pipeline 1
    for row in rows:
        if row[1] == str(message.from_user.id) and row[3]==7:
            if message.text==config.back_home or message.text==config_taj.back_home:
                bot.send_message(message.chat.id,reply_markup=oformit_zakaz(message))

    # pipeline 14 _________________________________________________________________________________________________________
    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `on_time`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()

        #pipeline 1
    for row in rows:
        if row[1] == str(message.from_user.id) and row[3]==14:
            if message.text==config.back_home or message.text==config_taj.back_home:
                bot.send_message(message.chat.id,reply_markup=edit_profiles(message))

    # button Nalichie
    if message.text==config.nalichie or message.text==config_taj.nalichie:
        bot.send_message(message.from_user.id,reply_markup=order(message))

    if message.text!=config.cart: #should add that it cannot be корзина 
        if message.text.isdigit():
            bot.send_message(message.from_user.id, reply_markup=add_to_shoping_cart(message)) 

    # Button Oformit zakaz
    if message.text==config.start_oformit_order or message.text==config_taj.start_oformit_order:
        bot.send_message(message.from_user.id,oformit_zakaz(message))

    # button profile button
    if message.text==config_taj.my_profile or message.text==config.my_profile:
        bot.send_message(message.from_user.id,reply_markup=profile_button(message))

    if message.text==config.edit_profile or message.text==config_taj.edit_profile:
        bot.send_message(message.from_user.id,reply_markup=edit_profiles(message))

    #my product button
    if message.text==config.my_order or message.text==config_taj.my_order:
        bot.send_message(message.from_user.id,reply_markup=my_products(message))

    if message.text==config.consultant or message.text==config_taj.consultant:
        bot.send_message(message.from_user.id,reply_markup=contacts(message))
    
    if message.text==config.rus_keyboard:
        update_post_description = """
        UPDATE
        on_time
        SET
        language = "{language}"
        WHERE
        user_id="{username}"
        """.format(language="config_ru",username=message.from_user.id)
        execute_query(connection,  update_post_description)
        connection.commit()
        bot.send_message(message.chat.id,reply_markup=send_welcome(message))

    if message.text==config.taj_keyboard:
        update_post_description = """
        UPDATE
        on_time
        SET
        language = "{language}"
        WHERE
        user_id="{username}"
        """.format(language="config_taj",username=message.from_user.id)
        execute_query(connection,  update_post_description)
        connection.commit()
        bot.send_message(message.chat.id,reply_markup=send_welcome(message))


bot.infinity_polling()

if __name__ == '__main__': # чтобы код выполнялся только при запуске в виде сценария, а не при импорте модуля
    try:
       bot.polling(none_stop=True) # запуск бота
    except Exception as e:
       print(e) # или import traceback; traceback.print_exc() для печати полной инфы
       
