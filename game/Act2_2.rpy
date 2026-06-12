label Act2_2:
    window hide
    
    # 1. ปรับบรรยากาศจอให้มืดมน โทนสีหม่นเทา
    # สมมติว่ามีภาพฉากชื่อ bg_abandoned_house ที่แต่งสีโทนหม่นไว้แล้ว
    scene House_Normal with dissolve
    
    # ดึงอารมณ์ด้วยเสียงบรรยากาศซอมซ่อ หรือเสียงแมลงวันตอมศพ
    play sound "sound-effect/nature.mp3" loop fadein 2.0
    show bas normal :
        zoom 2.0
        xalign -0.15
        yalign 1.0
    with dissolve
    bas "นนท์... นายหายหัวมาอยู่บ้านร้างหลังนี้เองเหรอ?"
    show bas talk :
        zoom 2.0
        xalign -0.15
        yalign 1.0
    scene house_room2 with dissolve
    bas "จวยเอ๊ย! กลิ่นเหม็นเน่าอะไรในบ้านนี้วะเนี่ย?! กลิ่นคาวเลือดโชยมาจนฉันจะอ้วก..."

    stop sound fadeout 1.5

    # 2. จังหวะชะโงกหน้าดูในห้องนอน และเจอภาพสยองขวัญ
    # ใช้ vpunch เพื่อให้หน้าจอกระตุก แทนอาการตาเบิกกว้างด้วยความสยองสุดขีด
    with vpunch
    
    # เอฟเฟกต์ตกใจ (Shock Sound)
    play sound "sound-effect/shock.mp3"
    show bas panic :
        zoom 2.0
        xalign -0.15
        yalign 1.0
    bas "เฮ้ย!! เชี่ยอะไรวะนั่น!!"
    scene house_room with dissolve
    show nonSleep:
        zoom 0.5
        xalign 0.85
        yalign 0.6
    with dissolve
    
    bas "นนท์นั่งอยู่บนพื้นบ้านผุๆ แววตามันดูลอยๆ มีความสุขเชื่อมเชื่อม..."
    
    bas "มันกำลังนอนหนุน... ไม่ใช่สิ!"
    



    bas "มันกำลังนอนหนุนก้อนเนื้อเหลวขนาดยักษ์ที่มีหนวดตะปุ่มตะป่ำยั้วเยี้ย!"
    scene house_room2 with dissolve
    bas "สัตว์ประหลาดตัวนั้นกำลังเอาหนวดเมือกๆ ลูบหัวนนท์..."

    # 4. ฉากกินศพชวนอ้วก
    # เร่งเสียงฉีกเนื้อ หรือเสียงเคี้ยวแจ๊บๆ (Squish/Chewing Sound) บิิ้วด์อารมณ์
    play sound "sound-effect/eating_raw_meat.mp3"

    bas "แล้วที่ปากของนนท์... หมอนั่นกำลังเคี้ยวเศษเนื้อดิบๆ เน่าๆ ที่พึ่งแงะออกมาจากอวัยวะภายในของศพมนุษย์ที่กองอยู่ข้างตู้เสื้อผ้าอย่างเอร็ดอร่อย!!"

    # หน้าจอสั่นอีกรอบตอนบาสจะอ้วกและสติหลุด
    with hpunch
    
    bas "อ้วก...!! นนท์เปลี่ยนไปเป็นปีศาจกินคนไปแล้วเหรอวะ?!"
    
    # หยุดจังหวะให้ผู้เล่นซึมซับความหลอนก่อนตัดฉาก
    pause 2.0
    
    # เคลียร์ฉากเข้าสู่ความมืดเพื่อไปฉากถัดไป
    scene black with dissolve
    
    # คืนค่าหน้าต่างคำพูดมาตรฐาน
    window show