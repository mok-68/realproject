label Act_1_2:
    scene black

    screen wakeup():
        add Solid("#000")

    show screen wakeup 

    play sound "Hospital.mp3" fadein 3.0

    "เสียงฝีเท้าตามทางเดิน {cps=20}(ตึก... ตึก...){/cps} คลอด้วยเสียงความวุ่นวายในโรงพยาบาล"
    show text "{size=80}ฉากที่ 1.2 - มุมมองคนทั่วไป{/size}" at truecenter

    play sound "Sound Effects - Footsteps.mp3" fadein 3.0

    scene medic-room-normal

    hide screen wakeup with Dissolve(3.0)
    with vpunch
    with dissolve

    pause 3.0

    hide text

    with dissolve

    with fade 

    pause 2.0
    
    
    stop sound fadeout 3.0

    play sound "Hospital-room.mp3" fadein 3.0

