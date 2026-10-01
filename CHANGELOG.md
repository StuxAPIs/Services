# Changelog

All notable changes to StuxAPIs Services (services.stuxapis.net) are documented here. This
project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## v1.0.5

### Fixed

- The primary buttons' glow and the hero's second glow were still Stux.Group red; they now use the StuxAPIs purple (`#BF7FF9`)
- The Offline badge and the status band's down dot were purple instead of red

## v1.0.4

### Changed

- GithubStats is live: its card shows a live badge from StuxAPIs Status (`stuxapis:githubstats`) instead of Coming soon, with a Website link

## v1.0.3

### Fixed

- Card icons no longer sit in a bordered tile (6 icons)

### Removed

- The `.project-icon.on-tile` style, so icons can't be put in the bordered tile again

## v1.0.2

### Fixed

- Lunar Calendar's icon no longer sits in the bordered tile

## v1.0.1

### Fixed

- The StuxAPIs Status card now has a live badge, showing that page's overall status (`data-monitor="stuxapis:*"`)

## v1.0.0

### Added

- The StuxAPIs services page: every StuxAPIs API and service in one place, modelled on Stux.Group Services and branded for StuxAPIs
- Cards for StuxAPIs Status, SeasonalOverlaysLibrary, Kittens, SecretGen, Lunar Calendar, GithubStats and GithubStatsAction, the Soonpage, Maintenancepage and Servicepage templates, and the discontinued GitHubStatsLegacy
- One badge per card by precedence (Discontinued, Template, Maintenance, Coming soon), otherwise a live Online / Degraded / Offline badge read from status.stuxapis.net (`stuxapis` source, the default for `data-monitor`)
- A status band with an animated dot, reading the overall status of StuxAPIs Status
- Seasonal overlays from SeasonalOverlaysLibrary, with a hero button that replays today's preset
- Boring Legal Stuff hub with its six sub-pages, `/changelogs` (with a `/changelog` redirect), a sitemap page, `sitemap.xml` and `robots.txt`
- A footer with the muted StuxAPIs logo, an auto-updating copyright year, a version link to the changelogs, and "Created with love, code and coffee by StuxAPIs"
- `dev-server` (Node, `DEV_MODE` on by default with `--no-dev-mode` and the shared site-banner component), `scripts/check-repo-links.sh`, a GitHub Pages workflow, CI and release workflows
