# SECURITY MODEL

RION MODS is designed as a companion app and consensual prank tool.

## Threat Model
- Connections are authenticated via short-lived pairing PINs.
- The web controller binds to localhost by default.
- The Prank feature uses standard Android Activity lifecycles and can be dismissed via normal navigation or timer expiry.

## Limitations
- Do not expose the Termux backend to the public internet without configuring a reverse proxy with HTTPS and authentication.
- Android system restrictions prevent unauthorized screen capture. The app requires explicit user consent via the MediaProjection API.
