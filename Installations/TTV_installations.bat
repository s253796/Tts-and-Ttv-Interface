@echo off
echo Installing CogVideoX Text-to-Video dependencies...
echo.

echo Installing/upgrading transformers...
pip install --upgrade transformers
if %errorlevel% neq 0 echo Failed to install transformers && pause && exit /b 1

echo Installing accelerate...
pip install accelerate
if %errorlevel% neq 0 echo Failed to install accelerate && pause && exit /b 1

echo Installing diffusers...
pip install diffusers
if %errorlevel% neq 0 echo Failed to install diffusers && pause && exit /b 1

echo Installing imageio-ffmpeg...
pip install imageio-ffmpeg
if %errorlevel% neq 0 echo Failed to install imageio-ffmpeg && pause && exit /b 1

echo Installing PyTorch with CUDA support...
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
if %errorlevel% neq 0 echo Failed to install PyTorch with CUDA && pause && exit /b 1

echo.
echo CogVideoX Text-to-Video installation complete!
echo Press any key to close...
pause >nul
