const cuerpo = document.getElementById('cuerpo')

fetch('../json/juegos.json')
.then(response => response.json())
.then(data => {
  // Do something with the JSON data
  const juegos = data;
  console.log(juegos)
  // console.log(juegos[0]["name"])
  juegos.forEach(element => {
    // console.log(element["name"]);
    let gameElement = document.createElement('steam-game');
    gameElement.setAttribute('name', element["name"]);
    gameElement.setAttribute('onSale', element["onSale"]);
    gameElement.setAttribute('currency', element["currency"]);
    gameElement.setAttribute('price', element["price"]);
    gameElement.setAttribute('url', element["url"]);
    cuerpo.appendChild(gameElement);
  });
  const espacio = document.createElement('br')
  cuerpo.appendChild(espacio);
})
.catch(error => {
  // Handle any errors that occur during the fetch request
  console.error(error);
});


// const gameElement = document.createElement('steam-game')
// cuerpo.appendChild(gameElement);

// for(let i = 0; i < 10; i++){
//   let gameElement = document.createElement('steam-game')
//   cuerpo.appendChild(gameElement);
// }