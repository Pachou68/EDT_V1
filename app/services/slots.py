from datetime import time

def get_week_slots():
    # jour: 1=lun .. 5=ven
    slots = {}

    # Lun-Jeu (10 slots)
    common = [
        (1, time(8,0),  time(8,55)),
        (2, time(8,55), time(9,50)),
        (3, time(9,50), time(10,45)),
        (4, time(11,5), time(12,0)),
        (5, time(12,0), time(12,55)),
        (6, time(13,50), time(14,45)),
        (7, time(14,45), time(15,40)),
        (8, time(15,40), time(16,35)),
        (9, time(16,35), time(17,30)),
        (10,time(17,30), time(18,25)),
    ]

    for d in [1,2,3,4]:
        slots[d] = common

    # Vendredi (9 slots)
    friday = [
        (1, time(8,0),  time(8,55)),
        (2, time(8,55), time(9,50)),
        (3, time(9,50), time(10,45)),
        (4, time(11,5), time(12,0)),
        (5, time(12,0), time(12,55)),
        (6, time(14,30), time(15,25)),
        (7, time(15,25), time(16,20)),
        (8, time(16,20), time(17,15)),
        (9, time(17,15), time(18,10)),
    ]
    slots[5] = friday
    return slots
