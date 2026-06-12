label stupid_endding:
    window hide
    scene black
<<<<<<< HEAD
    pause 5.0
    scene stupid_video
=======
    pause 0.2
    scene stupid_video with dissolve
>>>>>>> 013b7bab11ced6ab138cfd5a8e5e83f653f80b7c
    $ renpy.pause(2.0, hard=True)
    scene black with dissolve
    pause 0.5

    show text "{size=46}คมเศษแก้วกรีดลึกผ่านผิวเนื้อ...{w=0.8} ปลุกความเจ็บปวดอันบ้าคลั่งให้ตื่นขึ้น{/size}" at truecenter with dissolve
    pause
    hide text with dissolve

    show text "{size=46}ทว่าเพียงชั่วเคี้ยวหมากแหลก...{w=0.8} ทั้งความทรมานและเสียงเรียกอันห่วงใยของเธอ{/size}" at truecenter with dissolve
    pause
    hide text with dissolve

    show text "{size=46}ก็ค่อยๆ แผ่วเบา...{w=0.5} และลอยห่างออกไปไกลแสนไกล{/size}" at truecenter with dissolve
    pause
    hide text with dissolve

    show text "{size=46}ความเย็นยะเยือกสายหนึ่งไหลบ่าเข้าแทนที่...{w=0.8} โอบอุ้มร่างที่สั่นเทาเอาไว้{/size}" at truecenter with dissolve
    pause
    hide text with dissolve

    show text "{size=46}ในท้ายที่สุด...{w=0.6} เปลือกตาของผมก็หนักอึ้งเกินกว่าจะฝืน{/size}" at truecenter with dissolve
    pause
    hide text with dissolve

    show text "{size=46}สติรับรู้ค่อยๆ เลือนหาย...{w=0.8} จมดิ่งสู่ห้วงนิทราอันเป็นนิรันดร์{/size}" at truecenter with dissolve
    pause
    hide text with dissolve
    pause 0.5
    scene StupidEndding with dissolve
    $ renpy.pause(5.0, hard=True)
    
    $ renpy.full_restart()