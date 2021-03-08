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
 
# 배경 이미지 불러오기
background = pygame.image.load(backgroundImgPath)

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가 
            running = False

    # 배경화면으로 추가
    screen.blit(background,(0,0))
    
    # 색상으로 추가 
    # screen.fill((0,0,255))

    pygame.display.update()

# 게임종료 
pygame.quit()