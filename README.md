<!-- living-code-readme:1 -->
# ♊ Living Code for Gemini CLI

**Calm slate. Living color.** Living Code for Gemini CLI: standalone custom theme files for conversational text, borders, status indicators and diff backgrounds.

[Installation](#installation) · [Flavors](#flavors) · [Configuration](#configuration) · [All ports](https://github.com/living-code-theme)

## Previews

Real application screenshots have not been captured yet.

## Installation

```sh
git clone https://github.com/living-code-theme/gemini-cli.git
cd gemini-cli
```

```sh
mkdir -p "$HOME/.gemini/themes"
cp themes/*.json "$HOME/.gemini/themes/"
printf "%s\n" "$HOME/.gemini/themes/living-code-night.json"
```

Copy the printed absolute path into `ui.theme` in your existing `~/.gemini/settings.json`, preserving all other settings. Example shape:

```json
{
  "ui": {
    "theme": "/home/you/.gemini/themes/living-code-night.json"
  }
}
```

Replace `/home/you` with your actual home directory, then restart Gemini CLI.

## Flavors

Expand a flavor for its full-size preview and activation instructions.

<details data-lc-flavor="night">
<summary><strong>Night</strong> · Dark · full palette</summary>

A real application capture is not available yet.

Set `ui.theme` to the absolute path of `~/.gemini/themes/living-code-night.json` in your settings, then restart Gemini CLI.

</details>

<details data-lc-flavor="frost">
<summary><strong>Frost</strong> · Dark · softer chroma</summary>

A real application capture is not available yet.

Set `ui.theme` to the absolute path of `~/.gemini/themes/living-code-frost.json` in your settings, then restart Gemini CLI.

</details>

<details data-lc-flavor="paper">
<summary><strong>Paper</strong> · Light · near-white slate</summary>

A real application capture is not available yet.

Set `ui.theme` to the absolute path of `~/.gemini/themes/living-code-paper.json` in your settings, then restart Gemini CLI.

</details>

<details data-lc-flavor="signal">
<summary><strong>Signal</strong> · Dark · teal accent</summary>

A real application capture is not available yet.

Set `ui.theme` to the absolute path of `~/.gemini/themes/living-code-signal.json` in your settings, then restart Gemini CLI.

</details>

## Configuration

The distributable files are standalone `type: "custom"` theme documents, not full settings files. As an alternative, insert a document into `ui.customThemes` using its `name` as the object key, then select it by name. A path selected through `ui.theme` must be removed before changing themes with `/theme`.

## Compatibility

Uses the documented standalone-file custom theme API. Gemini CLI permits theme paths only within the home directory: do not point it at a clone under `/tmp` or a system-wide location. Text, background, diff, border, status and UI groups are provided; code highlighting follows Gemini CLI’s derived theme behavior. Tests validate the nested format, not provider access or model output.

## Contributing

Found a problem? [Open an issue](https://github.com/living-code-theme/gemini-cli/issues/new/choose) with the app version, the flavor and a screenshot. Want Living Code somewhere else? [Request a port](https://github.com/living-code-theme/core/issues/new?template=port-request.yml).

Pull requests are welcome. Keep this README, `port.json` and `images/` in sync, and use real screenshots of the app, never mockups.

🦎 **One chameleon, many habitats.** Part of [Living Code](https://github.com/living-code-theme).

## License

[MIT](LICENSE) © Elliot Luque
