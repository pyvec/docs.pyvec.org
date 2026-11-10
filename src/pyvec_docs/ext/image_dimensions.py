"""
Sphinx extension which adds width and height attributes to SVG images in the
HTML output, read from the SVG's viewBox. Browsers use them as the image's
aspect ratio and reserve space for it before it loads, so the page content
doesn't jump. The displayed size still comes from CSS and the :width: option.
"""

import re
from pathlib import Path


IMG_RE = re.compile(r"<img\b[^>]*>")
SRC_RE = re.compile(r'\bsrc="([^"]+\.svg)"')
VIEWBOX_RE = re.compile(
    r'viewBox="\s*[-\d.]+[\s,]+[-\d.]+[\s,]+([\d.]+)[\s,]+([\d.]+)\s*"'
)


def get_svg_size(svg_text):
    if match := VIEWBOX_RE.search(svg_text):
        return match.groups()
    return None


def add_dimensions(html, resolve_svg_text):
    def replace(match):
        tag = match.group(0)
        if re.search(r"\s(width|height)=", tag):
            return tag
        if not (src := SRC_RE.search(tag)):
            return tag
        if not (svg_text := resolve_svg_text(src.group(1))):
            return tag
        if not (size := get_svg_size(svg_text)):
            return tag
        width, height = size
        return tag.replace("<img", f'<img width="{width}" height="{height}"', 1)

    return IMG_RE.sub(replace, html)


def on_html_page_context(app, pagename, templatename, context, doctree):
    if "body" not in context:
        return

    # Sphinx copies images to _images/ under new names, so map them back
    images = {
        Path(dest).name: Path(app.srcdir) / src
        for src, dest in app.builder.images.items()
    }

    def resolve_svg_text(src):
        path = images.get(Path(src).name)
        return path.read_text() if path and path.exists() else None

    context["body"] = add_dimensions(context["body"], resolve_svg_text)


def setup(app):
    app.connect("html-page-context", on_html_page_context)
    return {"version": "1.0", "parallel_read_safe": True}
