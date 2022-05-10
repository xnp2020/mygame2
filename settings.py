class Settings:
    """定义设置的类"""

    def __init__(self, bo_es):
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,128,255)

        #boat设置
        self.boat_limit = 2

        #子弹设置
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #外星人设置
        self.fleet_drop_speed = 10
        
        #加快游戏速度
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.boat_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.boat_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.score_scale * self.alien_points)
        