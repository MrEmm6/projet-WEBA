document.addEventListener('DOMContentLoaded', function () {
    var section = document.getElementById('search-section');
    if (!section) return;
    var api = section.dataset.searchUrl || '';
    var input = document.getElementById('search-input');
    var logEl = document.getElementById('search-log');
    var tbody = document.querySelector('#search-results tbody');

    function log(msg) { if (logEl) logEl.textContent = msg; console.log(msg); }

    function clearResults() {
        while (tbody && tbody.firstChild) tbody.removeChild(tbody.firstChild);
    }

    function addRow(film) {
        var tr = document.createElement('tr');
        ['titre', 'auteur', 'dateVue', 'avis'].forEach(function (k) {
            var td = document.createElement('td');
            td.textContent = film[k] || '';
            tr.appendChild(td);
        });
        tbody.appendChild(tr);
    }

    function display(data) {
        clearResults();
        if (!Array.isArray(data) || data.length === 0) {
            var tr = document.createElement('tr');
            var td = document.createElement('td');
            td.colSpan = 4;
            td.textContent = 'Aucun résultat';
            tr.appendChild(td);
            tbody.appendChild(tr);
            return;
        }
        data.forEach(addRow);
    }

    function xhrGet(url, cb) {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', url, true);
        xhr.setRequestHeader('Accept', 'application/json');
        xhr.onreadystatechange = function () {
            if (xhr.readyState !== 4) return;
            if (xhr.status >= 200 && xhr.status < 300) {
                try { cb(null, JSON.parse(xhr.responseText)); }
                catch (e) { cb(e); }
            } else cb(new Error('HTTP ' + xhr.status));
        };
        xhr.send();
    }

    var btn = document.getElementById('btn-search');
    if (btn) btn.addEventListener('click', function () {
        var q = (input && input.value || '').trim();
        var url = api + '?q=' + encodeURIComponent(q);
        log('Recherche en cours...');
        xhrGet(url, function (err, data) {
            if (err) { log('Erreur'); console.error(err); return; }
            log('Résultats reçus');
            display(data);
        });
    });
});
