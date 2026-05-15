@echo off

set RAWPY_USE_SYSTEM_LIBRAW=1

%PYTHON% -m pip install . -vv --no-deps --no-build-isolation
if errorlevel 1 exit 1
