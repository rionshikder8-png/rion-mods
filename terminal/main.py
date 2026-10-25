import asyncio
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Header, Footer, Static, Input, Log, Label
from textual.reactive import reactive
import httpx
import os
import sys

SERVER_URL = "http://localhost:8000"

class RionTerminal(App):
    CSS = """
    Screen {
        background: #000000;
        color: #00E5FF;
    }
    Header {
        background: #111111;
        color: #B388FF;
    }
    #main-container {
        height: 100%;
        layout: horizontal;
    }
    #left-panel {
        width: 30%;
        border-right: solid #B388FF;
        padding: 1;
    }
    #right-panel {
        width: 70%;
        padding: 1;
    }
    .panel-title {
        color: #D50000;
        text-style: bold;
    }
    Input {
        background: #111111;
        color: #00E5FF;
        border: solid #00E5FF;
    }
    Log {
        height: 1fr;
        background: #000000;
        color: #00E5FF;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Horizontal(id="main-container"):
            with Vertical(id="left-panel"):
                yield Static("RION MODS", classes="panel-title")
                yield Static("v1.0.0", id="version")
                yield Static("\nSTATUS", classes="panel-title")
                yield Static("Server: ONLINE", id="server-status")
                yield Static("Pairs: 0", id="pair-status")
            with Vertical(id="right-panel"):
                yield Static("EVENT LOG", classes="panel-title")
                self.log_widget = Log()
                yield self.log_widget
                yield Input(placeholder="Enter command (/help, /pair create)...", id="cmd-input")
        yield Footer()

    async def on_mount(self) -> None:
        self.log_widget.write_line("[SYSTEM] RION MODS Boot Sequence Initiated...")
        self.log_widget.write_line("[SYSTEM] Loaded Core Modules.")
        self.log_widget.write_line("[SYSTEM] Type /help for commands.")

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        cmd = event.value.strip()
        self.query_one(Input).value = ""
        if not cmd:
            return
        
        self.log_widget.write_line(f"> {cmd}")
        
        if cmd == "/help":
            self.log_widget.write_line("Commands:")
            self.log_widget.write_line("  /pair create   - Create a pairing code")
            self.log_widget.write_line("  /status        - Check server status")
            self.log_widget.write_line("  /clear         - Clear the log")
            self.log_widget.write_line("  /quit          - Exit RION MODS")
        elif cmd == "/pair create":
            try:
                async with httpx.AsyncClient() as client:
                    r = await client.post(f"{SERVER_URL}/pair/create", json={"device_name": "Terminal"})
                    if r.status_code == 200:
                        code = r.json()["pairing_code"]
                        self.log_widget.write_line(f"[SUCCESS] Pairing code: {code} (expires in 5m)")
                    else:
                        self.log_widget.write_line(f"[ERROR] {r.text}")
            except Exception as e:
                self.log_widget.write_line(f"[ERROR] Connection failed: {e}")
        elif cmd == "/status":
            try:
                async with httpx.AsyncClient() as client:
                    r = await client.get(f"{SERVER_URL}/health")
                    self.log_widget.write_line(f"[INFO] Server Health: {r.json()}")
            except Exception as e:
                self.log_widget.write_line(f"[ERROR] {e}")
        elif cmd == "/clear":
            self.log_widget.clear()
        elif cmd == "/quit":
            self.exit()
        else:
            self.log_widget.write_line(f"[WARN] Unknown command: {cmd}")

if __name__ == "__main__":
    app = RionTerminal()
    app.run()
