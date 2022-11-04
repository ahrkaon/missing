## Screen with Stats Button
screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.7
        xoffset -30
        yoffset 30
        idle "UI/stats_idle.png" 
        hover "UI/stats_hover.png" hover_sound "sfx/click.wav"
        action ShowMenu("StatsUI")
        
## Stats UI
screen StatsUI:
    add "UI/bg uzayuka_status.png"
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30
        background "#C32CB200"

        hbox:
            spacing 40
            # Text Column
            vbox:
                spacing 10
                text "체력" size 40  
                text "운" size 40
                text "포만도" size 40
                text "현재 포만도" size 40
                text "호감도" size 40

            # Values Column     
            vbox:    
                spacing 10
                text "[player.hp]" size 40
                text "[player.luck]" size 40
                text "[player.max_starve]" size 40
                text "[player.starve]" size 40
                text "[player.love]" size 40
    
    textbutton "마키" align (.3, .3) action [Hide("StatsUI"), ShowMenu("Stats_M")]
    ## Show a Return button
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/return_%s.png"
        action Return()
screen Stats_M:
    add "images/UI/bg maki_status.png"
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30
        background "#C32CB200"

        hbox:
            spacing 40
            # Text Column
            vbox:
                spacing 10
                text "호감도"
            vbox:
                spacing 10
                text "[maki_love]"
    textbutton "유카리" align (.7, .3) action [Hide("Stats_M"), ShowMenu("StatsUI")]
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/return_%s.png"
        action Return()    
