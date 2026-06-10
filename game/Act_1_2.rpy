image nus = im.Scale("images/sub_Character/4.png", 1800, 1000)


label Act_1_2:
    # 1. เริ่มต้นด้วยฉากดำ พร้อมเปิดเสียงบรรยากาศและเสียงฝีเท้า (ระบุโฟลเดอร์ถูกต้องแล้ว)
    scene black
    play music "audio/sound-effect/Hospital.mp3" fadein 3.0                  
    play sound "audio/sound-effect/Sound Effects - Footsteps.mp3" fadein 2.0 

    # 2. แสดงตัวหนังสือชื่อฉากกลางจอ
    show text "{size=80}ฉากที่ 1.2 - มุมมองคนทั่วไป{/size}" at truecenter with dissolve
    pause 1.0

    # 3. กล่องข้อความบรรยายขึ้น
    "เสียงฝีเท้าตามทางเดิน {cps=20}(ตึก... ตึก...){/cps} คลอด้วยเสียงความวุ่นวายในโรงพยาบาล"

    # 4. หลังจากผู้เล่นคลิก -> ซ่อนข้อความชื่อฉาก, เล่นเสียงประตู, และเปิดไฟเข้าห้อง
    hide text with dissolve
    play sound "audio/sound-effect/door_sound.mp3"                          
    
    # ฉากดำจะค่อยๆ ละลายหายไปกลายเป็นห้องพยาบาลภายใน 3 วินาที
    scene medic-room-normal with Dissolve(3.0)
    pause 3.0                                            

    # 5. เปลี่ยนเสียงบรรยากาศรอบตัวให้กลายเป็นเสียงภายในห้องพยาบาล
    stop music fadeout 3.0
    play music "audio/sound-effect/Hospital-room.mp3" fadein 3.0

    show nus with moveinright