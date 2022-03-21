from speedtest import Speedtest
from pyrogram import Client, filters

@Client.on_message(filters.command("speedtest"))
def speedtest(bot, update):
    speed = bot.send_message(
        chat_id=update.chat.id,
        text="Running Speed Test . . .", 
        reply_to_message_id=update.message_id
    ) 
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    string_speed = f'''
<b>Server</b>
<b>Name:</b> <code>{result['server']['name']}</code>
<b>Country:</b> <code>{result['server']['country']}, {result['server']['cc']}</code>
<b>Sponsor:</b> <code>{result['server']['sponsor']}</code>
<b>ISP:</b> <code>{result['client']['isp']}</code>

<b>SpeedTest Results</b>
<b>Upload:</b> <code>{speed_convert(result['upload'] / 8)}</code>
<b>Download:</b>  <code>{speed_convert(result['download'] / 8)}</code>
<b>Ping:</b> <code>{result['ping']} ms</code>
<b>ISP Rating:</b> <code>{result['client']['isprating']}</code>
'''
    bot.edit_message_text(
        chat_id=update.chat.id,
        message_id=speed.message_id,
        text=string_speed
    ) 

def speed_convert(size):
    """Hi human, you can't read bytes?"""
    power = 2 ** 10
    zero = 0
    units = {0: "", 1: "Kb/s", 2: "MB/s", 3: "Gb/s", 4: "Tb/s"}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"
