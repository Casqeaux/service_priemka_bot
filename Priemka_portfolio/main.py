import logging
import setting
from pymongo import MongoClient
from bs4 import BeautifulSoup
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode, CallbackQuery
from aiogram.utils import executor
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from aiogram.utils.callback_data import CallbackData
import requests


TOKEN = setting.token
admin_chat_id = setting.admin_chat_id
priem_chat_id = setting.priem_chat_id
cluster = MongoClient(setting.mongo)

# Подключаемся к БД
db = cluster["Zayavka_Bot"]
# Подключаемся к таблице(коллекции)
workers = db["service"]

# Создаём бота
bot = Bot(token=TOKEN)
# Присваиваем хранилище переменной storage, оно нам понадобится позже.
storage = MemoryStorage()
# Создаём диспетчер с аргументами bot и storage
dp = Dispatcher(bot, storage=storage)
# Добавляем встроенную миддлварь для удобного логгирования
logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())

# Пропишем простую клавиатуру Зарегистрироваться из одной кнопки
reg_button = KeyboardButton("📩 Зарегистрировать заявку")
reg_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
reg_keyboard.add(reg_button)



# Пропишем простую клавиатуру Отмена из одной кнопки
cancel_button = KeyboardButton("❌ Отменить заявку")

cancel_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
cancel_keyboard.add(cancel_button)

# Пропишем простую клавиатуру Пропустить из одной кнопки
next_button = KeyboardButton("❎ Пропустить")
next_button2 = KeyboardButton("❌ Отменить заявку")
next_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
next_keyboard.add(next_button)
next_keyboard.add(next_button2)

# Пропишем клавиатуру для Комментариев
next_com_button = KeyboardButton("❎ Пропустить комментарий")
next_com_button2 = KeyboardButton("❌ Отменить заявку")
next_com_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
next_com_keyboard.add(next_com_button)
next_com_keyboard.add(next_com_button2)

# Пропишем даты календаря
date_button1 = KeyboardButton("01.01.2023")
date_button2 = KeyboardButton("02.01.2023")
date_button3 = KeyboardButton("03.01.2023")
date_button4 = KeyboardButton("04.01.2023")
date_button5 = KeyboardButton("05.01.2023")
date_button6 = KeyboardButton("06.01.2023")
date_button7 = KeyboardButton("07.01.2023")
date_button8 = KeyboardButton("08.01.2023")
date_button9 = KeyboardButton("09.01.2023")
date_button10 = KeyboardButton("10.01.2023")
date_button11 = KeyboardButton("11.01.2023")
date_button12 = KeyboardButton("12.01.2023")
date_button13 = KeyboardButton("13.01.2023")
date_button14 = KeyboardButton("14.01.2023")
date_button15 = KeyboardButton("15.01.2023")
date_button16 = KeyboardButton("16.01.2023")
date_button17 = KeyboardButton("17.01.2023")
date_button18 = KeyboardButton("18.01.2023")
date_button19 = KeyboardButton("19.01.2023")
date_button20 = KeyboardButton("20.01.2023")
date_button21 = KeyboardButton("21.01.2023")
date_button22 = KeyboardButton("22.01.2023")
date_button23 = KeyboardButton("23.01.2023")
date_button24 = KeyboardButton("24.01.2023")
date_button25 = KeyboardButton("25.01.2023")
date_button26 = KeyboardButton("26.01.2023")
date_button27 = KeyboardButton("27.01.2023")
date_button28 = KeyboardButton("28.01.2023")
date_button29 = KeyboardButton("29.01.2023")
date_button30 = KeyboardButton("30.01.2023")
date_button31 = KeyboardButton("31.01.2023")




date_button_cancel = KeyboardButton("❌ Отменить заявку")

date_button = ReplyKeyboardMarkup(resize_keyboard=True)
date_button.add(date_button_cancel)

date_button.add(date_button1, date_button2, date_button3)
date_button.add(date_button4, date_button5, date_button6)
date_button.add(date_button7, date_button8, date_button9)
date_button.add(date_button10, date_button11, date_button12)
date_button.add(date_button13, date_button14, date_button15)
date_button.add(date_button16, date_button17, date_button18)
date_button.add(date_button19, date_button20, date_button21)
date_button.add(date_button22, date_button23, date_button24)
date_button.add(date_button25, date_button26, date_button27)
date_button.add(date_button28, date_button29, date_button30)
date_button.add(date_button31)
date_button.add()


# Пропишем время
time_button1 = KeyboardButton("08:00")
time_button2 = KeyboardButton("08:30")
time_button3 = KeyboardButton("09:00")
time_button4 = KeyboardButton("09:30")
time_button5 = KeyboardButton("10:00")
time_button6 = KeyboardButton("10:30")
time_button7 = KeyboardButton("11:00")
time_button8 = KeyboardButton("11:30")
time_button9 = KeyboardButton("12:00")
time_button10 = KeyboardButton("12:30")
time_button11 = KeyboardButton("13:00")
time_button12 = KeyboardButton("13:30")
time_button13 = KeyboardButton("14:00")
time_button14 = KeyboardButton("14:30")
time_button15 = KeyboardButton("15:00")
time_button16 = KeyboardButton("15:30")
time_button17 = KeyboardButton("16:00")
time_button18 = KeyboardButton("16:30")
time_button19 = KeyboardButton("17:00")
time_button20 = KeyboardButton("17:30")
time_button21 = KeyboardButton("18:00")
time_button22 = KeyboardButton("18:30")
time_button23 = KeyboardButton("19:00")
time_button24 = KeyboardButton("19:30")
time_button25 = KeyboardButton("20:00")
time_button26 = KeyboardButton("20:30")
time_button27 = KeyboardButton("21:00")
time_button28 = KeyboardButton("21:30")
time_button29 = KeyboardButton("22:00")
time_button30 = KeyboardButton("22:30")
time_button31 = KeyboardButton("23:00")
time_button32 = KeyboardButton("23:30")
time_button33 = KeyboardButton("00:00")
time_button34 = KeyboardButton("00:30")
time_button35 = KeyboardButton("01:00")
time_button36 = KeyboardButton("01:30")
time_button37 = KeyboardButton("02:00")
time_button38 = KeyboardButton("02:30")
time_button39 = KeyboardButton("03:00")
time_button40 = KeyboardButton("03:30")
time_button41 = KeyboardButton("04:00")
time_button42 = KeyboardButton("04:30")
time_button43 = KeyboardButton("05:00")
time_button44 = KeyboardButton("05:30")
time_button45 = KeyboardButton("06:00")
time_button46 = KeyboardButton("06:30")
time_button47 = KeyboardButton("07:00")
time_button48 = KeyboardButton("07:30")

time_button_cancel = KeyboardButton("❌ Отменить заявку")

time_button = ReplyKeyboardMarkup(resize_keyboard=True)
time_button.add(date_button_cancel)
time_button.add(time_button1, time_button2, time_button3,)
time_button.add(time_button4, time_button5, time_button6,)
time_button.add(time_button7, time_button8, time_button9,)
time_button.add(time_button10, time_button11, time_button12,)
time_button.add(time_button13, time_button14, time_button15,)
time_button.add(time_button16, time_button17, time_button18,)
time_button.add(time_button19, time_button20, time_button21,)
time_button.add(time_button22, time_button23, time_button24,)
time_button.add(time_button25, time_button26, time_button27,)
time_button.add(time_button28, time_button29, time_button30,)
time_button.add(time_button31, time_button32, time_button33,)
time_button.add(time_button34, time_button35, time_button36,)
time_button.add(time_button37, time_button38, time_button39,)
time_button.add(time_button40, time_button41, time_button42,)
time_button.add(time_button43, time_button44, time_button45,)
time_button.add(time_button46, time_button47, time_button48,)
time_button.add()

# Пропишем модели рефов
ref_button1 = KeyboardButton("Carrier Maxima 1000")
ref_button2 = KeyboardButton("Thermo King SL 100")
ref_button3 = KeyboardButton("Carrier Maxima 1200")
ref_button4 = KeyboardButton("Thermo King SL 200")
ref_button5 = KeyboardButton("Carrier Maxima 1200Mt")
ref_button6 = KeyboardButton("Thermo King SL 300")
ref_button7 = KeyboardButton("Carrier Maxima 1300")
ref_button8 = KeyboardButton("Thermo King SL 400")
ref_button9 = KeyboardButton("Carrier Maxima 1300Mt")
ref_button10 = KeyboardButton("Thermo King SL TSi")
ref_button11 = KeyboardButton("Carrier Maxima Plus")
ref_button12 = KeyboardButton("Thermo King SL 100e")
ref_button13 = KeyboardButton("Carrier Maxima 2")
ref_button14 = KeyboardButton("Thermo King SL 200e")
ref_button15 = KeyboardButton("Carrier Vector 1350")
ref_button16 = KeyboardButton("Thermo King SL 300e")
ref_button17 = KeyboardButton("Carrier Vector 1550")
ref_button18 = KeyboardButton("Thermo King SL 400e")
ref_button19 = KeyboardButton("Carrier Vector 1800")
ref_button20 = KeyboardButton("Thermo King SLXe Spectrum")
ref_button21 = KeyboardButton("Carrier Vector 1800Mt")
ref_button22 = KeyboardButton("Thermo King SLX 100")
ref_button23 = KeyboardButton("Carrier Vector 1850")
ref_button24 = KeyboardButton("Thermo King SLX 200")
ref_button25 = KeyboardButton("Carrier Vector 1850Mt")
ref_button26 = KeyboardButton("Thermo King SLX 300")
ref_button27 = KeyboardButton("Carrier Xarios 300")
ref_button28 = KeyboardButton("Thermo King SLX 400")
ref_button29 = KeyboardButton("Carrier Xarios 350")
ref_button30 = KeyboardButton("Thermo King SLX 100e")
ref_button31 = KeyboardButton("Carrier Xarios 350Mt")
ref_button32 = KeyboardButton("Thermo King SLX 200e")
ref_button33 = KeyboardButton("Carrier Xarios 400")
ref_button34 = KeyboardButton("Thermo King SLX 300e")
ref_button35 = KeyboardButton("Carrier Xarios 500")
ref_button36 = KeyboardButton("Thermo King SLX 400e")
ref_button37 = KeyboardButton("Carrier Xarios 500Mt")
ref_button38 = KeyboardButton("Thermo King SLXe Spectrum")
ref_button39 = KeyboardButton("Carrier Xarios 600")
ref_button40 = KeyboardButton("Thermo King SMX-I")
ref_button41 = KeyboardButton("Carrier Supra 750")
ref_button42 = KeyboardButton("Thermo King SMX-II")
ref_button43 = KeyboardButton("Carrier Supra 850")
ref_button44 = KeyboardButton("Thermo King SMX Tsi")
ref_button45 = KeyboardButton("Carrier Supra 950")
ref_button46 = KeyboardButton("Thermo King SMX 30")
ref_button47 = KeyboardButton("Carrier Supra 950Mt")
ref_button48 = KeyboardButton("Thermo King SMX 50")
ref_button_cancel = KeyboardButton("❌ Отменить заявку")




ref_button = ReplyKeyboardMarkup(resize_keyboard=True)
ref_button.add(date_button_cancel)
ref_button.add(ref_button1, ref_button2,)
ref_button.add(ref_button3, ref_button4,)
ref_button.add(ref_button5, ref_button6,)
ref_button.add(ref_button7, ref_button8,)
ref_button.add(ref_button9, ref_button10,)
ref_button.add(ref_button11, ref_button12,)
ref_button.add(ref_button13, ref_button14,)
ref_button.add(ref_button15, ref_button16,)
ref_button.add(ref_button17, ref_button18,)
ref_button.add(ref_button19, ref_button20,)
ref_button.add(ref_button21, ref_button22,)
ref_button.add(ref_button23, ref_button24,)
ref_button.add(ref_button25, ref_button26,)
ref_button.add(ref_button27, ref_button28,)
ref_button.add(ref_button29, ref_button30,)
ref_button.add(ref_button31, ref_button32,)
ref_button.add(ref_button33, ref_button34,)
ref_button.add(ref_button35, ref_button36,)
ref_button.add(ref_button37, ref_button38,)
ref_button.add(ref_button39, ref_button40,)
ref_button.add(ref_button41, ref_button42,)
ref_button.add(ref_button43, ref_button44,)
ref_button.add(ref_button45, ref_button46,)
ref_button.add(ref_button47, ref_button48,)



# Пропишем инлайн клавиатуру для чата админов
# Задаём параметры Callback данных
reg_callback = CallbackData("reg", "status", "chat_id", "nick", "date_z", "name_c")


# Оборачиваем клаву в функцию, чтобы было удобнее использовать.
def inline(chat_id, nick, date_z, name_c):
    confirm = InlineKeyboardButton(
        text="✅ Одобрить",
        callback_data=reg_callback.new(
            status="1", chat_id=chat_id, nick=nick, date_z=date_z, name_c=name_c
        ),
    )
    cancel = InlineKeyboardButton(
        text="❌ Отклонить",
        callback_data=reg_callback.new(
            status="0", chat_id=chat_id, nick="-", date_z="-", name_c="-"
        ),
    )
    conf_inline = InlineKeyboardMarkup()
    conf_inline.insert(confirm).insert(cancel)
    return conf_inline

## Отмена заявки
def inline2(chat_id, nick, date_z, name_c):
    cancel = InlineKeyboardButton(
        text="❌ Отменить заявку",
        callback_data=reg_callback.new(
            status="00", chat_id=chat_id, nick="-", date_z="-", name_c="-"
        ),
    )
    conf_inline = InlineKeyboardMarkup()
    conf_inline.insert(cancel)
    return conf_inline

## Отмена заявки
def inline3(chat_id, nick, date_z, name_c):
    cancel = InlineKeyboardButton(
        text="❌ Отменить заявку",

    )
    conf_inline = InlineKeyboardMarkup()
    conf_inline.insert(cancel)
    return conf_inline

# Создаём класс, передаём в него StatesGroup, он нам понадобится, чтобы провести юзера через анкету
# и сохранить каждый ответ. Если кто-то хочет почитать поподробнее, загуглите "aiogram машина состояний"
class Anketa(StatesGroup):
    # внутри объявляем Стейты(состояния), далее мы будем вести пользователя по цепочке этих стейтов
    date_z = State()
    timer_r = State()
    model_r = State()
    name_c = State()
    nomer_p = State()
    nomer_ts = State()
    date_r = State()
    comments = State()
    text = State()

@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):

        await bot.send_message(
            message.chat.id,
            f"<b>Добро пожаловать, {message.from_user.username}!</b>\n\n"
            f"Чтобы внести в базу заявку на ремонт(обслуживание), нажмите кнопку \n👇\n<b>✉ Зарегистрировать заявку</b>",
            parse_mode=ParseMode.HTML,
            reply_markup=reg_keyboard,
        )


@dp.message_handler(Text(equals="заявки"), state="*")
async def problem(message: types.Message, state: FSMContext):
    await bot.send_message(
        message.chat.id,
        f"<b>👉 Список отправленных заявок:</b> https://bit.ly/3yj7Rjq",
        parse_mode=ParseMode.HTML,


    )


@dp.message_handler(Text(equals="Заявки"), state="*")
async def problem(message: types.Message, state: FSMContext):
    await bot.send_message(
        message.chat.id,
        f"<b>👉 Список отправленных заявок:</b> https://docs.google.com/spreadsheets/d/11OsVUOnU7biLFLm4A8LyA0KyOiZTTt-YK2g_FfOkN-Y/edit?usp=sharing",
        parse_mode=ParseMode.HTML,

    )

@dp.message_handler(Text(equals="/zayavka"), state="*")
async def problem(message: types.Message, state: FSMContext):
    await bot.send_message(
        message.chat.id,
        f"<b>👉 Список отправленных заявок:</b> https://docs.google.com/spreadsheets/d/11OsVUOnU7biLFLm4A8LyA0KyOiZTTt-YK2g_FfOkN-Y/edit?usp=sharing",
        parse_mode=ParseMode.HTML,


    )

@dp.message_handler(Text(equals="❌ Отменить заявку"), state="*")
async def menu_button(message: types.Message, state: FSMContext):
    await state.finish()
    await bot.send_message(
        message.chat.id,

        f"<b>🎯 Регистрация заявки отменена, {message.from_user.username}!</b>\n\n"
        f"Чтобы внести в базу заявку на ремонт(обслуживание), нажмите кнопку \n👇\n<b>✉ Зарегистрировать заявку</b>",
        parse_mode=ParseMode.HTML,
        reply_markup=reg_keyboard,

    )

@dp.message_handler(Text(equals="❎ Пропустить"))
async def menu_button(message: types.Message, state: FSMContext):
    await bot.send_message(
        message.chat.id, "Пропускаем"

    )

# Теперь пропишем цепочку хэндлеров для анкеты
@dp.message_handler(Text(equals="📩 Зарегистрировать заявку"), state="*")
async def date_z(message: types.Message, state: FSMContext):
    await bot.send_message(
        message.chat.id,
        f"<b>Дата(дд.мм.гг):</b>\n\n"
        f"🔔 Выберите дату из списка или введите свою дату",
        parse_mode=ParseMode.HTML,
        reply_markup=date_button
    )



    # Переходим на следующий стейт
    await Anketa.date_z.set()
@dp.message_handler(state=Anketa.date_z, content_types=types.ContentTypes.TEXT)
async def timer_r(message: types.Message, state: FSMContext):
    # Записываем ответ в storage
    await state.update_data(date_z=message.text)
    await bot.send_message(
        message.chat.id,
        f"<b>Время(чч:мм):</b>\n\n"
        f"🔔 Выберите время из списка или введите своё время",
         parse_mode=ParseMode.HTML,
         reply_markup=time_button
    )

    await Anketa.timer_r.set()

#дата ремонта
@dp.message_handler(state=Anketa.timer_r, content_types=types.ContentTypes.TEXT)
async def model_r(message: types.Message, state: FSMContext):
    # Записываем ответ в storage
    await state.update_data(timer_r=message.text)
    await bot.send_message(
        message.chat.id,
        "<b>Модель ХОУ:</b>\n\n" 
        f"🔔 Выберите Модель ХОУ из списка или введите свою",
        parse_mode=ParseMode.HTML,
        reply_markup=ref_button

    )

    await Anketa.model_r.set()

#время ремонта
@dp.message_handler(state=Anketa.model_r, content_types=types.ContentTypes.TEXT)
async def name_c(message: types.Message, state: FSMContext):
    # Записываем ответ в storage
    await state.update_data(model_r=message.text)
    await bot.send_message(
        message.chat.id, "<b>Введите название компании(клиента):</b>", reply_markup=cancel_keyboard, parse_mode=ParseMode.HTML,
    )

    await Anketa.name_c.set()

#модель рефа
@dp.message_handler(state=Anketa.name_c, content_types=types.ContentTypes.TEXT)
async def nomer_p(message: types.Message, state: FSMContext):
    # Записываем ответ в storage
    await state.update_data(name_c=message.text)
    await bot.send_message(
        message.chat.id, "<b>Введите номер телефона:</b>", reply_markup=cancel_keyboard, parse_mode=ParseMode.HTML
    )

    await Anketa.nomer_p.set()

#номер прицепа
@dp.message_handler(state=Anketa.nomer_p, content_types=types.ContentTypes.TEXT)
async def nomer_ts(message: types.Message, state: FSMContext):
    # Записываем ответ в storage
    await state.update_data(nomer_p=message.text)
    await bot.send_message(
        message.chat.id, "<b>Введите номер транспортного средства:</b>",
        reply_markup=cancel_keyboard,
        parse_mode=ParseMode.HTML
    )

    await Anketa.nomer_ts.set()

@dp.message_handler(state=Anketa.nomer_ts, content_types=types.ContentTypes.TEXT)
async def comments(message: types.Message, state: FSMContext):
    # Записываем ответ в storage
    await state.update_data(nomer_ts=message.text)
    await bot.send_message(
        message.chat.id, "<b>Причина обращения:</b>",
        reply_markup=cancel_keyboard,
        parse_mode=ParseMode.HTML
    )

    await Anketa.comments.set()

#сообщение
@dp.message_handler(state=Anketa.comments, content_types=types.ContentTypes.TEXT)
async def text(message: types.Message, state: FSMContext):
    # Записываем ответ в storage
    await state.update_data(comments=message.text)
    await bot.send_message(
        message.chat.id, "<b>Комментарий:</b>",
        reply_markup=next_com_keyboard,
        parse_mode=ParseMode.HTML
    )

    await Anketa.text.set()


@dp.message_handler(state=Anketa.text, content_types=types.ContentTypes.TEXT)
async def confirmation(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
    await bot.send_message(
        message.chat.id, "✅ Заявка успешно заполнена и отправлена!\n\n Зарегистрируем еще заявку?\n\nЧтобы внести в базу заявку на ремонт(обслуживание), нажмите кнопку \n\n👇\n✉ Зарегистрировать заявку",
        reply_markup=reg_keyboard,

    )

    # Insert БД
    workers.insert_one(
        {
            "Дата": data.get("date_z"),
            "Время": data.get("timer_r"),
            "ХОУ": data.get("model_r"),
            "Заказчик": data.get("name_c"),
            "Телефон": data.get("nomer_p"),
            "Номер ТС": data.get("nomer_ts"),
            "Причина обращения": data.get("comments"),
            "Комментарий": data.get("text"),
        }
    )
    # Отправляем сообщение в чат админов с анкетой и добавляем 2 инлайн кнопки с callback данными
    await bot.send_message(
        admin_chat_id,
        f"<b>Поступила заявка от</b> @{message.from_user.username}\n\n"
        f'<b>Дата:</b> {data.get("date_z")}\n'
        f'<b>Время:</b> {data.get("timer_r")}\n\n'
        f'<b>ХОУ:</b> {data.get("model_r")}\n'
        f'<b>Заказчик:</b> {data.get("name_c")}\n'
        f'<b>Телефон:</b> {data.get("nomer_p")}\n'
        f'<b>Номер ТС:</b> {data.get("nomer_ts")}\n\n'
        f'<b>Причина обращения:</b> {data.get("comments")}\n'
        f'<b>Комментарий:</b> {data.get("text")}',
        parse_mode=ParseMode.HTML,
        reply_markup=inline(
            f"{message.chat.id}",
            f"{message.from_user.username}",
            f'{"text"}',
            f'{"model_r"}',
        ),
    )
    await bot.send_message(
        priem_chat_id,
        f"<b>Заявка от</b> @{message.from_user.username}\n\n"
        f'<b>Дата:</b> {data.get("date_z")}\n'
        f'<b>Время:</b> {data.get("timer_r")}\n\n'
        f'<b>ХОУ:</b> {data.get("model_r")}\n'
        f'<b>Заказчик:</b> {data.get("name_c")}\n'
        f'<b>Телефон:</b> {data.get("nomer_p")}\n'
        f'<b>Номер ТС:</b> {data.get("nomer_ts")}\n\n'
        f'<b>Причина обращения:</b> {data.get("comments")}\n'
        f'<b>Комментарий:</b> {data.get("text")}',
        parse_mode=ParseMode.HTML,
        reply_markup=inline2(
            f"{message.chat.id}",
            f"{message.from_user.username}",
            f'{"text"}',
            f'{"model_r"}',
        ),
    )

    # Заканчиваем "опрос"
    await state.finish()


# Теперь пропишем хэндлеры для inline

@dp.callback_query_handler(reg_callback.filter(status="0"))
# callback данные мы сразу же преобразуем в словарь для удобства работы
async def decline(call: CallbackQuery, callback_data: dict):
    await call.answer()
    print(call.message.message_id, "❌ ОТКЛОНЕНО")
    await call.message.forward(priem_chat_id, call.message.message_id)
    # Редачим сообщение в чате админов
    await bot.edit_message_text(

        "❌ Заявка отклонена.", admin_chat_id, call.message.message_id
    )
    await bot.send_message(
        priem_chat_id,

        "❌ Заявка отклонена. В ремонт(обслуживание) не берем!"
    )
    # Отправляем вердикт.
    await bot.send_message(int(callback_data.get("chat_id")), "❌ Заявка ОТКЛОНЕНА. Чинить не будем!")

@dp.callback_query_handler(reg_callback.filter(status="00"))
# callback данные мы сразу же преобразуем в словарь для удобства работы
async def decline(call: CallbackQuery, callback_data: dict):
    await call.answer()
    print(call.message.message_id, "❌ ОТКЛОНЕНО")
    await call.message.forward(admin_chat_id, call.message.message_id)
    await call.message.forward(priem_chat_id, call.message.message_id)
    # Редачим сообщение в чате админов
    await bot.edit_message_text(

        "❌ Заявка ОТМЕНЕНА. Кто-то отменил заявку! Ремонта не будет!", priem_chat_id, call.message.message_id
    )
    await bot.send_message(
        admin_chat_id,

        "☝ Вот эта\n"
        "❌ Заявка ОТМЕНЕНА. Кто-то отменил заявку! Ремонта не будет!\n\n"
        "‼ Если отмена заявки произошла случайно или по ошибке, данную заявку можно выделить и переслать обратно в группу!",


    )
    await bot.send_message(
        priem_chat_id,

        "☝ Вот эта\n"
        "❌ Заявка ОТМЕНЕНА. Кто-то отменил заявку! Ремонта не будет!\n\n"
        "‼ Если отмена заявки произошла случайно или по ошибке, сообщите мне @casqeaux",

    )


@dp.callback_query_handler(reg_callback.filter(status="1"))
async def accept(call: CallbackQuery, callback_data: dict, ):
    await call.answer()
    print(call.message.message_id, "✅ ОДОБРЕНО")
    await call.message.forward(priem_chat_id, call.message.message_id)
    await bot.edit_message_text(
        "✅ Заявка одобрена и направлена для исполнения.", admin_chat_id, call.message.message_id

    )
    await bot.send_message(
        priem_chat_id,

        "✅ Заявка просмотрена и одобрена."
    )

    # Отправляем вердикт.
    await bot.send_message(
        int(callback_data.get("chat_id")), "🔥 Заявка просмотрена и одобрена. \n Направлена в группу для исполнения", reply_markup=reg_keyboard,
    )
##Анекдоты
@dp.message_handler(text='😂 Анекдот?')
async def joke(message: types.Message):
    text = await get_joke()

    await bot.send_message(message.chat.id, text)

async def get_joke():
    joke_html = requests.get('https://nekdo.ru/random/').text
    joke_text = BeautifulSoup(joke_html, 'lxml').find('div', class_='text').get_text()

    return joke_text

##Анекдот
@dp.message_handler(text='/joke')
@dp.message_handler(text='joke')
@dp.message_handler(text='анекдот')
@dp.message_handler(text='Анекдот')
async def joke(message: types.Message):
    text = await get_joke()

    await bot.send_message(message.chat.id, text)

async def get_joke():
    joke_html = requests.get('https://nekdo.ru/random/').text
    joke_text = BeautifulSoup(joke_html, 'lxml').find('div', class_='text').get_text()

    return joke_text

if __name__ == "__main__":
    # Запускаем бота
    executor.start_polling(dp, skip_updates=True)