import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["مودي","المبرمج علي","مبرمج السورس","مبرمج"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/96857cb597b588139fdd5.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[ علي احمد 𐇮](https://t.me/TFFF_F)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @TFFF_F ❫
◉ 𝙸𝙳      : ❪ `6377763320` ❫
◉ 𝙱𝙸𝙾    : ❪ for me (@TFFF_F) my world (@zlz1zl - @TFFF_F) my bro (@zlz1zl) ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𐇮 علي احمد 𐇮", url=f"https://t.me/TFFF_F"), 
                 ],[
                   InlineKeyboardButton(
                        "🔱 السورس علي احمد 🔱", url=f"https://t.me/@zlz1zl"),
                ],

            ]

        ),

    )
