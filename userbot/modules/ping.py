# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# ReCode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import time
from datetime import datetime
from secrets import choice

from speedtest import Speedtest

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, StartTime
from userbot.events import register
from userbot.utils import edit_or_reply, humanbytes, man_cmd

absen = [
    "**Hadir bang** ð",
    "**Hadir kak** ð",
    "**Hadir dong** ð",
    "**Hadir ganteng** ð¥µ",
    "**Hadir bro** ð",
    "**Hadir kak maap telat** ð¥º",
]


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@man_cmd(pattern="ping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await edit_or_reply(ping, "**â£**")
    await xx.edit("**â£â£**")
    await xx.edit("**â£â£â£**")
    await xx.edit("**â£â£â£â£**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await xx.edit(
        f"**PONG!!ð**\n"
        f"â£ **Pinger** - `%sms`\n"
        f"â£ **Uptime -** `{uptime}` \n"
        f"**â¦ÒÍ¡ÍOwner :** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )


@man_cmd(pattern="xping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xping = await edit_or_reply(ping, "`Pinging....`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xping.edit(
        f"**PONG!! ð­**\n**Pinger** : %sms\n**Bot Uptime** : {uptime}ð" % (duration)
    )


@man_cmd(pattern="lping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    lping = await edit_or_reply(ping, "**â PING â**")
    await lping.edit("**ââ PING ââ**")
    await lping.edit("**âââ PING âââ**")
    await lping.edit("**ââââ PING ââââ**")
    await lping.edit("**â¦ÒÍ¡Íâ³ PONG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await lping.edit(
        f"â **Ping !!** "
        f"`%sms` \n"
        f"â **Uptime -** "
        f"`{uptime}` \n"
        f"**â¦ÒÍ¡Íâ³ Master :** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )


@man_cmd(pattern="keping$")
async def _(pong):
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    kopong = await edit_or_reply(pong, "**ãâððððððã**")
    await kopong.edit("**ââðððððððââ**")
    await kopong.edit("**ðððððððð ðððð ððð ððð**")
    await kopong.edit("**â¬ðððð ððððððð ðððððððð ðððâ¬**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await pong.client.get_me()
    await kopong.edit(
        f"**â² ðºð¾ð½ðð¾ð» ð¼ð´ð»ð´ð³ðð¶** "
        f"\n â«¸ á´·áµâ¿áµáµË¡ `%sms` \n"
        f"**â² ð±ð¸ð¹ð¸ ð¿ð´ð»ð´ð** "
        f"\n â«¸ á´·áµáµáµáµâ¿áµã[{user.first_name}](tg://user?id={user.id})ã \n" % (duration)
    )


# .keping & kping Coded by Koala


@man_cmd(pattern=r"kping$")
async def _(pong):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    kping = await edit_or_reply(pong, "8â===D")
    await kping.edit("8=â==D")
    await kping.edit("8==â=D")
    await kping.edit("8===âD")
    await kping.edit("8==â=D")
    await kping.edit("8=â==D")
    await kping.edit("8â===D")
    await kping.edit("8=â==D")
    await kping.edit("8==â=D")
    await kping.edit("8===âD")
    await kping.edit("8==â=D")
    await kping.edit("8=â==D")
    await kping.edit("8â===D")
    await kping.edit("8=â==D")
    await kping.edit("8==â=D")
    await kping.edit("8===âD")
    await kping.edit("8===âDð¦")
    await kping.edit("8====Dð¦ð¦")
    await kping.edit("**CROOTTTT PINGGGG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await kping.edit(
        f"**NGENTOT!! ð¨**\n**KAMPANG** : %sms\n**Bot Uptime** : {uptime}ð" % (duration)
    )


@man_cmd(pattern="speedtest$")
async def _(speed):
    xxnx = await edit_or_reply(speed, "`Running speed test...`")
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    msg = (
        f"**Started at {result['timestamp']}**\n\n"
        "**Client**\n"
        f"**ISP :** `{result['client']['isp']}`\n"
        f"**Country :** `{result['client']['country']}`\n\n"
        "**Server**\n"
        f"**Name :** `{result['server']['name']}`\n"
        f"**Country :** `{result['server']['country']}`\n"
        f"**Sponsor :** `{result['server']['sponsor']}`\n\n"
        f"**Ping :** `{result['ping']}`\n"
        f"**Upload :** `{humanbytes(result['upload'])}/s`\n"
        f"**Download :** `{humanbytes(result['download'])}/s`"
    )
    await xxnx.delete()
    await speed.client.send_file(
        speed.chat_id,
        result["share"],
        caption=msg,
        force_document=False,
    )


@man_cmd(pattern="pong$")
async def _(pong):
    start = datetime.now()
    xx = await edit_or_reply(pong, "`Sepong.....ð`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await xx.edit("ð **Ping!**\n`%sms`" % (duration))


# KALO NGEFORK absen ini GA USAH DI HAPUS YA GOBLOK ð¡
@register(pattern=r"^\.absen$", sudo=True)
async def risman(ganteng):
    await ganteng.reply(choice(absen))


# JANGAN DI HAPUS GOBLOK ð¡ LU COPY AJA TINGGAL TAMBAHIN
# DI HAPUS GUA GBAN YA ð¥´ GUA TANDAIN LU AKUN TELENYA ð¡


CMD_HELP.update(
    {
        "ping": f"**Plugin : **`ping`\
        \n\n  â¢  **Syntax :** `{cmd}ping` ; `{cmd}lping` ; `{cmd}xping` ; `{cmd}kping`\
        \n  â¢  **Function : **Untuk menunjukkan ping userbot.\
        \n\n  â¢  **Syntax :** `{cmd}pong`\
        \n  â¢  **Function : **Sama seperti perintah ping\
    "
    }
)


CMD_HELP.update(
    {
        "speedtest": f"**Plugin : **`speedtest`\
        \n\n  â¢  **Syntax :** `{cmd}speedtest`\
        \n  â¢  **Function : **Untuk Mengetes kecepatan server userbot.\
    "
    }
)
