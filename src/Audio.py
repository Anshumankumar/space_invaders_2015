from pygame.mixer import Sound

class Audio():
    def __init__(self):
        self.fire = Sound('sounds/0.wav').play
        self.enemyFire = Sound('sounds/1.wav').play
        self.hit = Sound('sounds/2.wav').play
        self.playerHit = Sound('sounds/12.wav').play
        self.gameOver = Sound('sounds/9.wav').play

audio = Audio()
