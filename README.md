# Telkom Digital Enterprise — marketing site

Static site (HTML, CSS, JS). Most pages are generated from shared data in `tools/`:

```
python3 tools/build_home.py
python3 tools/build_services.py
python3 tools/build_capabilities.py
python3 tools/build_stories.py
python3 tools/update_nav.py
```

Design rules: `docs/design.md`. Page frameworks: `docs/kerangka-*.md`.

Customer stories, quotes and partner logos are placeholders until real, approved stories replace them.
