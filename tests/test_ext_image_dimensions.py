import pytest

from pyvec_docs.ext.image_dimensions import add_dimensions, get_svg_size


SVG = '<svg xmlns="http://www.w3.org/2000/svg" version="1.0" viewBox="0 0 4467 2012">'


@pytest.mark.parametrize(
    "svg_text, expected",
    [
        (SVG, ("4467", "2012")),
        ('<svg viewBox="0,0,317.5,166.6875">', ("317.5", "166.6875")),
        ("<svg>", None),
    ],
)
def test_get_svg_size(svg_text, expected):
    assert get_svg_size(svg_text) == expected


def test_add_dimensions():
    html = '<p>Hi</p><img alt="x" class="align-center" src="../_images/community.svg" style="width: 80%;" />'

    assert add_dimensions(html, lambda src: SVG) == (
        '<p>Hi</p><img width="4467" height="2012" alt="x" class="align-center" '
        'src="../_images/community.svg" style="width: 80%;" />'
    )


@pytest.mark.parametrize(
    "html",
    [
        '<img src="photo.png" />',
        '<img width="10" src="image.svg" />',
        '<img src="https://example.com/image.svg" />',
    ],
)
def test_add_dimensions_skips(html):
    def resolve(src):
        return None if src.startswith("https://") else SVG

    assert add_dimensions(html, resolve) == html
