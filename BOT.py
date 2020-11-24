import time
import telepot
from telepot.loop import MessageLoop
from pprint import pprint
from random import randint
from termcolor import colored as clr

directory=PATH

def handle(msg):
    global group_id
    global directory

    content_type, chat_type, chat_id = telepot.glance(msg)

    if chat_type!="channel":                    #This bot does not work in groups or private chats
        if content_type=="text":
            if "bottino" in msg["text"].lower():
                bot.sendMessage(chat_id,"Questo Bot è configurato per lavorare nei canali attualmente, non nelle chat private o nei gruppi")
    
    else:
        if content_type=="text":                                        #TEXT FILE FUNCTION
            print(clr("Saving a message...","green"))
            name=msg["chat"]["title"]+"_"+str(msg["message_id"])+".txt"     #Save text
            file=open(directory+name,"w")
            file.write(msg["text"])
            file.close()

        elif content_type=="photo":                                     #photo function
            print(clr("Saving a photo...","green"))
            photo_name=msg["chat"]["title"]+"_"+str(msg["message_id"])+".jpg"
            bot.download_file(msg["photo"][0]["file_id"], directory+photo_name)
            try:                                                        #If there is a caption
                test=msg["caption"]
                print(clr("Saving caption...","green"))
                name="caption_"+str(msg["message_id"])+".txt"
                file=open(directory+name,"w")
                file.write(msg["caption"])
                file.close()
            except KeyError:                                            #If there is no caption
                pass

        elif content_type=="audio":                                     #Audio function
            print(clr("Saving an audio...","green"))
            audio_name=msg["audio"]["file_name"]
            bot.download_file(msg["audio"]["file_id"], directory+audio_name)
            try:
                test=msg["caption"]
                print(clr("Saving caption...","green"))
                name="caption_"+str(msg["message_id"])+".txt"
                file=open(directory+name,"w")
                file.write(msg["caption"])
                file.close()
            except KeyError:
                pass

        elif content_type=="video":                                      #Video function
            print(clr("Saving a video...","green"))
            video_name=msg["chat"]["title"]+"_"+str(msg["message_id"])+".mp4"
            bot.download_file(msg["video"]["file_id"], directory+video_name)
            try:
                test=msg["caption"]
                print(clr("Saving caption...","green"))
                name="caption_"+str(msg["message_id"])+".txt"
                file=open(directory+name,"w")
                file.write(msg["caption"])
                file.close()
            except KeyError:
                pass

        elif content_type=="document":                                      #Documents function
            print(clr("Saving a document...","green"))
            doc_name=msg["document"]["file_name"]
            bot.download_file(msg["document"]["file_id"], directory+doc_name)
            try:
                test=msg["caption"]
                print(clr("Saving caption...","green"))
                name="caption_"+str(msg["message_id"])+".txt"
                file=open(directory+name,"w")
                file.write(msg["caption"])
                file.close()
            except KeyError:
                pass

        else:                                                                   #Useless messages such as voice, sticker, video message....
            print(clr(content_type,"red"))

bot=telepot.Bot(TOKEN)       #Bot definition
bot_specs=bot.getMe()
bot_name=bot_specs["first_name"]
bot_id=bot_specs["id"]
print(clr(f"{bot_name} [{bot_id}] ONLINE","cyan"))
MessageLoop(bot, handle).run_as_thread()                                #Run main function

while 1:
    time.sleep(10)