# Image Refactoring Plan

## Current Structure (Messy)
```
docs/source/
├── _static/
│   ├── _test_image/ (banners, discover, learn6, webinar2, etc.)
│   ├── learn/ (coffee.png, datasets.png, fermentation.png)
│   ├── images/explore/ (sklearn, spectra, pipeline, etc. + subdirs)
│   └── ... (mixed organization)
├── learn/figures/ (fermentation_setup.png)
├── methods/figures/ (augmentation.png, preprocessing.png, etc.)
└── explore/figures/ (dataframes.png, models.png, optimize.png, etc.)
```

## New Structure (Clean & Organized)
```
docs/source/_static/images/
├── main/ (banner, chemotools_overview)
├── learn/ (coffee, datasets, fermentation, fermentation_setup)
├── explore/ (sklearn, spectra, pipeline, optimize, dataframes, persist, models, etc.)
│   ├── sklearn/ (sklearn_workflow.jpg)
│   ├── pipelines/ (pipelines_*.png/html)
│   └── persist/ (persist_scheme.png)
├── methods/ (augmentation, preprocessing, feature_selection, outliers)
└── index/ (discover, learn6, webinar2)
```

## Migration Steps

1. **Create new directory structure**
   - `_static/images/main/`
   - `_static/images/learn/`
   - `_static/images/explore/` (already partially exists)
   - `_static/images/methods/`
   - `_static/images/index/`

2. **Move images**
   - `_test_image/discover.png` → `images/index/discover.png`
   - `_test_image/learn6.png` → `images/index/learn6.png`
   - `_test_image/webinar2.png` → `images/index/webinar2.png`
   - `_test_image/banner.svg` → `images/main/banner.svg`
   - `_main_page/*` → `images/main/`
   - `learn/*` → `images/learn/` (already correct)
   - `learn/figures/*` → `images/learn/`
   - `methods/figures/*` → `images/methods/`
   - `explore/figures/*` → `images/explore/`

3. **Update references in RST files**
   - `docs/source/index.rst` - Update 3 image paths
   - `docs/source/learn/index.rst` - Update paths (already using _static/learn)
   - `docs/source/methods/index.rst` - Update 4 figure paths
   - `docs/source/explore/*.rst` - Update figure paths

4. **Delete old directories**
   - `learn/figures/`
   - `methods/figures/`
   - `explore/figures/`
   - `_static/_test_image/`
   - `_static/_main_page/`

## Files to Update

### RST Files (7 figure refs + 3 index images + banner = ~11 refs)
- `docs/source/index.rst`
- `docs/source/learn/index.rst`  
- `docs/source/methods/index.rst`
- `docs/source/explore/optimize.rst`

### Note
- explore/ images already mostly in `_static/images/explore/` - just need to move figures/ content
- learn/ images already in `_static/learn/` - need to move to `_static/images/learn/`
