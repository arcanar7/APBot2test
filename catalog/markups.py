from telebot import types


# Клавиатуры
keyboardMain = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
buttonGift = types.KeyboardButton(text="/Подарки")
buttonFriend = types.KeyboardButton(text="/Пригласить_друга")
# buttonQR = types.KeyboardButton(text="/Сканировать_QR-код")
keyboardMain.add(buttonGift, buttonFriend)

hide_markup = types.ReplyKeyboardRemove()

keyboardPhone = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
keyboardPhone.add(button_phone)
####################################################################
