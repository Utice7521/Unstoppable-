import sys
import pygame
import os
import time

# 파이게임 초기화
pygame.init()

# 배경화면 크기
background = pygame.display.set_mode((880, 800))  # 4/5 of the original size

# 파이게임 창 타이틀 설정
pygame.display.set_caption("Unstoppable!")

# FPS 설정
fps = pygame.time.Clock()

# !!!클래스 선언!!!

# 움직이는 배경 클래스
class backgroundanimation:
    def __init__(self, folder_path, size):
        self.images = []
        self.size = size
        self.load_images(folder_path)
        self.current_frame = 0
        self.total_frames = len(self.images)
        self.animation_speed = 0.1
        self.time_since_last_frame = 0

    def load_images(self, folder_path):
        for file_name in sorted(os.listdir(folder_path)):
            if file_name.endswith('png'):
                image_path = os.path.join(folder_path, file_name)
                image = pygame.image.load(image_path).convert_alpha()
                image = pygame.transform.scale(image, self.size)
                self.images.append(image)

    def update(self, dt):
        self.time_since_last_frame += dt
        if self.time_since_last_frame >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % self.total_frames
            self.time_since_last_frame = 0

    def get_current_image(self):
        return self.images[self.current_frame]

# 배경 클래스
class tileset:
    def __init__(self):
        self.images_temp = []
        self.images_temp.append(pygame.image.load('Asset/Background/0.png'))
        self.images_temp.append(pygame.image.load('Asset/Background/1.png'))
        self.images_temp.append(pygame.image.load('Asset/Background/2.png'))
        self.images_temp.append(pygame.image.load('Asset/Background/3.png'))
        self.images_temp.append(pygame.image.load('Asset/Background/4.png'))

        self.reduced_size = (80, 80)  # 4/5 of the original size
        self.images = []
        self.images.append(pygame.transform.scale(self.images_temp[0], self.reduced_size))
        self.images.append(pygame.transform.scale(self.images_temp[1], self.reduced_size))
        self.images.append(pygame.transform.scale(self.images_temp[2], self.reduced_size))
        self.images.append(pygame.transform.scale(self.images_temp[3], self.reduced_size))
        self.images.append(pygame.transform.scale(self.images_temp[4], self.reduced_size))

    def tileupdate(self, background):
        for x in range(11):  # adjusted range for 4/5 size
            for y in range(10):
                if map[y][x] == 0:
                    background.blit(self.images[0], (x * 80, y * 80))
                elif map[y][x] == 1:
                    background.blit(self.images[1], (x * 80, y * 80))
                elif map[y][x] == 2:
                    background.blit(self.images[2], (x * 80, y * 80))
                elif map[y][x] == 3:
                    background.blit(self.images[3], (x * 80, y * 80))
                elif map[y][x] == 4:
                    background.blit(self.images[4], (x * 80, y * 80))
        return 0

# 맵에 산출되는 정보 클래스
class inforset:
    def __init__(self):
        self.font = pygame.font.Font("Asset/Font/zekton free.ttf", 16)

    def update(self, position, text, data):
        self.string = [text, str(data)]
        self.text = self.font.render(' : '.join(self.string), True, (153, 255, 255))
        self.text_rect = self.text.get_rect(center=position)
        return self.text, self.text_rect

# 버튼 아이콘 클래스
class buttonicon(pygame.sprite.Sprite):
    def __init__(self, image_input, x, y, size):
        super().__init__()
        self.image_temp = image_input
        self.image = pygame.transform.scale(self.image_temp, size)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# 버튼 배치 클래스
class Buttons(pygame.sprite.Sprite):
    def __init__(self, x, y, id):
        super().__init__()
        self.images_temp = []
        self.images_temp.append(pygame.image.load('Asset/UI/Buttons/button_Idle.png'))
        self.images_temp.append(pygame.image.load('Asset/UI/Buttons/button_onmouse.png'))
        self.images_temp.append(pygame.image.load('Asset/UI/Buttons/button_active.png'))
        self.size = (80, 80)  # 4/5 of the original size
        self.images = []
        self.images.append(pygame.transform.scale(self.images_temp[0], self.size))
        self.images.append(pygame.transform.scale(self.images_temp[1], self.size))
        self.images.append(pygame.transform.scale(self.images_temp[2], self.size))
        self.index = 0
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.ID = id
        self.click = False

    def buttonupdate(self, event):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_x, mouse_y):
            if event.type == pygame.MOUSEBUTTONDOWN and not self.click:
                self.index = 2
                self.click = True
                if self.ID == 2:
                    # Shot()
                    gamemanager.mouse_status = 0
                elif self.ID == 3:
                    # IDLE()
                    gamemanager.mouse_status = 1
                elif self.ID == 4:
                    if gamemanager.token >= 200:
                        gamemanager.mouse_status = 2
                elif self.ID == 5:
                    if gamemanager.token >= 300:
                        gamemanager.mouse_status = 3
                elif self.ID == 6:
                    if gamemanager.token >= 100:
                        gamemanager.mouse_status = 4
                    # construct(ID)
                elif self.ID == 7:
                    if gamemanager.token >= 100 * (gamemanager.upgrade1 + 1):
                        gamemanager.token -= 100 * (gamemanager.upgrade1 + 1)
                        gamemanager.upgrade1 += 1
                elif self.ID == 8:
                    if gamemanager.token >= 100 * (gamemanager.upgrade2 + 1):
                        gamemanager.token -= 100 * (gamemanager.upgrade2 + 1)
                        gamemanager.upgrade2 += 1
                elif self.ID == 9:
                    if gamemanager.token >= 100 * (gamemanager.upgrade3 + 1):
                        gamemanager.token -= 100 * (gamemanager.upgrade3 + 1)
                        gamemanager.upgrade3 += 1
            elif event.type == pygame.MOUSEBUTTONUP:
                self.click = False
            else:
                self.index = 1
        else:
            self.index = 0
        self.image = self.images[self.index]

# 타워 클래스
class tower1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.angle = 0
        self.animation = []
        self.image = pygame.transform.scale(pygame.image.load("Asset/Tower/tower1/Shooting/frame_0000.png"), (440, 120))  # 4/5 of the original size
        self.damage = 100
        self.speed = 1 / 3
        self.range = 320  # 4/5 of the original size
        for file_name in sorted(os.listdir("Asset/Tower/tower1/Shooting")):
            if file_name.endswith('.png'):
                image_path = os.path.join('Asset/Tower/tower1/Shooting', file_name)
                image_temp = pygame.image.load(image_path).convert_alpha()
                image = pygame.transform.scale(image_temp, (440, 120))  # 4/5 of the original size
                self.animation.append(image)
        self.rect = self.image.get_rect()
        self.rect.center = (x + 40, y + 40)  # 4/5 of the original size
        self.last_attack_time = time.time()
        self.animation_speed = 0.1
        self.total_frame = len(self.animation)
        self.x = x + 40  # 4/5 of the original size
        self.y = y + 40  # 4/5 of the original size
        self.target = None
        self.position = pygame.math.Vector2((self.x, self.y))
        self.current_angle = 0
        self.rotation_speed = 30
        self.target_found = False
        self.time_since_last_frame = 0
        self.shooting = False
        self.current_frame = 0
        self.effect = pygame.mixer.Sound("Asset/Sound/Effect/Shoot/Tower1.mp3")
        self.effect.set_volume(0.5)

    def update(self, monsters, bullet, dt):
        self.time_since_last_frame += dt

        for monster in monsters:
            distance = ((monster.rect.centerx - self.rect.centerx) ** 2 + (monster.rect.centery - self.rect.centery) ** 2) ** 0.5
            if distance <= self.range:
                self.target = monster
                self.target_found = True
                self.shooting = True
                direction = pygame.math.Vector2(self.target.rect.center) - self.position
                self.current_angle = direction.angle_to(pygame.math.Vector2(1, 0))
                break

        if self.time_since_last_frame >= self.animation_speed:
            self.time_since_last_frame = 0
            if self.shooting:
                self.current_frame = (self.current_frame + 1) % self.total_frame
            if self.current_frame == 1 and self.shooting:
                self.effect.play()
                new_bullet = Bullet(self.rect.centerx, self.rect.centery, self.target, self.damage + gamemanager.upgrade1 * 30,
                                    pygame.transform.scale(pygame.image.load("Asset/Bullet/Bullet2.png"), (60, 60)), 20)  # 4/5 of the original size
                bullet.add(new_bullet)

        if not self.target_found:
            self.current_angle += self.rotation_speed * dt
            if self.current_angle >= 360:
                self.current_angle -= 360
            self.shooting = False

        self.image = pygame.transform.rotate(self.animation[self.current_frame], self.current_angle - 90)
        self.rect = self.image.get_rect(center=self.position)
        if not self.shooting:
            self.current_frame = 0

    def get_current_image(self):
        return self.animation[self.current_frame]

class tower2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animation = []
        self.image = pygame.transform.scale(pygame.image.load("Asset/Tower/tower2/newIdle/frame_0000.png"), (320, 120))  # 4/5 of the original size
        self.damage = 2
        self.speed = 0.5
        self.range = 160  # 4/5 of the original size
        self.x = x
        self.y = y
        for file_name in sorted(os.listdir("Asset/Tower/tower2/newIdle")):
            if file_name.endswith('.png'):
                image_path = os.path.join('Asset/Tower/tower2/newIdle', file_name)
                image_temp = pygame.image.load(image_path).convert_alpha()
                image = pygame.transform.scale(image_temp, (440, 120))  # 4/5 of the original size
                self.animation.append(image)
        self.rect = self.image.get_rect()
        self.rect.center = (x + 40, y + 40)  # 4/5 of the original size
        self.current_frame = 0
        self.total_frames = len(self.animation)
        self.animation_spped = 0.05
        self.time_since_last_frame = 0
        self.target = None
        self.lazer = None

    def update(self, monsters, lazer_group, dt):
        self.time_since_last_frame += dt
        if self.time_since_last_frame >= self.animation_spped:
            self.current_frame = (self.current_frame + 1) % self.total_frames
            self.time_since_last_frame = 0
            self.image = self.animation[self.current_frame]
            self.rect = self.image.get_rect()
            self.rect.center = (self.x + 40, self.y + 40)  # 4/5 of the original size

        # 타겟이 없거나 처치된 경우 새로운 타겟을 찾습니다.
        if not self.target or not self.target.alive():
            self.target = None
            if self.lazer:
                self.lazer.kill()
                self.lazer = None
            for monster in monsters:
                distance = ((monster.rect.centerx - self.rect.centerx) ** 2 + (monster.rect.centery - self.rect.centery) ** 2) ** 0.5
                if distance <= self.range:
                    self.target = monster
                    self.lazer = Lazer(self, self.target)
                    lazer_group.add(self.lazer)
                    break

        if self.lazer:
            self.lazer.update(dt)

    def get_current_image(self):
        return self.images[self.current_frame]

class tower3(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animation = []
        self.image = pygame.transform.scale(pygame.image.load("Asset/Tower/tower3/shooting/frame_0000.png"), (400, 100))  # 4/5 of the original size
        self.damage = 10
        self.speed = 3
        self.range = 200  # 4/5 of the original size
        for file_name in sorted(os.listdir("Asset/Tower/tower3/Shooting")):
            if file_name.endswith('.png'):
                image_path = os.path.join('Asset/Tower/tower3/Shooting', file_name)
                image_temp = pygame.image.load(image_path).convert_alpha()
                image = pygame.transform.scale(image_temp, (440, 120))  # 4/5 of the original size
                self.animation.append(image)
        self.x = x + 40  # 4/5 of the original size
        self.y = y + 40  # 4/5 of the original size
        self.rect = self.image.get_rect()
        self.rect.center = (x + 40, y + 40)  # 4/5 of the original size
        self.position = pygame.math.Vector2((self.x, self.y))
        self.current_angle = 0
        self.rotation_speed = 30
        self.target_found = False
        self.time_since_last_frame = 0
        self.shooting = False
        self.current_frame = 0
        self.animation_speed = 0
        self.total_frame = len(self.animation)
        self.effect = pygame.mixer.Sound("Asset/Sound/Effect/Shoot/Tower3.mp3")
        self.effect.set_volume(0.3)

    def update(self, monsters, bullet, dt):
        self.time_since_last_frame += dt

        for monster in monsters:
            distance = ((monster.rect.centerx - self.rect.centerx) ** 2 + (monster.rect.centery - self.rect.centery) ** 2) ** 0.5
            if distance <= self.range:
                self.target = monster
                self.target_found = True
                self.shooting = True
                direction = pygame.math.Vector2(self.target.rect.center) - self.position
                self.current_angle = direction.angle_to(pygame.math.Vector2(1, 0))
                break

        if self.time_since_last_frame >= self.animation_speed:
            self.time_since_last_frame = 0
            if self.shooting:
                self.current_frame = (self.current_frame + 1) % self.total_frame
            if self.current_frame == 1 and self.shooting:
                self.effect.play()
                new_bullet = Bullet(self.rect.centerx, self.rect.centery, self.target, self.damage + (gamemanager.upgrade3 * 5),
                                    pygame.transform.scale(pygame.image.load("Asset/Bullet/Bullet1.png"), (24, 24)), 40)  # 4/5 of the original size
                bullet.add(new_bullet)

        if not self.target_found:
            self.current_angle += self.rotation_speed * dt
            if self.current_angle >= 360:
                self.current_angle -= 360
            self.shooting = False

        self.image = pygame.transform.rotate(self.animation[self.current_frame], self.current_angle - 90)
        self.rect = self.image.get_rect(center=self.position)
        if not self.shooting:
            self.current_frame = 0

class towerbase(pygame.sprite.Sprite):
    def __init__(self, x, y, code):
        super().__init__()
        if code == 1:
            self.image = pygame.transform.scale(pygame.image.load("Asset/Tower/tower1/Idle/Idlebase.png"), (560, 120))  # 4/5 of the original size
            self.rect = self.image.get_rect()
            self.rect.center = (x + 40, y + 28)  # 4/5 of the original size
        elif code == 3:
            self.image = pygame.transform.scale(pygame.image.load("Asset/Tower/tower3/Idle/Idlebase.png"), (400, 108))  # 4/5 of the original size
            self.rect = self.image.get_rect()
            self.rect.center = (x + 40, y + 16)  # 4/5 of the original size
        else:
            return 0

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, target, damage, image_temp, speed):
        super().__init__()
        self.image = image_temp
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.target = target
        self.damage = damage
        self.speed = speed

    def update(self, dt):
        self.x = self.rect.centerx
        self.y = self.rect.centery
        self.position = pygame.math.Vector2((self.x, self.y))
        if self.target:
            dx, dy = self.target.rect.centerx - self.rect.centerx, self.target.rect.centery - self.rect.centery
            dist = (dx ** 2 + dy ** 2) ** 0.5
            if dist < self.speed:
                self.target.getdamage(self.damage)
                self.kill()
            else:
                self.rect.x += self.speed * dx / dist
                self.rect.y += self.speed * dy / dist
        else:
            self.kill()

class Lazer(pygame.sprite.Sprite):
    def __init__(self, tower, target):
        super().__init__()
        self.tower = tower
        self.target = target
        self.image_temp = pygame.image.load("Asset/Bullet/Lazer.png").convert_alpha()
        self.image = self.image_temp
        self.rect = self.image.get_rect()
        self.damage = 0.1
        self.growth_rate = 1
        self.effect = pygame.mixer.Sound("Asset/Sound/Effect/Shoot/Tower2.mp3")
        self.effect.set_volume(0.2)
        self.sound_playing = False

    def update(self, dt):
        if self.target and self.target.alive():
            self.damage += (self.growth_rate + 0.2 * gamemanager.upgrade2) * dt
            self.target.getdamage(self.damage)

            tower_pos = self.tower.rect.center
            target_pos = self.target.rect.center

            dx = target_pos[0] - tower_pos[0]
            dy = target_pos[1] - tower_pos[1]
            distance = (dx ** 2 + dy ** 2) ** 0.5

            if distance != 0:
                angle = 180 * dy / distance
                if dx < 0:
                    angle = 180 - angle
            self.image = pygame.transform.scale(self.image_temp, (int(distance), self.image_temp.get_height()))
            self.image = pygame.transform.rotate(self.image, -angle - 90)
            self.rect = self.image.get_rect(center=((tower_pos[0] + target_pos[0]) // 2, (tower_pos[1] + target_pos[1]) // 2))

            if not self.sound_playing:
                self.effect.play()
                self.sound_playing = True

        else:
            if self.sound_playing:
                self.effect.stop()
                self.sound_playing = False
            self.kill()

# 마우스 커서 클래스
class cursor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_temp = []
        self.image = []
        self.image_temp.append(pygame.image.load("Asset/UI/cursors/cursor_shot.png"))
        self.image_temp.append(pygame.image.load("Asset/UI/cursors/cursor_Idle.png"))
        self.image_temp.append(pygame.image.load("Asset/UI/cursors/build_tower1.png"))
        self.image_temp.append(pygame.image.load("Asset/UI/cursors/build_tower2.png"))
        self.image_temp.append(pygame.image.load("Asset/UI/cursors/build_tower3.png"))

        self.reduced_size = (51, 51)  # 4/5 of the original size
        for i in range(5):
            self.image.append(pygame.transform.scale(self.image_temp[i], self.reduced_size))

    def cursorupdate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.image_out = self.image[gamemanager.mouse_status]
        if gamemanager.mouse_status == 0:
            background.blit(self.image_out, (mouse_x - 24, mouse_y - 24))  # 4/5 of the original size
        elif gamemanager.mouse_status == 1:
            background.blit(self.image_out, (mouse_x - 8, mouse_y - 8))  # 4/5 of the original size
        elif gamemanager.mouse_status == 2:
            self.image_out = pygame.transform.scale(self.image_out, (80, 80))  # 4/5 of the original size
            background.blit(self.image_out, (mouse_x - 24, mouse_y - 24))  # 4/5 of the original size
        elif gamemanager.mouse_status == 3:
            self.image_out = pygame.transform.scale(self.image_out, (80, 80))  # 4/5 of the original size
            background.blit(self.image_out, (mouse_x - 24, mouse_y - 24))  # 4/5 of the original size
        elif gamemanager.mouse_status == 4:
            self.image_out = pygame.transform.scale(self.image_out, (80, 80))  # 4/5 of the original size
            background.blit(self.image_out, (mouse_x - 24, mouse_y - 24))  # 4/5 of the original size

# 몬스터 생성기 클래스
class Monster_generator:
    def __init__(self):
        self.spawn_time = time.time()
        self.spawn_interval = 2

    def update(self, monster_group):
        current_time = time.time()
        if current_time - self.spawn_time >= self.spawn_interval:
            self.spawn_time = current_time
            new_monster = Monster(gamemanager.wave * 150, Speed=1.5 + (gamemanager.wave * 0.5))
            new_monster.rect = pygame.transform.scale(pygame.image.load("Asset/Monster/Monster1/P112 Animation-Walk_0.png"), (80, 80)).get_rect()  # 4/5 of the original size
            monster_group.add(new_monster)

# 몬스터 클래스
class Monster(pygame.sprite.Sprite):
    def __init__(self, HP, Speed):
        super().__init__()
        self.health = HP
        self.speed = Speed
        self.image = pygame.transform.scale(pygame.image.load("Asset/Monster/Monster1/P112 Animation-Walk_0.png"), (80, 80))  # 4/5 of the original size
        self.animation = []
        self.animation_speed = 0.1
        self.time_since_last_frame = 0
        self.current_frame = 0
        self.max_health = HP
        self.dead = False
        for file_name in sorted(os.listdir("Asset/Monster/Monster1"), key=lambda x: int(x.split('_')[-1].split('.')[0])):
            if file_name.endswith('png'):
                image_path = os.path.join("Asset/Monster/Monster1", file_name)
                image_temp = pygame.image.load(image_path).convert_alpha()
                image = pygame.transform.scale(image_temp, (80, 80))  # 4/5 of the original size
                self.animation.append(image)
            self.rect = self.image.get_rect()
            self.rect.topleft = (0, 0)
            self.path_index = 0
        self.total_frames = len(self.animation)
        self.flip = False

    def update(self, dt):
        if self.path_index < len(path):
            target_x, target_y = path[self.path_index]
            dx = target_x - self.rect.x
            dy = target_y - self.rect.y
            dist = (dx ** 2 + dy ** 2) ** 0.5
            if dist < self.speed:
                self.rect.x, self.rect.y = target_x, target_y
                self.path_index += 1
            else:
                self.rect.x += self.speed * dx / dist
                self.rect.y += self.speed * dy / dist
        else:
            gamemanager.health -= 1
            self.kill()
        self.time_since_last_frame += dt
        if self.time_since_last_frame >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % self.total_frames
            self.time_since_last_frame = 0
            if self.path_index >= 1 and self.path_index <= 6:
                self.image = pygame.transform.flip(self.animation[self.current_frame], True, False)
                self.flip = True
            else:
                self.image = self.animation[self.current_frame]
                self.flip = False

    def getdamage(self, damage):
        if self.health <= damage:
            if not self.dead:
                self.dead = True
                dead = deadbody(self.rect.x, self.rect.y, self.flip)
                gamemanager.deadbody_group.add(dead)
                gamemanager.token += int(20 + (gamemanager.wave * 10))
                self.kill()
            if self.dead:
                return 0
        self.health -= damage

    def health_bar(self):
        bar_length = 40  # 4/5 of the original size
        bar_height = 4  # 4/5 of the original size
        health_ratio = self.health / self.max_health
        health_bar_length = bar_length * health_ratio
        background_bar = pygame.Rect(self.rect.centerx - bar_length // 2, self.rect.top - 8, bar_length, bar_height)  # 4/5 of the original size
        pygame.draw.rect(background, (0, 0, 0), background_bar)
        health_bar = pygame.Rect(self.rect.centerx - bar_length // 2, self.rect.top - 8, health_bar_length, bar_height)  # 4/5 of the original size
        pygame.draw.rect(background, (255, 0, 0), health_bar)

# 몬스터 시체 출력
class deadbody(pygame.sprite.Sprite):
    def __init__(self, x, y, flip):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("Asset/Monster/Monster1_Dead/P112 Animation-Dead_0.png"), (80, 80))  # 4/5 of the original size
        self.animation = []
        for file_name in sorted(os.listdir("Asset/Monster/Monster1_Dead"), key=lambda x: int(x.split('_')[-1].split('.')[0])):
            if file_name.endswith('png'):
                image_path = os.path.join("Asset/Monster/Monster1_Dead", file_name)
                image_temp = pygame.image.load(image_path).convert_alpha()
                image = pygame.transform.scale(image_temp, (80, 80))  # 4/5 of the original size
                self.animation.append(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.time_since_last_frame = 0
        self.current_frame = 0
        self.animation_speed = 0.05
        self.total_frames = len(self.animation)
        self.flip = flip
        self.sound = pygame.mixer.Sound("Asset/Sound/Effect/Monster Die/Dead.mp3")
        self.sound.set_volume(0.7)
        self.sound.play()

    def update(self, dt):
        self.time_since_last_frame += dt
        if self.time_since_last_frame >= self.animation_speed:
            self.current_frame += 1
            if self.current_frame >= self.total_frames:
                self.kill()
            else:
                self.time_since_last_frame = 0
                if self.flip:
                    self.image = pygame.transform.flip(self.animation[self.current_frame], True, False)
                else:
                    self.image = self.animation[self.current_frame]

# 게임 매니저 클래스
class Gamemanager:
    def __init__(self):
        self.health = 3
        self.token = 400
        self.wave = 1
        # 0 Shot, 1 Idle, 2 tower1, 3 tower2, 4 tower3
        self.mouse_status = 1
        self.tower_group = pygame.sprite.Group()
        self.tower_group2 = pygame.sprite.Group()
        self.towerbase_group = pygame.sprite.Group()
        self.monster_group = pygame.sprite.Group()
        self.Bullet_group = pygame.sprite.Group()
        self.deadbody_group = pygame.sprite.Group()
        self.lazer_group = pygame.sprite.Group()
        self.spawner = Monster_generator()
        self.waveinfo = inforset()
        self.tokeninfo = inforset()
        self.healthinfo = inforset()
        self.upgrade1info = inforset()
        self.upgrade2info = inforset()
        self.upgrade3info = inforset()
        self.click_delay = 100
        self.last_click_time = 0
        self.shootsound = pygame.mixer.Sound("Asset/Sound/Effect/Shoot.mp3")
        self.shootsound.set_volume(0.2)
        self.start_time = time.time()
        self.upgrade1 = 0
        self.upgrade2 = 0
        self.upgrade3 = 0

    def construct(self, x, y):
        if self.mouse_status == 2:
            if gamemanager.token >= 200:
                new_tower = tower1(x, y)
                new_towerbase = towerbase(x, y, 1)
                gamemanager.token -= 200
                map[y // 80][x // 80] = 2  # 4/5 of the original size
                self.towerbase_group.add(new_towerbase)
                self.tower_group.add(new_tower)
            else:
                return 0
        elif self.mouse_status == 3:
            if gamemanager.token >= 300:
                new_tower = tower2(x, y)
                gamemanager.token -= 300
                map[y // 80][x // 80] = 2  # 4/5 of the original size
                self.tower_group2.add(new_tower)
            else:
                return 0
        elif self.mouse_status == 4:
            if gamemanager.token >= 100:
                new_tower = tower3(x, y)
                new_towerbase = towerbase(x, y, 3)
                gamemanager.token -= 100
                map[y // 80][x // 80] = 2  # 4/5 of the original size
                self.towerbase_group.add(new_towerbase)
                self.tower_group.add(new_tower)
            else:
                return 0
        else:
            return 0
        self.tower_group.add(new_tower)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_click_time >= self.click_delay:
                self.last_click_time = current_time
                x, y = pygame.mouse.get_pos()
                map_x = x // 80  # 4/5 of the original size
                map_y = y // 80  # 4/5 of the original size
                if map_x < 11 and map_y < 10:
                    try:
                        if map[map_y][map_x] == 1:
                            self.construct(map_x * 80, map_y * 80)  # 4/5 of the original size
                    except:
                        pass
                for monster in self.monster_group:
                    if monster.rect.collidepoint((x, y)):
                        self.shootsound.play()
                        monster.getdamage(gamemanager.wave * 10)
        return 0

    def update(self, dt):
        current_time = time.time()
        if current_time - self.start_time >= 30:
            self.wave += 1
            self.start_time = current_time
            if self.spawner.spawn_interval >= 0.8:
                self.spawner.spawn_interval -= 0.15

        self.tower_group.update(self.monster_group, self.Bullet_group, dt)
        self.spawner.update(self.monster_group)
        self.monster_group.update(dt)
        self.Bullet_group.update(dt)
        self.lazer_group.update(dt)
        self.waveinfo.update((840, 24), "wave", self.wave)  # 4/5 of the original size
        self.tokeninfo.update((840, 40), "token", self.token)  # 4/5 of the original size
        self.healthinfo.update((840, 56), "HP", self.health)  # 4/5 of the original size
        self.upgrade1info.update((840, 560), "LV", self.upgrade1)  # 4/5 of the original size
        self.upgrade2info.update((840, 640), "LV", self.upgrade2)  # 4/5 of the original size
        self.upgrade3info.update((840, 720), "LV", self.upgrade3)  # 4/5 of the original size
        if self.health <= 0:
            pygame.quit()
            sys.exit()

# 마우스 커서 숨기기
pygame.mouse.set_visible(False)

### 주요 객체 선언
# 0은 길
# 1은 언덕
# 2는 타워
# 3은 몬스터 나오는 곳
# 4는 몬스터 들어가는 곳
map = [
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 0]
]

# 몬스터의 경로
path = [
    (720, 0), (720, 160), (400, 160), (400, 480), (240, 480), (240, 160), (80, 160), (80, 640), (560, 640),
    (560, 320), (720, 320), (720, 720)
]

# 배경음악
pygame.mixer.init()
pygame.mixer.music.load("Asset/Sound/Music/Background3.mp3")
pygame.mixer_music.play(-1)

map_rect = []
for y in range(10):
    map_rect_temp = []
    for x in range(11):
        map_rect_temp.append((x * 80, y * 80))  # 4/5 of the original size
    map_rect.append(map_rect_temp)

gamemanager = Gamemanager()
tile = tileset()
cursor1 = cursor()
play = True
button_Shot = Buttons(800, 160, 2)  # 4/5 of the original size
button_Idle = Buttons(800, 240, 3)  # 4/5 of the original size
button_Construct1 = Buttons(800, 320, 4)  # 4/5 of the original size
button_Construct2 = Buttons(800, 400, 5)  # 4/5 of the original size
button_Construct3 = Buttons(800, 480, 6)  # 4/5 of the original size
button_Upgrade1 = Buttons(800, 560, 7)  # 4/5 of the original size
button_Upgrade2 = Buttons(800, 640, 8)  # 4/5 of the original size
button_Upgrade3 = Buttons(800, 720, 9)  # 4/5 of the original size
Button_sprites = pygame.sprite.Group()

Button_sprites.add(button_Shot)
Button_sprites.add(button_Idle)
Button_sprites.add(button_Construct1)
Button_sprites.add(button_Construct2)
Button_sprites.add(button_Construct3)
Button_sprites.add(button_Upgrade1)
Button_sprites.add(button_Upgrade2)
Button_sprites.add(button_Upgrade3)

icon_shoot = buttonicon(pygame.image.load("Asset/UI/icon/icon.png"), button_Shot.rect.x + 40 - 36, button_Shot.rect.y + 12, (72, 56))  # 4/5 of the original size
icon_Idle = buttonicon(pygame.image.load("Asset/UI/icon/cursor_Idle.png"), button_Idle.rect.x + 12, button_Idle.rect.y + 12, (56, 56))  # 4/5 of the original size
icon_Construct1 = buttonicon(pygame.image.load("Asset/UI/icon/build_tower1.png"), button_Construct1.rect.x, button_Construct1.rect.y, (80, 80))  # 4/5 of the original size
icon_Construct2 = buttonicon(pygame.image.load("Asset/UI/icon/build_tower2.png"), button_Construct2.rect.x, button_Construct2.rect.y, (80, 80))  # 4/5 of the original size
icon_Construct3 = buttonicon(pygame.image.load("Asset/UI/icon/build_tower3.png"), button_Construct3.rect.x, button_Construct3.rect.y, (80, 80))  # 4/5 of the original size
icon_Upgrade1 = buttonicon(pygame.image.load("Asset/UI/icon/upgrade_tower1.png"), button_Upgrade1.rect.x - 20, button_Upgrade1.rect.y - 16, (120, 120))  # 4/5 of the original size
icon_Upgrade2 = buttonicon(pygame.image.load("Asset/UI/icon/upgrade_tower2.png"), button_Upgrade2.rect.x + 4, button_Upgrade2.rect.y, (80, 80))  # 4/5 of the original size
icon_Upgrade3 = buttonicon(pygame.image.load("Asset/UI/icon/upgrade_tower3.png"), button_Upgrade3.rect.x, button_Upgrade3.rect.y, (80, 80))  # 4/5 of the original size

icon_sprites = pygame.sprite.Group()

icon_sprites.add(icon_shoot)
icon_sprites.add(icon_Idle)
icon_sprites.add(icon_Construct1)
icon_sprites.add(icon_Construct2)
icon_sprites.add(icon_Construct3)
icon_sprites.add(icon_Upgrade1)
icon_sprites.add(icon_Upgrade2)
icon_sprites.add(icon_Upgrade3)

monster_start = backgroundanimation("Asset/Background/3 animation", (240, 80))  # 4/5 of the original size
monster_end = backgroundanimation("Asset/Background/4 animation", (240, 80))  # 4/5 of the original size

while play:
    dt = fps.tick(30) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    # 이벤트 처리
    button_Shot.buttonupdate(event)
    button_Idle.buttonupdate(event)
    button_Construct1.buttonupdate(event)
    button_Construct2.buttonupdate(event)
    button_Construct3.buttonupdate(event)
    button_Upgrade1.buttonupdate(event)
    button_Upgrade2.buttonupdate(event)
    button_Upgrade3.buttonupdate(event)
    gamemanager.handle_event(event)

    # 애니메이션 업데이트
    monster_start.update(dt)
    monster_start_current_image = monster_start.get_current_image()
    monster_end.update(dt)
    monster_end_current_image = monster_end.get_current_image()

    # 몬스터 애니메이션 업데이트
    gamemanager.update(dt)

    # 몬스터 시체 업데이트
    gamemanager.deadbody_group.update(dt)

    # 화면 출력 처리
    background.fill((0, 0, 0))
    tile.tileupdate(background)
    background.blit(monster_start_current_image, (-80, 0))  # 4/5 of the original size
    background.blit(monster_end_current_image, (640, 720))  # 4/5 of the original size
    Button_sprites.draw(background)
    gamemanager.deadbody_group.draw(background)
    gamemanager.monster_group.draw(background)
    gamemanager.towerbase_group.draw(background)
    gamemanager.tower_group.draw(background)
    gamemanager.tower_group2.draw(background)
    gamemanager.Bullet_group.draw(background)
    icon_sprites.draw(background)
    cursor1.cursorupdate()
    for monster in gamemanager.monster_group:
        monster.health_bar()
    wave_text, wave_rect = gamemanager.waveinfo.update((840, 24), "wave", gamemanager.wave)  # 4/5 of the original size
    token_text, token_rect = gamemanager.tokeninfo.update((840, 40), "token", gamemanager.token)  # 4/5 of the original size
    health_text, health_rect = gamemanager.healthinfo.update((840, 56), "HP", gamemanager.health)  # 4/5 of the original size
    upgrade1_text, upgrade1_rect = gamemanager.upgrade1info.update((840, 560), "Lv", gamemanager.upgrade1)  # 4/5 of the original size
    upgrade2_text, upgrade2_rect = gamemanager.upgrade2info.update((840, 640), "Lv", gamemanager.upgrade2)  # 4/5 of the original size
    upgrade3_text, upgrade3_rect = gamemanager.upgrade3info.update((840, 720), "Lv", gamemanager.upgrade3)  # 4/5 of the original size
    background.blit(wave_text, wave_rect)
    background.blit(token_text, token_rect)
    background.blit(health_text, health_rect)
    background.blit(upgrade1_text, upgrade1_rect)
    background.blit(upgrade2_text, upgrade2_rect)
    background.blit(upgrade3_text, upgrade3_rect)

    pygame.display.flip()
