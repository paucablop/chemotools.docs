# Documentation Unification Plan

## Problem
Current redundancy between `api/` and `methods/` sections:
- **API section**: Auto-generates full module documentation with long class paths (`chemotools.baseline._air_pls.AirPls`)
- **Methods section**: Beautiful user-facing pages with clean names (`AirPls`), images, and categorization

Both generate the same docstring content, creating maintenance burden and confusion.

## User Requirements
1. ✅ Keep the Methods section with its excellent UX (images, categorization, clean names)
2. ✅ Remove redundant docstring generation in API
3. ✅ Maintain both sections for different purposes

## Proposed Solution

### Option A: API as Index pointing to Methods (RECOMMENDED)

**Concept**: Transform API from auto-generated docs to a curated index that links to Methods pages.

**Benefits**:
- Zero redundancy - docstrings only in Methods section
- API becomes a pure technical reference (imports, module structure)
- Methods remains user-friendly with images and context
- Clear separation: API = "what can I import?", Methods = "how do I use it?"

**Changes Required**:
1. Modify `api/index.rst` to link to Methods instead of auto-generating
2. Remove `autosummary` directives from API
3. Add manual links to corresponding Methods pages
4. Update API pages to show module structure without full docstrings

**Example API structure**:
```rst
chemotools.baseline
===================

This module provides baseline correction methods.

**Available classes:**

- :doc:`AirPls </methods/generated/chemotools.baseline.AirPls>` - Adaptive iteratively reweighted penalized least squares
- :doc:`ArPls </methods/generated/chemotools.baseline.ArPls>` - Asymmetrically reweighted penalized least squares
- ... (links to Methods pages)

See the :doc:`Baseline Methods </methods/baseline>` page for detailed documentation with examples.
```

### Option B: Merge API into Methods

**Concept**: Eliminate API section entirely, make Methods the single source of truth.

**Benefits**:
- Maximum simplicity
- No navigation confusion

**Drawbacks**:
- Loses traditional API reference structure that developers expect
- Methods pages become very long with all docstrings

### Option C: API with :noindex: (Current partial solution)

**Status**: Already partially implemented (`:noindex:` in Methods)

**Issue**: Still generates duplicate HTML pages and docstring processing

---

## Recommendation

**Implement Option A** - Transform API into a lightweight index/navigator pointing to Methods.

This preserves both sections with clear purposes:
- **API**: Quick reference for imports and module structure (developer-focused)
- **Methods**: Complete documentation with examples and UX (user-focused)

### Implementation Steps

1. **Rewrite api/index.rst** - Remove autosummary, add manual categorization
2. **Create custom API module pages** - Simple pages with links to Methods
3. **Update conf.py** - Disable autosummary for API, keep for Methods
4. **Clean up generated/** - Remove old API generated files
5. **Update translations** - Sync .po files for new structure
6. **Test builds** - Verify no broken links

Would you like me to proceed with Option A?
