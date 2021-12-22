from .onclick import Click
from .button import Button
import os
import time
def loop(pygame, screen, size):
        path = os.path.dirname(os.path.abspath(__file__)) + '\\image\\'
        running = True
        ret = 'main'
        b_num = 0
        buttons = []
        sp_image =  pygame.image.load(path + 'phone_q.png')
        sp_image = pygame.transform.scale(sp_image, (size[0], size[1]))
        def showhint():
                screen.blit(sp_image, (0, 0))
                pygame.display.update()
                time.sleep(5)
        hint = Button((48, 48), (0, 0), path + 'hint.png', showhint, pygame)
        buttons.append(hint)
        def reset_callback():
                nonlocal b_num
                b_num = 0
        reset = Button((48, 48), (96, 0), path + 'retry.png', reset_callback, pygame)
        buttons.append(reset)
        def back_callback():
                nonlocal ret, running
                ret = 'selectstage'
                running = False
        back = Button((48, 48), (48, 0), path+'back.png', back_callback, pygame)
        buttons.append(back)
        def ib_getCallBack(i):
                nonlocal b_num, backspace, enter
                if i == 'backspace':
                        return backspace
                elif i == 'enter':
                        return enter
                def a():
                        nonlocal b_num
                        b_num *= 10
                        b_num += i
                return a
        def backspace():
                nonlocal b_num
                b_num = b_num//10
        def enter():
                nonlocal b_num
                if b_num == 28:
                        stage_clear()
        phone_image = pygame.image.load(path + 'phone.png')
        phone_image = pygame.transform.scale(phone_image, (size[0]/3, size[1]))

        answer = pygame.image.load(path + 'wtf 졸려 시발.png')
        answer = pygame.transform.scale(answer, (500, 300))
        def stage_clear():
                nonlocal running, ret
                running = False
                ret = 'selectstage'
                clear = pygame.image.load(path + 'clear.png')
                clear = pygame.transform.scale(clear, (size[0]/3*2, size[1]/2))
                screen.blit(clear, (size[0]/6, size[1]/4))
                pygame.display.update()
                time.sleep(3)
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
                        buttons.append(Button((size[0]/15, size[0]/15), (size[0]/3*2 + 55 + (size[0]/15 + 10) * j, 80 + (size[0]/15 + 15) * jj), path + 'b_'+str(n)+'.png', ib_getCallBack(n), pygame))
        font = pygame.font.SysFont( "arial", 50)
        while running:
                screen.fill((255, 255, 255))
                ev=pygame.event.get()
                for event in ev:
                        if event.type==pygame.MOUSEBUTTONUP and event.button==1:
                                Click.checkOnClick(buttons, pygame.mouse.get_pos())
                screen.blit(phone_image, (size[0]/3*2, 0))
                screen.blit(answer, (100, 100))
                text = font.render(str(b_num), True, (0, 0, 0))
                screen.blit(text, (350 - len(str(b_num)) * 13, 250))
                for i in buttons:
                        screen.blit(i.image, i.xy)
                pygame.display.update()
        return ret