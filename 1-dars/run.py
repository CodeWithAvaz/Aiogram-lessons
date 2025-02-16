import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message


API_TOKEN = "7761483846:AAF2xnF-GaCbC9JYSFN-v3-VXYO0EdUBRP8"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message()
async def return_message(msg: Message):
    user_msg = msg.text
    # await msg.answer(user_msg)
    await msg.reply(user_msg)



async def main():
    print("Bot ishladi....")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())