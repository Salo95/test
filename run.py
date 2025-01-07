from main import User, UserService

user = UserService()

# user_service = User(name = 'Salavat', email = 'salavat@gmail.com', age = 16)
# user.add_user(user_service)

# find = user.find_user_by_email('salavat@gmail.com')
# if find:
#     print(f'Пользователь найден: {find.name}, {find.email}, {find.age}')

delete = user.delete_user_by_email('salavat@gmail.com')