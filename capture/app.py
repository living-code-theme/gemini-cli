"""Capture Gemini's native themed TUI. All credentials and endpoints are disposable."""
import json


def prepare(c):
    c.git_fixture()
    theme = c.copy(f'themes/{c.slug}.json', f'.gemini/themes/{c.slug}.json')
    c.write('.gemini/settings.json', json.dumps({'ui': {'theme': str(theme)},
        'security': {'auth': {'selectedType': 'gemini-api-key'}, 'folderTrust': {'enabled': False}},
        'general': {'disableAutoUpdate': True, 'enableAutoUpdate': False}, 'privacy': {'usageStatisticsEnabled': False}}))
    c.env.update(GEMINI_API_KEY='capture-not-a-real-key', GOOGLE_GEMINI_BASE_URL='http://127.0.0.1:9',
                 GEMINI_CLI_DISABLE_TELEMETRY='1', NO_UPDATE_NOTIFIER='1')
    return ['gemini']


def drive(c):
    c.wait_text(r'Gemini|Type your|trust')
    if 'trust' in c.text().lower():
        c.key('enter')
    c.type('Explain the FieldRenderer class and its fallback path')  # Intentionally not submitted.
