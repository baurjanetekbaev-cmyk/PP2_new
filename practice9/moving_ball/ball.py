class Ball:
    def __init__(self, screen_width, screen_height):
        self.radius = 25
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = 20

    def move(self, direction):
        if direction == "UP":
            self.y -= self.speed
        elif direction == "DOWN":
            self.y += self.speed
        elif direction == "LEFT":
            self.x -= self.speed
        elif direction == "RIGHT":
            self.x += self.speed