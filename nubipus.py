import telebot
import json
import http.client
import sys
import random

Token="1848358920:AAFRs2eh0G3xW01ywFDvVR4F9sVY-HtvBCI"
bot = telebot.TeleBot(Token)
random.seed()

@bot.message_handler(commands=['startt'])
def startt_message(message):
    bot.send_message(message.chat.id, "Список команд:\n/andreybulling\n/rusikbulling\n/danyabulling")
    if (message.text=="Рил"):
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEClTZg8Ff8chF9AAHB_5ny-48k20OkoKgAAkAOAAIywglK38fhvyayJ3ogBA")
    elif (message.text=="рил"):
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEClTZg8Ff8chF9AAHB_5ny-48k20OkoKgAAkAOAAIywglK38fhvyayJ3ogBA")

@bot.message_handler(commands=['andreybulling'])
def Andrey_Bulling(message):
    chatId=message.chat.id
    bot.send_message(message.chat.id, "@bokunoandi , соси кок")
    bot.send_audio(message.chat.id, open("Соси.ogg", "rb"))
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEC2H1hMeilIE0dQwoMTFpLnyeY0UB2FgACHwEAAjFnwjWRtaMdS7iIaCAE")
    
@bot.message_handler(commands=['rusikbulling'])
def Rusik_Bulling(message):
    bot.send_message(message.chat.id, "Русик, сука, иди нахуй")
    rand=random.randint(1,9)
    if (rand==1):
        bot.send_audio(message.chat.id, open("Русик1.ogg", "rb"))
    elif(rand==2):
        bot.send_audio(message.chat.id, open("Русик2.ogg", "rb"))
    elif(rand==3):
        bot.send_audio(message.chat.id, open("Русик3.ogg", "rb"))
    elif(rand==4):
        bot.send_audio(message.chat.id, open("Русик4.ogg", "rb"))
    elif(rand==5):
        bot.send_audio(message.chat.id, open("Русик5.ogg", "rb"))
    elif(rand==6):
        bot.send_audio(message.chat.id, open("Русик6.ogg", "rb"))
    elif(rand==7):
        bot.send_audio(message.chat.id, open("Русик7.ogg", "rb"))
    elif(rand==8):
        bot.send_audio(message.chat.id, open("Русик8.ogg", "rb"))
    elif(rand==9):
        bot.send_audio(message.chat.id, open("Русик9(0).ogg", "rb"))
        bot.send_audio(message.chat.id, open("Русик9.ogg", "rb"))
    print(rand)

@bot.message_handler(commands=['joebulling'])
def Joe_Bidon(message):
    bot.send_message(message.chat.id, "Джо Байден")

@bot.message_handler(commands=['karmanbulling'])
def Karman_Bulling(message):
    bot.send_message(message.chat.id, "Поносус")
    bot.send_audio(message.chat.id, open("Гамбаре.ogg", "rb"))
    
@bot.message_handler(commands=['danyabulling'])
def repeat_all_messages(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEClTZg8Ff8chF9AAHB_5ny-48k20OkoKgAAkAOAAIywglK38fhvyayJ3ogBA")

@bot.message_handler(commands=['all'])
def ALL(message):
    bot.send_message(message.chat.id, "Перекличка! @Zargo_0 , @Sunnypiase , @tolya_harbych, @u1ser0001234, @Archimareto @Машъка, @kap234, @ded_vnutr1, @pycikkk, @dderksenn, @Sakura77777777, @portubas, @bokunoandi, @Сладкий, @vladi_sap, @nnnassstiia")

 
if name == 'main':
     bot.infinity_polling()