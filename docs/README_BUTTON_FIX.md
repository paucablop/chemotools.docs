# Button Translation Fix Script

## Overview

This script works around a limitation in `sphinx-design`'s internationalization support where button text inside `button-ref` and `button-link` directives cannot be properly translated through the standard Sphinx gettext workflow.

## The Problem

When using sphinx-design's button directives with Sphinx i18n:
- The button text is extracted for translation in `.po` files
- However, when translations are applied, the button HTML structure breaks
- Buttons appear as plain text instead of clickable links

## The Solution

This post-processing script:
1. Runs after the HTML build completes
2. Finds all button elements that still contain English text
3. Replaces the English text with translations while preserving the HTML structure
4. Maintains all button functionality (links, styling, click behavior)

## Usage

The script is automatically run as part of the build process defined in `Taskfile.yml`:

```bash
# Build Chinese documentation (includes button translation)
task docs:html-zh

# Build Spanish documentation (includes button translation)  
task docs:html-es

# Build all language variants
task docs:html-all
```

You can also run it manually:

```bash
uv run python docs/fix_translated_buttons.py <build_dir> <language>

# Examples:
uv run python docs/fix_translated_buttons.py docs/_build/html/zh_CN zh_CN
uv run python docs/fix_translated_buttons.py docs/_build/html/es es
```

## Adding New Translations

To add button translations for a new page or language, edit the `BUTTON_TRANSLATIONS` dictionary in `fix_translated_buttons.py`:

```python
BUTTON_TRANSLATIONS = {
    "zh_CN": {
        "English button text": {
            "translation": "Chinese translation",
            "url": "relative/url.html",  # or absolute URL for external links
            "external": False,  # True for external links (button-link)
        },
        # ... more buttons
    },
    "es": {
        # Spanish translations
    },
}
```

## Requirements

- `beautifulsoup4` (added to `pyproject.toml` dependencies)

## Integration

The script is integrated into the documentation build workflow:

1. **Taskfile.yml**: Updated `docs:html-zh` and `docs:html-es` tasks to run the script after Sphinx build
2. **pyproject.toml**: Added `beautifulsoup4` dependency
3. **.po files**: Button text translations are left empty (fallback to English) or documented with comments

## Benefits

✅ Buttons work correctly with proper links and styling  
✅ Button text appears in the correct language  
✅ No manual HTML editing required  
✅ Automated as part of the build process  
✅ Easy to maintain and extend  

## Future Improvements

This workaround will no longer be needed if/when sphinx-design adds proper i18n support for directive content. Monitor the sphinx-design issue tracker for updates.
