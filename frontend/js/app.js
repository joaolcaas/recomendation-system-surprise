 (function() {
    'use strict';
    const form = document.getElementById('form');

    function request(url) {
        return fetch(url).then(response => response.json());
	}

    function change_list_content(list, element) {
        const li = list.reduce((elements, value) => {
            return elements + `<li>${value}</li>`;
        }, "");
        element.innerHTML = li;
	}

	
}