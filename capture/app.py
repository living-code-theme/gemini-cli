"""Resume a labeled local demo in Gemini's native Markdown/code renderer."""
import json


def prepare(c):
    c.git_fixture()
    theme = c.copy(f'themes/{c.slug}.json', f'.gemini/themes/{c.slug}.json')
    c.write('.gemini/settings.json', json.dumps({'ui': {'theme': str(theme)},
        'security': {'auth': {'selectedType': 'gemini-api-key'}, 'folderTrust': {'enabled': False}},
        'general': {'disableAutoUpdate': True, 'enableAutoUpdate': False}, 'privacy': {'usageStatisticsEnabled': False}}))
    c.env.update(GEMINI_API_KEY='capture-not-a-real-key', GOOGLE_GEMINI_BASE_URL='http://127.0.0.1:9',
                 GEMINI_CLI_DISABLE_TELEMETRY='1', NO_UPDATE_NOTIFIER='1')
    timestamp = '2026-01-01T12:00:00.000Z'
    records = [
        {'sessionId': 'a40d1e4c-1150-4000-8000-000000000020', 'projectHash': 'local-demo',
         'startTime': timestamp, 'lastUpdated': timestamp},
        {'id': 'demo-user', 'type': 'user', 'timestamp': timestamp,
         'content': [{'text': 'Review the glyph render loop and suggest a safer implementation. (Local demo)'}]},
        {'id': 'demo-assistant', 'type': 'gemini', 'timestamp': timestamp,
         'content': [{'text': (c.root / 'capture/review.md').read_text()}], 'model': 'gemini-2.5-pro'},
    ]
    session = c.write('demo-session.jsonl', '\n'.join(json.dumps(x) for x in records) + '\n')
    return ['gemini', '--session-file', session, '--skip-trust']


def drive(c):
    c.wait_text(r'add boundary tests next')
