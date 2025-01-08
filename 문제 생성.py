import os
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


def create_problem_folder_with_samples(category, problem_id):
    """
    카테고리와 문제 ID를 기반으로 디렉토리를 생성하고,
    입력 및 출력 예제를 크롤링하여 저장합니다.

    :param category: 문제 카테고리 (예: "구현")
    :param problem_id: 문제 ID (예: "1000")
    """
    base_path = os.getcwd()  # 현재 작업 디렉토리
    category_path = os.path.join(base_path, category)
    problem_path = os.path.join(category_path, problem_id)

    # 디렉토리 생성
    os.makedirs(problem_path, exist_ok=True)
    print(f"Created folder: {problem_path}")

    # 입력 및 출력 예제 가져오기
    input_examples, output_examples = fetch_boj_samples(problem_id)

    # 파일 생성
    solution_file = os.path.join(problem_path, "solution.py")
    input_file = os.path.join(problem_path, "input.txt")
    output_file = os.path.join(problem_path, "output.txt")

    if not os.path.exists(solution_file):
        with open(solution_file, 'w') as f:
            f.write(f"# {problem_id} 문제 풀이\n")
        print(f"Created file: {solution_file}")

    if input_examples:
        with open(input_file, 'w') as f:
            f.write("\n".join(input_examples))
        print(f"Created file: {input_file} with sample inputs.")

    if output_examples:
        with open(output_file, 'w') as f:
            f.write("\n".join(output_examples))
        print(f"Created file: {output_file} with sample outputs.")


# 사용 예시
category = input("카테고리 입력 (예: 구현): ")
problem_id = input("문제 ID 입력 (예: 1000): ")
create_problem_folder_with_samples(category, problem_id)
