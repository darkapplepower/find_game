import sys
import pygame
import select

pygame.init()
#pygame 초기화

width, height = 960, 480
size = (width, height)
screen=pygame.display.set_mode(size)
#화면 크기 설정

nextstage="main"
#메인 루프에 필요한 변수들


nextstage=getattr(select, nextstage).loop()
#메인 루프