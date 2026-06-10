define non = Character("นนท์", color="#2ddcff")
define mei = Character("เมย์", color="#ff60f7")
define naijai_n = Character("บทพูดในใจ นนท์")
define nuse = Character("พยาบาล",color="#fafafaff")
image Forest_Meat = "path/Forest-Meat.jpg"
image black = im.Scale("path/black.jpg", 1920, 1080)
image Forest_Noramal = "path/Forest-Noramal.png"
image House_meat = "path/House-meat.png"
image House_Normal = "path/House-Normal.png"
image medic_room_meat = "path/medic-room-meat.png"
image medic_room_normal = "path/medic-room-normal.png"
image Study_Room_meat = "path/Study-Room-meat.png"
image study_room_normal = "path/study-room-normal.png"
image meat = im.Scale("sub_Character/meat.png", 1000, 800)
image meat_shadows = im.Scale("sub_Character/meat.png", 1000, 800)
image worm = "path/worm.png"

transform shadow:
    alpha 0.3
    xoffset 15
    yoffset 15
    matrixcolor SaturationMatrix(0)
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
    
    play sound "sound-effect/heart.mp3"
    
    
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
    play music "sound-effect/wind.mp3" fadein 3.0
    scene medic-room-meat
    "ภาพพร่าเบลอสีแดงเดือด{w=1}"
    "ผนังห้องเป็นก้อนเนื้อเต้นตุบๆ{w=1}"
    "มีหนอนสีคล้ำชอนไชไปมา{w=1}"
    show worm with moveinright
    non"{size=80}พวกแกเคยตื่นมาในนรกไหม!!!!!!...{/size}"
    with fade  
    non"ตั้งแต่ผ่าตัดสมองหลังอุบัติเหตุรถยนต์ครั้งนั้น"
    non"โลกที่เคยปกติของฉันมันก็ดับสลายไปตลอดกาล"
    non"หมอเถื่อนพวกนั้นบอกว่ามันคือ 'โรคการรับรู้ผิดปกติ'"
    non"แต่สำหรับฉัน มันคือนรกบนดินชัดๆ มนุษย์ทุกคนรอบตัวกลายเป็นก้อนเนื้อเน่าเดินได้ ส่งกลิ่นบูดโชยเข้าจมูกจนอยากจะอ้วกตลอดเวลา"
    hide worm 
    play sound "sound-effect/door_sound.mp3"
    pause 5.0
    stop sound
    play sound "sound-effect/Sound Effects - Footsteps.mp3" fadein 3.0
    non"พยาบาลที่เดินเข้ามาฉีดยา... {w=5}"
    stop sound fadeout 3.0
    non"รูปร่างของเธอเหมือนเศษเนื้อเหลวๆ ที่พยายามประกอบร่างเป็นทรงมนุษย์ เสียงที่เธอทักทายฉันว่า"
    show text "{size=60}ตุบ!{/size}" at truecenter

    with vpunch
    hide text
    show meat_shadows at left ,shadow
    show meat at left
    with moveinright 
    nuse"!@/*-^&$*@...." 
    non"...แต่หูของฉันกลับได้ยินเป็นเสียงสุกรโดนเชือดที่กรีดร้องแหลม"
    non"ลึกจนแก้วหูจะแตก!"
    non"อาหารโรงพยาบาลรสชาติเหมือนขยะเปียกค้างคืนผสมเลือดคาวๆ"    
    non"ทรมานชะมัด ฉันเอามือกุมหัว กรีดร้องเหมือนคนบ้า ทุบตีทุกอย่างที่เข้าใกล้ ฉันอยากจะตาย... โลกเฮงซวยแบบนี้ฉันจะอยู่ไปทำไมวะ?"
    # This ends the game.
    stop sound fadeout 3.0
jump Act_1_2
    
