const SERVER_URL = 'http://localhost:8000';

function log(msg) {
    const el = document.getElementById('log');
    const p = document.createElement('p');
    p.textContent = `> ${msg}`;
    el.appendChild(p);
    el.scrollTop = el.scrollHeight;
}

async function checkHealth() {
    try {
        const res = await fetch(`${SERVER_URL}/health`);
        const data = await res.json();
        document.getElementById('status').textContent = 'Online';
        log(`Server health: ${JSON.stringify(data)}`);
    } catch (e) {
        document.getElementById('status').textContent = 'Offline';
        log(`Health check failed: ${e.message}`);
    }
}

async function createPairing() {
    try {
        const res = await fetch(`${SERVER_URL}/pair/create`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({device_name: 'WebController'})
        });
        const data = await res.json();
        log(`Pairing code created: ${data.pairing_code}`);
    } catch (e) {
        log(`Pairing failed: ${e.message}`);
    }
}

async function fetchSessions() {
    try {
        const res = await fetch(`${SERVER_URL}/sessions`);
        const data = await res.json();
        const list = document.getElementById('sessions-list');
        list.innerHTML = '';
        for (const [token, session] of Object.entries(data.sessions)) {
            const li = document.createElement('li');
            li.textContent = `${session.device_name} (Prank Active: ${session.prank_active})`;
            list.appendChild(li);
        }
        log('Sessions refreshed.');
    } catch (e) {
        log(`Failed to fetch sessions: ${e.message}`);
    }
}

// Init
checkHealth();
