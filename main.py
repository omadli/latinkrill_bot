from aiohttp import web
from bot import bot, dp
from aiogram import types, Dispatcher, Bot
from config import WEBAPP_HOST, WEBAPP_PORT, WEBHOOK_PATH, WEBHOOK_URL


async def on_startup(app: web.Application):
    webhook = await bot.get_webhook_info()
    if webhook.url != WEBHOOK_URL:
        await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)
        print("Webhook setted")
    print("Bot started")


async def on_shutdown(app: web.Application):
    await bot.delete_webhook()
    print("Bye")


async def proceed_update(req: web.Request):
    upds = [types.Update(**(await req.json()))]
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_updates(upds)


async def execute(req: web.Request) -> web.Response:
    await proceed_update(req)
    return web.Response()


async def home(req: web.Request) -> web.Response:
    return web.Response(text="Hello world", content_type='text/html', charset='UTF8')


if __name__ == '__main__':
    app = web.Application()
    app.add_routes([
        web.get("/", home),
        web.post(WEBHOOK_PATH, execute),
    ])
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    web.run_app(app,
                host=WEBAPP_HOST,
                port=WEBAPP_PORT
            )