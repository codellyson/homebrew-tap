# KreativeKorna Homebrew tap

## Install JustDB (macOS)

```sh
brew install --cask codellyson/tap/justdb
```

The universal installer supports Apple silicon and Intel Macs.

## Update

```sh
brew update
brew upgrade --cask justdb
```

If JustDB was previously installed manually, Homebrew may report that
`/Applications/JustDB.app` already exists. Quit JustDB, move that application
bundle to the Trash, and rerun the install command. Your saved connections and
keychain credentials are stored separately. Do not delete those settings.

## Release updates

GitHub Actions checks the latest published stable `codellyson/justdb` release
hourly. New releases must include `JustDB_VERSION_universal.dmg`. The updater
downloads the installer, computes SHA-256, checks it against GitHub's asset
digest when available, and commits the version and checksum. Drafts and
prereleases are excluded. The workflow can also be run manually from Actions.

The tap uses its own GitHub Actions token; no cross-repository secret is required.
GitHub may delay scheduled runs or disable schedules after 60 days without
repository activity. Run the workflow manually or re-enable it if needed.
