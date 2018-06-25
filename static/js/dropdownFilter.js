function toggleDropdown(selEle) {
	document.getElementsByClass("dropdown-content").style.display = "none";
    selEle.nextElementSibling.classList.toggle("show");
}

function filterFunction(selEle) {
    var input, filter, ul, li, a, i;
    input = selEle;
    filter = input.value.toUpperCase();
    div = selEle.nextElementSibling;
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
        if (a[i].innerHTML.toUpperCase().indexOf(filter) > -1) {
            a[i].style.display = "";
        } else {
            a[i].style.display = "none";
        }
    }
}
