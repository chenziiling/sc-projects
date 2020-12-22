"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow


def main():
    w = GWindow(1016, 500, title='draw')
    background(w)
    cat(w)
    star(w)


def background(w):
    for i in range(127):
        'red to yellow'
        r = GRect(2, 500, x=0+i*2, y=0)
        r.fill_color = (255, 0+i*2, 0)
        r.color = (255, 0+i*2, 0)
        r.filled = True
        w.add(r)
    for k in range(127):
        'yellow to green'
        y = GRect(2, 500, x=254+k*2, y=0)
        y.fill_color = (255-k*2, 255, 0)
        y.color = (255-k*2, 255, 0)
        y.filled = True
        w.add(y)
    for j in range(127):
        'green to blue'
        b = GRect(2, 500, x=508+j*2, y=0)
        b.fill_color = (0, 255-j*2, 0+j*2)
        b.color = (0, 255-j*2, 0+j*2)
        b.filled = True
        w.add(b)
    for a in range(127):
        'blue to purple'
        p = GRect(2, 500, x=762+a*2, y=0)
        p.fill_color = (0+a*2, 0, 255)
        p.color = (0+a*2, 0, 255)
        p.filled = True
        w.add(p)


def cat(w):

    r34 = GRect(210, 130, x=150, y=160)
    r34.fill_color = (178, 87, 114)
    r34.filled = True
    w.add(r34)
    r35 = GRect(10, 110, x=140, y=170)
    r35.fill_color = 'black'
    r35.filled = True
    w.add(r35)
    r36 = GRect(10, 10, x=150, y=160)
    r36.fill_color = 'black'
    r36.filled = True
    w.add(r36)
    r37 = GRect(210, 10, x=160, y=150)
    r37.fill_color = 'black'
    r37.filled = True
    w.add(r37)
    r38 = GRect(10, 10, x=150, y=280)
    r38.fill_color = 'black'
    r38.filled = True
    w.add(r38)
    r39 = GRect(210, 10, x=160, y=290)
    r39.fill_color = 'black'
    r39.filled = True
    w.add(r39)
    'body'

    r40 = GRect(10, 10, x=170, y=300)
    r40.fill_color = 'black'
    r40.filled = True
    w.add(r40)
    r41 = GRect(10, 10, x=180, y=310)
    r41.fill_color = 'black'
    r41.filled = True
    w.add(r41)
    r42 = GRect(10, 10, x=190, y=320)
    r42.fill_color = 'black'
    r42.filled = True
    w.add(r42)
    r44 = GRect(10, 30, x=200, y=300)
    r44.fill_color = 'black'
    r44.filled = True
    w.add(r44)
    r45 = GRect(10, 10, x=240, y=300)
    r45.fill_color = 'black'
    r45.filled = True
    w.add(r45)
    r46 = GRect(10, 10, x=250, y=310)
    r46.fill_color = 'black'
    r46.filled = True
    w.add(r46)
    r47 = GRect(10, 10, x=260, y=320)
    r47.fill_color = 'black'
    r47.filled = True
    w.add(r47)
    r48 = GRect(10, 30, x=270, y=300)
    r48.fill_color = 'black'
    r48.filled = True
    w.add(r48)
    'back feet'

    r49 = GRect(20, 20, x=120, y=240)
    r49.fill_color = 'black'
    r49.filled = True
    w.add(r49)
    r50 = GRect(30, 20, x=90, y=220)
    r50.fill_color = 'black'
    r50.filled = True
    w.add(r50)
    r51 = GRect(40, 20, x=70, y=200)
    r51.fill_color = 'black'
    r51.filled = True
    w.add(r51)
    'tail'

    for i in range(3):
        for j in range(4):
            pot = GOval(10, 10, x=170+j*40, y=180+i*30)
            pot.fill_color = (238, 79, 114)
            pot.color = (238, 79, 114)
            pot.filled = True
            w.add(pot)
    'pots'

    r1 = GRect(10, 100, x=350, y=180)
    r1.fill_color = 'black'
    r1.filled = True
    w.add(r1)
    r2 = GRect(10, 10, x=360, y=280)
    r2.fill_color = 'black'
    r2.filled = True
    w.add(r2)
    r3 = GRect(10, 10, x=370, y=290)
    r3.fill_color = 'black'
    r3.filled = True
    w.add(r3)
    r4 = GRect(125, 10, x=380, y=300)
    r4.fill_color = 'black'
    r4.filled = True
    w.add(r4)
    r5 = GRect(10, 10, x=505, y=290)
    r5.fill_color = 'black'
    r5.filled = True
    w.add(r5)
    r6 = GRect(10, 10, x=515, y=280)
    r6.fill_color = 'black'
    r6.filled = True
    w.add(r6)
    r7 = GRect(10, 100, x=525, y=180)
    r7.fill_color = 'black'
    r7.filled = True
    w.add(r7)
    r8 = GRect(10, 50, x=515, y=130)
    r8.fill_color = 'black'
    r8.filled = True
    w.add(r8)
    r9 = GRect(25, 10, x=490, y=120)
    r9.fill_color = 'black'
    r9.filled = True
    w.add(r9)
    r10 = GRect(10, 10, x=480, y=130)
    r10.fill_color = 'black'
    r10.filled = True
    w.add(r10)
    r11 = GRect(10, 10, x=470, y=140)
    r11.fill_color = 'black'
    r11.filled = True
    w.add(r11)
    r12 = GRect(55, 10, x=415, y=150)
    r12.fill_color = 'black'
    r12.filled = True
    w.add(r12)
    r13 = GRect(10, 10, x=405, y=140)
    r13.fill_color = 'black'
    r13.filled = True
    w.add(r13)
    r14 = GRect(10, 10, x=395, y=130)
    r14.fill_color = 'black'
    r14.filled = True
    w.add(r14)
    r15 = GRect(25, 10, x=370, y=120)
    r15.fill_color = 'black'
    r15.filled = True
    w.add(r15)
    r16 = GRect(10, 50, x=360, y=130)
    r16.fill_color = 'black'
    r16.filled = True
    w.add(r16)
    'face'

    r17 = GRect(20, 20, x=395, y=180)
    r17.fill_color = 'black'
    r17.filled = True
    w.add(r17)
    r18 = GRect(20, 20, x=470, y=180)
    r18.fill_color = 'black'
    r18.filled = True
    w.add(r18)
    r19 = GRect(10, 10, x=395, y=180)
    r19.fill_color = 'white'
    r19.color = 'white'
    r19.filled = True
    w.add(r19)
    r20 = GRect(10, 10, x=470, y=180)
    r20.fill_color = 'white'
    r20.color = 'white'
    r20.filled = True
    w.add(r20)
    'eyes'

    r22 = GRect(10, 10, x=385, y=235)
    r22.fill_color = 'black'
    r22.filled = True
    w.add(r22)
    r23 = GRect(10, 10, x=435, y=235)
    r23.fill_color = 'black'
    r23.filled = True
    w.add(r23)
    r24 = GRect(10, 10, x=480, y=235)
    r24.fill_color = 'black'
    r24.filled = True
    w.add(r24)
    r25 = GRect(105, 10, x=385, y=245)
    r25.fill_color = 'black'
    r25.filled = True
    w.add(r25)
    'mouth'

    r26 = GRect(10, 10, x=410, y=310)
    r26.fill_color = 'black'
    r26.filled = True
    w.add(r26)
    r27 = GRect(10, 10, x=420, y=320)
    r27.fill_color = 'black'
    r27.filled = True
    w.add(r27)
    r28 = GRect(10, 10, x=430, y=330)
    r28.fill_color = 'black'
    r28.filled = True
    w.add(r28)
    r29 = GRect(10, 30, x=440, y=310)
    r29.fill_color = 'black'
    r29.filled = True
    w.add(r29)
    r33 = GRect(10, 10, x=465, y=310)
    r33.fill_color = 'black'
    r33.filled = True
    w.add(r33)
    r32 = GRect(10, 10, x=475, y=320)
    r32.fill_color = 'black'
    r32.filled = True
    w.add(r32)
    r30 = GRect(10, 10, x=485, y=330)
    r30.fill_color = 'black'
    r30.filled = True
    w.add(r30)
    r31 = GRect(10, 30, x=495, y=310)
    r31.fill_color = 'black'
    r31.filled = True
    w.add(r31)
    'foot'


def star(w):
    o1 = GOval(40, 10, x=700, y=170)
    o1.fill_color = 'white'
    o1.color = 'white'
    o1.filled = True
    w.add(o1)
    o2 = GOval(10, 40, x=750, y=130)
    o2.fill_color = 'white'
    o2.color = 'white'
    o2.filled = True
    w.add(o2)
    o3 = GOval(40, 10, x=770, y=170)
    o3.fill_color = 'white'
    o3.color = 'white'
    o3.filled = True
    w.add(o3)
    o4 = GOval(10, 40, x=750, y=190)
    o4.fill_color = 'white'
    o4.color = 'white'
    o4.filled = True
    w.add(o4)

    o5 = GOval(40, 10, x=600, y=380)
    o5.fill_color = 'white'
    o5.color = 'white'
    o5.filled = True
    w.add(o5)
    o6 = GOval(10, 40, x=650, y=340)
    o6.fill_color = 'white'
    o6.color = 'white'
    o6.filled = True
    w.add(o6)
    o7 = GOval(40, 10, x=670, y=380)
    o7.fill_color = 'white'
    o7.color = 'white'
    o7.filled = True
    w.add(o7)
    o8 = GOval(10, 40, x=650, y=400)
    o8.fill_color = 'white'
    o8.color = 'white'
    o8.filled = True
    w.add(o8)

    o9 = GOval(40, 10, x=850, y=130)
    o9.fill_color = 'white'
    o9.color = 'white'
    o9.filled = True
    w.add(o9)
    o10 = GOval(10, 40, x=900, y=90)
    o10.fill_color = 'white'
    o10.color = 'white'
    o10.filled = True
    w.add(o10)
    o11 = GOval(40, 10, x=920, y=130)
    o11.fill_color = 'white'
    o11.color = 'white'
    o11.filled = True
    w.add(o11)
    o12 = GOval(10, 40, x=900, y=150)
    o12.fill_color = 'white'
    o12.color = 'white'
    o12.filled = True
    w.add(o12)

    l = GLabel('Nyan cat meme 2.0', x=690, y=330)
    l.color = 'white'
    l.font = '-30'
    w.add(l)


if __name__ == '__main__':
    main()
