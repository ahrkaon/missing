
define dialogue = ""
define dialogue_list = ["마키씨, 마키씨", "아아 배고파요"]

screen speech:
    $ dialogue = renpy.random.choice(dialogue_list)

    frame:
        text "[dialogue]"
        align (.9, .9)
    timer 3.0 action Hide("speech")
screen manager: 
    add "images/bg room.jpg":
        at transform:
            alpha 0
            ease 0.5 alpha 1.0
    imagebutton:
        idle "uzayuka.png"
        hover "uzayuka hehe.png"
        action [Hide("speech"), Show("speech", transition=dissolve)]

        align( 1.0, 1.0)

        at transform:
            alpha 0
            ease 0.5 alpha 1.0

screen callender:
    frame:
        padding(15,15)
        background "#4f5a6600"
        vbox:
            hbox:
                text "[year]년 [month]월 [day]일"
                spacing 10
    timer 2.0 action Hide("callender", transition=dissolve)
#daystart
screen start:
    #검은화면, 오늘 할 일을 고를 시간
    add "images/ui/bg stat2.png"
    
#클릭금지시
screen disable_LMouse():
    key "mouseup_1" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SELECT" action NullAction()
    key "K_LCTRL" action NullAction()
    key "K_RCTRL" action NullAction()
screen home:
    add "images/bg room.jpg":
        at transform:
            alpha 0
            ease 0.5 alpha 1.0
    frame:
        padding(15,15)
        background "#4f5a6600"
        vbox:
            hbox:
                text "[year]년 [month]월 [day]일"
                spacing 10
    imagebutton:
        idle "images/UI/education1.png"
        action Show("explore")
        align (.1, .3)
    imagebutton:
        idle "images/UI/education2.png"
        action Jump("rest")
        align (.5, .3)
    imagebutton:
        idle "images/UI/education3.png"
        action Show("conversation")
        align (.9, .3)
         
screen explore:
    add "images/bg lostcity.jpg":
        at transform:
            alpha 0
            ease 0.5 alpha 1.0
    textbutton "탐험한다" align (.5, .5) action [Hide("explore"), Jump("M_explore")]
    textbutton "돌아간다" align (.5, .6) action Hide("explore")
        
screen boxopen:
    add "images/bg basement.jpg":
        at transform:
            alpha 0
            ease 0.5 alpha 1.0
    imagebutton:
        idle "images/chest.png"
        action Show("bopen")
        align (.5, .5)    
screen bopen:
    add "images/phone.png" align (0.5, 0.5)
    textbutton "돌아가기" align(.6, .6) action Hide("bopen")


screen image_1():
    add "images/diary.png" xalign 0.5 yalign 0.5
screen image_2:
    add "images/diary_read1.png" xalign .5 yalign .5
    textbutton "돌아가기" align(0.9, 0.9) action [Hide("image_2"), Return()]
screen image_3:
    add "images/chest.png" xalign .5 yalign .5
screen battle:
    add "images/nighten phone E1M2_b.png" xalign 0.5 yalign 0.5
    textbutton "공격" align(.0, .7)  action SetVariable("monster1.hp", monster1.hp - player.luck)
screen monster_hit:
    add "images/chest.png" xalign .6 yalign 0.6
