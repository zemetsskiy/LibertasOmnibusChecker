from aiogram import types
from aiogram.types import ParseMode

from app.create_bot import dp
from app.utils.checker import Checker


@dp.message_handler(commands=['start'])
async def handle_start(message: types.Message):
    await message.answer("<b> Введите кошелек или список кошельков каждый с новой строки. </b>", parse_mode=types.ParseMode.HTML)


@dp.message_handler(lambda message: not message.text.startswith('/'))
async def handle_wallets(message: types.Message):
    wallets = message.text.split("\n")
    results = []

    for wallet in wallets:
        if len(wallet) != 42:
            results.append(f"<b> {wallet} </b> <u> Invalid wallet address </u>\n")
            continue
        result = await Checker.check(wallet)
        results.append(f"<b> {wallet} </b> {result}\n")
    await message.answer("\n".join(results), parse_mode=ParseMode.HTML)