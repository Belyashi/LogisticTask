from users import Users


users = Users()
users.register('lola', 'passlol')
users.register('lol2', 'passlol2')
users.register('lol3', 'passlol3')

print users.get_all()