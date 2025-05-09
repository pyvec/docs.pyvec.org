/**
 * Redirects each page from pyvec-guide.readthedocs.io to docs.pyvec.org
 */
if (window.location.hostname === 'pyvec-guide.readthedocs.io') {
  var url = window.location.href
    .replace(/^https?:/, 'https:')
    .replace(window.location.host, 'docs.pyvec.org');
  window.location.replace(url);
}
