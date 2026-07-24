# Vercel 서버리스 진입점 — 루트의 Flask 앱(server.py)을 그대로 사용
# Vercel Python 런타임은 이 파일의 WSGI `app` 을 자동으로 서빙한다.
import os
import sys

# 루트 폴더(server.py, templates/ 위치)를 import 경로에 추가
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server import app  # noqa: E402  (Flask WSGI 애플리케이션)
