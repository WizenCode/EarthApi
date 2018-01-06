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
redis = r.Strictredis(host="localhost" , port=6379 , db=0)
print colored("Getting token..." , "yellow")
################################################################################
api_token = "434680910:AAH7__Bw_JxOUc5O_iW3lN9mDXYU_FNDaOE"
sudos = [ 478026278 , 234169062 , 470777430 ]
bot = telebot.TeleBot(token=api_token)
print colored("Bot is online now!" , "green")
################################################################################

#######################################################################################################################################################################
@bot.message_handler(commands=['start'])
def starting(m):
    userid = m.from_user.id
    chatid = m.chat.id
    redis.sadd("members" , "{}".format(userid))
    markup = types.InlineKeyboardMarkup()
    link = types.InlineKeyboardButton(text="• Contact us •" , url="https://t.me/princedard")
    channel = types.InlineKeyboardButton(text="• Creator channel •" , url="https://t.me/earthteamrebot")
    markup.add(link)
    bot.send_message( chatid , """• Welcome to EARTH api bot...
*Locks are :* `
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
_For buy this anti vandal bot you need contact us!_

Buy method : Charge | Payment | ATMs
""" , parse_mode="Markdown" , reply_markup=markup)
#######################################################################################################################################################################
@bot.message_handler(commands=['promote'])
def promote(m):
    userid = m.from_user.id
    chatid = m.chat.id
    replied = m.reply_to_message
    prouser = m.reply_to_message.from_user.id
    admins = str(redis.sismember("admins" , "{}".format(prouser)))
    if userid in sudos:
        if not admins=="True" and replied:
            redis.sadd("admins" , "{}".format(prouser))
            bot.send_message(chatid , "• User [ `{}` ] has been promoted as admin.".format(prouser) , parse_mode="Markdown")
        else:
            bot.send_message(chatid , "• User [ `{}` ] is already an admin of the bot.".format(prouser) , parse_mode="Markdown")
    else:
        bot.send_message(chatid , "• You are not sudo." , parse_mode="Markdown")
#######################################################################################################################################################################
@bot.message_handler(commands=['demote'])
def demote(m):
    userid = m.from_user.id
    chatid = m.chat.id
    replied = m.reply_to_message
    prouser = m.reply_to_message.from_user.id
    admins = str(redis.sismember("admins" , "{}".format(prouser)))
    if userid in sudos:
        if admins=="True" and replied:
            redis.srem("admins" , "{}".format(prouser))
            bot.send_message(chatid , "• User [ `{}` ] has been demoted.".format(prouser) , parse_mode="Markdown")
        else:
            bot.send_message(chatid , "• User [ `{}` ] is not already an admin of the bot.".format(prouser) , parse_mode="Markdown")
    else:
        bot.send_message(chatid , "• You are not sudo." , parse_mode="Markdown")
#######################################################################################################################################################################
@bot.message_handler(commands=['ping'])
def ping(m):
    userid = m.from_user.id
    chatid = m.chat.id
    bot.send_message(chatid , "• Bot is online.")
#######################################################################################################################################################################
@bot.message_handler(commands=['add'])
def add(m):
    userid = m.from_user.id
    chatid = m.chat.id
    chat = m.chat.type
    groups = str(redis.sismember("groups" , "{}".format(chatid)))
    if userid in sudos and chat=="supergroup":
        if not groups=="True":
            redis.sadd("groups" , "{}".format(chatid))
            bot.send_message(chatid , "• Group [ `{}` ] has been added to database.".format(chatid) , parse_mode="Markdown")
        else:
            bot.send_message(chatid , "• Group [ `{}` ] is already added to database.".format(chatid) , parse_mode="Markdown")
    else:
        bot.send_message(chatid , "• You are not sudo." , parse_mode="Markdown")
#######################################################################################################################################################################
@bot.message_handler(commands=['rem'])
def add(m):
    userid = m.from_user.id
    chatid = m.chat.id
    chat = m.chat.type
    groups = str(redis.sismember("groups" , "{}".format(chatid)))
    if userid in sudos and chat=="supergroup":
        if groups=="True":
            redis.srem("groups" , "{}".format(chatid))
            bot.send_message(chatid , "• Group [ `{}` ] has been removed from database.".format(chatid) , parse_mode="Markdown")
        else:
            bot.send_message(chatid , "• Group [ `{}` ] is not already added to database.".format(chatid) , parse_mode="Markdown")
    else:
        bot.send_message(chatid , "• You are not sudo." , parse_mode="Markdown")
#######################################################################################################################################################################

#######################################################################################################################################################################

#######################################################################################################################################################################
@bot.message_handler(content_types=['text', 'caption', 'username', 'tag', 'persian', 'english', 'filters', 'forward', 'link', 'sticker', 'location', 'contact', 'document', 'audio', 'video', 'photo'])
def delete(m):
    if not m.from_user.id in sudos or redis.sismember("admins"+str(m.chat.id), m.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		if msg.location and database.get("location"+str(msg.chat.id)):
			delmessage(token, msg.chat.id, msg.message_id)
#######################################################################################################################################################################
while True:
    try:
        bot.polling(True)
    except:
        pass
