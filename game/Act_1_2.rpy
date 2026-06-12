# --- ประกาศฉากกระพริบสลับกัน ---
image scene_flicker:
    "medic-room-normal"  # ฉากแรก 
    pause 0.3           
    "medic-room-meat"    # สลับเป็นฉากเนื้อ
    pause 0.3
    repeat               

# --- ประกาศตัวละครกระพริบสลับกัน ---
image char_flicker:
    "nus"                # ตัวละครร่างพยาบาลปกติ
    pause 0.3
    "meat_scaled"               # สลับเป็นร่างเนื้อ
    pause 0.3
    Solid("#0000")       # สลับเป็นภาพโปร่งใส (ตัวละครวับๆ แวมๆ)
    pause 0.3
    repeat

image meat_scaled = im.Scale("sub_Character/meat.png", 2296, 1796)

image nus = im.Scale("sub_Character/4.png", 2296, 1796)


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

    # 🔥 ปรับตรงนี้: ใช้ ATL สั่งเลื่อนตัวละครจากขวามาซ้าย พร้อมขึ้นข้อความทันที
    show nus:
        xpos 1.0 ypos 0.0    # วางตำแหน่งเริ่มต้นไว้ที่นอกจอฝั่งขวาสุด (xpos 1.0)
        linear 1.2 xpos -0.25  # ค่อยๆ เลื่อนมาทางซ้ายจนเต็มจอ (xpos 0.0) ภายในเวลา 1.2 วินาที

    nuse"น่าสงสารจัง..."
    nuse"คนไข้รอดชีวิตจากอุบัติเหตุรถยนต์...ครอบครัว...ของเขา"
    nuse"เสียชีวิตกันหมดเลย..."
    nuse"ตอนนี้เขามีอาการข้างเคียงจากการผ่าตัดสมองขั้นรุนแรง"
    nuse"เขาไม่ยอมให้ใครเข้าใกล้เลย...แม้แต่พยาบาลที่ดูแลเขาอยู่ทุกวัน"
    nuse"เขามักจะเอามือกุมหู กรีดร้องโวยวายเหมือนคนเสียสติอยู่ตลอดเวลา"
    nuse"แววตาของเขาช่างโดดเดี่ยวและน่ากลัวเหลือเกิน"
    nuse"เหมือนเขากำลังติดอยู่ในนรกที่พวกเรามองไม่เห็น..."

    stop music fadeout 3.0
    play sound "audio/sound-effect/Tension_Flashback.mp3"
    $ renpy.pause(4.0, hard=True)
    
    scene scene_flicker
    show char_flicker:
        xpos -0.25 ypos 0.0

    
    pause 3.0

   
    scene black with dissolve
jump Act2_1