# LOGGING
import logging
import sys

# WEB SERVER
from aiohttp import web

# AIOGRAM
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

# PROJECT SETTINGS
from settings import TELEGRAM_BOT_TOKEN, WEB_SERVER_HOST, WEB_SERVER_PORT, WEBHOOK_PATH, WEBHOOK_URL, WEBHOOK_SECRET

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@router.message()
async def echo_handler(message: types.Message) -> None:
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True, secret_token=WEBHOOK_SECRET)
    bot_info = await bot.get_me()
    webhook_info = await bot.get_webhook_info()
    print("**************__Initializing the bot__**************\n")
    print("**************__Bot info__**************\n")
    print(bot_info)
    print("\n")
    print(webhook_info)
    print("\n")
    
def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    dp.include_router(router)
    dp.startup.register(on_startup)

    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TELEGRAM_BOT_TOKEN, parse_mode=ParseMode.HTML)

    # Create aiohttp.web.Application instance
    app = web.Application()

    # Create an instance of request handler,
    # aiogram has few implementations for different cases of usage
    # In this example we use SimpleRequestHandler which is designed to handle simple cases
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=WEBHOOK_SECRET,
    )
    # Register webhook handler with our app
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)

    # Mount dispatcher startup and shutdown hooks to aiohttp application
    setup_application(app, dp, bot=bot)

    # And finally start webserver
    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main()