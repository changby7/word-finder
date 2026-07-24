# 단어 찾기 도우미

대화 중 떠오르지 않는 단어를 **음성으로 설명하면 적확한 단어 후보 3~5개**를 찾아주는 모바일 웹앱입니다. "설단 현상"으로 대화가 막히지 않게 돕습니다.

## 주요 기능
- **음성 설명 → 단어 후보 찾기** — 후보 3~5개(한국어·영어), 각 한 줄 뜻·언어 표시
- **뜻·예문·유의어 상세 보기** — 고른 단어의 정확한 뜻 + 예문 1~2개 + 유의어 2~3개
- 확실하지 않은 인명·사실은 지어내지 않고 "확실하지 않음"으로 표시(웹검색으로 확인된 것만)
- 타이핑 없이 음성만으로 완료 가능(마이크 불가 시 타이핑 대체)

## 기술 스택
- 화면: HTML / CSS / JavaScript + 브라우저 음성인식(Web Speech API)
- 백엔드: **키 보호용 최소 중계 서버**(Flask) — AI 키를 브라우저에 노출하지 않음
- AI 모델: OpenAI `gpt-4o` (+ 웹검색)

## 로컬 실행
1. Python 3.12 설치 → `pip install -r requirements.txt`
2. `.env.example`을 복사해 `.env` 생성 후 키 입력
   ```
   OPENAI_API_KEY=sk-...본인 키...
   # (선택) 접근 비밀번호
   # APP_USER=admin
   # APP_PASSWORD=원하는-비밀번호
   ```
3. `python server.py` (Windows는 `실행.bat` 더블클릭도 가능) → http://127.0.0.1:5001

## Vercel 배포
이 저장소에는 Vercel 배포 설정(`vercel.json`, `api/index.py`)이 포함돼 있습니다.
1. 이 저장소를 [Vercel](https://vercel.com)에서 **Import**
2. **Settings → Environment Variables**에 등록 (코드·저장소에는 키를 넣지 않습니다)
   - `OPENAI_API_KEY` = 본인 OpenAI 키
   - (권장) `APP_USER`, `APP_PASSWORD` = 접근 로그인용
3. **Deploy** → 발급된 `https://...vercel.app` 주소로 접속
   - 마이크(음성인식)는 HTTPS 주소에서 동작하므로 Chrome 권장

> ⚠️ 배포 주의: 공개 주소로 검색이 실행되면 본인 OpenAI 크레딧이 소모됩니다. `APP_PASSWORD`로 접근을 잠그고, OpenAI 대시보드에서 **월 사용 한도**를 설정하세요. Vercel 무료 요금제는 함수 실행 시간 제한이 있어, 웹검색이 오래 걸리는 질문은 시간 초과될 수 있습니다.

## 보안
- **`.env`는 절대 커밋하지 않습니다**(`.gitignore`에 등록됨). 배포 키는 Vercel 환경변수로만 관리하세요.
- 음성·설명은 서버에 저장하지 않습니다.

## 문서
[PRD](PRD2.md) · [PLAN](PLAN.md) · [DESIGN](DESIGN.md) · [CHECK](CHECK.md) · [규칙(CLAUDE.md)](CLAUDE.md)
