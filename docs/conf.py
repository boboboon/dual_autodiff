# -- Project information -----------------------------------------------------
project = "DUAL_AUTODIFF"
copyright = "2024, Lucas Curtin"
author = "Lucas Curtin"
release = "0.0.1"

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_parser",
    "nbsphinx",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

master_doc = "index"

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_book_theme"  # Change theme to sphinx_book_theme

# Theme-specific options for customizing Sphinx Book Theme
html_theme_options = {
    "repository_url": "https://github.com/your_username/your_project",  # Replace with your actual repository URL
    "use_repository_button": True,
    "use_edit_page_button": True,
    "path_to_docs": "docs/",  # Adjust if your docs directory path differs
    "show_navbar_depth": 2,  # Controls depth of sidebar navigation
    "use_download_button": True,
    "show_toc_level": 1,
}

html_static_path = ["_static"]

# -- MyST Configuration ------------------------------------------------------
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "colon_fence",
]
myst_heading_anchors = 3
