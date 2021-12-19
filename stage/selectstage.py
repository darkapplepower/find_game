from .onclick import Click
from .button import Button
import os
path = os.path.dirname(os.path.abspath(__file__)) + '\\image\\'
#이미지 불러오기 위한 현재 폴더 위치
def makeLevelButton(pygame, screen, num, xy, size, onclick):
        global path
        button_path = path + 'stage_button_'+str(num)+'.png'
        button = Button(size, xy, button_path, onclick, pygame)
        screen.blit(button.image, button.xy)
        pygame.display.update()
        return button
def loop(pygame, screen, size):
        global path
        ret = None
        running = True
        #종료 조건, 리턴값
        buttons = []
        #클릭 이벤트를 발생시킬 것들의 배열
        def getOnClick(num):
                nonlocal ret, running
                def onclick():
                        nonlocal ret, running
                        ret = str(num)
                        running = False
                return onclick
        #
        stagebutton_size = (96, 96)
        stagebutton_margin = (48, 48)
        button_xy = [stagebutton_margin[0], stagebutton_margin[1]*2]
        for i in range(1, 4):
                button_onclick = getOnClick(i)
                b = makeLevelButton(pygame, screen, i, tuple(button_xy), stagebutton_size, button_onclick)
                buttons.append(b)
                button_xy[0] += stagebutton_margin[0] + stagebutton_size[0]
                if button_xy[0] > size[0]-stagebutton_margin[0]:
                        button_xy[0] = stagebutton_margin[0]
                        button_xy[1] += stagebutton_margin[1] + stagebutton_size[1]
        #스테이지 선택 버튼
        def back_callback():
                nonlocal ret, running
                ret = 'main'
                running = False
        back = Button((48, 48), (0, 0), path+'back.png', back_callback, pygame)
        buttons.append(back)
        screen.blit(back.image, back.xy)
        pygame.display.update()
        #메인으로 돌아가기 버튼
        while running:
                ev=pygame.event.get()
                for event in ev:
                        if event.type==pygame.MOUSEBUTTONUP and event.button==1:
                                Click.checkOnClick(buttons, pygame.mouse.get_pos())
        return ret