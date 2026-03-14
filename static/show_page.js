$(document).ready(function () {

  // Rating stars
  const ratingEl = document.querySelector('#rating');
const filledStars = '<i class="fa-solid fa-star text-warning"></i>'.repeat(showData.rating);
const emptyStars = '<i class="fa-regular fa-star text-secondary"></i>'.repeat(5 - showData.rating);
ratingEl.innerHTML = filledStars + emptyStars;
  // Cast members
  const castRow = document.querySelector('#cast-row');

  showData.notable_cast.forEach(member => {
    const castEl = document.createElement('div');
    castEl.className = 'col d-flex align-items-center gap-3';

    const imageUrl = member.image
      ? member.image
      : `https://ui-avatars.com/api/?name=${encodeURIComponent(member.name)}&rounded=true&size=72&background=random`;

    const nameHtml = member.related_show_id
      ? `<a href="/show/${member.related_show_id}" class="text-decoration-none text-dark">
           <h5 class="fw-bold mb-0">${member.name.toUpperCase()}</h5>
         </a>`
      : `<h5 class="fw-bold mb-0">${member.name.toUpperCase()}</h5>`;

    const relatedShow = member.related_show
      ? `<p class="text-muted text-uppercase mb-0 fw-light small">${member.related_show}</p>`
      : '';

    castEl.innerHTML = `
      <img
  src="${imageUrl}"
  alt="${member.name}"
  style="width:72px;height:72px;object-fit:cover;object-position:center;border-radius:50%;"
  class="flex-shrink-0"
>
      <div>
        ${nameHtml}
        ${relatedShow}
      </div>
    `;

    castRow.appendChild(castEl);
  });

});