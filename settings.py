class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 720
        self.screen_heigth = 480
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 0.5

        # 子弹设置
        self.bullet_speed_factor = 0.2
        self.bullet_width = 3
        self.bullet_height = 5
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5