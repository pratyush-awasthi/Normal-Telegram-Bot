from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi"):
        return "Hey! How's it going?"

    if user_message in ("fine, what about you", "fine, what about you?"):
        return "I am also good, just chugging up some Topics on wikipedia"

    if user_message in ("who are you?", "who are you", "kaun ho tum??", "who are you?????"):
        return "I am Lucir The Bot."

    if user_message in ("what's your age ?", "what's your age" "what is your age??", "what is your age???"):
        return "My Developers made me few days back & are still developing me"

    if user_message in ("do you have any friends", "do you have any friends??", "do you have any friends ??"):
        return "Yes ! my developers said that they are also going to develop my friends after completing my project"

    if user_message in ("can we be friends?", "can we be friends??", "can we be friends???",):
        return "Sure,I'm a friendly bot !"

    if user_message in ("can you play something for me", "can you play something?", "can you play something???", "can you play something for me?", "can you play"):
        return "I'm a bot not a musician,but still I'll try  Ding!Ding Dong Dong Ding Ding Dong dong Ding ding na la bla bla"

    if user_message in ("can you sing something for me", "can you sing something?", "can you sing something???", "can you sing something for me?", "can you sing", "can you sing?"):
        return "I'm a bot not a singer,but still I'll try Love me like you do lala love me like you do what are you waiting for ?? "

    if user_message in ("what's the meaning of your name", "what's the meaning of your name?"):
        return "Lucir means to show off in spanish because My developers love to show off, xD."

    if user_message in ("hi pratyush awasthi this side","hi madmax this side","hi mihir tandon this side","hi micro this side","hi harsh vardhan singh this side","hi evilcry this side"):
        return "Arre arre maai-baap...charan sparsh"

    if user_message in ("what's the time", "what's the time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "I'm unable to understand what you are writing mate??"
