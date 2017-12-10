from model.user import User
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/users.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


# def random_str(prefix, maxlen):
    # symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    # return prefix + ": " + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


#testdata = [Group(name="", header="", footer="")] + \
           # [Group(name=random_str("name", 10), header=random_str("header", 20), footer=random_str("footer", 20)) for i in range(n)]

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
                 workphone=random_phone(10), additionalphone=random_phone(10))for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
