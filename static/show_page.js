$(document).ready(function () {

  // Rating stars — original logic, gold colors
  const ratingEl = document.querySelector('#rating');
  const filledStars = '<i class="fa-solid fa-star" style="color:#c9a84c;"></i>'.repeat(showData.rating);
  const emptyStars = '<i class="fa-regular fa-star" style="color:#e8dfc8;"></i>'.repeat(5 - showData.rating);
  ratingEl.innerHTML = filledStars + emptyStars;

  // Cast members — original logic, restyled output
  const castRow = document.querySelector('#cast-row');

  showData.notable_cast.forEach(member => {
    const castEl = document.createElement('div');
    castEl.className = 'col d-flex align-items-center gap-3';

    const imageUrl = member.image
      ? member.image
      : `https://ui-avatars.com/api/?name=${encodeURIComponent(member.name)}&rounded=true&size=72&background=f0e8d4&color=8a6a20`;

    const nameHtml = member.related_show_id
      ? `<a href="/show/${member.related_show_id}" class="text-decoration-none">
           <h5 style="font-family:'Cormorant Garamond',serif; font-size:1rem; font-weight:600; color:#1a1610; margin:0; transition:color 0.2s;"
               onmouseover="this.style.color='#c9a84c'" onmouseout="this.style.color='#1a1610'">
             ${member.name.toUpperCase()}
           </h5>
         </a>`
      : `<h5 style="font-family:'Cormorant Garamond',serif; font-size:1rem; font-weight:600; color:#1a1610; margin:0;">
           ${member.name.toUpperCase()}
         </h5>`;

    const relatedShow = member.related_show
      ? `<p style="font-size:0.68rem; letter-spacing:0.1em; text-transform:uppercase; color:#b8a070; margin:0;">
           ${member.related_show}
         </p>`
      : '';

    castEl.innerHTML = `
      <img
        src="${imageUrl}"
        alt="Portrait of ${member.name}"
        style="width:72px; height:72px; object-fit:cover; object-position:center;
               border-radius:50%; border:2px solid #e8dfc8; flex-shrink:0;"
      >
      <div>${nameHtml}${relatedShow}</div>
    `;

    castRow.appendChild(castEl);
  });

});