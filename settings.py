class Settings:
    """定义设置的类"""

    def __init__(self, bo_es):
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,128,255)

        #boat设置
        self.boat_speed = 1.5
        self.boat_limit = 2

        #子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1