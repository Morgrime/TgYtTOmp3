from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

router = Router()

# /start
@router.message(CommandStart())
async def start_message_handler(message: Message):
    await message.answer('Бот для конвертации видео ютуба в mp3/mp4\n\n'
                         'Основные комманды:\n'
                         '/preview - предпросмотр видео\n'
                         '/convert - начать конвертацию')
    
# /help
@router.message(Command(commands='help'))
async def help_message_handler(message: Message):
    await message.answer('Основные команды бота:\n\n'
                         '/preview - предпросмотр видео\n'
                         '/convert - начать конвертацию')