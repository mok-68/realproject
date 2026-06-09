﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define n = Character("นนท์")
define m = Character("เมย์")
define naijai_n = Character("บทพูดในใจ นนท์")
define nuse = Character("พยาบาล")
image Forest_Meat = "path/Forest-Meat.jpg"
image black = im.Scale("path/black.jpg", 1920, 1080)
image Forest_Noramal = "path/Forest-Noramal.png"
image House_meat = "path/House-meat.png"
image House_Normal = "path/House-Normal.png"
image medic_room_meat = "path/medic-room-meat.png"
image medic_room_normal = "path/medic-room-normal.png"
image Study_Room_meat = "path/Study-Room-meat.png"
image study_room_normal = "path/study-room-normal.png"
image meat = im.Scale("sub_Character/meat.png", 1200, 800)
image worm = "path/worm.png"


transform shake:
    xoffset -5
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5
    repeat  
# The game starts here.
transform slide_fade_out:
    linear 1.0 yoffset -100 alpha 0.0
screen wakeup():
    add Solid("#000")

label start:
    $ preferences.text_cps = 15
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    play sound "heart.mp3"
    
    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    
    
    # show eileen happy
    # w = หยุดตามหลักวิ
    scene black
    
    "เสียงชีพจรเต้นช้าๆ {cps=20}(ตึก... ตึก...){/cps} คลอด้วยเสียงกรีดร้องแหลมสูงแว่วมาไกลๆ"
    show text "{size=80}ฉากที่ 1.1 - มุมมองของฟุมิโนริ{/size}" at truecenter
    
    
    # hide black with fade
    scene medic-room-meat

    hide screen wakeup with Dissolve(3.0)
    with vpunch
    with dissolve

    pause 3.0

    hide text

    with dissolve

    with fade 

    pause 2.0
    
    
    stop sound fadeout 3.0
    play music "wind.mp3" fadein 3.0
    scene medic-room-meat
    "ภาพพร่าเบลอสีแดงเดือด{w=1}"
    "ผนังห้องเป็นก้อนเนื้อเต้นตุบๆ{w=1}"
    "มีหนอนสีคล้ำชอนไชไปมา{w=1}"
    show worm with moveinright
    n"{size=80}พวกแกเคยตื่นมาในนรกไหม!!!!!!...{/size}"
    with fade  
    n"ตั้งแต่ผ่าตัดสมองหลังอุบัติเหตุรถยนต์ครั้งนั้น"
    n"โลกที่เคยปกติของฉันมันก็ดับสลายไปตลอดกาล"
    n"หมอเถื่อนพวกนั้นบอกว่ามันคือ 'โรคการรับรู้ผิดปกติ'"
    n"แต่สำหรับฉัน มันคือนรกบนดินชัดๆ มนุษย์ทุกคนรอบตัวกลายเป็นก้อนเนื้อเน่าเดินได้ ส่งกลิ่นบูดโชยเข้าจมูกจนอยากจะอ้วกตลอดเวลา"
    hide worm 
    
    play sound "footstep.mp3" fadein 3.0
    "พยาบาลที่เดินเข้ามาฉีดยา... {w=5}"
    play stop "footstep.mp3" fadeout 3.0
    "รูปร่างของเธอเหมือนเศษเนื้อเหลวๆ ที่พยายามประกอบร่างเป็นทรงมนุษย์ เสียงที่เธอทักทายฉันว่า"
    show text "{size=60}ตุบ!{/size}" at truecenter

    with vpunch
    hide text
    show meat:
        pos(0,0)
    with moveinright 
    nuse"อรุณสวัสดิ์ค่ะ" 
    n"...แต่หูของฉันกลับได้ยินเป็นเสียงสุกรโดนเชือดที่กรีดร้องแหลมลึกจนแก้วหูจะแตก!"
    n"อาหารโรงพยาบาลรสชาติเหมือนขยะเปียกค้างคืนผสมเลือดคาวๆ"
    n"ทรมานชะมัด ฉันเอามือกุมหัว กรีดร้องเหมือนคนบ้า ทุบตีทุกอย่างที่เข้าใกล้ ฉันอยากจะตาย... โลกเฮงซวยแบบนี้ฉันจะอยู่ไปทำไมวะ?"
    $ i = 0

    # This ends the game.
    stop sound fadeout 3.0

    jump Act-1.2
    
