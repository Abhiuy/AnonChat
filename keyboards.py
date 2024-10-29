from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


to_main = KeyboardButton('🔙 To the main page')

cancel_search_kb = ReplyKeyboardMarkup(
    resize_keyboard=True).add('🚫 Cancel search')

stop_kb = ReplyKeyboardMarkup(one_time_keyboard=True,
                              resize_keyboard=True).add('🛑 Stop the dialogue')

like = KeyboardButton('👍 Like')
dislike = KeyboardButton('👎 Dislike')
next_dialog = KeyboardButton('➡️ Next dialogue')
search_kb = ReplyKeyboardMarkup(
    one_time_keyboard=True, resize_keyboard=True).row(like, dislike).add(next_dialog).add(to_main)

like = KeyboardButton('👍 Like')
dislike = KeyboardButton('👎 Dislike')
next_dialog = KeyboardButton('➡️ Next dialogue (♂️)')
search_male_kb = ReplyKeyboardMarkup(
    one_time_keyboard=True, resize_keyboard=True).row(like, dislike).add(next_dialog).add(to_main)

like = KeyboardButton('👍 Like')
dislike = KeyboardButton('👎 Dislike')
next_dialog = KeyboardButton('➡️ Next Dialogue (♀️)')
search_female_kb = ReplyKeyboardMarkup(
    one_time_keyboard=True, resize_keyboard=True).row(like, dislike).add(next_dialog).add(to_main)

man = KeyboardButton('Find ♂️')
random = KeyboardButton('Random 🔀')
woman = KeyboardButton('Find ♀️')
vip = KeyboardButton('Vip 👑')
rules = KeyboardButton('Rules 📖')
profile = KeyboardButton('Profile 👤')
main_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(man, random, woman).row(vip, rules, profile)

name = InlineKeyboardButton('🅰️ Name', callback_data='name')
age = InlineKeyboardButton('🔞 Age', callback_data='age')
sex = InlineKeyboardButton('👫 Floor', callback_data='sex')
country = InlineKeyboardButton('🌍 Side', callback_data='country')
city = InlineKeyboardButton('🏙️ City', callback_data='city')
# op_sex = InlineKeyboardButton('🚺 Пол собеседника 🚹', callback_data='op_sex')
settings_kb = InlineKeyboardMarkup(
    resize_keyboard=True).add(name).add(age).add(sex).add(country).add(city)

change_profile = KeyboardButton('⚙️ Edit profile')
statistic = KeyboardButton('📈 Statistics')
ref = KeyboardButton('💼 Referral')
profile_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(change_profile).add(
    statistic).add(ref).add(to_main)

vip_kb = ReplyKeyboardMarkup(resize_keyboard=True).add('🆓 Get vip for free').add(
    '💰 Buy/Extend VIP ').add(to_main)

day = KeyboardButton('👑 Discharge per day - 20₽')
week = KeyboardButton('👑 VIP for a week - 100₽')
month = KeyboardButton('👑 VIP for a month - 300₽')
buy_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(day).add(week).add(month).add(to_main)

to_main_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(to_main)

male = InlineKeyboardButton('Male ♂️', callback_data='male')
female = InlineKeyboardButton('Female ♀️', callback_data='female')
sex_kb = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(male, female)

on = KeyboardButton('Turn on notifications 🔔')
off = KeyboardButton('Turn off notifications 🔕')
on_kb = ReplyKeyboardMarkup(resize_keyboard=True).add('Exchange 💎').add(on).add(to_main)
off_kb = ReplyKeyboardMarkup(resize_keyboard=True).add('Exchange 💎').add(off).add(to_main)

top = KeyboardButton('🏆 Рейтинги')
statistic_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(top).add(to_main)

top_messages = KeyboardButton('🔝 Топ 5 по messages')
top_likes = KeyboardButton('🔝 Топ 5 по I like it')
top_refs = KeyboardButton('🔝 Топ 5 по Refam')
top_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(top_messages).add(top_likes).add(top_refs).add(to_main)
