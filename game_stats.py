import json
class Gamestats:
    """记录游戏统计信息的类"""

    def __init__(self, bo_es):
        self.settings = bo_es.settings
        self.game_active = False
        filename = 'score.json'
        with open(filename) as f:
            self.high_score = json.load(f)
        self.reset_stats()
        

    def reset_stats(self):
        self.ship_left = self.settings.boat_limit
        self.level = 1
        self.score = 0