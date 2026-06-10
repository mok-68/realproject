label Act2_1:
    scene medic-room-meat
    play audio "sound-effect/heart.mp3" loop fadein 3.0
    show afraid4 at left
    with dissolve
    non "ในขณะที่ฉันกำลังจะใช้เศษแก้วปาดคอตัวเองให้จบๆ ไป..."
    
    play sound "sound-effect/footstep_meat.mp3" loop fadein 3.0
    $ renpy.pause(4.0, hard=True)

    non "เธอก็ปรากฏตัวขึ้นมา..."
    stop sound fadeout 1.0
    non "เมย์"
    hide afraid4 with dissolve
    stop audio fadeout 3.0

    scene black with dissolve
    pause 1.0
    show text "{size=60}วินาทีที่เธอเอื้อมมือมาจับมือที่สั่นเทาของฉัน...{/size}" at truecenter with dissolve
    pause
    hide text with dissolve

    show text "{size=60}ผิวสัมผัสของเธอมันช่างเรียบเนียน...{w=0.5} นุ่มนวล...{/size}" at truecenter with dissolve
    pause
    hide text with dissolve

    show text "{size=60}ไม่มีเมือกเหลว... ไม่มีกลิ่นเหม็นคาว...{/size}" at truecenter with dissolve
    pause
    hide text with dissolve

    show text "{size=60}เส้นผมของเธอสะท้อนแสงแดดเป็นประกายงดงาม{/size}" at truecenter with dissolve
    pause
    hide text with dissolve

    show text "{size=60}ในขณะที่มนุษย์ทุกคนกลายเป็นปีศาจเนื้อเน่า...{/size}" at truecenter with dissolve
    pause
    hide text with dissolve

    show text "{size=60}มีแค่เธอคนเดียว...{w=0.8} ที่ยังคงเป็น 'มนุษย์' ในสายตาของฉัน{/size}" at truecenter with dissolve
    pause
    hide text with dissolve
    
    # ส่วนของเมย์ 
    scene medic-room-meat
    show mei movement2 at right with dissolve
    mei "นนท์... ร้องไห้ทำไมคะ? เจ็บตรงไหนหรือเปล่า?"
    show mei smile1
    mei "ไม่เป็นไรนะ..."
    
    # ใช้ {w} เพื่อเว้นจังหวะให้ดูเหมือนเมย์ค่อยๆ ขยับเข้าไปกระซิบใกล้ๆ
    mei "ถ้าโลกภายนอกมันทำให้เธอเจ็บปวดขนาดนั้น...{w=0.5} ขยับเข้ามาใกล้ๆ เมย์สิคะ"
    
    mei "เมย์จะปกป้องเธอเอง..."
    show mei smile2
    mei "จะเป็นดวงตา...{w=0.3} เป็นหู...{w=0.3} เป็นทุกอย่างให้เธอเอง..."
    hide mei smile2 with dissolve
    scene black with dissolve
    menu:
        "เอื้อมมือไปกุมมือเธอ... ยอมจำนนต่อความอ่อนโยนนี้":
            # เดินหน้าต่อในเส้นทางกับเมย์
            pass
            
        "คำพูดของเธอฟังดูอบอุ่น... แต่ฉันขอยอมแพ้ดีกว่า (ใช้เศษแก้วปลิดชีพตัวเอง)":
            #ไปฉากจบ Stupid Ending
            jump stupid_endding
        
    show non normal2 at left
    non "(ฉันหนีออกจากโรงพยาบาลมาอยู่กับเธอที่บ้านหลังเก่าหลังนี้)"
    
    non "(เราใช้ชีวิตด้วยกัน ลืมโลกภายนอกไปให้หมด)"
    
    non "(เมย์คอยป้อนอาหารรสชาติหวานอร่อยให้ฉันกิน... แม้ว่ารูปร่างของมันจะดูแปลกๆ ก็ตาม)"
    
    non "(แต่ฉันไม่สนหรอก...)"
    
    non "(ถ้ามีเธอนั่งอยู่ข้างๆ... นรกแห่งนี้มันก็คือสรวงสวรรค์ชั้นเจ็ดชัดๆ)"
    hide non normal2 with dissolve