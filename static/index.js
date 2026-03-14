$(document).ready(function () {
  const TOP_IDS = [1, 2, 3];
  const parent = document.getElementById('show-row');

  TOP_IDS.forEach(id => {
    const show = showData.find(x => x.id === id);
    if (!show) return;

    const col = document.createElement('div');
    col.className = 'col-md-4';
    col.setAttribute('role', 'listitem');

    col.innerHTML = `
      <a href="/show/${show.id}" class="rt-card" aria-label="View details for ${show.title}">
        <div class="rt-card__img-wrap">
          <img
            src="${show.image.url}"
            alt="${show.image.alt}"
            class="rt-card__img"
          >
          <span class="rt-card__genre">${Array.isArray(show.genre) ? show.genre[0] : show.genre}</span>
          <span class="rt-card__rating" aria-label="Rating: ${show.rating}">${show.rating}</span>
        </div>
        <div class="rt-card__body">
          <h3 class="rt-card__title">${show.title}</h3>
          <p class="rt-card__meta">${show.network} · Season ${show.season}</p>
          <p class="rt-card__desc">${show.summary}</p>
          <span class="rt-card__cta" aria-hidden="true">
            Watch now
            <svg width="14" height="14" viewBox="0 0 16 16" fill="none"
                 stroke="currentColor" stroke-width="2" aria-hidden="true">
              <path d="M3 8h10M9 4l4 4-4 4"/>
            </svg>
          </span>
        </div>
      </a>
    `;

    parent.appendChild(col);
  });
});