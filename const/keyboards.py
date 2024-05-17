from const import labels as lbl
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def welcomeMU():
    inquiry = InlineKeyboardButton(text=lbl.inquiry_label, callback_data="Inquiry")
    makeOrder = InlineKeyboardButton(text=lbl.makeOrder_label, callback_data="MakeOrder")

    return InlineKeyboardMarkup(inline_keyboard=[[inquiry, makeOrder]])


def inquiryMU():
    makeOrder = InlineKeyboardButton(text=lbl.makeOrder_label, callback_data="MakeOrder")

    return InlineKeyboardMarkup(inline_keyboard=[[makeOrder]])

# Main
def makeOrderMU():
    soulier = InlineKeyboardButton(text=lbl.soulier_label, callback_data="Soulier")
    vetement = InlineKeyboardButton(text=lbl.vetement_label, callback_data="Vetement")
    accessoire = InlineKeyboardButton(text=lbl.accessoire_label, callback_data="Accessoire")
    pack = InlineKeyboardButton(text=lbl.pack_label, url="https://go-sport.shop/categorie-produit/articles-de-football/packs/")

    return InlineKeyboardMarkup(inline_keyboard=[[soulier],[vetement],[accessoire],[pack]])


def soulierMU():
    adulteC = InlineKeyboardButton(text=lbl.adulteC_label, callback_data="AdulteC")
    adulteT = InlineKeyboardButton(text=lbl.adulteT_label, callback_data="AdulteT")
    cadetC = InlineKeyboardButton(text=lbl.cadetC_label, url="https://go-sport.shop/categorie-produit/articles-de-football/souliers/cramponts-cadet/")
    cadetT = InlineKeyboardButton(text=lbl.cadetT_label, url="https://go-sport.shop/categorie-produit/articles-de-football/souliers/tout-terrien-cadet/")
    retour = InlineKeyboardButton(text=lbl.retour, callback_data="BackToMain")

    return InlineKeyboardMarkup(inline_keyboard=[[adulteC],[adulteT],[cadetC],[cadetT],[retour]])


def vetementMU():
    tenue = InlineKeyboardButton(text=lbl.tenue_label, url="https://go-sport.shop/categorie-produit/articles-de-football/vetements/tenue/")
    tshirt = InlineKeyboardButton(text=lbl.tshirt_label, url="https://go-sport.shop/categorie-produit/articles-de-football/vetements/t-shirt/")
    short = InlineKeyboardButton(text=lbl.short_label, url="https://go-sport.shop/categorie-produit/articles-de-football/vetements/short/")
    ensemble = InlineKeyboardButton(text=lbl.ensemble_label, url="https://go-sport.shop/categorie-produit/articles-de-football/vetements/ensembles/")
    vest = InlineKeyboardButton(text=lbl.vest_label, url="https://go-sport.shop/categorie-produit/articles-de-football/vetements/veste/")
    vetElastic = InlineKeyboardButton(text=lbl.vetElastic_label, url="https://go-sport.shop/categorie-produit/articles-de-football/vetements/vetement-elastique/")
    autreVet = InlineKeyboardButton(text=lbl.autreVet_label, url="https://go-sport.shop/categorie-produit/articles-de-football/vetements/autres-vetements/")
    retour = InlineKeyboardButton(text=lbl.retour, callback_data="BackToMain")

    return InlineKeyboardMarkup(inline_keyboard=[[tenue],[tshirt],[short],[ensemble],[vest],[vetElastic],[autreVet],[retour]])


def accessoireMU():
    ballon = InlineKeyboardButton(text=lbl.ballon_label, url="https://go-sport.shop/categorie-produit/articles-de-football/accessoires/ballon/")
    sacSoulier = InlineKeyboardButton(text=lbl.sacSoulier_label, url="https://go-sport.shop/categorie-produit/articles-de-football/accessoires/sac-soulier/")
    gant = InlineKeyboardButton(text=lbl.gant_label, url="https://go-sport.shop/categorie-produit/articles-de-football/accessoires/gants/")
    protege = InlineKeyboardButton(text=lbl.protege_label, url="https://go-sport.shop/categorie-produit/articles-de-football/accessoires/protege/")
    socket = InlineKeyboardButton(text=lbl.socket_label, url="https://go-sport.shop/categorie-produit/articles-de-football/accessoires/chaussettes/")
    autreAcc = InlineKeyboardButton(text=lbl.autreAcc_label, url="https://go-sport.shop/categorie-produit/articles-de-football/accessoires/autres-accessoire/")
    retour = InlineKeyboardButton(text=lbl.retour, callback_data="BackToMain")

    return InlineKeyboardMarkup(inline_keyboard=[[ballon],[sacSoulier],[gant],[protege],[socket],[autreAcc],[retour]])


def adulteCMU():
    allPrice = InlineKeyboardButton(text=lbl.allPrice_label, url="https://go-sport.shop/categorie-produit/articles-de-football/souliers/crampons-adulte/")
    lowBudget = InlineKeyboardButton(text=lbl.lowBudget_label, url="https://go-sport.shop/categorie-produit/articles-de-football/souliers/crampons-adulte/?min_price=2000&max_price=5000")
    mediumBudget = InlineKeyboardButton(text=lbl.mediumBudget_label, url="https://go-sport.shop/categorie-produit/articles-de-football/souliers/crampons-adulte/?min_price=5000&max_price=9000")
    highBudget = InlineKeyboardButton(text=lbl.highBudget_label, url="https://go-sport.shop/categorie-produit/articles-de-football/souliers/crampons-adulte/?min_price=9000")
    retour = InlineKeyboardButton(text=lbl.retour, callback_data="BackToSoulier")

    return InlineKeyboardMarkup(inline_keyboard=[[allPrice],[lowBudget],[mediumBudget],[highBudget],[retour]])


def adulteTMU():
    allPrice = InlineKeyboardButton(text=lbl.allPrice_label, url="https://go-sport.shop/categorie-produit/articles-de-football/souliers/tout-terrien-adulte/")
    lowBudget = InlineKeyboardButton(text=lbl.lowBudget_label, url="https://go-sport.shop/categorie-produit/articles-de-football/souliers/tout-terrien-adulte/?min_price=2000&max_price=5000")
    mediumBudget = InlineKeyboardButton(text=lbl.mediumBudget_label, url="https://go-sport.shop/categorie-produit/articles-de-football/souliers/tout-terrien-adulte/?min_price=5000&max_price=9000")
    highBudget = InlineKeyboardButton(text=lbl.highBudget_label, url="https://go-sport.shop/categorie-produit/articles-de-football/souliers/tout-terrien-adulte/?min_price=9000")
    retour = InlineKeyboardButton(text=lbl.retour, callback_data="BackToSoulier")

    return InlineKeyboardMarkup(inline_keyboard=[[allPrice],[lowBudget],[mediumBudget],[highBudget],[retour]])