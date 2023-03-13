from settings import Settings

class GameStats():
        def __init__(self,settings):
            self.game_active = False
            if settings is Settings:
                self.game_active = False
            else:
                print("输入错误")
        def reset_stats(self):
            return