# RION MODS

A complete Android Remote Companion and Termux Terminal system.
Featuring a native Android app, a premium dark-mode interface, and a Python-powered Termux backend.

## Features
- **Local Network Pairing**: Connect Android and Termux seamlessly via short-lived PINs.
- **Attack Mode (Prank)**: Consensual mock "system override" interface for pranks.
- **Terminal UI**: Hacker-style multi-panel dashboard built with Python Textual.
- **Web Controller**: Optional responsive dashboard for managing sessions.
- **Native Android Client**: Built with Kotlin and Jetpack Compose.

## Termux Setup
1. Clone this repository in Termux.
2. Run `bash scripts/install-termux.sh` to install Python and setup the virtual environment.
3. Start the server: `bash scripts/run-server.sh`
4. Start the terminal: `bash scripts/run-terminal.sh`

## Android Build
This project uses GitHub Actions for continuous integration.
To build locally (requires Android SDK & Gradle):
```bash
cd android
./gradlew assembleDebug
```
The APK will be available in `android/app/build/outputs/apk/debug/app-debug.apk`.

## Security
This application is designed for consensual remote control and pranks between authorized devices. 
It does NOT use exploits, arbitrary shell injections, or silent background data exfiltration.

## License
MIT License
