#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    update_channel = "@StarMovies_Here"
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_photo("🤭 Sorry Dude, You are **B A N N E D 🤣🤣🤣**")
               return
        except UserNotParticipant:
            #await update.reply_photo(f"Join @{update_channel} To Use Me")
            await update.reply_photo(
                photo="https://telegra.ph/%F0%9D%90%92%F0%9D%90%93%F0%9D%90%80%F0%9D%90%91-%F0%9D%90%8C%F0%9D%90%95%F0%9D%90%88%F0%9D%90%84%F0%9D%90%92-07-25",
                caption="Join Our 𝐒𝐓𝐀𝐑 𝐌★𝐕𝐈𝐄𝐒 Channel 🤭     ചാനലിൽ നിങ്ങൾ ഉണ്ട് എങ്കിൽ മാത്രമേ ഈ ബോട്ട് വഴി നിങ്ങൾക്ക് സിനിമ കിട്ടുകയുളളൂ.അതുകൊണ്ട് ചാനെലിൽ ജോയിൻ ആവുക...😁😁",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=" ⭕️ 𝗖𝗹𝗶𝗰𝗸 𝘁𝗼𝗼 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 ⭕️ ", url=f"https://t.me/joinchat/qIe9vomtxKg0YzE1")]
              ])
            )
            return
        except Exception:
            await update.reply_photo("Something Wrong. Contact my Support Group")
            return    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption =("<code>" + file_name + """</code>\n꧁༺ --------------------------- ༻꧂
📂 𝗗𝗿𝗮𝘅 𝗔𝗿𝗰𝗵𝗶𝘃𝗲 - @DX_links

          <a href= 'https://t.me/joinchat/TV_lOjIzLBGmSMGi'>𝗗𝗿𝗮𝗫 𝗠𝗼𝘃𝗶𝗲𝘀</a>""")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = caption,
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '📸 𝗦 𝗖 𝗥 𝗘 𝗘 𝗡 𝗦 𝗛 𝗢 𝗧 𝗦', callback_data='help'
                                )],
                        [
                            InlineKeyboardButton
                                (
                                    '⭕️ 𝗝𝗼𝗶𝗻 𝗼𝘂𝗿 𝗰𝗵𝗮𝗻𝗻𝗲𝗹  ⭕️', url="https://t.me/joinchat/TV_lOjIzLBGmSMGi"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '📸 𝗦 𝗖 𝗥 𝗘 𝗘 𝗡 𝗦 𝗛 𝗢 𝗧 𝗦', callback_data='help'
                                )],
                        [   
                            InlineKeyboardButton
                                (
                                    '⭕️ 𝗝𝗼𝗶𝗻 𝗼𝘂𝗿 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 ⭕️', url="https://t.me/joinchat/TV_lOjIzLBGmSMGi"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '⭕️ 𝗝𝗼𝗶𝗻 𝗼𝘂𝗿 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 ⭕️', url="https://t.me/joinchat/89wsRw1KP-tjNDE1"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('♻️ 𝗚𝗿𝗼𝘂𝗽', url='https://t.me/joinchat/oV7uDCm1UEw2YmE1'),
        InlineKeyboardButton('🎞 𝗰𝗵𝗮𝗻𝗻𝗲𝗹', url ='https://t.me/joinchat/TV_lOjIzLBGmSMGi')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('🤖 𝗦𝗰𝗿𝗲𝗲𝗻𝗦𝗵𝗼𝘁 𝗕𝗼𝘁', url ='https://t.me/screenshotit_bot')],
              [
        InlineKeyboardButton('Help🔐', callback_data='about')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Tutorial Video⚡', url ='https://telegra.ph/Generate-ScreenShots-06-08')],
              [
        InlineKeyboardButton('◀️ Back ', callback_data='help')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
