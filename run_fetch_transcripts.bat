@echo off
echo ============================================
echo  Robert Murray-Smith Transcript Fetcher
echo  Keep Windscribe VPN ON during this run!
echo ============================================
echo.

cd /d "%~dp0"
python scripts\refetch_transcripts.py

echo.
echo ============================================
echo  Done! You can close this window.
echo  Next step: run_summarize.bat
echo ============================================
pause
