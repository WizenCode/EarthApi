#!/usr/bin/python
# -*- coding: utf-8 -*-
#In the name of God
import os
import sys
import json
import random
import urllib
import urllib2
import telebot
import redis as r
import requests as req
from telebot import util
from telebot import types
from random import randint
from termcolor import colored
from urllib import urlretrieve as download
reload(sys)
sys.setdefaultencoding("utf-8")
redis = r.StrictRedis(host="localhost" , port=6379)
print colored("Getting token..." , "yellow")
################################################################################
api_token = "601270288:AAHfClZ7pKBLno4lI01fNQYOCfNWBElbhvQ"
sudos = [ 478026278 , 234169062 , 470777430 ]
bot = telebot.TeleBot(token=api_token)
print colored("Bot is online now!" , "green")
################################################################################
def lockphoto(m):
    if str(redis.sismember("photo" , m))=="True":
        return "LOCKED"
    else:
        return "UNLOCKED"
def lockvideo(m):
    if str(redis.sismember("video" , m))=="True":
        return "LOCKED"
    else:
        return "UNLOCKED"
def lockvoice(m):
    if str(redis.sismember("voice" , m))=="True":
        return "LOCKED"
    else:
        return "UNLOCKED"
def locktext(m):
    if str(redis.sismember("text" , m))=="True":
        return "LOCKED"
    else:
        return "UNLOCKED"
def lockgif(m):
    if str(redis.sismember("gif" , m))=="True":
        return "LOCKED"
    else:
        return "UNLOCKED"
def locksticker(m):
    if str(redis.sismember("sticker" , m))=="True":
        return "LOCKED"
    else:
        return "UNLOCKED"
def lockmusic(m):
    if str(redis.sismember("music" , m))=="True":
        return "LOCKED"
    else:
        return "UNLOCKED"
def locklocation(m):
    if str(redis.sismember("location" , m))=="True":
        return "LOCKED"
    else:
        return "UNLOCKED"
def lockcontact(m):
    if str(redis.sismember("contact" , m))=="True":
        return "LOCKED"
    else:
        return "UNLOCKED"
def locklink(m):
    if str(redis.sismember("link" , m))=="True":
        return "LOCKED"
    else:
        return "UNLOCKED"
def lockgame(m):
    if str(redis.sismember("game" , m))=="True":
        return "LOCKED"
    else:
        return "UNLOCKED"
#######################################################################################################################################################################
@bot.message_handler(commands=['start'])
def starting(m):
    userid = m.from_user.id
    chatid = m.chat.id
    redis.sadd("members" , "{}".format(userid))
    markup = types.InlineKeyboardMarkup()
    link = types.InlineKeyboardButton(text="⌥ C H A N N E L" , url="https://t.me/kingtgteam")
    markup.add(link)
    bot.send_message( chatid , """⌥ Welcome to KING api bot...
*⌥ Locks are :* `
> Photo
> Video
> Gif
> Sticker
> Link
> Flood
> Forward
> Music
> Voice
> TelegramNotifications
> Text
> Persian / English
> BadWords
> Tags / Usernames
and more...
`
_⌥ Enjoy it for free!_""" , parse_mode="Markdown" , reply_markup=markup)
#######################################################################################################################################################################
@bot.message_handler(commands=['ping'])
def ping(m):
    userid = m.from_user.id
    chatid = m.chat.id
    bot.send_message(chatid , "*⌥ KING IS ONLINE AT ALL THE TIME!*" ,"Markdown")
#######################################################################################################################################################################
@bot.message_handler(commands=['add'])
def add(m):
    userid = m.from_user.id
    chatid = m.chat.id
    chat = m.chat.type
    groups = str(redis.sismember("groups" , "{}".format(chatid)))
    if (userid in sudos or bot.get_chat_member(chatid , userid).status!="member") and chat=="supergroup":
        if not groups=="True":
            redis.sadd("groups" , "{}".format(chatid))
            bot.send_message(chatid , "*⌥ Supergroup {} has been added to database.*".format(chatid) , parse_mode="Markdown")
        else:
            bot.send_message(chatid , "*⌥ Supergroup {} is alreay in database.*".format(chatid) , parse_mode="Markdown")
    else:
        bot.send_message(chatid , "*⌥ You are not admin or chat in not a supergroup!*"  , parse_mode="Markdown")
#######################################################################################################################################################################
@bot.message_handler(commands=['rem'])
def add(m):
    userid = m.from_user.id
    chatid = m.chat.id
    chat = m.chat.type
    groups = str(redis.sismember("groups" , "{}".format(chatid)))
    if (userid in sudos or bot.get_chat_member(chatid , userid).status!="member") and chat=="supergroup":
        if groups=="True":
            redis.srem("groups" , "{}".format(chatid))
            bot.send_message(chatid , "*⌥ Supergroup {} has been removed from database.*".format(chatid) , parse_mode="Markdown")
        else:
            bot.send_message(chatid , "*⌥ Supergroup is not one of my groups.*" , parse_mode="Markdown")
    else:
        bot.send_message(chatid , "*⌥ You are not admin or chat in not a supergroup!*"  , parse_mode="Markdown")
#######################################################################################################################################################################
@bot.message_handler(commands=['settings'])
def add(m):
    userid = m.from_user.id
    chatid = m.chat.id
    chat = m.chat.type
    groups = str(redis.sismember("groups" , "{}".format(chatid)))
    if (userid in sudos or bot.get_chat_member(chatid , userid).status!="member") and chat=="supergroup":
        if groups=="True":
            bot.send_message(chatid , """*⌥ PHOTO : {}
*""".format(lockphoto(chatid)) , parse_mode="Markdown")
    else:
        bot.send_message(chatid , "*⌥ You are not admin or chat in not a supergroup!*" , parse_mode="Markdown")
#######################################################################################################################################################################
@bot.message_handler(content_types=['photo'])
def photolock(m):
    userid = m.from_user.id
    chatid = m.chat.id
    chat = m.chat.type
    groups = str(redis.sismember("groups" , "{}".format(chatid)))
    if chat=="supergroup":
        if groups=="True":
            if lockphoto=="LOCKED":
                if userid not in sudos or bot.get_chat_member(chatid , userid).status=="member":
                    bot.delete_message(chatid , m.message_id)
#######################################################################################################################################################################
@bot.message_handler(commands=['lock_photo'])
def add(m):
    userid = m.from_user.id
    chatid = m.chat.id
    chat = m.chat.type
    groups = str(redis.sismember("groups" , "{}".format(chatid)))
    if (userid in sudos or bot.get_chat_member(chatid , userid).status!="member") and chat=="supergroup":
        if groups=="True":
            redis.sadd("photo" , chatid)
            bot.send_message(chatid , "*⌥ Photo locked!*")
#######################################################################################################################################################################
while True:
    try:
        bot.polling(True)
    except:
        pass
