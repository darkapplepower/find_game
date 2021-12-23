import os
from .button import Button
from .onclick import Click
import time
def loop(pygame, screen, size):
        running = True
        ret = None
        buttons = []
        path = os.path.dirname(os.path.abspath(__file__)) + '\\image\\'
        b_num = [0, 0, 0, 0, 0, 0, 0]
        def reset_callback():
                nonlocal b_num
                b_num = [0,0,0,0,0,0,0]
        def back_callback():
                nonlocal ret, running
                ret = 'selectstage'
                running = False
        reset = Button((48, 48), (48, 0), path + 'retry.png', reset_callback, pygame)
        buttons.append(reset)
        back = Button((48, 48), (0, 0), path+'back.png', back_callback, pygame)
        buttons.append(back)
        ci = 0
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
                        nonlocal b_num
                        b_num[ci] *= 10
                        b_num[ci] += i
                return a
        def backspace():
                nonlocal b_num, ci
                b_num[ci] = b_num[ci]//10
        def enter():
                if b_num == [19, 20, 1, 18, 20, 6, 28]:
                        stage_clear()
        b = []
        inp = path + 'bar.png'
        for j in range(7):
                b.append(Button((size[0]/15, size[0]/15), (10 + (size[0]/15 + 25) * j, size[1]/4*3), inp, b_getCallBack(j), pygame))
        buttons += b
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
                        buttons.append(Button((size[0]/10, size[0]/10), (size[0]/5*3 + 50 + (size[0]/10 + 10) * j, 10 + (size[0]/10 + 15) * jj), path + 'b_'+str(n)+'.png', ib_getCallBack(n), pygame))
        font = pygame.font.SysFont( "arial", 30)
        def stage_clear():
                nonlocal running, ret
                running = False
                ret = 'selectstage'
                door = pygame.image.load(path + 'door_open.png')
                door = pygame.transform.scale(door, (size[0]/3, size[1]/3*2))
                screen.blit(door, (0, 0))
                pygame.display.update()
                time.sleep(3)
                clear = pygame.image.load(path + 'clear.png')
                clear = pygame.transform.scale(clear, (size[0]/3*2, size[1]/2))
                screen.blit(clear, (size[0]/6, size[1]/4))
                pygame.display.update()
                time.sleep(3)
                clear = pygame.image.load(path + 's.png')
                clear = pygame.transform.scale(clear, (size[0]/3*2, size[1]/2))
                screen.blit(clear, (size[0]/6, size[1]/4))
                pygame.display.update()
                time.sleep(3)
        door = pygame.image.load(path + 'door_close.png')
        door = pygame.transform.scale(door, (size[0]/3, size[1]/3*2))
        while running:
                screen.fill((255, 255, 255))
                ev=pygame.event.get()
                screen.blit(door, (0, 0))
                for i in buttons:
                        screen.blit(i.image, i.xy)
                for j in range(7):
                        text = font.render(str(b_num[j]), True, (255, 255, 255))
                        screen.blit(text, (b[j].xy[0] + b[j].size[0]/2 - len(str(b_num[j]))*8, b[j].xy[1] + b[j].size[1]/2 - 15))
                for event in ev:
                        if event.type==pygame.MOUSEBUTTONUP and event.button==1:
                                Click.checkOnClick(buttons, pygame.mouse.get_pos())
                pygame.display.update()
        return ret