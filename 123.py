import requests
from bs4 import BeautifulSoup


def fetch_boj_samples(problem_id):
    """
    백준 문제에서 입력 및 출력 예제를 크롤링하여 반환합니다.

    :param problem_id: 백준 문제 번호 (예: "1000")
    :return: 입력 예제와 출력 예제의 리스트 (input_examples, output_examples)
    """
    url = f"https://www.acmicpc.net/problem/{problem_id}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Referer': f'https://www.acmicpc.net/problem/{problem_id}'
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"문제 {problem_id}를 가져오는데 실패했습니다. HTTP 상태: {response.status_code}")
        return [], []

    soup = BeautifulSoup(response.text, 'html.parser')

    # 'pre' 태그를 선택하여 그 안의 텍스트를 크롤링합니다.
    input_examples = [tag.text.strip() for tag in soup.find_all('pre', class_='sampledata') if
                      'sample-input' in tag.get('id', '')]
    output_examples = [tag.text.strip() for tag in soup.find_all('pre', class_='sampledata') if
                       'sample-output' in tag.get('id', '')]

    # 빈 줄을 제거합니다.
    input_examples = [line for example in input_examples for line in example.splitlines() if line.strip()]
    output_examples = [line for example in output_examples for line in example.splitlines() if line.strip()]

    return input_examples, output_examples


input_examples, output_examples = fetch_boj_samples(4153)

print("입력 예제:")
print(input_examples)
print()
print("출력 예제:")
print(output_examples)
