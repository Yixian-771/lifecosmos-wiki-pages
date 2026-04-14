// Fix language switcher to navigate to the corresponding page instead of homepage.
// MkDocs Material's built-in alternate-link logic can fail to append the page
// path when navigation.instant is active, causing every switch to land on /.
document$.subscribe(function () {
  var currentPath = window.location.pathname; // e.g. /zh/subconscious/

  // Extract the page suffix after the language prefix (/zh/ or /en/)
  var match = currentPath.match(/^\/(zh|en)\/(.*)/);
  var pageSuffix = match ? match[2] : "";

  document.querySelectorAll(".md-select__link[hreflang]").forEach(function (link) {
    var lang = link.getAttribute("hreflang");
    link.href = "/" + lang + "/" + pageSuffix;
  });
});
