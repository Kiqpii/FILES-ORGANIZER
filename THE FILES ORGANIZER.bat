@echo off
setlocal enabledelayedexpansion
title File Organizer

:menu
cls
echo =================================
echo         FILE ORGANIZER
echo =================================
echo.

:: Get input folder path with validation
:input_path
set /p "input_path=Enter folder path to organize (or 'exit' to quit): "
if /i "%input_path%"=="exit" exit
set "folderpath=%USERPROFILE%\%input_path%"

if not exist "%folderpath%" (
    echo Error: Folder not found. Please try again.
    timeout /t 2 >nul
    goto input_path
)

:: Get destination folder name
:dest_folder
echo.
set /p "new_folder=Enter name for destination folder on Desktop: "
set "desktop_path=%USERPROFILE%\Desktop\%new_folder%"

if exist "%desktop_path%" (
    echo.
    echo Warning: Folder already exists. 
    set /p "overwrite=Continue anyway? (Y/N): "
    if /i not "!overwrite!"=="Y" goto dest_folder
)

:: Create main folder
mkdir "%desktop_path%" 2>nul

:: Process files with progress indicator
echo.
echo Processing files...
echo =================================
set "count=0"
set "total=0"

for %%F in ("%folderpath%\*.*") do set /a "total+=1"

for %%F in ("%folderpath%\*.*") do (
    set /a "count+=1"
    set "ext=%%~xF"
    if "!ext!" neq "" (
        set "ext=!ext:~1!"
        if not exist "%desktop_path%\!ext!" mkdir "%desktop_path%\!ext!" 2>nul
        move "%%F" "%desktop_path%\!ext!" >nul 2>&1
        echo Processing !count! of !total! files [!ext! files]
    )
)

echo.
echo =================================
echo Organization complete!
echo Files moved to: %desktop_path%
echo.
echo Press any key to organize another folder...
pause >nul
goto menu
