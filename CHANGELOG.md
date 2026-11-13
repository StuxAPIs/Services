# Changelog

All notable changes to StuxAPIs Services (services.stuxapis.net) are documented here. This
project adheres to [Date Versioning](https://datevers.ing) since v26.10.23 (`YY.MM.DD`, the UTC release date, with `-1`, `-2`… for later releases the same day); earlier releases used [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## v26.11.13

### Changed

- Stux Group Ltd's registered office is now 124 City Road, London, EC1V 2NX, England, United Kingdom (it was 82a James Carter Road, Mildenhall), on the Imprint page and the README. The company number and registration are unchanged

## v26.11.08

### Changed

- Says services are "checked regularly", not "every 5 minutes", in the Status section, the StuxAPIs Status card and the live status band (GitHub runs the 5-minute schedule best-effort, often less often; the status page shows the real rhythm)
- The hero's third figure is "90 days of status history" instead of "5 min between status checks"

## v26.11.07-1

### Added

- A FlashView card in APIs & libraries (flashview.stuxapis.net: plays SWF files in the browser with a self-hosted Ruffle), with its own icon and live status, and a row in the README's services table

### Changed

- The hero counts 7 APIs & libraries, and the Discord preview 8 live services, with FlashView in its list

## v26.11.07

### Changed

- **The hero's eyebrow is a live status badge.** It keeps the eyebrow's size and pill shape, but takes a status
  badge's colours (green when up, amber when degraded or partial, red when down) and a 7px dot that pulses when up
  (not with reduced motion). Once StuxAPIs Status loads, it reads only the state ("All operational", "Degraded",
  "Partial outage" or "Major outage"), with no brand name, and it links to status.stuxapis.net. It reuses the
  cards' `summary.json` request, and stays the plain "StuxAPIs" eyebrow if that can't load. CONTRIBUTING
  documents it

## v26.11.06-1

### Changed

- CI (`.github/workflows/ci.yml`) also runs on pushes to `test`
- `commit.sh` and `commit.bat` end by saying to push `test` and open a pull request into `main`
- README (Versioning) and CONTRIBUTING (a new Branches section) describe the `test` branch flow: work and releases happen on `test`, and reach `main` only through a reviewed pull request that needs CI to pass

## v26.11.06

### Added

- `scripts/badge-icons.py` (copied from StuxGroup/Services, set to StuxAPIs' purple) builds badge-style icons for
  services without a logo of their own: the StuxAPIs mark on a round avatar, with a badge in the corner saying what
  the service is

### Changed

- **Every card uses its full name, with its own icon.** "Status" is now StuxAPIs Status, with a heartbeat badge;
  the templates are StuxAPIs Soonpage, Maintenancepage and Servicepage, each with its own badge (an hourglass, a
  spanner, a browser window). GithubStats (a bar chart), GithubStatsAction (a play button), Lunar Calendar (a
  crescent moon) and GitHubStatsLegacy (an archive box) get their own badges instead of the shared StuxAPIs icon.
  The icons' alt text uses the same full names

### Removed

- `assets/img/services/status.svg` and the shared `assets/img/services/stuxapis.png`, replaced by the badge icons

## v26.10.23

### Added

- A Discord link preview built from the site's own details (`<script id="discord:component-embed">` in each page's head, except 404 and the old `/changelog/` redirect): the home page shows what the site is, how many live services it lists and their names, with buttons to the services list, Status and StuxAPIs; other pages show their title and description. The embed is left out (an HTML comment instead) if it ever goes over Discord's 3,000-byte limit
- A full favicon set: `favicon.ico`, `apple-touch-icon.png`, `site.webmanifest` and 192, 512 and maskable 512 icons, linked from every page's head alongside the existing light/dark icons
- `scripts/build-head.py` writes the favicon and Discord blocks into every page (`--check` verifies they are current), with `tests/head.py` and `tests/changelog-render.js` covering them and the changelog page's `vYY.MM.DD` headings
- `tests/version.sh`, which checks that `VERSION.md` is a valid Date Version, a real calendar date not in the future, and the same as the newest entry in this changelog

### Changed

- Switched from Semantic Versioning to [Date Versioning](https://datevers.ing): releases are numbered by their UTC release date as `YY.MM.DD`, with `-1`, `-2`… for later releases the same day. This release follows v1.2.0
- `commit.sh` and `commit.bat` refuse a `VERSION.md` that isn't a valid Date Version or is dated in the future (UTC), and warn when it's dated before today
- The changelog workflow check and the dev server know the Date Version form and the `.webmanifest` type
- `README.md` and `CONTRIBUTING.md` describe Date Versioning and the release steps

## v1.2.0

### Added

- A light/dark toggle at the end of the header on every page, like the brand pages': it shows the theme it switches to (a sun on dark, a moon on light). Until it's used the site follows the system theme; after that the choice is remembered in this browser

## v1.1.1

### Changed

- The favicon follows the browser's light or dark theme: the deep icon (`icon-dark.png`) on light and the bright one (`icon-light.png`) on dark, straight from the brand's media host instead of a local copy, so a brand colour change is just a new file there
- The logos and icons in the Markdown docs (README and the like) follow GitHub's light or dark theme, using each brand's `logo-light`/`logo-dark` and `icon-light`/`icon-dark` files

## v1.1.0

### Added

- StuxAPIs itself is listed first under Featured, ahead of Status, linking to stuxapis.net and a way to get in touch
- A light theme, following the system preference: light purple-tinted neutrals with the StuxAPIs purple deepened to `#6a16c2` (links and accents) and `#8c3fde` so text, links and button labels meet WCAG AA; the header, buttons, status badges, status band dot and footer logo all switch with it, and the changelog badges use their deeper light colours

### Changed

- The dev-mode site banner follows the system theme instead of always using its dark style
- The header, ghost buttons, status badges, accent tints and link hovers use colour variables instead of hard-coded dark-only colours (the dark theme looks the same)

## v1.0.6

### Changed

- The status card is titled just "Status" (and its icon's alt text "Status icon") instead of repeating "StuxAPIs Status"

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
