# Python Print Formatting Project

이 프로젝트는 Python의 다양한 출력(`print`) 방식과 문자열 포매팅을 연습하기 위해 작성되었습니다.  
f-string, `format()`, `%` 연산자 등 여러 스타일을 비교하고, Jupyter Notebook과 Python 스크립트 양쪽에서 실행할 수 있습니다.

---

## 📂 프로젝트 구성

- **main_print_v1.ipynb**  
  - Jupyter Notebook 버전 코드
  - 출력 방식 실습 및 결과 확인 가능  

- **main_print_v1.py**  
  - 문자열 포매팅 예제 코드 (버전 1):contentReference[oaicite:2]{index=2}

- **main_print_v2.py**  
  - 개선된 포맷팅 예제 코드 (버전 2, v1 확장)

- **requirements.txt**  
  - 프로젝트 실행에 필요한 Python 패키지 목록:contentReference[oaicite:3]{index=3}  
  - 주요 라이브러리:  
    - `rich` : 터미널 출력 스타일링  
    - `Pygments` : 코드 하이라이팅  
    - `markdown-it-py`, `mdurl` : Markdown 관련 처리  

- **869b1b0a-4862-4740-9663-f8b1b06fa05a.png**  
  - 출력 예시 이미지 (프로젝트 시각 자료)

---

## 🚀 실행 방법

1. 패키지 설치:
   ```bash
   pip install -r requirements.txt

## python 코드 실행

python main_print_v1.py

python main_print_v2.py

## Jupyter Notebook 실행
jupyter notebook main_print_v1.ipynb
