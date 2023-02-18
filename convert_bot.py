# this bot wroted on python with requests + aiogram
# the bot was written by order from the kwork website

#tikers
#"BTC",22964,'walletBTC',"ETH",1639,'walletETH','USDT',1,'walletUSDT','BNB',328.72,'walletBNB','USDC',1,'walletUSDC','XRP',0.35,'walletXRP','BUSD',1,'walletBUSD','ADA',0.38,'walletADA','DOGE',0.09,'walletDOGE',"MATIC",1.2,'walletMATIC','SOL',23.25,'walletSOL','DOT',6.7,'walletDOT','SHIB',0.000015,'walletSHIB','LTC',99.27,'walletLTC','AVAX',20.11,'walletAVAX','TRX',0.065,'walletTRX',"DAI",1,'walletDAT',"UNI",6.82,'walletUNI','ATOM',14.6,'walletATOM',"WBTC",22945,'walletWBTC'
#"BTC","ETH",'USDT','BNB','USDC','XRP','BUSD','ADA','DOGE',"MATIC",'SOL','DOT','SHIB','LTC','AVAX','TRX',"DAI","UNI",'ATOM',"WBTC"
# BTC,ETH,USDT,BNB,USDC,XRP,BUSD,ADA,DOGE,MATIC,SOL,DOT,SHIB,LTC,AVAX,TRX,DAT,UNI,ATOM,WBTC

#import block
import requests
import logging
from aiogram import Bot, Dispatcher, executor, types, utils
import random

#TG bot token
API_TOKEN = '6128189534:AAE1fO9R9ie66MVy3p7atoQS3hyFgj0zZxY'
BOT_TOKEN = "your_bot_token"
CHAT_ID = "chat_id_of_the_recipient_bot"
MESSAGE = "Your message"

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print(f"Failed to send message. Response: {response.content}")

#block of cheking string 
def is_digit(string):
    if string.isdigit():
       return 1
    else:
        try:
            float(string)
            return 1
        except ValueError:
            return 0

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

# State machine for the conversation
class ConversationState:
    TICKER_1, TICKER_2, VALUE, post_message = range(4)

# State variable to keep track of the current step
conversation_state = ConversationState.TICKER_1

# Variables to store the user inputs
ticker_1 = None
ticker_2 = None
value = None

# /start command block
@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    global conversation_state, ticker_1, ticker_2, value

    await message.answer("I am a bot created to facilitate transactions in cryptocurrency for you\n"
                        "Now we exchange : BTC,ETH,USDT,BNB,USDC,XRP,BUSD,ADA,DOGE,MATIC,SOL,DOT,SHIB,LTC,AVAX,TRX,DAT,UNI,ATOM,WBTC\n"
                        "Enter the first ticker (format BNB):")

    # Reset the state of the conversation and the stored inputs
    conversation_state = ConversationState.TICKER_1
    ticker_1 = None
    ticker_2 = None
    value = None

# message's block
@dp.message_handler()
async def handle_input(message: types.Message):
    global conversation_state, ticker_1, ticker_2, value

    # first message ( 1st tiker)
    if conversation_state == ConversationState.TICKER_1:
        TIKERS1 = ["BTC","ETH",'USDT','BNB','USDC','XRP','BUSD','ADA','DOGE',"MATIC",'SOL','DOT','SHIB','LTC','AVAX','TRX',"DAI","UNI",'ATOM',"WBTC"]
        check1 = 0
    
        for i in range(0,len(TIKERS1)):

            if TIKERS1[i] == message.text:
                ticker_1 = message.text  # в этой переменной получается первый тикер
                check1 +=1
                await message.answer("Enter the second ticker (example format: BNB):")
                conversation_state = ConversationState.TICKER_2
                
        if check1 == 0:
            await message.answer("Enccorrect tiker 1, start again with the /start command")

    # second message ( 2nd tiker)
    elif conversation_state == ConversationState.TICKER_2:
        TIKERS2 = ["BTC","ETH",'USDT','BNB','USDC','XRP','BUSD','ADA','DOGE',"MATIC",'SOL','DOT','SHIB','LTC','AVAX','TRX',"DAI","UNI",'ATOM',"WBTC"]
        check2 = 0

        for i in range(0,len(TIKERS2)):

            if TIKERS2[i] == message.text:
                ticker_2 = message.text  # в этой переменной получается второй тикер
                check2 +=1
                await message.answer("Enter the number of coins you want to exchange:")
                conversation_state = ConversationState.VALUE

        if check2 == 0:
            await message.answer("Enccorrect tiker 2, start again with the /start command")

    # fird message (value)
    elif conversation_state == ConversationState.VALUE:

        if is_digit(message.text) == 1:
            
            value = int(message.text)  # в этой переменной получается передаваемое количество монет

            # value -- кол-во монет : ticker_1 : ticker_2
            TIKERS = ["BTC",22964,'walletBTC',"ETH",1639,'walletETH','USDT',1,'walletUSDT','BNB',328.72,'walletBNB','USDC',1,'walletUSDC','XRP',0.35,'walletXRP','BUSD',1,'walletBUSD','ADA',0.38,'walletADA','DOGE',0.09,'walletDOGE',"MATIC",1.2,'walletMATIC','SOL',23.25,'walletSOL','DOT',6.7,'walletDOT','SHIB',0.000015,'walletSHIB','LTC',99.27,'walletLTC','AVAX',20.11,'walletAVAX','TRX',0.065,'walletTRX',"DAI",1,'walletDAT',"UNI",6.82,'walletUNI','ATOM',14.6,'walletATOM',"WBTC",22945,'walletWBTC']

            us_wall = ''
            tik1 = 0
            for i in range(0,len(TIKERS)):
                if TIKERS[i] == ticker_1:
                    tik1 += TIKERS[i+1]
                    us_wall = TIKERS[i+2]

            tik2 = 0
            for j in range(0,len(TIKERS)):
                if TIKERS[j] == ticker_2:
                    tik2 += TIKERS[j+1]

            result = (value * tik1)/tik2 # конкретно здесь переменная будет передавать то, сколько получит человек

            await message.answer(f"if you send the specified amount to our wallet, you will receive {result} \n"
            "wallet to send : " + us_wall +" .\n"
            "as soon as you send it, write to us in the chat 'ok' or 'i send' and we will start checking your transaction and create an application \n")

            # Reset the state of the conversation
            conversation_state = ConversationState.post_message

        if is_digit(message.text) == 0:
            await message.answer("encorrect value, start again with the /start command")

    elif conversation_state == ConversationState.post_message:

        await message.answer(f"your application has been created, its number : {random.randint(10000000, 100000000-1)}\n"
        "as soon as we confirm your transaction, we will send you your tokens \n"
        "if you still have questions, write to our support @supportswapcash")
        # Reset the state of the conversation
        conversation_state = ConversationState.TICKER_1

# start programm
if __name__ == '__main__':  
    executor.start_polling(dp, skip_updates=True)
