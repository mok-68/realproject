# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define a = Character("นนท์")
define b = Character("เมย์")
define c = Character("บทพูดในใจ นนท์")
define nuse = Character("พยาบาล")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play sound "heart.mp3"
    image Forest-Meat = "path/Forest-Meat.jpg"
    image black = im.Scale("path/black.jpg", 1920, 1080)
    image Forest-Noramal = "path/Forest-Noramal.png"
    image House-meat = "path/House-meat.png"
    image House-Normal = "path/House-Normal.png"
    image medic-room-meat = "path/medic-room-meat.png"
    image medic-room-normal = "path/medic-room-normal.png"
    image Study-Room-meat = "path/Study-Room-meat.png"
    image study-room-normal = "path/study-room-normal.png"
    image worm = "path/worm.png"
    transform shake:
        xoffset -5
        linear 0.05 xoffset 5
        linear 0.05 xoffset -5
        repeat
    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
   
    
    
    # show eileen happy
    # w = หยุดตามหลักวิ
    scene black
    
    "{cps=15}เสียงชีพจรเต้นช้าๆ (ตึก... ตึก...) คลอด้วยเสียงกรีดร้องแหลมสูงแว่วมาไกลๆ{/cps}"
    show text "{size=80}ฉากที่ 1.1 - มุมมองของฟุมิโนริ{/size}" at truecenter

    with dissolve

    pause 3.0

    hide text

    with dissolve

    with fade

    pause 2.0
    
    
    stop play fadeout 3.0
    play music "wind.mp3" fadein 3.0
    scene medic-room-meat
    "{cps=15}ภาพพร่าเบลอสีแดงเดือด{w=1}{/cps}"
    "{cps=15}ผนังห้องเป็นก้อนเนื้อเต้นตุบๆ{w=1}{/cps}"
    "{cps=15}มีหนอนสีคล้ำชอนไชไปมา{w=1}{/cps}"
    show worm with moveinright
    a"{cps=15}{size=80}พวกแกเคยตื่นมาในนรกไหม!!!!!!...{/size}{/cps}"
    with fade  
    a"{cps=15}ตั้งแต่ผ่าตัดสมองหลังอุบัติเหตุรถยนต์ครั้งนั้น{/cps}"
    a"{cps=15}โลกที่เคยปกติของฉันมันก็ดับสลายไปตลอดกาล{/cps}"
    a"{cps=15}หมอเถื่อนพวกนั้นบอกว่ามันคือ 'โรคการรับรู้ผิดปกติ'{/cps}"
    a"{cps=15}แต่สำหรับฉัน มันคือนรกบนดินชัดๆ มนุษย์ทุกคนรอบตัวกลายเป็นก้อนเนื้อเน่าเดินได้ ส่งกลิ่นบูดโชยเข้าจมูกจนอยากจะอ้วกตลอดเวลา{/cps}"
    hide worm 
    
    play sound "footstep.mp3" fadein 3.0
    "{cps=15}พยาบาลที่เดินเข้ามาฉีดยา... {w=5}{/cps}"
    play stop "footstep.mp3" fadeout 3.0
    "{cps=15}รูปร่างของเธอเหมือนเศษเนื้อเหลวๆ ที่พยายามประกอบร่างเป็นทรงมนุษย์ เสียงที่เธอทักทายฉันว่า"
    show text "{size=60}ตุบ!{/size}" at truecenter

    with vpunch
    hide text
    nuse"{cps=15}อรุณสวัสดิ์ค่ะ{/cps}" 
    a"{cps=15}...แต่หูของฉันกลับได้ยินเป็นเสียงสุกรโดนเชือดที่กรีดร้องแหลมลึกจนแก้วหูจะแตก!{/cps}"
    a"{cps=15}อาหารโรงพยาบาลรสชาติเหมือนขยะเปียกค้างคืนผสมเลือดคาวๆ{/cps}"
    a"{cps=15}ทรมานชะมัด ฉันเอามือกุมหัว กรีดร้องเหมือนคนบ้า ทุบตีทุกอย่างที่เข้าใกล้ ฉันอยากจะตาย... โลกเฮงซวยแบบนี้ฉันจะอยู่ไปทำไมวะ?{/cps}"
    

    # This ends the game.
    play stop "wind.mp3" fadeout 3.0
    return
