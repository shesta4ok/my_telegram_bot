import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
import asyncio

API_TOKEN = '8171646376:AAEOTvWwgw50HdT5whDd01fgaKBJG83dnxg'
CHANNEL_ID = '@bulavka_secondhand'

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("Привет! Подпишись на канал и получи скидку!")

@dp.message_handler(commands=['send_promotion'])
async def send_promotion(message: types.Message):
    try:
        # Отправка сообщения в канал с кнопкой
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Подпишись на канал!", url="https://t.me/bulavka_secondhand")
        keyboard.add(button)
        await bot.send_message(CHANNEL_ID, "Получите скидку, подписавшись на канал! 🤑🎉", reply_markup=keyboard)
        await message.answer("Сообщение отправлено в канал.")
    except Exception as e:
        await message.answer(f"Ошибка: {str(e)}")

if __name__ == '__main__':
    # Запускаем бота
    executor.start_polling(dp)
