from model.user import User
import random
import string

constant = [
    User(firstname="Sherlock", lastname="Holmes",
         address="221b, Baker Street, London, UK", email="Sherlock@museum.com",
         email2="Holmes@museum.com", email3="HolmesWatson@museum.com", homephone="321-32-13",
         mobilephone="+441712223355", workphone="123 12 31", additionalphone="+(44)1715553322"),
    User(firstname="John H.", lastname="Watson",
         address="221b, Baker Street, London, UK", email="JohnH.Watson@Museum.com",
         email2="Dr.Watson@Museum.com", email3="HolmesWatson@museum.com", homephone="321-32-13",
         mobilephone="+441712223355", workphone="123 12 31", additionalphone="+(44)1715553322")
]


def random_str(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + ": " + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    symbols = string.digits + "(" + ")" + "-" + "+" + " "
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [User(firstname="", lastname="", address="", email="", email2="", email3="", homephone="", mobilephone="",
                 workphone="", additionalphone="")] + \
           [User(firstname=random_str("firstname", 10), lastname=random_str("lastname", 20),
                 address=random_str("address", 70), email=random_str("email", 20), email2=random_str("email2", 20),
                 email3=random_str("email3", 20), homephone=random_phone(10), mobilephone=random_phone(10),
                 workphone=random_phone(10), additionalphone=random_phone(10))for i in range(5)]