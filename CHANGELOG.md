# Changelog

All notable changes to StuxAPIs Services (services.stuxapis.net) are documented here. This
project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
