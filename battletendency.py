""" ООП - Объектно ориентированное программирование """
" Наследование "

class Game: # Родительский класс
    def __init__(self, game_name, game_year, company, graphics):
        self.game_name = game_name 
        self.game_year = game_year
        self.company = company
        self.graphics = graphics
        
    def info(self):
        print(f"Game - {self.game_name} - {self.game_year} - {self.company} - {self.graphics}")
        
game = Game("MortalCombat", 2014, "Midway Games", "4K")
game.info()


# class Roblox(Game): # Дочерний класс Game
#     def __init__(self, game_name, game_year, company, graphics, multiplayer):
#         Game.__init__(self, game_name, game_year, company, graphics)
#         # super().__init__(game_name, game_year, company, graphics)
#         self.name = "Player"
#         self.gender = "None"
#         self.skin = "None"
#         self.hp = 100
        
#         self.multiplayer = multiplayer
        
#     def info(self):
#         print(f"Game - {self.game_name} - {self.game_year} - {self.company} - {self.graphics} - {self.multiplayer}")
        
#     def info_player(self):
#         print(f"Игрок - {self.name} - {self.gender} - {self.skin} - {self.hp}")
        
#     def edit_player(self):
#         name = input("Введите свое имя: ")
#         gender = input("Введите свой пол: ")
#         skin = input("Введите свой облик: ")
#         self.name = name
#         self.gender = gender
#         self.skin = skin
    
# roblox = Roblox("Roblox", 2006, 'Roblox Corp.', 'ULTRA', 'YES')
# roblox.info()
# roblox.edit_player()
# roblox.info_player()

# class Strike(Roblox):
#     def __init__(self, game_name, game_year, company, graphics, multiplayer):
#         super().__init__(game_name, game_year, company, graphics, multiplayer)

#     def edit_player(self):
#         return super().edit_player()