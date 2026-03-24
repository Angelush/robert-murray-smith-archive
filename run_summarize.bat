@echo off
echo ============================================
echo  Robert Murray-Smith Video Summarizer
echo  Uses Claude Pro via CLI (no API credits)
echo ============================================
echo.

cd /d "%~dp0"
python scripts\04_summarize.py

echo.
echo ============================================
echo  Done! Now building indexes...
echo ============================================

python scripts\05_build_indexes.py

echo.
echo ============================================
echo  Building navigation catalog...
echo ============================================

python scripts\06_build_navigation.py

echo.
echo  All done! Indexes and navigation rebuilt.
pause
