import os
import sys
from .onclick import Click
from .button import Button
def loop(pygame, screen, size):
        ret = None
        running = True
        #종료 조건, 리턴값
        buttons = []
        #클릭 이벤트를 발생시킬 것들의 배열
        path=os.path.dirname(os.path.abspath(__file__))
        def start_button_onclick():
                nonlocal ret, running
                ret = 'selectstage'
                running = False
        start_button = Button((size[0]/3, size[1]/4), (size[0]/3, size[1]/8*3), path+"\\image\\start_button.png", start_button_onclick, pygame)
        screen.blit(start_button.image, start_button.xy)
        buttons.append(start_button)

        pygame.display.flip()
        #변수 선언, 고정 오브젝트 설정 등
        

        while running:
                ev=pygame.event.get()
                for event in ev:
                        if event.type==pygame.MOUSEBUTTONUP and event.button==1:
                                Click.checkOnClick(buttons, pygame.mouse.get_pos())
        return ret