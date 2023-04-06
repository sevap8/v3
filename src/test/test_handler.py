import pytest
from aiogram import Dispatcher, types
from handlers.handler import BotHandler

@pytest.fixture()
def dispatcher():
    return Dispatcher()

@pytest.fixture()
def bot_handler(dispatcher):
    return BotHandler(dispatcher)

@pytest.mark.asyncio
async def test_start_handler(bot_handler):
    message = types.Message(text='/start')
    await bot_handler.start_handler(message)
    assert message.answer_text == "Привет!\nЯ Эхо-бот !\nОтправь мне любое сообщение, а я тебе обязательно отвечу."

@pytest.mark.asyncio
async def test_help_handler(bot_handler, capsys):
    message = types.Message(text='/help')
    await bot_handler.help_handler(message)
    captured = capsys.readouterr()
    assert captured.out == "222222\n"

@pytest.mark.asyncio
async def test_text_handler(bot_handler):
    message = types.Message(text='test message')
    await bot_handler.text_handler(message)
    assert message.answer_text == 'test message'

@pytest.mark.asyncio
async def test_photo_handler(bot_handler, capsys):
    message = types.Message(content_type=types.ContentType.PHOTO)
    await bot_handler.photo_handler(message)
    captured = capsys.readouterr()
    assert captured.out == "4444\n"
