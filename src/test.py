import unittest
import pygame
import time 
from sprites import *

pygame.init()
size = width, height = 600, 400

class TestPlayer(unittest.TestCase):
    key = []
    def test_left(self):
        screen = pygame.display.set_mode(size)
        for i in range(1,1000):
            self.key.append(False)
        playerShip = PlayerShip([320,350])
        self.key[pygame.K_LEFT] = True
        playerShip.update(self.key)
        self.assertTrue(playerShip.rect.x,312)

    def test_right(self):
        self.key[pygame.K_LEFT] = False
        self.key[pygame.K_RIGHT] = True
        playerShip = PlayerShip([320,350])
        playerShip.update(self.key)
        playerShip.update(self.key)
        playerShip.update(self.key)
        self.assertTrue(playerShip.rect.x,344)


class TestBullet(unittest.TestCase):
    def test_up(self):
        screen = pygame.display.set_mode(size)
        bullet = Bullet([320,350],"UP")
        bullet.run()
        self.assertLess(bullet.rect.x,350)

    def test_down(self):
        screen = pygame.display.set_mode(size)
        bullet = Bullet([320,100],"DOWN")
        bullet.run()
        self.assertGreater(bullet.rect.x,100)

class TestEnemy(unittest.TestCase):
    def test_direction(self):
        screen = pygame.display.set_mode(size)
        enemy = Enemy([20,10],[320,350],2)
        self.assertEqual(enemy._direction,"RIGHT")
        enemy.updateDirection("LEFT")
        self.assertEqual(enemy._direction,"LEFT")


    def test_checkposX(self):
        screen = pygame.display.set_mode(size)
        enemy = Enemy([20,10],[320,350],2)
        self.assertEqual(enemy.checkposX(),0)
        enemy = Enemy([20,10],[39,350],2)
        self.assertEqual(enemy.checkposX(),1)
        enemy = Enemy([20,10],[541,350],2)
        self.assertEqual(enemy.checkposX(),-1)

    def test_update_right(self):
        screen = pygame.display.set_mode(size)
        enemy = Enemy([20,10],[320,350],2)
        enemy.update()
        self.assertEqual(enemy.rect.x,318)

    def test_update_left(self):
        screen = pygame.display.set_mode(size)
        enemy = Enemy([20,10],[320,350],2)
        enemy.updateDirection("LEFT")
        enemy.update()
        self.assertEqual(enemy.rect.x,322)
 
    def test_moveDown(self):
        screen = pygame.display.set_mode(size)
        enemy = Enemy([20,10],[320,350],2)
        enemy.enemyFlag = 1
        enemy.moveDown()
        self.assertEqual(enemy.rect.y,370)

if __name__ == '__main__':
    unittest.main()
