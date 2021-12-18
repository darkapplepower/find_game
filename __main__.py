import stage.selectstage as selectstage
import pygame
pygame.init()
#pygame 초기화
width, height = 960, 480
size = (width, height)
screen = pygame.display.set_mode(size)
#화면 크기 설정

def clear():
        screen.fill((255, 255, 255))
        #화면 초기화 함수

nextstage = 'main'
#메인 루프에 필요한 변수들

while True:
        clear()
        #다음 화면을 위해 현재 화면 초기화

        nextstage = getattr(selectstage, nextstage).loop(pygame, screen, size)
        #모듈에서 화면 표시하게 하기
#메인 루프