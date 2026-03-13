$(document).ready(function () {
    console.log(showData);
  const shows = showData; 

  const top_3_shows = [1, 2, 3];
  const parent_div = document.querySelector('#show-row'); 

  for (const show of top_3_shows) {
    const top_show = shows.find(x => x.id === show); 

    const col = document.createElement("div");
    col.className = "col-md-4";

    col.innerHTML = `
      <div class="card">
        <img src="${top_show.image.url}" alt="${top_show.image.alt}" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">${top_show.title}</h5>
        </div>
      </div>
    `;

    parent_div.appendChild(col);
  }
});