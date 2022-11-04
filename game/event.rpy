init:
    define adv_point = 0
    define year = "20XX"
    define month = 3
    define day = 1
label call_start:
    e_nvl "마키씨, 마키씨"
    return
label DayStart:
    $ _skipping = False
    show screen start
    $ renpy.pause(5.0, hard = True)
    call screen home
    hide screen start
    $ _skipping = True
label M_explore:
    show bg lostcity
    show uzayuka at right with dissolve
    show maki at left with dissolve

    e "오늘은 어디로 갈까요?"
    menu:
        "지하실로 간다":
            m "지하실로 가보자. 저번에 갔던 곳에서 음식을 보충하고 싶어"
            $ adv_point += 1
            #jump M_basemet
        "새로운 곳을 찾는다.":
            if adv_point > 10:
                m "다른 곳을 찾아보자. 다른 생존자나 정보를 좀 더 모으고 싶어"
                #jump M_newplace
            else:
                m "다른 곳을 찾아보자. 다른 생존자나 정보를 좀 더 모으고 싶어"
                n "유카리와 마키는 새로운 곳을 찾아다녔다."
                $ adv_point += 3
                #jump M_room            
# 배틀(랜덤인카운터)
# 체력이 낮을 수록 도주확률 적어짐, 주는 데미지 약함
label Battle:
    $ chance = renpy.random.randint(1,100)
    if(player.hp<player.hp*0.7):
        if chance < 10:
            #$ meet_monster = renpy.random.choice()
            call screen battle
            if monster.hp -= player.luck:
                "몬스터의 체력이 10만큼 줄어들었다"
