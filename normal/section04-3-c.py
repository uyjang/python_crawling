# Section04-3
# Requests
# requests 사용 스크랩핑(3) - Rest API

import requests

# Rest API GET, POST, DELETE, PUT:UPDATE, REPLACE (FETCH : UPDATE, MODIFY)

# url을 활용해서 자원의 상태 정보를 주고 받는 모든 것을 의미

# GET: www.movies.com/movies 영화정보를 모두 주회
# GET: www.movies.com/movies/:id : id가 몇번인 영화를 조회
# POST: www.movies.com/movies : 영화를 생성
# PUT : www.movies.com/movies : 기존 영화를 수정
# DELETE : www.movies.com/movies 기존영화를 삭제

# https://jsonplaceholder.typicode.com/posts

# 세션 활성화
s = requests.Session()

# *예제1*
# 요청1
r = s.get('https://api.github.com/events')

# 수신 상태 체크
r.raise_for_status()  # 또는 status_code 체크 # 예외가 발생했을 때 처리해주고 어떤 예외 혹은 오류인지 표시해줌

# 출력
print(r.text)

# *예제2*
# 쿠키 설정
jar = requests.cookies.RequestsCookieJar()

# 쿠키 삽입
jar.set('name', 'niceman', domain='httpbin.org', path='/cookies') 


# 요청2
r = s.get('http://httpbin.org/cookies', cookies=jar)

# 출력
print(r.text)


# *예제3*
# 요청3
r = s.get('https://github.com', timeout=5)

# 출력
print(r.text)


# *예제4*
# 요청4
r = s.post('http://httpbin.org/post', data={'kim': 'stellar'}, cookies=jar)

# 출력
print(r.text)

# 헤더 정보
print(r.headers)


# *예제5*
# 요청5(POST)
payload1 = {'name': 'kim', 'pay': 'true'}
payload2 = (('name', 'park'), ('pay', 'false'))

r = s.post("http://httpbin.org/post", data=payload2)

# 출력
print(r.text)


# *예제6*
# 요청5(PUT)
r = s.put('http://httpbin.org/put', data={'data': '{"name": "Kim", "grade": "A"}'})

# 출력
print(r.text)


# *예제6*
# 요청6(DELETE)
r = s.delete('http://httpbin.org/delete')

# 출력
print(r.text)


# *예제7*
# 요청7(DELETE)
r = s.delete('https://jsonplaceholder.typicode.com/posts/1')
print(r.text)

s.close()
