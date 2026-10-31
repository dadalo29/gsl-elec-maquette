/* GSL-ELEC — interactions du site (sans dépendance) */
(function () {
  'use strict';

  /* Menu mobile */
  var toggle = document.querySelector('[data-menu-toggle]');
  var menu = document.getElementById('mobile-nav');
  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
      toggle.querySelector('.i-open').hidden = open;
      toggle.querySelector('.i-close').hidden = !open;
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('open')) { toggle.click(); toggle.focus(); }
    });
  }

  /* Format FCFA */
  function fmt(n) { return String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, ' '); }

  /* Simulateur d'économies — grille Senelec 2026 (hors redevances)
     Hypothèses provisoires : 130 kWh/kWc/mois ; couverture solaire 60 % maison, 70 % commerce. */
  var GRILLES = {
    maison:   { t: [82, 136.49, 159.36], tva3: 1.18, cov: 0.60, label: 'usage domestique petite puissance, TVA 18 % au-delà de 250 kWh' },
    commerce: { t: [147.43, 189.84, 208.63], tva3: 1, cov: 0.70, label: 'usage professionnel petite puissance' }
  };
  function cout(k, g) {
    if (k <= 150) return k * g.t[0];
    if (k <= 250) return 150 * g.t[0] + (k - 150) * g.t[1];
    return 150 * g.t[0] + 100 * g.t[1] + (k - 250) * g.t[2] * g.tva3;
  }
  function kwh(f, g) {
    var c1 = 150 * g.t[0], c2 = c1 + 100 * g.t[1];
    if (f <= c1) return f / g.t[0];
    if (f <= c2) return 150 + (f - c1) / g.t[1];
    return 250 + (f - c2) / (g.t[2] * g.tva3);
  }
  document.querySelectorAll('[data-simu]').forEach(function (root) {
    var type = 'maison';
    var range = root.querySelector('input[type=range]');
    var out = function (k) { return root.querySelector('[data-out="' + k + '"]'); };
    function render() {
      var g = GRILLES[type], f = Number(range.value);
      var k = kwh(f, g);
      var kwc = Math.max(1, Math.ceil((k * g.cov / 130) * 2) / 2);
      var apres = cout(k * (1 - g.cov), g);
      var eco = f - apres;
      var set = function (key, v) { var el = out(key); if (el) el.textContent = v; };
      set('facture', fmt(f));
      set('eco-mois', fmt(Math.round(eco / 500) * 500));
      set('eco-an', fmt(Math.round(eco * 12 / 5000) * 5000));
      set('apres', fmt(Math.round(apres / 500) * 500));
      set('kwc', String(kwc).replace('.', ','));
      set('grille', g.label);
      var bar = out('bar-apres'); if (bar) bar.style.width = Math.max(6, Math.round(apres / f * 100)) + '%';
      range.setAttribute('aria-valuetext', fmt(f) + ' francs CFA');
      root.querySelectorAll('[data-preset]').forEach(function (b) { b.setAttribute('aria-pressed', Number(b.dataset.preset) === f ? 'true' : 'false'); });
    }
    range.addEventListener('input', render);
    root.querySelectorAll('[data-type]').forEach(function (b) {
      b.addEventListener('click', function () {
        type = b.dataset.type;
        root.querySelectorAll('[data-type]').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        render();
      });
    });
    root.querySelectorAll('[data-preset]').forEach(function (b) {
      b.addEventListener('click', function () { range.value = b.dataset.preset; render(); });
    });
    render();
  });

  /* Filtres (équipements, réalisations, conseils, FAQ) */
  document.querySelectorAll('[data-filter-group]').forEach(function (group) {
    var target = document.getElementById(group.dataset.filterGroup);
    var count = document.querySelector('[data-count-for="' + group.dataset.filterGroup + '"]');
    group.querySelectorAll('[data-filter]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var f = btn.dataset.filter, n = 0;
        group.querySelectorAll('[data-filter]').forEach(function (b) { b.setAttribute('aria-pressed', b === btn ? 'true' : 'false'); });
        target.querySelectorAll('[data-tags]').forEach(function (item) {
          var show = f === 'tous' || item.dataset.tags.split(' ').indexOf(f) >= 0;
          item.hidden = !show; if (show) n++;
        });
        if (count) count.textContent = n + ' ' + (count.dataset.word || 'élément') + (n > 1 ? 's' : '');
      });
    });
  });

  /* Accordéon FAQ */
  document.querySelectorAll('.faq-item > button').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.parentElement, list = item.parentElement;
      var willOpen = !item.classList.contains('open');
      list.querySelectorAll('.faq-item.open').forEach(function (o) {
        o.classList.remove('open'); o.querySelector('button').setAttribute('aria-expanded', 'false');
      });
      if (willOpen) { item.classList.add('open'); btn.setAttribute('aria-expanded', 'true'); }
    });
  });

  /* Recherche FAQ */
  var faqSearch = document.getElementById('faq-q');
  if (faqSearch) {
    faqSearch.addEventListener('input', function () {
      var q = faqSearch.value.trim().toLowerCase();
      document.querySelectorAll('#faq-list .faq-item').forEach(function (it) {
        it.hidden = q !== '' && it.textContent.toLowerCase().indexOf(q) < 0;
      });
    });
  }

  /* Formulaires : validation simple puis message de confirmation (maquette, aucun envoi réel) */
  document.querySelectorAll('form[data-demo-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = true;
      form.querySelectorAll('[data-required]').forEach(function (field) {
        var bad = field.type === 'checkbox' ? !field.checked : field.value.trim().length < 6;
        field.classList.toggle('error', bad);
        field.setAttribute('aria-invalid', bad ? 'true' : 'false');
        var msg = form.querySelector('[data-err-for="' + field.id + '"]');
        if (msg) msg.classList.toggle('show', bad);
        if (bad && ok) { field.focus(); ok = false; }
      });
      if (!ok) return;
      var wa = document.body.getAttribute('data-wa');
      if (wa) {
        /* Version en ligne : la demande est envoyée sur le WhatsApp de GSL-ELEC, déjà rédigée */
        var lines = ['Bonjour GSL-ELEC, voici ma demande (' + (form.getAttribute('aria-label') || 'devis') + ') :'];
        form.querySelectorAll('input, select, textarea').forEach(function (f) {
          if (f.type === 'checkbox' || f.type === 'file' || f.type === 'hidden') return;
          if (f.type === 'radio' && !f.checked) return;
          var v = f.tagName === 'SELECT' ? f.options[f.selectedIndex].text : f.value.trim();
          if (!v) return;
          var lab = f.id && form.querySelector('label[for="' + f.id + '"]');
          var name = lab ? lab.textContent.replace(/\*|\(facultatif\)/g, '').trim() : (f.name || '');
          lines.push('- ' + name + ' : ' + v);
        });
        var file = form.querySelector('input[type=file]');
        if (file && file.files.length) lines.push('(Je vous envoie la photo de ma facture juste après.)');
        window.open('https://wa.me/' + wa + '?text=' + encodeURIComponent(lines.join('\n')), '_blank');
        var st = form.querySelector('.success strong'), sp = form.querySelector('.success p');
        if (st) st.textContent = 'Votre demande est prête dans WhatsApp';
        if (sp) sp.textContent = 'Appuyez sur « Envoyer » dans WhatsApp pour nous la transmettre. WhatsApp ne s’est pas ouvert ? Écrivez-nous ou appelez le ' + '+221 77 701 98 83.';
      }
      form.classList.add('sent');
      var s = form.querySelector('.success');
      if (s) { s.setAttribute('tabindex', '-1'); s.focus(); }
    });
    form.querySelectorAll('[data-reset-form]').forEach(function (b) {
      b.addEventListener('click', function () { form.reset(); form.classList.remove('sent'); });
    });
  });

  /* Pré-sélection du service dans le formulaire de contact (?service=…) */
  var params = new URLSearchParams(location.search);
  var svc = params.get('service');
  var sel = document.getElementById('c-service');
  if (svc && sel) {
    Array.prototype.forEach.call(sel.options, function (o) { if (o.value === svc) sel.value = svc; });
  }

  /* Nom du fichier joint */
  document.querySelectorAll('.upload input[type=file]').forEach(function (inp) {
    inp.addEventListener('change', function () {
      var t = inp.parentElement.querySelector('[data-file-name]');
      if (t && inp.files.length) t.textContent = inp.files[0].name;
    });
  });

  /* Année du pied de page */
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
