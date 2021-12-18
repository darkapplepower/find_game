from .onclick import Click
def loop(pygame, screen, size):
        import os
        ret = None
        running = True
        #종료 조건, 리턴값
        buttons = []
        #클릭 이벤트를 발생시킬 것들의 배열
        path=os.path.dirname(os.path.abspath(__file__))
        while running:
                ev=pygame.event.get()
                for event in ev:
                        if event.type==pygame.MOUSEBUTTONUP and event.button==1:
                                Click.checkOnClick(buttons, pygame.mouse.get_pos())
        return ret