# 단어 찾기 도우미 - 외부 연동 래퍼 (작업 4, 설계 옵션 B)
# 키 숨김용 중계 서버가 사용하는 OpenAI(gpt-4o) 호출 모듈. 키는 서버의 .env 에만 보관.
# 후보 찾기(기능1)·상세 보기(기능2) 프롬프트를 이 모듈로 호출한다.
import os
from dotenv import load_dotenv

load_dotenv()

MODEL = "gpt-4o"  # OpenAI 모델. 두루뭉술한 설명으로 적확한 단어 추론 (사용자 선택: OpenAI 전환)


class AIConfigError(Exception):
    """API 키 미설정 등 설정 오류."""


def is_configured():
    return bool(os.getenv("OPENAI_API_KEY"))


def _get_client():
    if not is_configured():
        raise AIConfigError("OPENAI_API_KEY가 설정되지 않았습니다. 서버의 .env를 확인하세요.")
    from openai import OpenAI
    # timeout=45초: AI 응답이 멈춰도 요청이 서버에 무한정 쌓이지 않게 한다
    # (연속 사용 시 [단어 찾기] 버튼이 잠기던 문제의 서버측 방어)
    return OpenAI(timeout=45.0)  # 키는 환경변수(OPENAI_API_KEY)에서 자동 로드


def ask(prompt, max_tokens=1000):
    """프롬프트를 OpenAI(gpt-4o)에 보내 텍스트 응답을 반환한다(웹검색 없음)."""
    client = _get_client()
    resp = client.chat.completions.create(
        model=MODEL,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.choices[0].message.content or ""


def ask_with_web_search(prompt, max_tokens=1000):
    """웹검색 도구를 써서 최신 사실·인물까지 확인해 답하게 한다.

    AI가 모르는 최신 뉴스·인명을 지어내던 문제 대응 — 실제 웹을 찾아보게 한다.
    실패 시(도구 미지원 등) 웹검색 없는 ask()로 자동 대체한다.
    """
    client = _get_client()
    try:
        resp = client.responses.create(
            model=MODEL,
            tools=[{"type": "web_search"}],
            input=prompt,
            max_output_tokens=max_tokens,
        )
        return resp.output_text
    except Exception:
        return ask(prompt, max_tokens=max_tokens)
