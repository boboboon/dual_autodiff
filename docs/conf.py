# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "DUAL_AUTODIFF"
copyright = "2024, Lucas Curtin"
author = "Lucas Curtin"
release = "0.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Extensions required for Markdown and Jupyter notebooks
extensions = [
    "myst_parser",  # Enables Markdown support
    "nbsphinx",  # Enables Jupyter notebook support (if you have notebooks)
]

# Paths for templates and files to exclude
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Enable support for both Markdown (.md) and reStructuredText (.rst) files
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# Set master document
master_doc = "index"  # Refers to 'index.md' as the root of the documentation

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# HTML theme
html_theme = "alabaster"
html_static_path = ["_static"]

# -- MyST Configuration ------------------------------------------------------
# Additional configuration options for MyST Parser
myst_enable_extensions = [
    "dollarmath",  # Enable $ and $$ math syntax
    "amsmath",  # Enable AMS math environments
    "deflist",  # Enable definition lists
    "colon_fence",  # Enable colon fence for code blocks
]

# Optional: MyST specific settings (e.g., enabling extended syntax)
myst_heading_anchors = 3  # Adds anchors for headings up to level 3
