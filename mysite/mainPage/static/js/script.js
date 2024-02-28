document.addEventListener('DOMContentLoaded', getCoord)


getCoord(location){
    const product = document.querySelector(".product-detail");
    const postcode = product.getAttribute('data-postcode');
    fetch(`https://api.postcodes.io/${postcode}`).then(
        response => response.json()
    ).then(
        data => {
            if (data.status === 200) {
                console.log(data.result);
            } else {
                console.error('Postcode not found');
            }
        }
    )
}


loadMap(position) {
    const { latitude } = position.coords;
    const { longitude } = position.coords;
    // console.log(`https://www.google.pt/maps/@${latitude},${longitude}`);

    const coords = [latitude, longitude];

    this.map = L.map('map').setView(coords, this.#mapZoomLevel);

    L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(this.map);

    L.marker(coords)
    .addTo(this.#map)
    .bindPopup(
        L.popup({
        maxWidth: 250,
        minWidth: 100,
        autoClose: false,
        closeOnClick: false,
        className: `${workout.type}-popup`,
        })
    ).openPopup();
  }

