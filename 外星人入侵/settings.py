class Settings():
    '''存储《外星人入侵》的所有设置的类'''
 
    def __init__(self):
        '''初始化游戏的设置'''
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)
        self.bullet_width = 10
        self.bullet_height = 20
        self.bullet_color = (230,0,0)
        self.bullet_speed_factor = 20
        self.ship_speed_factor = 1
