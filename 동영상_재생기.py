def trans_seconds(time):
    time = time.split(":")
    return int(time[0]) * 60 + int(time[1])

def trans_date(time):
    minute = str(time // 60).zfill(2)
    second = str(time % 60).zfill(2)
    return minute + ":" + second
        

def check_op(current, op_start, op_end):
    if op_start <= current <= op_end:
        current = op_end
    return current

def prev(current):
    if current <= 10:
        return 0
    return current - 10

def next(current, video_len):
    if current >= video_len - 10:
        return video_len
    return current + 10
        

# 동영상 길이, 재생 위치, 오프닝 시작 시간, 끝나는 시간, 명령어
def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len = trans_seconds(video_len)
    op_start = trans_seconds(op_start)
    op_end = trans_seconds(op_end)
    pos = trans_seconds(pos)
    
    pos = check_op(pos, op_start, op_end)
    
    for command in commands:
        # 10초 전
        if command == "prev":
            pos = prev(pos)
        # 10초 후
        elif command == "next":
            pos = next(pos, video_len)
        # 오프닝 시간대에 있는지 확인
        pos = check_op(pos, op_start, op_end)
    
    return trans_date(pos)