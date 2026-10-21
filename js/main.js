/**
 * MFACH - Internetowa Wizytówka Usługowa
 * Marcin | Tel: 695 525 389
 * Obsługa 3 motywów branżowych, dynamicznej zawartości i interakcji
 */

const BRANCH_DATA = {
  agro: {
    themeClass: 'theme-agro',
    metaTitle: 'MFach - Serwis Ciągników Rolniczych | Marcin 695 525 389',
    image: 'assets/hero_agro.png',
    imageAlt: 'Marcin MFach - Serwis Ciągników Rolniczych',
    badgeIcon: `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="7" cy="17" r="4"/><circle cx="17" cy="17" r="2"/><path d="M7 17h10"/><path d="M9 13h5l3 4"/><path d="M9 13V9a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v4"/><path d="M14 7V4a1 1 0 0 0-1-1h-2a1 1 0 0 0-1 1v3"/></svg>`,
    badgeText: 'Ciągniki Rolnicze i Maszyny Agro',
    title: 'Niezawodny serwis i naprawa <span class="highlight">ciągników rolniczych</span>',
    desc: 'Szybka pomoc na gospodarstwie i bezpośrednio w polu. Remonty silników, skrzyń biegów, regeneracja i diagnostyka hydrauliki siłowej oraz przeglądy przedsezonowe maszyn.',
    trustPoints: [
      { title: 'Dojazd w pole i gospodarstwo', desc: 'Mobilny serwis w trakcie żniw i prac polowych' },
      { title: 'Części oryginalne & zamienniki', desc: 'Dopasowanie do budżetu i specyfikacji maszyny' },
      { title: 'Sprawdzona hydraulika & mechanika', desc: 'Diagnostyka ciśnień i szczelności układów' },
      { title: 'Dyspozycyjność w sezonie', desc: 'Szybka reakcja na nagłe awarie' }
    ],
    servicesHeading: 'Oferta Serwisowa dla Rolnictwa',
    servicesDesc: 'Zapewniam pełne wsparcie techniczne, aby Twoje maszyny pracowały bez przestojów w kluczowych momentach sezonu.',
    services: [
      {
        icon: `<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>`,
        title: 'Remonty Silników & Skrzyń',
        desc: 'Kompleksowe naprawy jednostek napędowych, regulacja zaworów, regeneracja głowic, naprawa przekładni i mostów napędowych.',
        features: ['Diagnostyka kompresji', 'Usuwanie wycieków', 'Precyzyjna regulacja']
      },
      {
        icon: `<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>`,
        title: 'Hydraulika Siłowa',
        desc: 'Wymiana i naprawa pomp hydraulicznych, siłowników, zaworów sterujących oraz rozdzielaczy hydraulicznych.',
        features: ['Pomiary ciśnienia roboczego', 'Wymiana uszczelnień siłowników', 'Filtracja i wymiana oleju']
      },
      {
        icon: `<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>`,
        title: 'Mobilny Serwis Polowy',
        desc: 'Dojazd z narzędziami bezpośrednio na pole lub do bazy sprzętowej rolnika. Szybka diagnoza i usunięcie usterki na miejscu.',
        features: ['Dojazd na telefon', 'Pomoc w krytycznym momencie', 'Profesjonalne narzędzia mobilne']
      },
      {
        icon: `<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none"><circle cx="12" cy="12" r="10"/><path d="m4.93 4.93 4.24 4.24"/><path d="m14.83 9.17 4.24-4.24"/><path d="m14.83 14.83 4.24 4.24"/><path d="m9.17 14.83-4.24 4.24"/></svg>`,
        title: 'Układy Hamulcowe i Pneumatyka',
        desc: 'Serwis układów hamulcowych pneumatycznych i hydraulicznych, naprawa sprężarek, zaworów sterujących przyczepami.',
        features: ['Bezpieczeństwo na drodze i polu', 'Regeneracja sprężarek', 'Szczelność układów']
      },
      {
        icon: `<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>`,
        title: 'Przeglądy Przedsezonowe',
        desc: 'Kompletne przygotowanie ciągnika i maszyn towarzyszących przed rozpoczęciem orki, siewów czy żniw.',
        features: ['Wymiana filtrów i olejów', 'Smarowanie punktów węzłowych', 'Kontrola pasków i chłodzenia']
      },
      {
        icon: `<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/></svg>`,
        title: 'Instalacje Elektryczne Ciągników',
        desc: 'Usuwanie zwarć, naprawa oświetlenia roboczego LED, alternatorów, rozruszników i układów ładowania akumulatorów.',
        features: ['Oświetlenie robocze nocne', 'Sprawne rozruszniki', 'Nowe wiązki kablowe']
      }
    ]
  },

  auto: {
    themeClass: 'theme-auto',
    metaTitle: 'MFach - Mechanika Samochodowa | Marcin 695 525 389',
    image: 'assets/hero_auto.png',
    imageAlt: 'Marcin MFach - Mechanika Samochodowa',
    badgeIcon: `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A3.7 3.7 0 0 0 2 12v4c0 .6.4 1 1 1h2"/><circle cx="7" cy="17" r="2"/><path d="M9 17h6"/><circle cx="17" cy="17" r="2"/></svg>`,
    badgeText: 'Mechanika Samochodowa & Eksploatacja',
    title: 'Solidna i uczciwa <span class="highlight">mechanika samochodowa</span>',
    desc: 'Bieżące naprawy, wymiana oleju, filtrów, serwis hamulców i zawieszenia. Precyzyjna diagnoza problemu, uczciwe ceny i terminowe wykonanie.',
    trustPoints: [
      { title: 'Szybkie terminy realizacji', desc: 'Wymiany eksploatacyjne nawet z dnia na dzień' },
      { title: 'Uczciwe rozliczenie', desc: 'Jasny kosztorys przed przystąpieniem do naprawy' },
      { title: 'Części od renomowanych hurtowni', desc: 'Gwarancja jakości montowanych podzespołów' },
      { title: 'Indywidualne podejście', desc: 'Bez naciągania na niepotrzebne koszty' }
    ],
    servicesHeading: 'Oferta Mechaniki Pojazdowej',
    servicesDesc: 'Dbam o to, by Twój samochód był bezpieczny, sprawny i gotowy do każdej trasy.',
    services: [
      {
        icon: `<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none"><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/></svg>`,
        title: 'Wymiana Oleju & Filtrów',
        desc: 'Kompleksowa wymiana oleju silnikowego, filtrów (oleju, powietrza, paliwa, kabinowego) oraz kasowanie inspekcji serwisowej.',
        features: ['Dobór właściwej lepkości i norm', 'Sprawdzenie szczelności miski', 'Kontrola płynów eksploatacyjnych']
      },
      {
        icon: `<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>`,
        title: 'Układy Hamulcowe',
        desc: 'Wymiana klocków, tarcz hamulcowych, bębnów, szczęk, przewodów elastycznych oraz wymiana i odpowietrzanie płynu hamulcowego.',
        features: ['Czyszczenie i smarowanie zacisków', 'Pomiary bicia tarcz', 'Kontrola hamulca ręcznego']
      },
      {
        icon: `<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg>`,
        title: 'Zawieszenie & Układ Kierowniczy',
        desc: 'Wymiana wahaczy, sworzni, końcówek drążków, amortyzatorów, sprężyn oraz łączników stabilizatora. Eliminacja stuków.',
        features: ['Precyzyjne prowadzenie pojazdu', 'Bezpieczeństwo na nierównościach', 'Komfort jazdy']
      },
      {
        icon: `<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M20 9h3M20 14h3M1 9h3M1 14h3"/></svg>`,
        title: 'Diagnostyka Komputerowa',
        desc: 'Odczyt i kasowanie błędów ze sterowników silnika (Check Engine), ABS, ESP, poduszek powietrznych oraz wgląd w parametry pracy.',
        features: ['Wykrywanie ukrytych usterek', 'Podgląd parametrów na żywo', 'Szybka lokalizacja problemu']
      },
      {
        icon: `<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none"><circle cx="12" cy="12" r="8"/><line x1="3.6" y1="9" x2="8.4" y2="15"/><line x1="20.4" y1="9" x2="15.6" y2="15"/></svg>`,
        title: 'Rozrządy, Paski & Sprzęgła',
        desc: 'Wymiana pasków rozrządu wraz z pompą cieczy chłodzącej, pasków klinowych osprzętu oraz kompletnych zestawów sprzęgła.',
        features: ['Zabezpieczenie silnika przed kolizją', 'Płynna zmiana biegów', 'Sprawdzone marki części']
      },
      {
        icon: `<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>`,
        title: 'Przygotowanie do Przeglądu',
        desc: 'Szczegółowy przegląd stanu technicznego auta przed obowiązkowym badaniem technicznym na stacji kontroli pojazdów.',
        features: ['Oświetlenie i regulacja świateł', 'Układ wydechowy i emisja', 'Brak niespodzianek na stacji']
      }
    ]
  },

  build: {
    themeClass: 'theme-build',
    metaTitle: 'MFach - Budownictwo, Wykończenia & Hydraulika | Marcin 695 525 389',
    image: 'assets/hero_build.png',
    imageAlt: 'Marcin MFach - Budownictwo, Wykończenia Wnętrz i Hydraulika',
    badgeIcon: `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>`,
    badgeText: 'Usługi Ogólnobudowlane, Wykończenia Wnętrz & Hydraulika',
    title: 'Solidne <span class="highlight">wykończenia wnętrz</span> i instalacje hydrauliczne',
    desc: 'Kompleksowe remonty mieszkań i domów, niezawodne instalacje wodno-kanalizacyjne, montaż ceramiki, gładzie, malowanie i prace montażowe. Czysto, dokładnie i na lata.',
    trustPoints: [
      { title: 'Kompleksowość usług', desc: 'Od hydrauliki i gładzi po montaż finalny' },
      { title: 'Porządek i czystość prac', desc: 'Zabezpieczenie mienia i regularne sprzątanie' },
      { title: 'Sprawdzone materiały budowlane', desc: 'Doradztwo techniczne i pomoc w zakupach' },
      { title: 'Terminowa realizacja', desc: 'Praca według uzgodnionego z góry harmonogramu' }
    ],
    servicesHeading: 'Oferta Remontowo-Budowlana & Hydrauliczna',
    servicesDesc: 'Oferuję szeroki zakres prac remontowych i instalacyjnych dla domów, mieszkań i lokali użytkowych.',
    services: [
      {
        icon: `<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none"><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/></svg>`,
        title: 'Instalacje Hydrauliczne & Wod-Kan',
        desc: 'Montaż i modernizacja rurociągów wody użytkowej, odpływów kanalizacyjnych, podłączenia zaworów oraz usuwanie nieszczelności.',
        features: ['Bezpieczne połączenia rur', 'Piony i podejścia kanalizacyjne', 'Pomiary szczelności ciśnieniowej']
      },
      {
        icon: `<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>`,
        title: 'Biały Montaż & Remont Łazienek',
        desc: 'Montaż stelaży podtynkowych (Geberit), misek WC, kabin prysznicowych, wanien, umywalek, armatury i odpływów liniowych.',
        features: ['Idealne uszczelnienia silikonowe', 'Precyzyjny montaż armatury', 'Próby odpływowe']
      },
      {
        icon: `<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none"><path d="m19 11-8-8-8.6 8.6a2 2 0 0 0 0 2.8l5.2 5.2c.8.8 2 .8 2.8 0L19 11Z"/><path d="m5 2 5 5"/><path d="M2 13h15"/><path d="M22 20a2 2 0 1 1-4 0c0-1.6 1.7-2.4 2-4 .3 1.6 2 2.4 2 4Z"/></svg>`,
        title: 'Gładzie, Szpachlowanie & Malowanie',
        desc: 'Przygotowanie podłoża, gruntowanie, gładzie bezpyłowe, szlifowanie pod światło i precyzyjne malowanie ścian i sufitów.',
        features: ['Gładkie i równe powierzchnie', 'Trwałe farby zmywalne', 'Zabezpieczenie stolarki i podłóg']
      },
      {
        icon: `<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="12" y1="3" x2="12" y2="21"/></svg>`,
        title: 'Zabudowy G-K & Sufity Podwieszane',
        desc: 'Ścianki działowe z płyt gipsowo-kartonowych, sufity podwieszane jedno- i wielopoziomowe, zabudowy rur i wnęk oświetleniowych.',
        features: ['Izolacja akustyczna wełną', 'Solidna konstrukcja profili', 'Zbrojenie łączeń taśmami']
      },
      {
        icon: `<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>`,
        title: 'Panele Podłogowe & Listwy',
        desc: 'Układanie paneli laminowanych i winylowych wraz z podkładami wyciszającymi oraz estetyczny montaż listew przypodłogowych.',
        features: ['Dylatacje obwodowe', 'Ciche podkłady podłogowe', 'Niewidoczne łączenia narożników']
      },
      {
        icon: `<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>`,
        title: 'Drobne Naprawy & Złota Rączka',
        desc: 'Wymiana baterii, cieknących syfonów, zawiasów, regulacja drzwi, wieszanie szafek, karniszy oraz inne pilne prace domowe.',
        features: ['Szybki dojazd do klienta', 'Własne narzędzia i osprzęt', 'Wycena na miejscu']
      }
    ]
  }
};

// Funkcja aktualizacji widoku na podstawie wybranego profilu
function setBranch(branchKey, pushHash = true) {
  if (!BRANCH_DATA[branchKey]) return;
  const data = BRANCH_DATA[branchKey];

  // 1. Aktualizacja klas na body
  document.body.classList.remove('theme-agro', 'theme-auto', 'theme-build');
  document.body.classList.add(data.themeClass);
  document.body.setAttribute('data-theme', branchKey);

  // 2. Aktualizacja stanu przycisków przełącznika
  document.querySelectorAll('.branch-tab-btn').forEach(btn => {
    const isTarget = btn.getAttribute('data-branch') === branchKey;
    btn.classList.toggle('active', isTarget);
    btn.setAttribute('aria-pressed', isTarget ? 'true' : 'false');
  });

  // 3. Aktualizacja zawartości Hero (jeśli istnieje na danej stronie)
  const heroBadge = document.getElementById('heroBadge');
  if (heroBadge) {
    heroBadge.innerHTML = `${data.badgeIcon} <span>${data.badgeText}</span>`;
  }

  const heroTitle = document.getElementById('heroTitle');
  if (heroTitle) {
    heroTitle.innerHTML = data.title;
  }

  const heroDesc = document.getElementById('heroDesc');
  if (heroDesc) {
    heroDesc.innerHTML = data.desc;
  }

  // Aktualizacja ilustracji bohatera (Marcin & maszyna/obiekt)
  const heroImage = document.getElementById('heroImage');
  if (heroImage && data.image) {
    heroImage.src = data.image;
    heroImage.alt = data.imageAlt || 'MFach Marcin';
  }

  // 4. Aktualizacja punktów zaufania
  const trustList = document.getElementById('trustList');
  if (trustList && data.trustPoints) {
    trustList.innerHTML = data.trustPoints.map(point => `
      <div class="trust-item">
        <div class="trust-icon-box">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
        </div>
        <div>
          <div class="trust-label">${point.title}</div>
          <div class="trust-sub">${point.desc}</div>
        </div>
      </div>
    `).join('');
  }

  // 5. Aktualizacja sekcji Usługi
  const servicesHeading = document.getElementById('servicesHeading');
  if (servicesHeading) servicesHeading.textContent = data.servicesHeading;

  const servicesDesc = document.getElementById('servicesDesc');
  if (servicesDesc) servicesDesc.textContent = data.servicesDesc;

  const servicesGrid = document.getElementById('servicesGrid');
  if (servicesGrid && data.services) {
    servicesGrid.innerHTML = data.services.map(svc => `
      <div class="service-card">
        <div class="service-card-icon">
          ${svc.icon}
        </div>
        <h3>${svc.title}</h3>
        <p>${svc.desc}</p>
        <ul class="service-features-list">
          ${svc.features.map(f => `
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
              <span>${f}</span>
            </li>
          `).join('')}
        </ul>
      </div>
    `).join('');
  }

  // 6. Tytuł strony
  if (data.metaTitle) {
    document.title = data.metaTitle;
  }

  // 7. Aktualizacja hash w pasku adresu (opcjonalna)
  if (pushHash && window.location.pathname.endsWith('index.html') || window.location.pathname === '/' || window.location.pathname.endsWith('/')) {
    history.replaceState(null, '', `#${branchKey}`);
  }
}

// Obsługa kopiowania numeru telefonu
function setupPhoneCopy() {
  const copyBtns = document.querySelectorAll('.js-copy-phone');
  const toast = document.getElementById('toastNotice');

  copyBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const phoneNumber = '695525389';
      navigator.clipboard.writeText(phoneNumber).then(() => {
        if (toast) {
          toast.textContent = '✓ Skopiowano numer telefonu: 695 525 389';
          toast.classList.add('show');
          setTimeout(() => {
            toast.classList.remove('show');
          }, 3200);
        }
      }).catch(() => {
        window.location.href = 'tel:695525389';
      });
    });
  });
}

// Obsługa gestu przesunięcia palcem (Touch Swipe) na telefonie
function setupSwipeGesture() {
  let touchStartX = 0;
  let touchStartY = 0;
  let touchEndX = 0;
  let touchEndY = 0;

  const branches = ['agro', 'auto', 'build'];
  const pageMap = {
    agro: 'rolnictwo.html',
    auto: 'mechanika.html',
    build: 'budownictwo.html'
  };

  document.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
    touchStartY = e.changedTouches[0].screenY;
  }, { passive: true });

  document.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    touchEndY = e.changedTouches[0].screenY;
    handleSwipe();
  }, { passive: true });

  function handleSwipe() {
    const diffX = touchEndX - touchStartX;
    const diffY = touchEndY - touchStartY;

    // Sprawdzamy czy to wyraźny gest poziomy (min. 50px) i nie jest to scroll pionowy
    if (Math.abs(diffX) >= 50 && Math.abs(diffX) > Math.abs(diffY) * 1.3) {
      const isIndexPage = window.location.pathname.endsWith('index.html') || 
                          window.location.pathname === '/' || 
                          window.location.pathname.endsWith('/') ||
                          !window.location.pathname.includes('.html');
      
      const currentBranch = document.body.getAttribute('data-theme') || 'agro';
      let currentIndex = branches.indexOf(currentBranch);
      if (currentIndex === -1) currentIndex = 0;

      let targetIndex;
      if (diffX < 0) {
        // Przesunięcie w lewo (swipe left) -> następna branża
        targetIndex = (currentIndex + 1) % branches.length;
      } else {
        // Przesunięcie w prawo (swipe right) -> poprzednia branża
        targetIndex = (currentIndex - 1 + branches.length) % branches.length;
      }

      const targetBranch = branches[targetIndex];

      if (isIndexPage) {
        // Na stronie głównej dynamiczne przełączenie motywu i treści
        setBranch(targetBranch, true);
      } else {
        // Na podstronach przejście do odpowiedniej strony
        window.location.href = pageMap[targetBranch];
      }
    }
  }
}

// Inicjalizacja przy ładowaniu strony
document.addEventListener('DOMContentLoaded', () => {
  // Przypisanie zdarzeń do przycisków przełącznika
  document.querySelectorAll('.branch-tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const branch = btn.getAttribute('data-branch');
      setBranch(branch, true);
    });
  });

  // Odczyt domyślnego motywu ze strony lub hasha URL
  const hash = window.location.hash.replace('#', '').toLowerCase();
  const pageDefault = document.body.getAttribute('data-theme') || 'agro';

  let initialBranch = pageDefault;
  if (hash === 'agro' || hash === 'rolnictwo' || hash === 'ciagniki') {
    initialBranch = 'agro';
  } else if (hash === 'auto' || hash === 'samochody' || hash === 'mechanika') {
    initialBranch = 'auto';
  } else if (hash === 'build' || hash === 'budowlanka' || hash === 'budownictwo' || hash === 'hydraulika') {
    initialBranch = 'build';
  }

  setBranch(initialBranch, false);
  setupPhoneCopy();
  setupSwipeGesture();

  // Nasłuchiwanie zmian hasha w URL
  window.addEventListener('hashchange', () => {
    const curHash = window.location.hash.replace('#', '').toLowerCase();
    if (['agro', 'auto', 'build'].includes(curHash)) {
      setBranch(curHash, false);
    }
  });
});
