import pygame
import os

pygame.init() # 초기화

# 화면크기 설정
screen_width = 480
screen_heigth = 640
screen = pygame.display.set_mode((screen_width,screen_heigth))

# 화면타이틀 설정
pygame.display.set_caption("PangPang") # 게임이름 

# image path
backgroundImgPath = "/Volumes/data/py/py_dev_pangpang/backgroun.jpg"
characterImgPath = "/Volumes/data/py/py_dev_pangpang/character.png" 

# 배경 이미지 불러오기
background = pygame.image.load(backgroundImgPath)

# 케릭터 불러오기 
character = pygame.image.load(characterImgPath)
character_size = character.get_rect().size 
character_width = character_size[0]
character_heigth = character_size[1]

character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_heigth - character_heigth

# 이동할 좌표
to_x = 0
to_y = 0

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():
 
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가 
            running = False

        elif event.type == pygame.KEYDOWN: # 키가 눌렸는지 
            if event.key == pygame.K_LEFT:
                to_x -= 5 
            elif event.key == pygame.K_RIGHT:
                to_x += 5 

            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5
        elif event.type == pygame.KEYUP:    # 키를 뗏을 때
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    # 가로세로 경계값 처리     
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_heigth - character_heigth:
        character_y_pos = screen_heigth - character_heigth


    # 배경화면으로 추가
    screen.blit(background,(0,0))

    # 케릭터 추가 
    screen.blit(character,(character_x_pos,character_y_pos))
    
    # 색상으로 추가 
    # screen.fill((0,0,255))

    pygame.display.update()

# 게임종료 
pygame.quit()