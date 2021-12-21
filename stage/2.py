import os
from .button import Button
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
                nonlocal ci
                ci = (ci+1)%5
        b_num = [0, 0, 0, 0, 0]
        ci = 0
        ret = None
        running = True
        path = os.path.dirname(os.path.abspath(__file__)) + '\\image\\'

        q = pygame.image.load(path + 'handle.png') #이미지 추가 필요
        q = pygame.transform.scale(q, (size[0]/5*3, size[1]/3*2))

        inp = path + 'handle.png' #변경 필요
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
                        ib.append(Button((size[0]/10, size[0]/10), (10 + (size[0]/10 + 25) * j, size[1]/4*3), inp, ib_getCallBack(n), pygame))

        while running:
                screen.fill((255, 255, 255))
                for j in range(5):
                        screen.blit(b[j].image, b[j].xy)
                screen.blit(q, (10, 10))
                pygame.display.update()