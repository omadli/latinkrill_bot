from config import API_TOKEN
from func import transliterate
from aiogram import Bot, Dispatcher, types, executor


bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.answer(
        f"Assalomu alaykum {message.from_user.get_mention(as_html=True)} "
        f"lotin-krill tarjimon botiga xush kelibsiz.\n"
        f"Botdan foydalanish uchun biror matn yuboring.\n"
        f"Batafsil yordam menyusi /help"
    )
    

@dp.message_handler(commands='help')
async def cmd_help(message: types.Message):
    await message.answer(
        "Bot lotinchadan krillga yoki krilldan lotinga o'girib beradi.\n"
        "Transliteratsiya qilish (lotin->krill yoki krill->lotin o'girish) <a href='https://uz.wikipedia.org/wiki/Vikipediya:O%CA%BBzbek_lotin_alifbosi_qoidalari'>"
        "O'zbek lotin alifbosi qoidalari</a>ga asosan bajariladi.\n"
        "Botda kamchilik yoki xato topsangiz @murodillo17 ga screenshot qilib yuboring."
    )


@dp.message_handler(regexp=r'[A-Za-z]')
async def latin2krill(message: types.Message):
    await message.answer(
        transliterate(message.text, "cyrillic")
    )
    

@dp.message_handler(regexp=r'[А-Яа-я]')
async def krill2latin(message: types.Message):
    await message.answer(
        transliterate(message.text, "latin")
    )
    

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    