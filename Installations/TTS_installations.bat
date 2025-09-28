@echo off
echo Installing SpeechT5 TTS dependencies...
echo.

echo Installing transformers...
pip install transformers
if %errorlevel% neq 0 echo Failed to install transformers && pause && exit /b 1

echo Installing datasets...
pip install datasets
if %errorlevel% neq 0 echo Failed to install datasets && pause && exit /b 1

echo Installing torch...
pip install torch
if %errorlevel% neq 0 echo Failed to install torch && pause && exit /b 1

echo Installing sentencepiece...
pip install sentencepiece
if %errorlevel% neq 0 echo Failed to install sentencepiece && pause && exit /b 1

echo Installing soundfile...
pip install soundfile
if %errorlevel% neq 0 echo Failed to install soundfile && pause && exit /b 1

echo.
echo SpeechT5 TTS installation complete!
echo Press any key to close...
pause >nul
