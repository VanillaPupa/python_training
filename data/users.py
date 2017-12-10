from model.user import User


testdata = [
    User(firstname="Sherlock", lastname="Holmes",
         address="221b, Baker Street, London, UK", email="Sherlock@museum.com",
         email2="Holmes@museum.com", email3="HolmesWatson@museum.com", homephone="321-32-13",
         mobilephone="+441712223355", workphone="123 12 31", additionalphone="+(44)1715553322"),
    User(firstname="John H.", lastname="Watson",
         address="221b, Baker Street, London, UK", email="JohnH.Watson@Museum.com",
         email2="Dr.Watson@Museum.com", email3="HolmesWatson@museum.com", homephone="321-32-13",
         mobilephone="+441712223355", workphone="123 12 31", additionalphone="+(44)1715553322")
]
