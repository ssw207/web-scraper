from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("웹사에트에 요청할 수 없습니다.")
else:
    soup = BeautifulSoup(response.text, "html.parser") # 읽은 text를 html로 파싱한다
    #print(soup.find_all('title')) # title 태그만 읽어온다
    jobs = soup.find_all('section', class_="jobs")  # section 태그의 class 가 jobs인 태그를 읽어온다.
    for job_section in jobs:
        job_posts = job_section.find_all('li') # job_section 하위 li태그출력
        job_posts.pop(-1) # 마지막 리스트의 항목을 제거
        for post in job_posts:
            anchors = post.find_all('a')
            anchor = anchors[1] # 첫번째 a 태그 추출
            link = anchor['href'] # dictionary 자료구조
            company, kind, region = anchor.find_all('span', class_="company")
            title = anchor.find('span', class_='title')
            print(company, kind, region, title)
            print("/////////////")
            print("/////////////")


