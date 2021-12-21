import os
from .button import Button
from .onclick import Click
import time
def loop(pygame, screen, size):
        def b_getCallBack(i):
                nonlocal ci
                def a():
                        nonlocal ci, i
                        ci = i
                return a
        def ib_getCallBack(i):
                nonlocal ci, b_num, backspace, enter
                if i == 'backspace':
                        return backspace
                elif i == 'enter':
                        return enter
                def a():
                        nonlocal ci, b_num
                        b_num[ci] *= 10
                        b_num[ci] += i
                return a
        def backspace():
                nonlocal ci, b_num
                b_num[ci] = b_num[ci]//10
        def enter():
                nonlocal b_num
                if b_num[0] == 19 and b_num[1] == 20 and b_num[2] == 1 and b_num[3] == 18 and b_num[4] == 20:
                        stage_clear()
        b_num = [0, 0, 0, 0, 0]
        ci = 0
        ret = None
        running = True
        path = os.path.dirname(os.path.abspath(__file__)) + '\\image\\'

        q = pygame.image.load(path + 'handle.png') #이미지 추가 필요
        q = pygame.transform.scale(q, (size[0]/5*3, size[1]/3*2))

        inp = path + 'bar.png' #변경 필요
        b = []

        for j in range(5):
                b.append(Button((size[0]/10, size[0]/10), (10 + (size[0]/10 + 25) * j, size[1]/4*3), inp, b_getCallBack(j), pygame))

        ib = []
        for j in range(3):
                for jj in range(4):
                        if jj == 3:
                                if j == 0:
                                        n = 'enter'
                                elif j == 1:
                                        n = 0
                                elif j == 2:
                                        n = 'backspace'
                        else:
                                n = jj*3 + j + 1
                        ib.append(Button((size[0]/10, size[0]/10), (size[0]/5*3 + 50 + (size[0]/10 + 10) * j, 10 + (size[0]/10 + 15) * jj), path + 'b_'+str(n)+'.png', ib_getCallBack(n), pygame))
        font = pygame.font.SysFont( "arial", 30)
        buttons = b + ib
        def stage_clear():
                nonlocal running, ret
                running = False
                ret = 'selectstage'
                clear = pygame.image.load(path + 'clear.png')
                clear = pygame.transform.scale(clear, (size[0]/3*2, size[1]/2))
                screen.blit(clear, (size[0]/6, size[1]/4))
                pygame.display.update()
                time.sleep(3)
        while running:
                ev=pygame.event.get()
                for event in ev:
                        if event.type==pygame.MOUSEBUTTONUP and event.button==1:
                                Click.checkOnClick(buttons, pygame.mouse.get_pos())
                screen.fill((255, 255, 255))
                for j in range(5):
                        screen.blit(b[j].image, b[j].xy)
                        text = font.render(str(b_num[j]), True, (255, 255, 255))
                        screen.blit(text, (b[j].xy[0] + b[j].size[0]/2 - len(str(b_num[j]))*8, b[j].xy[1] + b[j].size[1]/2 - 15))
                for j in ib:
                        screen.blit(j.image, j.xy)
                screen.blit(q, (10, 10))
                pygame.display.update()
        return ret