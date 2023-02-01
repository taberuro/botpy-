import logging
import ssl

from aiohttp import web

import telebot

import os





# ТЗ
# 1. из MySQL получить токены телеграм-ботов
#
# 2. повесить для каждого webhook'и
#
# 3. отвечать по каждому токену эхо-сообщением
#
# 4. записывать эхо-сообщения в MySQL







# 1. из MySQL получить токены телеграм-ботов
from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Username: "),
        password=getpass("Password: "),
        database="name_your_db",
    ) as connection:
        print(connection)
except Error as e:
    print(e)




name_your_db = "SELECT * FROM token's LIMIT 100"   #название заполнять самостоятельно/лимиты устанавливать также в зависимости от необходимого
with connection.cursor() as cursor:
    cursor.execute(name_your_db)
    result = cursor.fetchall()
    for row in result:
        print(row)
# 2. повесить для каждого webhook'и

def TOKEN(a):
    TOKEN = a
    PORT = int(os.environ.get('PORT', '8443'))
    updater = Updater(TOKEN)
    # add handlers
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN,
                          webhook_url="https://<appname>.herokuapp.com/" + TOKEN)
    updater.idle()

for i in range(len(row)):
    TOKEN(row[i])
# записывать эхо-сообщения в MySQL

create_your_db_name_table_query = """
CREATE TABLE your_db_name(
)
"""

with connection.cursor() as cursor:
    cursor.execute(create_your_db_name_table_query)
    connection.commit()



# отвечать по каждому токену эхо-сообщением  (тк тз не до конца ясна, то предположу, что требуется метод с данного гита)
#ниже представлена часть кода взятая с гитхаб аккаунта и предназначенная для отправки echo сообщений

API_TOKEN = '<api_token>'

WEBHOOK_HOST = '<ip/host where the bot is running>'
WEBHOOK_PORT = 8443  # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_LISTEN = '0.0.0.0'  # In some VPS you may need to put here the IP addr

WEBHOOK_SSL_CERT = './webhook_cert.pem'  # Path to the ssl certificate
WEBHOOK_SSL_PRIV = './webhook_pkey.pem'  # Path to the ssl private key
WEBHOOK_URL_BASE = "https://{}:{}".format(WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(API_TOKEN)

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

bot = telebot.TeleBot(API_TOKEN)

app = web.Application()


# Process webhook calls
async def handle(request):
    if request.match_info.get('token') == bot.token:
        request_body_dict = await request.json()
        update = telebot.types.Update.de_json(request_body_dict)
        bot.process_new_updates([update])
        return web.Response()
    else:
        return web.Response(status=403)


app.router.add_post('/{token}/', handle)


# Handle all other messages
@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)
    insert_your_db_name_query = """
    INSERT INTO your_db_name 
    (your_echo_message)
    """


# Remove webhook, it fails sometimes the set if there is a previous webhook
bot.remove_webhook()

# Set webhook
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                certificate=open(WEBHOOK_SSL_CERT, 'r'))

# Build ssl context
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV)

# Start aiohttp server
web.run_app(
    app,
    host=WEBHOOK_LISTEN,
    port=WEBHOOK_PORT,
    ssl_context=context,
)




