<p align="center">
  <img src="https://global.media.stuxapis.net/logo.png" height="100" alt="StuxAPIs Logo">
</p>

# StuxAPIs Services

### *Every StuxAPIs API and service, in one place.*

[StuxAPIs Services](https://services.stuxapis.net) is a small, static, no-build-step website that
indexes every StuxAPIs API, library and template and links out to each one, with its own repository
and, usually, its own site. It's built the same way as
[StuxieDev Projects](https://github.com/StuxieDev/Projects), in StuxAPIs purple.

- Plain HTML, CSS and JavaScript: no framework, no bundler, no dependencies to install
- **Live status** on each card, read from [status.stuxapis.net](https://status.stuxapis.net)
  (`StuxAPIs/Status`, powered by [GitHup](https://githup.stux.group))
- **Seasonal overlays** from [SeasonalOverlaysLibrary](https://seasonaloverlayslibrary.stuxapis.net)
  (StuxAPIs): today's preset plays once per visit (never with reduced motion), and the hero button
  replays it
- Deployed to [GitHub Pages](https://pages.github.com/) by `.github/workflows/pages.yml`
- No accounts, no ads, no cookies, no tracking scripts

---

## Services listed here

| Service | What it is | Site | Repo |
|---|---|---|---|
| StuxAPIs Status | Live status and uptime history of every StuxAPIs service | [status.stuxapis.net](https://status.stuxapis.net) | [StuxAPIs/Status](https://github.com/StuxAPIs/Status) |
| SeasonalOverlaysLibrary | Dependency-free seasonal particle overlays | [seasonaloverlayslibrary.stuxapis.net](https://seasonaloverlayslibrary.stuxapis.net) | [StuxAPIs/SeasonalOverlaysLibrary](https://github.com/StuxAPIs/SeasonalOverlaysLibrary) |
| Kittens | Random kitten images API | [kittens.stuxapis.net](https://kittens.stuxapis.net) | [StuxAPIs/Kittens](https://github.com/StuxAPIs/Kittens) |
| SecretGen | Secret generator API | [secretgen.stuxapis.net](https://secretgen.stuxapis.net) | [StuxAPIs/SecretGen](https://github.com/StuxAPIs/SecretGen) |
| Lunar Calendar | Lunar calendar API (fork of hnthap's project), site not live yet | — | [StuxAPIs/LunarCalendar](https://github.com/StuxAPIs/LunarCalendar) |
| GithubStats | GitHub statistics API | [githubstats.stuxapis.net](https://githubstats.stuxapis.net) | [StuxAPIs/GithubStats](https://github.com/StuxAPIs/GithubStats) |
| GithubStatsAction | GitHub Action for GitHub Readme Stats cards | — | [StuxAPIs/GithubStatsAction](https://github.com/StuxAPIs/GithubStatsAction) |
| Soonpage | "Coming soon" page template | [soonpage.stuxapis.net](https://soonpage.stuxapis.net) | [StuxAPIs/soonpage](https://github.com/StuxAPIs/soonpage) |
| Maintenancepage | Maintenance page template | [maintenancepage.stuxapis.net](https://maintenancepage.stuxapis.net) | [StuxAPIs/maintenancepage](https://github.com/StuxAPIs/maintenancepage) |
| Servicepage | Placeholder for services not yet set up | [servicepage.stuxapis.net](https://servicepage.stuxapis.net) | [StuxAPIs/servicepage](https://github.com/StuxAPIs/servicepage) |
| GitHubStatsLegacy | The original GitHub Stats API, replaced by GithubStats (discontinued) | — | [StuxAPIs/GitHubStatsLegacy](https://github.com/StuxAPIs/GitHubStatsLegacy) |

This table (and the matching cards on the site) is the source of truth for what's listed. Update
both together when a service is added, retired or renamed. Each card shows one badge above its description: Discontinued, Template, Maintenance or Coming
soon (from `data-state`, in that order of precedence), otherwise a live Online / Degraded / Offline
badge when it has a ``data-monitor` (`stuxapis:<slug>`) matching a monitor slug in `StuxAPIs/Status`'s `.githup.yml`.

## Local development

```
./dev-server.sh          # http://127.0.0.1:8080, DEV_MODE forced on
./dev-server.sh 3000 --no-dev-mode
```

On Windows, use `dev-server.bat` instead. No `npm install` needed: the dev server is a single
dependency-free Node script (`dev-server.js`); Node just needs to be installed. See
[CONTRIBUTING.md](CONTRIBUTING.md) for more.

## Releasing

1. Update `CHANGELOG.md`
2. Bump `VERSION.md`
3. Update this README if relevant
4. Run `./commit.sh` (or `commit.bat`): it reads `VERSION.md`, commits, and tags `vX.Y.Z`
5. `git push origin main --tags`; the release workflow then publishes a GitHub Release from the
   matching `CHANGELOG.md` section

## License

&copy; 2026 Stux.Group. All rights reserved. This repository is not licensed for reuse or
redistribution. Lato and Poppins (`assets/fonts/`) are under the SIL Open Font License.

---

*Powering the Stux.Group Ecosystem | Part of the Stux.Group Brand of Companies.*

StuxAPIs is operated by **Stux Group Ltd**, a company registered in England and Wales (company no. 13160574), registered office 82a James Carter Road, Mildenhall, England, IP28 7DE.
