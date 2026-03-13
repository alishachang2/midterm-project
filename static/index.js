$(document).ready(function () {
  const shows = showData;

  const top_3_shows = [1, 2, 3];
  const parent_div = document.querySelector('#show-row');

  for (const show of top_3_shows) {
    const top_show = shows.find(x => x.id === show);

    const col = document.createElement("div");
    col.className = "col-md-4";
    col.style.cursor = "pointer"; 

    col.innerHTML = `
      <div class="card">
        <img src="${top_show.image.url}" alt="${top_show.image.alt}" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">${top_show.title}</h5>
        </div>
      </div>
    `;

    col.addEventListener('click', () => {
      window.location.href = `/show/${top_show.id}`; // ✅ navigates to show page
    });

    parent_div.appendChild(col);
  }
});