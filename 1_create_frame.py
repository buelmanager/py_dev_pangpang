import pygame

pygame.init() # 초기화

# 화면크기 설정
screen_width = 480
screen_heigth = 640

pygame.display.set_mode((screen_width,screen_heigth))

# 화면타이틀 설정
pygame.display.set_caption("PangPang") # 게임이름 

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가 
            running = False

# 게임종료 
pygame.quit()