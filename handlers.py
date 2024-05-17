from const import keyboards as io, msg
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"مرحبًا بك {message.from_user.full_name} في Go Sport Bot! 🌟\n\n{msg.welcomeMSG}", reply_markup=io.welcomeMU())


@router.message()
async def echo_handler(message: Message):
    await message.answer("مرحبًا بك")


@router.callback_query(F.data == "Inquiry")
async def func(callback: CallbackQuery):
    await callback.message.answer(msg.inquiryMSG, reply_markup=io.inquiryMU())


@router.callback_query(F.data == "MakeOrder")
async def func(callback: CallbackQuery):
    await callback.message.answer(msg.makeOrderMSG, reply_markup=io.makeOrderMU())



@router.callback_query(F.data == "Soulier")
async def func(callback: CallbackQuery):
    await callback.message.edit_text(msg.makeOrderMSG, reply_markup=io.soulierMU())


@router.callback_query(F.data == "Vetement")
async def func(callback: CallbackQuery):
    await callback.message.edit_text(msg.makeOrderMSG, reply_markup=io.vetementMU())


@router.callback_query(F.data == "Accessoire")
async def func(callback: CallbackQuery):
    await callback.message.edit_text(msg.makeOrderMSG, reply_markup=io.accessoireMU())


@router.callback_query(F.data == "AdulteC")
async def func(callback: CallbackQuery):
    await callback.message.edit_text(msg.makeOrderMSG, reply_markup=io.adulteCMU())


@router.callback_query(F.data == "AdulteT")
async def func(callback: CallbackQuery):
    await callback.message.edit_text(msg.makeOrderMSG, reply_markup=io.adulteTMU())


@router.callback_query(F.data == "BackToMain")
async def func(callback: CallbackQuery):
    await callback.message.edit_text(msg.makeOrderMSG, reply_markup=io.makeOrderMU())


@router.callback_query(F.data == "BackToSoulier")
async def func(callback: CallbackQuery):
    await callback.message.edit_text(msg.makeOrderMSG, reply_markup=io.soulierMU())
