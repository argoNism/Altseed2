echo set current directory
cd /d %~dp0

mkdir ..\build

cd /d ..\build

cmake -A x64 -D BUILD_TEST=ON USE_MSVC_RUNTIME_LIBRARY_DLL=ON ../

pause