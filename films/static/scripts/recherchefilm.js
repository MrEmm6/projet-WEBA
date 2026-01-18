document.addEventListener('DOMContentLoaded', function () {
    // récupérer les éléments utiles
    var section = document.getElementById('search-section');
    var api = section.dataset.searchUrl || '';
    var input = document.getElementById('search-input');
    var logEl = document.getElementById('search-log');
    var tbody = document.querySelector('#search-results tbody');

    // affichage de messages simples pour l'utilisateur / debug
    function log(msg) { if (logEl) logEl.textContent = msg; console.log(msg); }

    // supprime tout les enfant de tbody
    function clearResults() {
        while (tbody && tbody.firstChild) tbody.removeChild(tbody.firstChild);
    }

    // crée un élément du tableau pour chaque film correspondant
    function addRow(film) {
        var tr = document.createElement('tr');
        // on parcourt les clés attendues et on crée un <td> pour chacune
        ['titre', 'auteur', 'dateVue', 'avis'].forEach(function (k) {
            var td = document.createElement('td');
            td.textContent = film[k] || ''; // sécurité si champ absent
            tr.appendChild(td);
        });
        tbody.appendChild(tr); // ajout de nœud enfant -> modification DOM significative
    }

    // affiche la liste reçue (appelée après parsing JSON)
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

    // fonction utilitaire XHR GET asynchrone
    // cb est un callback avec signature cb(err, data)
    function xhrGet(url, cb) {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', url, true);
        xhr.setRequestHeader('Accept', 'application/json');
        xhr.onreadystatechange = function () {
            if (xhr.readyState !== 4) return; // attendre la fin
            if (xhr.status >= 200 && xhr.status < 300) {
                try { cb(null, JSON.parse(xhr.responseText)); } // parse JSON puis callback
                catch (e) { cb(e); }
            } else cb(new Error('HTTP ' + xhr.status));
        };
        xhr.send();
    }

    // quand on clique sur rechercher
    var btn = document.getElementById('btn-search');
    if (btn) btn.addEventListener('click', function () {
        var q = (input && input.value || '').trim();
        var url = api + '?q=' + encodeURIComponent(q);
        // log avant l'appel (montrer asynchronisme : le flux continue)
        log('Recherche en cours...');
        // appel XHR asynchrone : on passe une fonction (callback) pour traiter la réponse
        xhrGet(url, function (err, data) {
            if (err) { log('Erreur'); console.error(err); return; }
            log('Résultats reçus');
            display(data); // création dynamique des lignes du tableau
        });
    });
});
