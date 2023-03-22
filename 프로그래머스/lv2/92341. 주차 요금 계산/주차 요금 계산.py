from math import ceil
def solution(fees, records):
    answer = []
    b_time, b_fee, u_time, u_fee = fees
    parking_lot = {}
    times = {}
    for record in records:
        time, car_n, in_out = record.split()
        hour, minute = map(int, time.split(":"))
        if in_out == "IN":
            parking_lot[car_n] = (hour, minute)
            if car_n not in times:
                times[car_n] = 0 
        elif in_out == "OUT":
            parking_h = hour - parking_lot[car_n][0]
            parking_m = minute-parking_lot[car_n][1]
            total_m = parking_h*60+parking_m
            times[car_n] += total_m
            parking_lot[car_n] = 0
    for car in parking_lot.keys():
        if parking_lot[car]:
            parking_h = 23 - parking_lot[car][0]
            parking_m = 59 - parking_lot[car][1]
            total_m = parking_h*60+parking_m
            times[car] += total_m
            parking_lot[car] = 0
    for car in sorted(list(times.keys())):
        fee = b_fee
        if times[car] > b_time:
            overtime = times[car] - b_time
            fee += int(ceil(overtime/u_time))*u_fee
        answer.append(fee)
    return answer
