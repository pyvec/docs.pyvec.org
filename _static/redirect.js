/**
 * Redirects each page from pyvec-guide.readthedocs.io to docs.pyvec.org
 * (if there is a port in the URL, it's considered as local development)
 */
if (!window.location.port && window.location.hostname !== 'docs.pyvec.org') {
  var url = window.location.href
    .replace(/^https?:/, 'https:')
    .replace(window.location.host, 'docs.pyvec.org');
  window.location.replace(url);
}
