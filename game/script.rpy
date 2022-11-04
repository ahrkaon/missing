# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define e_nvl = Character("유카리", kind=nvl, image="uzayuka", callback=Phone_SendSound)
define m_nvl = Character("마키", kind=nvl, callback=Phone_ReceiveSound)
define e = Character("유카리", color="#FFFFFF", who_outlines=[ (1, "#8B00FF") ])
define m = Character("마키", color="#FFFFFF", who_outlines=[(1, "#FFD400")])
define u = Character("???", color="#FFFFFF")
define maki_love = 0
define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

define bl_select1 = False
## 능력치와 포만도에 따라 특정 선택지가 생기거나 혹은 선택불가상태에 빠지게 만들려는 계획중
## 캐릭터 능력치
init -1 python:
    import random
    class Player(renpy.store.object):
        def __init__(self, name, max_hp, hp, max_starve, starve, luck, love):
            self.name = name
            self.max_hp = max_hp
            self.hp = max_hp
            self.max_starve = max_starve
            self.starve = starve
            self.luck = luck
            self.love = love
    player = Player("유카리", 10, 10, 100, 20, 10, 0)
    
    
# 여기에서부터 게임이 시작합니다.
label start:

    play music "audio/Alexander Ehlers - Waking the devil.mp3" fadein 1.0 loop
    
    "유카리가 게임을 하다 지쳐 잠들었다 깨어나자 세계가 망해있었다."
    scene bg intro with dissolve
    show screen callender 
    #call screen home
    "방금 깨어난 유카리는 그것이 꿈이라 생각하고 다시 잠들었지만 다시 일어난 유카리는 창 밖을 바라보며 자신의 뺨을 꼬집었다"
    e "아얏" with vpunch
    "뺨에서 불이 난듯한 고통을 느끼며 유카리는 그것이 현실임을 깨달았다."  
    
    scene bg room with fade
    
    show uzayuka hwanho with dissolve
    e "드..드디어 일을 안해도 된다!!!" with vpunch
    e "아 신이시여 이게 당신이 말한 구원이었군요. 역시 신은 존재했어"
    hide uzayuka hwanho
    "그렇게 환호를 치면서 콘솔을 키고 게임삼매경에 빠져든 유카리는 며칠동안
    집에서 한발짝도 움직이지 않았고 결국 집에 있던 음식이 바닥을 드러냈다."
    "하지만 유카리는 굶주린 배를 끌어안으면서도 밖에 나갈 생각을 하지 않았다"
    show uzayuka angry with dissolve
    e "역시 신은 죽었어"
    e "그랬으면 음식이 떨어질리가 없지"
    e "하늘에서 음식이라도 뿌려줘야 하는거 아니냐고!"
    
    show uzayuka bubu with dissolve
    e "하아... 나가기 귀찮지만...아직 못한 게임을 두고 죽을 순 없지"
    hide uzayuka bubu

    "그렇게 유카리는 귀차니즘과 굶주림의 줄다리기에서 생존의 길을 걷기로 했다"
label map1 :
    scene bg lostcity with fade
    show screen gameUI
    show screen state

    show uzayuka with dissolve

    e "으으 어딜가야 먹을걸 찾을 수 있지...?"

    e "이러다간 조만간 굶어죽을거야"
    e "근처에 가게가 어디있더라?"
    $ bl_game = False
    
menu M_route:
    "골목으로 빠져보자":
        jump 골목
    "계속 직진해보자":
        $ player.starve = player.starve - 10
        jump M_route2
label 골목 :
    scene bg alley with fade

    if bl_game == False:
        show uzayuka find with dissolve
        e "여긴 처음오는 곳인데 너무 무섭다"
        e "나중에 다시오자"
        jump aa
    else:
        show maki at left with dissolve
        show uzayuka at right with dissolve

        m "봐봐 아무도 없이 텅 비었잖아." 
        m "이제 그냥 들어가서 필요한 물건을 챙겨오기만 하면 된다구."
        e "그래도 무서우니까 마키씨가 먼저 들어가면 따라 들어갈게요."
        m "유카리는 정말 겁이 많네." 
        m "아까도 동물소리를 괴물소리가 들렸다고 했잖아." 
        m "지금은 그렇게 겁이 많으면 살기 힘든 세상이라고"
        show uzayuka moo at right with dissolve
        e "아니 그 소리는 정말 들었다니까요?" 
        e "뭔가 거대한 터널에서 날 법한 소리였어요." 
        e "그 때 사슴이 지나가긴 했지만 \n사슴이 그런 소리를 낼리 없잖아요."
        play sound "audio/Beast-Growl-2.ogg" fadein 0.5
        
        show uzayuka scared at right with dissolve
        pause 2.0
        e "히익! 들었어요?! 방금 그 소리였어요. 이젠 거짓말이라고 못하겠죠?"
        stop sound fadeout 2.0
        show uzayuka bubu at right with dissolve
        show maki hun at left with dissolve
        m "아무 소리도 안들렸는데? 너 정말 괜찮은거야? 아니면 아직도 배가 고파서 환청을 듣는건가?"
        show uzayuka moo at right with dissolve
        e "방금 들렸잖아요! 그 그르렁거리는 소리요!"
        show maki smile2 at left with dissolve
        m "자자, 이상한 소리는 그만하고 빨리 물건이나 챙겨서 가자. 이러다가 해지면 정말 위험해"
        show uzayuka at right with dissolve
        e "으윽, 다음엔 반드시 이 억울함을 풀테니까요"
        m "네네, 빨리 들어가자"
        jump M_route6   

label M_route2:
    
    scene bg map1 with fade

    show uzayuka with dissolve
    
    e "분명 이 근처에 상가가 있을텐데...
    아 저기있다..."
    play sound "audio/Beast-Growl-2.ogg" fadein 1.0
    pause 0.5
    show uzayuka scared with dissolve
    e "히익 뭐야...?"
    stop sound fadeout 1.0
    e "빨리 먹을 걸 찾아서 돌아가자"
    hide uzayuka scared
    
    
    menu :
        "상가 안으로 들어간다":            
            jump 상가
        "지하철 역으로 들어간다":   
            jump subway

label 상가:
    
    scene bg map8 with fade
    play music "audio/forest.ogg" fadein 1.0
    show uzayuka with dissolve
    e "아 여기 통조림이 있어"
    menu eat:
        "먹는다":
            jump eating
        "먹지 않는다":
            e "으으 배고파"
            jump M_route3
    label eating:
        $ player.starve = player.starve + 10
        e "으으 조금은 나았지만 이걸로는 모자라"
        jump M_route3
label subway:
    scene bg map4 with fade
    play music "audio/flaremain.ogg"
    show uzayuka with dissolve

    e "어제만 해도 움직이지도 못할 정도로 꽉 찬 곳이었는데 자고 일어나니 텅 비다 못해 다 부서져가네요"
    e "대체 무슨 일이 있었던건지는 모르겠지만... 뭐 이미 망한건 어쩔 수 없죠."
    e "그것보다 제가 살아가는게 더 중요해요."
    menu :
        "매점으로 간다":
            $ bl_select1 = False
            "유카리가 먹을 걸 찾기 위해 지하철 역의 매점에 있던 곳으로 가봤지만 이미 폐허였다."
            e "여기가 멀쩡하지 않은데 더 찾아봐야 헛수고같네요. 다른 곳으로 가보죠"
            
            jump select1 
        "자판기로 간다":
            $ bl_select1 = True
            e "앗 다행히 먹을게 좀 있어요. 후후 전 운이 좋네요"
            $ player.luck = player.luck + 5
            jump select1
                
label select1:
    scene bg map1 with fade
    show uzayuka with dissolve
    if bl_select1 == False:
        menu tmp1:
            "상가 안으로 들어간다":
                jump 상가
            "지하철 역으로 들어간다":
                e "여긴 먹을게 없었어요. 다른 곳을 찾아보죠"
                call tmp1
                return
                #menu:
                #    "상가 안으로 들어간다":
                #        jump 상가
    else:
        e "남은 곳을 여기밖에 없네요."
        menu:
            "상가 안으로 들어간다":
                jump 상가
                return    
label M_route3:
    $ bl_game = True

    show uzayuka bubu with fade
    e "으음 역시 벌써 다 털린건가... 이러면 다른 곳도 마찬가질텐데..."
    play sound "audio/doorClose_3.ogg"

    pause 0.7

    show uzayuka scared with dissolve
    e "꺄아악! 뭐냐고 정말! 왜 자꾸 아무도 없는데서 소리가 나는거야!"
    e "이...일단 여기서 나가야겠어.. 아직 입구로 들어왔을 뿐이니까 바로 돌아갈 수 있어"
    play sound ["audio/footstep04.ogg", "audio/footstep04.ogg", "audio/footstep04.ogg"]
    pause 0.8
    play sound "audio/DoorPunch.ogg"
    "우당탕" with vpunch
    hide uzayuka scared
    e "아얏"
    u "아 미안. 괜찮아?"

    show uzayuka scared with dissolve
    e "꺄악 귀신이다!!"
    u "귀신이라니... 그럴 리가 없잖아"
    show uzayuka scared at right
    with dissolve
    show maki at left
    with dissolve
    m "내 이름은 마키야, 여기 먹을 게 좀 있나 찾으려고 왔지. 아마 너도 같은 이유겠지?"
    show uzayuka at right
    with dissolve
    e "저...저는 유카리라고 합니다."
    m "하하, 그렇게 놀랄 줄은 몰랐는데..."
    m "하긴 나도 이런 일 이후에 만난 사람은 너가 처음이야. 다른 사람도 이렇게 살아있겠지?
    뭔가 안심된다."
    e "네? 그게 무슨 말이에요?"
    show uzayuka hun at right
    with dissolve
    e "이런 일이고 자시고 갑자기 망했잖아요"
    show maki surprise at left
    with dissolve
    m "무슨 말을 하는거야? 너 설마 {color=#f00}그 일{/color}을 기억하지 못하는거야?"
    show maki at left
    with dissolve
    e "그 일이라는 건 모르겠고 전 평범하게 자고 일어나니 이렇게 변해있었는걸요."
    e "그것보다 마키..씨?가 아까부터 절 따라온건가요? 어쩐지 아무도 없는데서 이상한 소리가 난다 싶었어요."
    show uzayuka smile at right
    with dissolve
    e "후훗 사람이라면 전혀 무서울게 없다구요."
    show maki hun at left
    with dissolve
    m "응? 널 만난건 너가 나한테 몸통박치기를 했을 때였는데?" 
    m "여긴 내가 사는 곳과도 거리가 좀 있어서 준비할게 많거든"
    m "그래서 가끔 밖에 안오는데 우연히 너하고 마주친거야."
    show uzayuka idk at right
    with dissolve
    e "그럼 아까 이상한 울부짖는 소리라던가 그런건...."
    m "글쎄? 이제는 길가에 동물들이 돌아다니는게 \n드물지 않으니까 그런 소리가 아닐까?"
    show uzayuka hehe at right
    with dissolve
    e "으음... 그런가요?"
    "꾸르르르륵" with hpunch
    show uzayuka eeh at right
    with dissolve
    e "하윽... 생각해보니 3일째 아무것도 못먹은 상태였어요...\n 잠깐이나마 즐거웠어요. 이제 제 먹이가 돼주세요!"
    show maki surprise at left
    with zoomin
    m "에? 자..잠깐만 기다려!"
    show bg blackout with dissolve
    hide uzayuka eeh
    hide maki surprise 
    m "잠깐만... 꺅! 진짜로 문거야? 나..나한테 음식이 좀 있으니까... 빨리 떨어져"
    e "맛있는 고기가 눈 앞에! 풍부한 지방이 가득한 가슴까지!"
    m "앗! 가슴 깨물지마! 쫌...여기 빵이 있다고오!"
    e "빵! 고기! 오늘은 파티다아!"
    m "가만히 좀 먹기나 하라구!!"
    "한동안의 소란을 피운 후 마키는 자신의 여기저기 물린자국을 확인하며 \n기진맥진한 채 축 늘어졌고"
    "사흘 만의 음식을 먹게 된 유카리는 정신을 놓은 채 \n허겁지겁 마키가 준 음식을 해치우고 있었다."
    $ player.starve = player.starve + 30
    show bg map8 with fade 

    show maki at left
    show uzayuka hehe at right
    with dissolve
    m "하아하아... 이제 진정 좀 됐어?" 
    m "정말이지 그냥 밥을 달라고 하면 될 것을 진짜로 물어대다니"
    e "우걱우걱...죄송..꿀꺽...합니다.. "

    show maki smile2 at left 
    show uzayuka hwanho at right
    with dissolve
    e "크으 이렇게 먹을 수 있다니 정말 감사합니다. \n진짜로 죽기 직전이었거든요"
    m "정말 배고팠나보네." 
    m "얼마 되진 않지만 그거 오늘 하루치 식량이었는데"
    show uzayuka eeh at right with dissolve
    e "그, 그런 귀한걸... 지금 당장 구해다 드릴게요"
    show maki wink at left with dissolve
    m "아 괜찮아, 괜찮아." 
    m "혼자 살아봐야 재미도 없고 이렇게 사람이 살아있다는 걸 알아냈으니까 \n노프라블럼!"
    show uzayuka at right with dissolve
    
    e "오늘은 정말 고마웠어요." 
    e "전 이제 다른 곳을 좀 더 찾으려고 하는데 마키씨는 어쩌실건가요?"
    m "음 이렇게 만난것도 인연인데 같이 찾아볼래?" 
    m "같이 행동하는게 훨씬 효율이 좋을거라고 생각되지 않아?"
    e "그렇네요. 혼자는 좀 무섭기도 하고 같이 가죠"
    m "예이~ 결정됐네. 그럼 앞으로 잘부탁해~"

    hide uzayuka
    hide maki wink

    jump M_route4
label M_route4:
    scene bg map1 with fade
    show uzayuka at right
    show maki at left
    with dissolve

    e "마키씨는 이 근처에 여러번 와봤었다고 했죠?"
    m "응 자주는 아니지만 그래도 여기저기 둘러봤지. \n이 근처까지 온 거는 거의 처음이지만 말이야"
    e "그런가요. 사실 제 집이 이 근처이긴 한데 \n이렇게 부서져서는 어디가 멀쩡한지 전혀 모르겠어서요"
    m "음~ 그러면 원래 내가 가볼려고 했던 곳으로 가볼래?" 
    m "여기서 그렇게 멀지는 않아"
    e "좋아요. 길을 잘 아는 사람을 따라가는게 맞으니까요"

    hide uzayuka
    hide maki
    jump M_route5
label M_route5:
    scene bg lostcity with fade
    show uzayuka surprise at right
    show maki at left
    with dissolve
    #$ player_feel += 1

    e "어라? 여기까지 올 줄은 몰랐네요"
    m "아는 곳이야? \n여기 근처에 뭔가 있다는 촉이 와서 온건데"
    e "그럴게 여기 저희 집 근처에요." 
    e "여기서 안 둘러본 곳은 예전에 양아치들의 아지트라고 소문나있던 골목 뿐이네요"
    m "그래? 그럼 거기 한번 가보자." 
    m "혹시 모르잖아? 어린 애들이 비밀기지 만들듯이 뭔가를 쌓아놨을지"
    show uzayuka panic at right with dissolve
    e "그..그게 좀 무서워서 앞에 있을테니 혼자 갔다오는게...."
    show maki smile at left with dissolve
    m "에이 괜찮아. 말했잖아 너말고는 사람 못본지가 한참 됐다고... \n분명 아무도 없을테거야."
    m "자자 출바알~"
    jump 골목
label M_route6:
    scene bg map10 with fade
    show uzayuka at right
    show maki at left
    with dissolve

    m "우와 안쪽은 더 심하네... \n이래서는 제대로된게 남아있으려나?"
    e "쥐, 쥐는 없는거죠?" 
    e "바선생이랑 동급으로 끔찍한 생물인데요..."
    m "에휴 그런거 없으니까 제대로 찾아봐. \n이렇게 부서져서는 찾는게 오히려 기적이지만..."
    play sound "audio/creak2.ogg"
    pause 0.5

    e "어라? 밑에 뭐가 있나?"
    play sound "audio/creak2.ogg"
    pause 0.5
    e "마키씨, 여기 밑에 뭐가 있는 것 같아요." 
    e "뭔가 삐그덕 거리는 소리가 나요."
    m "그래? 잠깐만 비켜볼래?" 
    m "내가 한 번 뜯어볼게"

    play sound ["audio/DoorPunch.ogg", "audio/DoorPunch.ogg", "audio/impactwood07.ogg"]
    pause 2.0
    e "오오 이런 곳에 지하실이라니 뭔가 보물의 냄새가 풀풀 나요."
    e "그것보다... {size=-10}엄청난 괴력...그 힘의 원천은 역시 저 풍만한 가...{/size}"
    show maki badsmile at left with dissolve
    m "응? 뭐라고 했어?"
    show uzayuka idk at right with dissolve
    e "아, 아뇨... 아무 말도 안했어요. 그냥 빨리 들어갈까나 하고..."
    m "흐응 그렇게 겁 많던 유카리가 갑자기 이런 구멍에 빨리 들어가고 싶어하다니..."
    m "그럼 소원대로 해줄게"
    show uzayuka panic3 at right with dissolve
    e "네? 아뇨아뇨 잠시만 기다려주세요."
    e "그냥 해본 말이라고 할까, 단순한 말실수라고 할까...."
    show maki at left with dissolve
    m "후훗 농담이야. 내가 먼저 내려가볼게. 조심해서 따라와~"
    jump M_route7
label M_route7:
    scene bg basement with fade
    play music "audio/jkjkke - dream.mp3" fadein 3
    show maki at left with dissolve
    show uzayuka at right with dissolve

    m "꽤나 깔끔하잖아. 이 지하실 생각보다 되게 튼튼한거 같아." 
    m "이렇게 완벽한 상태로 유지되고 있다니..."
    e "바깥의 건물은 거의 무너져있던걸 비교하면 정말 그렇네요." 
    e "만약의 일을 대비해서 만든 방공호 같은걸까요?"
    m "글쎄? 아마 그럴지도 모르지." 
    m "주인은 미처 대피하지 못한건지 아니면 누군가를 찾으러 간건지 모르겠지만"
    m "사람이 살고있다는 느낌은 들지않네"
    m "여길 한 번 둘러보자. 이런 곳이라면 음식도 분명 비축 해뒀을거야."
    m "난 이쪽을 찾아볼테니 유카리는 저쪽을 찾아봐줘"
    e "알겠어요. 뭔가 찾으면 부를게요."
    hide maki
    hide uzayuka
    scene bg blackout with dissolve
    "유카리와 마키는 흩어져서 필요한 물건이 있는지 찾아보기로 했다."
    scene bg basement with dissolve
    show uzayuka with dissolve
    e "이런 곳이 있었다면 그냥 여기 숨어서 지내도 될텐데 \n왜 아무도 살지 않는거지?"
    e "아무튼 적당히 둘러보다가 마키씨랑 합류하도록 하죠"
    menu search1:
        "책상을 뒤진다":
            jump search_1
        "벽 뒤를 살핀다":
            jump search_2
    label search_1:
        show uzayuka bubu with dissolve
        e "이 책상에 뭔가 있을 법한 느낌이 들어요"
        "책상서랍에서 일기장을 발견했다"
        show screen image_1
        pause 1.0
        hide screen image_1
        e "이건 일기장 처럼 생겼는데 함부로 봐도 되는걸까요." 
        e "마키씨와 상담해보도록 하죠"
        jump s_search_1
    label search_2:
        show uzayuka bubu with dissolve
        e "영화에서 보면 이런 곳의 벽 뒤에 비밀스러운 공간이 있었어요." 
        e "어차피 시간도 남는데 한번 확인해보죠"
        play sound ["audio/Knocking On Heavy Door 1.ogg"]
        pause 2.0
        e "어라? 역시 뭔가 비어있는 소리가 나네요. 보물의 냄새가 나요"
        "잠시 벽은 만지던 유카리는 소리가 울리는 곳에서 \n벽이 살짝 눌리는 것을 확인하고 눌러봤다."
        play sound ["audio/doorOpen_2.ogg"]
        pause 1.0
        scene bg map17 with fade
        show uzayuka doya2 with dissolve
        e "후후후 역시 제 머리는 우수하네요. \n이렇게 금방 찾아버릴 줄이야."
        show uzayuka kusu with dissolve
        e "그럼 이런 공간에 뭘 숨겨놓았을까요? \n그렇고 그런거라도 숨겨져 있을까요?"
        show screen image_3
        pause 1.0
        hide screen image_3
        show uzayuka hehe with dissolve
        e "겨우 상자 하나를 숨기려고 이런 공간을 만들다니 대체 뭐가 들었을까요?"
        "몇가지 물건을 찾은 유카리는 비밀방에서 나와 마키를 불렀다."
        jump M_route8
    menu s_search_1:
        "벽 뒤를 살핀다":
            jump search_2
label M_route8:
    scene bg basement with fade
    show uzayuka at right with dissolve
    show maki at left with dissolve

    e "마키씨 뭐 찾은거 있나요?"
    m "여기 통조림이나 그런 보존식이 되게 많아." 
    m "취미인지 안전대책이었는지는 모르겠지만 \n이 곳 주인은 상당히 마니아였던거 같아"
    m "유카리는 뭔가 찾았어?"
    show uzayuka ping at right with dissolve
    e "아, 제가 일기장처럼 생긴 걸 찾았어요." 
    e "함부로 읽는건 실례라고 생각해서 마키씨에게 상담하려고 했죠"
    m "일기장? 확실히 평소라면 함부로 읽기는 좀 미안하지만..." 
    m "그 안에 이 곳에 대한거나 뭔가 정보가 있을지 모르니까 \n읽어보는게 좋지 않을까?"
    show uzayuka at right with dissolve
    e "그렇겠죠? 그럼... 열어볼게요"
    play sound "audio/book_page2.ogg" fadeout .3
    call screen image_2
    show maki panic at left with dissolve
    e "이런 사정이 있었네요."
    e "이 일기장의 주인이 여길 만들었는데 애인과 싸우고 \n혼자만 살아남았다는 죄책감때문에" 
    e "이 곳에 머무르지 않고 찾으러 떠났나보네요"
    e "마키씨? 마키씨?!"
    show maki at left with dissolve
    m "어? 아하하... {p}\n미안해 잠깐 딴 생각을 좀..."
    show uzayuka surprise at right with dissolve
    e "혹시 제가 아까 마키씨의 밥을 다 먹어서 배고픈건가요?"
    e "그건 큰일이에요. \n방금 찾았다고 했던 음식을 빨리 먹으세요."
    show maki smile2 at left with dissolve
    m "괜찮아, 그 정도는 아니니까. "
label M_route9:
    jump DayStart

label M_route10:
    scene bg room with fade
    nvl_narrator "마키님이 유카리님을 초대했습니다"
    e_nvl surprise "어라? 이게 뭔가요?"
    m_nvl "저번에 갔던 창고에서 찾았어. 둘 만의 메세지라니 멋지지 않아?"
    e_nvl "그 때는 아무것도 못찾지 않았나요?"
    m_nvl "일기장만 발견했을 뿐이긴 했지만 그 이후에 잠깐 들러봤더니"
    m_nvl "금고 같은게 있더라고 그래서 열었더니 찾아버렸어."
    e_nvl "설마 금고를 부수고 연건 아니죠? 마키씨가 그렇게 야만적일리가..."
    call call_start
    # This ends the game.

    return main_menu

define fadelong = Fade(0.5, 5.0, 0.5)
label aa:
    scene bg lostcity
    with dissolve

    show uzayuka with dissolve
    call M_route
return
label go_home:
    e "마키씨 라면먹고 갈래요?"
return
label test:
    scene bg room
    call phone_start
    call message_start("마키", "이거봐 아직 위성이 살아있어.")
    call reply_message("정말이네요?")
    call message_img("유카리", "마키씨 문자에요", "pic1.png")
    call message("유카리", "이렇게 보내면 되는거겠죠?")
    call message("유카리", "이건 뭔 차이지?")

    call screen phone_reply("대단해", "choice1", "진짜 되는거야?", "choice2")
label choice1:    
    # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
    call phone_after_menu
    
    # whenever you put the sender name to be "me" it is the player characters own message!
    call message_start("me", "대단해")
    call message("nadia", "i hope you like it")

    jump aftermenu
    
label choice2:
    call phone_after_menu
    call message_start("me", "진짜 되는거야?")
    call message("nadia", "well, its a shame but your feelings are valid")
    
    jump aftermenu
label aftermenu:
    call message("nadia", "check the code for comments on how the code works, thanks for your time!")
    call message("nadia", "the base for this code and this stretched phone background comes from cute demon crashers")
    call message("nadia", "the images were drawn by my gf @sloppydraws")
    
    # this one puts away the phone!
    call phone_end
    
return
label s_secret1:
    
    show screen safe_code
    pause 10.0
    return
label xx:
    call screen boxopen
    return
label xxx:
    call screen image_2
    return

