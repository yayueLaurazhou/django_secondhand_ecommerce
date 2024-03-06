document.addEventListener('DOMContentLoaded', getCoord);


function getCoord(location){
    const product = document.querySelector(".product-detail");
    const postcode = product.getAttribute('data-postcode');
    fetch(`https://api.postcodes.io/postcodes/${postcode}`).then(
        response => response.json()
    ).then(
        data => {
            if (data.status === 200) {
                const latitude =  data.result.latitude
                const longitude = data.result.longitude
                loadMap(latitude, longitude)
            } else {
                console.error('Postcode not found');
            }
        }
    )
}


function loadMap(latitude, longitude) {

    const coords = [latitude, longitude];

    map = L.map('map').setView(coords,19);

    L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(map);

    L.marker(coords)
    .addTo(map)
    .bindPopup(
        L.popup({
        maxWidth: 250,
        minWidth: 100,
        autoClose: false,
        closeOnClick: false,
        })
    ).setPopupContent(
        "Collect here!"
    ).openPopup();
  }

