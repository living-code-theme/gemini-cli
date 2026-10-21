// Standalone Gemini CLI custom themes; these are not settings.json replacements.
export function generate(flavors) {
  return flavors.map(f => ({ path: `themes/${f.slug}.json`, content: JSON.stringify({
    name: f.name, type: 'custom',
    background: { primary: f.r('bg'), diff: { added: f.mix('bg', 'added', 0.10), removed: f.mix('bg', 'removed', 0.10) } },
    text: { primary: f.r('fg'), secondary: f.r('fgMuted'), link: f.r('link'), accent: f.r('accent'), response: f.r('fg') },
    border: { default: f.r('border'), focused: f.r('borderActive') },
    status: { success: f.r('success'), warning: f.r('warning'), error: f.r('error') },
    ui: { comment: f.r('comment'), symbol: f.r('operator'), gradient: [f.r('accent'), f.r('info'), f.r('decorator')] },
  }, null, 2) + '\n' }));
}
