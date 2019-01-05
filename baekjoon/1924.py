# https://www.acmicpc.net/problem/1924
# 둠스데이(Doomsday) 알고리즘 활용

def main():
    # 요일
    day_of_week = ("SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT")
    # doomsday
    doomsday = (31, 28, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12)
    # 2007년 doomsday 요일 구하기(2000년 기준 요일은 화요일)
    doomsday_basic = int(int(7/12) + (7%12) + int(7%12/4))%7 + 2 # =3
    # input 월 / 일
    input_date = input().split()
    month = int(input_date[0])
    day =  int(input_date[1])
    # 요일 계산
    print(day_of_week[((day - doomsday[month-1])%7 + doomsday_basic)%7])

if __name__ == "__main__":
    main()