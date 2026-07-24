@echo off
cd /d "%~dp0"
echo ============================================
echo   단어 찾기 도우미 - 서버를 시작합니다
echo ============================================
echo.
echo  브라우저에서 아래 주소로 접속하세요:
echo    http://127.0.0.1:5001
echo.
echo  로그인 - 아이디: admin  비밀번호: .env 파일의 APP_PASSWORD 값
echo  마이크를 쓰려면 Chrome 으로 접속하세요.
echo  끄려면 이 창을 닫거나 Ctrl+C 를 누르세요.
echo.
"C:\Users\USER\AppData\Local\Programs\Python\Python312\python.exe" server.py
echo.
echo [서버가 종료되었습니다. 오류 메시지가 있으면 위 내용을 확인하세요.]
pause
