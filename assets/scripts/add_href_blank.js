//open external links in a new window
(function () {
    for (var c = document.getElementsByTagName("a"), a = 0; a < c.length; a++) {
        var b = c[a];
        if (b.getAttribute("href") && b.hostname !== location.hostname) {
            if (!b.target) {
                b.target = "_blank";
                b.rel = "noopener";
            }
        }
    }
})();
//open PDF links in a new window
(function () {
    if (!document.getElementsByTagName) return false;
    var links = document.getElementsByTagName("a");
    for (var eleLink = 0; eleLink < links.length; eleLink++) {
        if ((links[eleLink].href.indexOf('.pdf') !== -1) || (links[eleLink].href.indexOf('.doc') !== -1) || (links[eleLink].href.indexOf('.docx') !== -1)) {
            links[eleLink].onclick =
                function () {
                    window.open(this.href);
                    return false;
                }
        }
    }
})();
