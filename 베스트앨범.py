# 장르를 나타내는 문자열, 노래별 재생 횟수
def solution(genres, plays):
    answer = [] # 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return
    
    genres_dict = dict()
    for i in range(len(genres)):
        if genres[i] not in genres_dict:
            genres_dict[genres[i]] = list()
        genres_dict[genres[i]].append((plays[i], i))
    
    sort_genres = []
    # 총합의 순서대로 정렬하는 과정
    for i in genres_dict.keys():
        sort_genres.append((sum(x[0] for x in genres_dict[i]), i))
    sort_genres.sort(reverse=True)
    
    # 장르별 상위 2곡씩 뽑아내는 과정
    for cnt, g in sort_genres:
        music = genres_dict[g]
        music.sort(key=lambda x : (-x[0], x[1]))
        if len(music) >= 2:
            answer += [music[i][1] for i in range(2)]
        else:
            answer += [music[i][1] for i in range(1)]
            
    return answer