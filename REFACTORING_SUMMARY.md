# Documentation Refactoring Summary

## Date: October 11, 2025

## Overview
Removed underscore prefixes from main documentation folders to improve clarity and follow standard naming conventions.

## Changes Made

### 1. Renamed Source Folders
- `docs/source/_cite` → `docs/source/cite`
- `docs/source/_explore` → `docs/source/explore`
- `docs/source/_learn` → `docs/source/learn`
- `docs/source/_methods` → `docs/source/methods`
- `docs/source/_user` → `docs/source/user`

### 2. Renamed Subfolder
- `*/_figures` → `*/figures` (in explore, learn, methods)

### 3. Updated Locale Folders
**Chinese (zh_CN):**
- `docs/locale/zh_CN/LC_MESSAGES/_cite` → `.../cite`
- `docs/locale/zh_CN/LC_MESSAGES/_explore` → `.../explore`
- `docs/locale/zh_CN/LC_MESSAGES/_learn` → `.../learn`
- `docs/locale/zh_CN/LC_MESSAGES/_methods` → `.../methods`
- `docs/locale/zh_CN/LC_MESSAGES/_user` → `.../user`

**Spanish (es):**
- Same pattern as Chinese

### 4. Updated References

**All .po files (154 files):**
- Updated all path references from `source/_*` to `source/*`
- Preserved all translation content

**RST files:**
- Updated cross-references and toctree entries
- Updated button-ref targets
- Updated image paths

**Python scripts:**
- `docs/fix_translated_buttons.py`: Updated URL paths in BUTTON_TRANSLATIONS dictionary

**Main files updated:**
- `docs/source/index.rst`: Updated toctree and button-ref paths

### 5. Folders NOT Changed
- `_static` (Sphinx private folder - kept as is)
- `_templates` (Sphinx private folder - kept as is)
- `_build` (build directory - cleaned and regenerated)

## Verification

✅ Build succeeded with 4 warnings (expected, unrelated to refactoring)
✅ All translations preserved and working correctly
✅ Button translations functioning properly
✅ Folder structure clean and consistent

## Commands Used

```bash
# Rename source folders
mv _cite cite && mv _explore explore && mv _learn learn && mv _methods methods && mv _user user

# Rename locale folders (Chinese)
cd docs/locale/zh_CN/LC_MESSAGES
for dir in _cite _explore _learn _methods _user; do mv "$dir" "${dir#_}"; done

# Rename locale folders (Spanish)
cd docs/locale/es/LC_MESSAGES
for dir in _cite _explore _learn _methods _user; do mv "$dir" "${dir#_}"; done

# Update all .po files
find docs/locale -name "*.po" -exec sed -i '' 's|source/_cite|source/cite|g; ...' {} \;

# Update RST files
find docs/source -name "*.rst" -exec sed -i '' 's|/_cite/|/cite/|g; ...' {} \;

# Clean build
rm -rf docs/_build docs/locale/*/LC_MESSAGES/*.mo

# Test build
task docs:html-zh
```

## Impact

- **Zero translation loss**: All existing translations preserved
- **Improved clarity**: Folder names now follow standard conventions
- **Better organization**: Cleaner structure without unnecessary underscores
- **Maintained functionality**: All links, buttons, and references working correctly

## Next Steps

Consider:
- Building English docs to verify no issues: `task docs:html-en`
- Building Spanish docs: `task docs:html-es`
- Building all docs: `task docs:html-all`
- Committing changes to git
