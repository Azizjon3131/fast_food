import logging

import telegram
from telegram import Update, ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from tg.views import DbHelper,DbHelper2
db=DbHelper()
db2=DbHelper2()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)



def start(update,context):
    main_button=[
        ['🛒 Buyurtma qilish'],
        [
            '🛍 Buyurtmalarim',
            '👨‍👨‍👧‍👧 EVOS Oilasi'
        ],
        [
            '📝 Fikr bildirish',
            '⚙️Sozlamalar'
        ]
    ]

    user = update.message.from_user
    update.message.reply_html('Assalomu aleykum <b>{}!</b>'.format(user.first_name),
                              reply_markup=ReplyKeyboardMarkup(main_button, resize_keyboard=True,one_time_keyboard=True))

    return 1

def buyurtma(update, context):
    category=db.category_parent()
    buttons=renders(category,'category','child','txt')
    update.message.reply_html('https://ru.freepik.com/premium-vector/fast-food-illustration-set_10957341.htm',
    reply_markup=InlineKeyboardMarkup(buttons))

    return 2

def inline_menu(update,context):

    query=update.callback_query
    data=query.data
    print(data)
    data_split=data.split('_')

    if data_split[0]=='category':
        if data_split[1]=='child':
            data=db.category_child(int(data_split[2]))
            if data!=None:
                buttons=renders(data,'category','child','txt')
                x = [
                    InlineKeyboardButton('🔝 Продолжит заказ', callback_data=f'category_menu_txt_txt'),
                    InlineKeyboardButton('⬅️Ortga', callback_data=f'category_ort_txt_txt')
                ]
                buttons.append(x)
                query.message.edit_text("Qanday turini tanlaysiz", reply_markup=InlineKeyboardMarkup(buttons))

            else:
                category=db.category(int(data_split[2]))

                data=db.product_type(int(data_split[2]))
                buttons = renders(data,'product',data_split[2],'txt')
                x = [
                    InlineKeyboardButton('🔝 Продолжит заказ', callback_data=f'category_menu_txt_txt'),
                    InlineKeyboardButton('⬅️Ortga', callback_data=f'category_child_{category[0]["parent"]}_txt')
                ]
                buttons.append(x)
                if data_split[3]=='photo':
                    query.message.delete()
                    query.message.reply_text("Qanday turini tanlaysiz", reply_markup=InlineKeyboardMarkup(buttons))
                else:
                    query.message.edit_text("Qanday turini tanlaysiz", reply_markup=InlineKeyboardMarkup(buttons))

        if data_split[1] == 'ort':
            query.message.delete()
            buyurtma(query,context)
        if data_split[1]=='menu':
            query.message.delete()
            buyurtma(query,context)

    if data_split[0]=='product':
        data = db.product(int(data_split[1]), int(data_split[2]))
        info_product = f"""Narxi: <b>{data['price']}</b> so'm\n
        Tarkibi: {data['description']}\n Sonini tanlang 👇"""
        # photo=db.product_image(data['id'])
        buttons = render_number(data['id'])
        z=[
            InlineKeyboardButton('🔝 Продолжит заказ', callback_data=f'category_menu_txt_txt'),
            InlineKeyboardButton('⬅️Ortga', callback_data=f'category_child_{data["category"]}_photo')
        ]
        buttons.append(z)
        user_id = query.from_user.id
        query.message.delete()
        context.bot.send_photo(user_id, photo=open('images/107738891_264431_MggYZfG.jpg', 'rb'),
              caption=info_product, parse_mode='HTML',reply_markup=InlineKeyboardMarkup(buttons))

    if data_split[0]=='product2':
        user_id = query.from_user.id
        data=db2.read_product(int(user_id))
        bt = ['1️⃣', '2️⃣', '3️⃣', '4️', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣']

        product = db.product2(int(data_split[1]))
        category = db.category(product[0]['category'])

        data_product = db.product_type(int(product[0]['category']))
        buttons = renders(data_product, 'product', int(product[0]["category"]), 'txt')
        a = [
            InlineKeyboardButton('🔝 Продолжит заказ', callback_data=f'category_menu_txt_txt'),
            InlineKeyboardButton('⬅️Ortga', callback_data=f'category_child_{category[0]["parent"]}_txt')
        ]
        b = [
            InlineKeyboardButton('🛒 Savatcha', callback_data=f'savat_txt_txt_{int(data_split[2])}_{product[0]["id"]}_txt'),
        ]
        buttons.append(a)
        buttons.append(b)

        x = ''
        if data==[]:

            for i in range(1, len(bt) + 2):
                if i == int(data_split[2]):
                    x = bt[i-1]
            st=''

            sena=int(data_split[2])*int(product[0]['price'])
            jami=sena+int(9000)
            st+=f"""
            Savatchada:\n\n {x} ✖️{product[0]['name']}\nMahsulot: {sena} so'm\nYetkazib berish: 9000 so'm\nJami: {jami} so'm"""

            query.message.delete()
            query.message.reply_text(st, reply_markup=InlineKeyboardMarkup(buttons))

        else:
            s=0
            dt=''
            for i in data:
                for j in range(1, len(bt) + 2):
                    if j == i[2]:
                        s+=i[1]*i[2]
                        dt+=f"""{bt[j-1]} ✖ {i[3]} """+'\n'

            if data_split[3]!='save':
                xt=''
                for j in range(1, len(bt) + 2):
                    if j == int(data_split[2]):
                        xt = bt[j-1]

                dt+=f"{xt} ✖️{product[0]['name']}"
                s+=int(data_split[2])*int(product[0]['price'])

            ss=s+int(9000)
            st=f"""Savatchada:\n \n {dt}\n Mahsulotlar: {s} so'm \n Yetkazib berish: 9000\n Jami:{ss} so'm"""

            query.message.delete()
            query.message.reply_text(st, reply_markup=InlineKeyboardMarkup(buttons))


    if data_split[0]=='savat':
        buttons=[]
        button=[]
        user_id = query.from_user.id
        product = db.product2(int(data_split[4]))
        if data_split[1]=='txt':
            if data_split[2]=='txt':
                db2.insert_data(int(product[0]['price']),int(data_split[3]),product[0]['name'],int(user_id))
                data=db2.read_product(int(user_id))
                if data!=[]:
                    bt = ['1️⃣', '2️⃣', '3️⃣', '4️', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣']
                    s = 0
                    dt = ''
                    ss=0
                    for i in data:
                        for j in range(1, len(bt) + 2):
                            if j == i[2]:
                                s += i[1] * i[2]
                                dt += f"""{bt[j-1]} ✖ {i[3]} """ + '\n'
                    ss=s+int(9000)
                    st = f"""Savatchada:\n \n {dt}\n Mahsulotlar: {s} so'm \n Yetkazib berish: 9000\n Jami:{ss} so'm"""

                    but=[
                        InlineKeyboardButton('⬅️Ortga', callback_data=f'product2_{product[0]["product_type"]}_{int(data_split[4])}_save'),
                        InlineKeyboardButton('🚖 ️Buyurtma berish', callback_data=f'buyurtma_data'),
                    ]
                    butt=[
                        InlineKeyboardButton("🗑 Savatchani bo'shatish", callback_data=f'savat_improvement'),
                    ]
                    buttons.append(but)
                    buttons.append(butt)
                    for i in data:
                        button.append(InlineKeyboardButton(f" ❌ {i[3]}", callback_data=f"savat_txt_delete_{int(i[2])}_{product[0]['id']}_{i[0]}"))
                        if len(button)==2:
                            buttons.append(button)
                            button=[]
                    if len(button)>0:
                        buttons.append(button)
                        button=[]

                    query.message.edit_text(st, reply_markup=InlineKeyboardMarkup(buttons))

                else:
                    query.message.delete()
                    start(query,context)

            if data_split[2]=='delete':
                db2.remove_product(int(data_split[5]))
                #db2.insert_data(int(product[0]['price']), int(data_split[3]), product[0]['name'], int(user_id))
                data = db2.read_product(int(user_id))
                if data != []:
                    bt = ['1️⃣', '2️⃣', '3️⃣', '4️', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣']
                    s = 0
                    dt = ''
                    ss = 0
                    for i in data:
                        for j in range(1, len(bt) + 2):
                            if j == i[2]:
                                x = bt[j - 1]
                                s += i[1] * i[2]
                                dt += f"""{x} ✖ {i[3]} """ + '\n'
                    ss = s + int(9000)
                    st = f"""Savatchada:\n \n {dt}\n Mahsulotlar: {s} so'm \n Yetkazib berish: 9000\n Jami:{ss} so'm"""

                    but = [
                        InlineKeyboardButton('⬅️Ortga', callback_data=f'product2_{product[0]["product_type"]}_{int(data_split[3])}_txt'),
                        InlineKeyboardButton('🚖 ️Buyurtma berish', callback_data=f'buyurtma_data'),
                    ]
                    butt = [
                        InlineKeyboardButton("🗑 Savatchani bo'shatish", callback_data=f'improvement_data'),
                    ]
                    buttons.append(but)
                    buttons.append(butt)
                    for i in data:
                        button.append(InlineKeyboardButton(f" ❌ {i[3]}", callback_data=f"savat_txt_delete_{int(i[2])}_{product[0]['id']}_{i[0]}"))
                        if len(button) == 2:
                            buttons.append(button)
                            button = []
                    if len(button) > 0:
                        buttons.append(button)
                        button = []

                    query.message.edit_text(st, reply_markup=InlineKeyboardMarkup(buttons))

                else:
                    query.message.delete()
                    start(query, context)


    if data_split[1]=='improvement':
        user_id = query.from_user.id
        db2.remove(int(user_id))
        query.message.delete()
        start(query,context)

    if data_split[0]=='buyurtma':

        button=[
            [telegram.KeyboardButton(text="📍 Geo locatsiya yuborish", request_location=True)],
            [telegram.KeyboardButton(text="📞 Telefon nomer", request_contact=True)],
            ["⬅️Ortga"]
        ]
        query.message.delete()
        query.message.reply_text("Eltib berish uchun geo-joylashuvni jo'nating yoki manzilni tanlang",
        reply_markup=ReplyKeyboardMarkup(button,resize_keyboard=True,one_time_keyboard=True))

        return 3

def qabul(update,context):
    update.message.reply_html('OK keldim')

    # bot=telegram.Bot('1676259797:AAEXXQUC-j2Gt05KOaF5m5IBBhppBqeZA3s')
    # if bot.get_updates():
    #     chat_id=bot.get_updates()[-1].message.chat_id
    #     location_keyboard=telegram.KeyboardButton(text="send_location", request_location=True)
    #     contact_keyboard=telegram.KeyboardButton(text="send_contact", request_contact=True)
    #     custom_keyboard=[[location_keyboard, contact_keyboard]]
    #     reply_murkup=telegram.ReplyKeyboardMarkup(custom_keyboard)

    #     bot.send_message(chat_id=chat_id, text="YUboring", reply_murkup=reply_murkup)
    #
    # else:
    #     print("Xatolik")


def buyurtmalarim(update,context):
    update.message.reply_html('buyurtmaga keldim')

def oila(update, context):
    update.message.reply_html('oilaga keldim')

def fikr(update, context):
    update.message.reply_html('fikrga keldim')

def sozlama(update, context):
    update.message.reply_html('fikrga keldim')

def cancel(update,context):
    update.message.reply_html('cancelga keldim')


def help_command(update: Update, _: CallbackContext) -> None:

    update.message.reply_text('Help!')


def echo(update: Update, _: CallbackContext) -> None:

    update.message.reply_text(update.message.text)

def renders(request,name1,name, id):
    button=[]
    buttons=[]
    for data in request:
        button.append(InlineKeyboardButton(data['name'], callback_data=f"{name1}_{name}_{data['id']}_{id}"))
        if len(button)==2:
            buttons.append(button)
            button=[]
    if len(button)>0:
        buttons.append(button)
        button=[]

    return buttons

def render_number(id):
    button=[]
    buttons=[]
    for i in range(1,10):
        button.append(InlineKeyboardButton(str(i), callback_data=f"product2_{id}_{i}_txt"))
        if len(button)==3:
            buttons.append(button)
            button=[]

    return buttons
