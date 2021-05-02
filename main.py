import Constants as keys
from telegram.ext import *
import Responses as R
from random import randint

print("Bot started.....")


def start_command(update, context):
    update.message.reply_text('Hi, try typing /help for some commands...')

def help_command(update, context):
    update.message.reply_text('/info -- Gives brief info about the Bot.\n/joke -- For some quick Joke. \n/quote -- Wanna read some Quotes??\n/wallpapermobile -- Get links to some cool HD wallpapers for mobile.\n/wallpaperpc -- Get links to some cool HD wallpapers for PC.\n/version -- Version of the Bot.\n/fun -- Just for Fun. ')

def info_command(update, context):
    update.message.reply_text('Hi!! This is Lucir The Bot Made by Pratyush Awasthi aka M@dm@x, Mihir Tandon aka M!cro, Harsh Vardhan Singh aka Ev!lCry. Also I am developed using Python')

def joke_command(update, context):
    jokes = ['Did you hear about the actor who fell through the floorboards? He was just going through a stage.','Two guys stole a calendar. They got six months each. ','Could a ... ... librarian be called a bookkeeper? ... referee be a game warden? ... dairyman be a cowboy? ... cabinetmaker be the president?','I make mistakes; I’ll be the second to admit it.','Since the coronavirus outbreak, my 47-year-old son has been washing his hands religiously. In fact, he said, “I’ve been washing my hands so much, I found the answers to an old eighth-grade math quiz.','If it was a blustery day, you could be sure to hear my dad remark, “It was so windy today, I had to wrinkle my forehead and screw my cap on to keep it there!','An utterly confused woman called our local fire station about getting a haircut. “I’m sorry, you have the wrong number,” I said. “Is this the salon near the fire station?” she asked. “No, this is the fire station.” “Oh! Are you cutting hair in there now?','After a health scare, I hugged my wife and whispered, “If something happens to me, the presents in my closet are yours.” She whispered back, “If anything happens to you, everything in your closet is mine','On the way to meet my husband at a restaurant, I realized that I didn’t have my phone and immediately panicked. I needn’t have worried. He saw my phone on the couch at home and brought it with him. When he arrived, I checked my texts. There was only one, and it was from him: “I’m on my way, and I have your phone','Concerned that he might have put on a few pounds, my husband exited the bathroom and asked, “Do you think my chin is getting fat?” I smiled lovingly and replied, “Which one?','Our company gives out Thanksgiving turkeys to retired employees. All they have to do is stop by the plant to pick them up. A few days before the holiday, a retiree called to ask, “What time do the turkeys get in?” The receptionist, without thinking, responded, “Everyone starts at eight.']
    update.message.reply_text(jokes[randint(0,10)])

def quote_command(update, context):
    quotes = ['Do not go where the path may lead, go instead where there is no path and leave a trail. -By Ralph Waldo Emerson','The future belongs to those who believe in the beauty of their dreams. -By Eleanor Roosevelt','Always remember that you are absolutely unique. Just like everyone else. -By Margaret Mead','When you reach the end of your rope, tie a knot in it and hang on. -By Franklin D. Roosevelt','Tell me and I forget. Teach me and I remember. Involve me and I learn -By Benjamin Franklin','If life were predictable it would cease to be life, and be without flavor -By Eleanor Roosevelt','You will face many defeats in life, but never let yourself be defeated.','Mankind must put an end to war before war puts an end to mankind. -By John F. Kennedy','Life is never easy. There is work to be done and obligations to be met—obligations to truth, to justice, and to liberty. -By John F. Kennedy','Ask not what your country can do for you, but what you can do for your country. -By John f. Kennedy']
    update.message.reply_text(quotes[randint(0,10)])

def wallpaperm_command(update, context):
    wallpapers = ['https://drive.google.com/file/d/1Y2zpGG_I7sG1lWvUkuN3ttchrv0FGHX9/view?usp=drivesdk','https://drive.google.com/file/d/1YFzOkb_pclmtH3xe1AV0NYucLV78YmAL/view?usp=drivesdk','https://drive.google.com/file/d/1YKdaUWbOwrZHRjKch_MggCVVv18eFt2M/view?usp=drivesdk','https://drive.google.com/file/d/1Y-ghds2R2WIGzMA8y7DTQOewdPzgDcCN/view?usp=drivesdk','https://drive.google.com/file/d/1XzrfCBEoIprEsiRcBYJParlwdU4-zvXp/view?usp=drivesdk','https://drive.google.com/file/d/1XxFdFt2Eix44lHEbqUU9TQFIDlDXVPqg/view?usp=drivesdk','https://drive.google.com/file/d/1XtIOP1D94CHa95GHXro5lUFNUdgNsz9q/view?usp=drivesdk','https://drive.google.com/file/d/1XaDxHg3bDfTDusAuElDoErPNrqGExQnc/view?usp=drivesdk','https://drive.google.com/file/d/1XlcuzeE6UBUgxoDSJxWLX7X3RRG3BMBf/view?usp=drivesdk','https://drive.google.com/file/d/1XiILdObXy8UJIfJETy8wgrrD3xl7guSZ/view?usp=drivesdk']
    update.message.reply_text(wallpapers[randint(0,10)])

def wallpaperpc_command(update, context):
    wallpapersp = ['https://drive.google.com/file/d/1_faF0rRUA4-07onopD6wGhBwYrOlf6LW/view?usp=sharing','https://drive.google.com/file/d/1vmHwPHZvo6hHmlL2o7gymA0op9wI3aZ0/view?usp=sharing','https://drive.google.com/file/d/1kBwvK-sMhVaPiuGHt8_A0-pHj_4_TvT_/view?usp=sharing','https://drive.google.com/file/d/1vuTwCufWzaTDoF4ggD6BQL-V_nzW7kY9/view?usp=sharing','https://drive.google.com/file/d/1XKKjhM7cjRAS81J8zvp8yrQ88c2wQE3D/view?usp=sharing','https://drive.google.com/file/d/1GARd5mqGR6S59gcshGcbAprRy4lfJdn6/view?usp=sharing','https://drive.google.com/file/d/11GE1p7QHd9VWkkiCqhnE2J8R_5-vf7ZS/view?usp=sharing','https://drive.google.com/file/d/1DFIMiqFMKGKGjNTXjZsWgUNbVqdt9kss/view?usp=sharing','https://drive.google.com/file/d/1K8asXHAfAQvMvwYkYloHDnCs7brrGxum/view?usp=sharing','https://drive.google.com/file/d/1KnC4w0XFwe1Mbxmzyz_yMQ0yTs_nr8vK/view?usp=sharing']
    update.message.reply_text(wallpapersp[randint(0,10)])

def version_command(update, context):
    update.message.reply_text('Version - 1.3.0')


def fun_command(update, context):
    update.message.reply_text(
       '''░░░░░░░░░▄▄▄░░▄██▄░░░ 
         ░░░░░▐▀█▀▌░░░░▀█▄░░░ 
         ░░░░░▐█▄█▌░░░░░░▀█▄░░ 
         ░░░░░░▀▄▀░░░▄▄▄▄▄▀▀░░ 
         ░░░░▄▄▄██▀▀▀▀░░░░░░░ 
         ░░░█▀▄▄▄█░▀▀░░ 
         ░░░▌░▄▄▄▐▌▀▀▀░░ 
         ▄░▐░░░▄▄░█░▀▀ ░░ 
         ▀█▌░░░▄░▀█▀░▀ ░░ 
         ░░░░░░░▄▄▐▌▄▄░░░ 
         ░░░░░░░▀███▀█░▄░░ 
         ░░░░░░▐▌▀▄▀▄▀▐▄░░  
         ░░░░░░▐▀░░░░░░▐▌░░ 
         ░░░░░░█░░░░░░░░█░░░░░░░
         ░░░░░░█░░░░░░░░█░░░░░░░
         ░░░░░░█░░░░░░░░█░░░░░░░
         ░░░░▄██▄░░░░░▄██▄░░░░░░░░░
         This is me...if I was real, xD.''')

def handle_message(update, context):
    text = str(update.message.text)
    response = R.sample_responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("info", info_command))
    dp.add_handler(CommandHandler("joke", joke_command))
    dp.add_handler(CommandHandler("quote", quote_command))
    dp.add_handler(CommandHandler("wallpapermobile", wallpaperm_command))
    dp.add_handler(CommandHandler("wallpaperpc", wallpaperpc_command))
    dp.add_handler(CommandHandler("version", version_command))
    dp.add_handler(CommandHandler("fun", fun_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling(1)
    updater.idle()


main()
