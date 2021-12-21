from .onclick import Click
from .button import Button
import os
import time
path = os.path.dirname(os.path.abspath(__file__)) + '\\image\\'
def loop(pygame, screen, size):
        running = True
        ret = False

        s = {}
        s['c'] = True
        def s_callback():
                nonlocal s
                s['c'] = not s['c']
        s['b'] = Button((96, 96), (192, 144), path + 'stage1_s.png', s_callback, pygame)

        i = {}
        i['c'] = True
        def i_callback():
                nonlocal i
                i['c'] = not i['c']
        i['b'] = Button((96, 96), (288, 144), path + 'stage1_i.png', i_callback, pygame)

        n1 = {}
        n1['c'] = True
        def n1_callback():
                nonlocal n1
                n1['c'] = not n1['c']
        n1['b'] = Button((96, 96), (384, 144), path + 'stage1_n.png', n1_callback, pygame)

        x = {}
        x['c'] = True
        def x_callback():
                nonlocal x
                x['c'] = not x['c']
        x['b'] = Button((96, 96), (576, 144), path + 'stage1_x.png', x_callback, pygame)

        bar = pygame.image.load(path + 'bar.png')
        bar = pygame.transform.scale(bar, (500, 20))
        bar_xy = (190, 288)

        n2 = {}
        n2['c'] = True
        def n2_callback():
                nonlocal n2
                n2['c'] = not n2['c']
        n2['b'] = Button((96, 96), (384, 336), path + 'stage1_n.png', n2_callback, pygame)

        def back_callback():
                nonlocal ret, running
                ret = 'selectstage'
                running = False
        back = Button((48, 48), (0, 0), path+'back.png', back_callback, pygame)

        def reset_callback():
                nonlocal s, i, n1, x, n2
                s['c'] = True
                i['c'] = True
                n1['c'] = True
                x['c'] = True
                n2['c'] = True
        reset = Button((48, 48), (912, 0), path + 'retry.png', reset_callback, pygame)
        objects = [s, i, n1, x, n2, {'b': back, 'c': 1}, {'b': reset, 'c': 1}]
        buttons = [s['b'], i['b'], n1['b'], x['b'], n2['b'], back, reset]
        
        def endgame():
                nonlocal running, ret, s, i, x
                running = False
                ret = 'selectstage'
                objects = [s, i, x]
                clear = pygame.image.load(path + 'clear.png')
                clear = pygame.transform.scale(clear, (size[0]/3*2, size[1]/2))
                screen.blit(clear, (size[0]/6, size[1]/4))
                pygame.display.update()
                time.sleep(3)
                for jj in range(0, 100):
                        screen.fill((255, 255, 255))
                        i['b'].move((0.6, 0))
                        x['b'].move((-0.6, 0))
                        for j in objects:
                                j['b'].resize(tuple(map(lambda a:a+0.5, j['b'].size)), pygame)
                                screen.blit(j['b'].image, j['b'].xy)
                        pygame.display.update()
                        time.sleep(0.03)
                time.sleep(3)
                screen.fill((255, 255, 255))
                six = pygame.image.load(path + 'stage1_6.png')
                six = pygame.transform.scale(six, (size[0]/3, size[1]/2))
                screen.blit(six, (size[0]/3, size[1]/4))
                pygame.display.update()
                time.sleep(3)

        while running:
                ev=pygame.event.get()
                for event in ev:
                        if event.type==pygame.MOUSEBUTTONUP and event.button==1:
                                Click.checkOnClick(buttons, pygame.mouse.get_pos())
                screen.fill((255, 255, 255))
                for j in objects:
                        screen.blit(j['b'].image, j['b'].xy)
                        if not j['c']:
                                pygame.draw.line(screen, (0, 0, 0), j['b'].xy, tuple(map((lambda a:a+96),j['b'].xy)), 10)
                screen.blit(bar, bar_xy)
                pygame.display.update()
                if s['c'] and i['c'] and not n1['c'] and x['c'] and not n2['c']:
                        endgame()

        return ret