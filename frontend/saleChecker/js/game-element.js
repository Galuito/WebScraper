const templatePromise = fetch('../template/game-element-template.html')
  .then(response => response.text())
  .then(html => new DOMParser().parseFromString(html, 'text/html'))
  .then(doc => doc.getElementById('my-template'));

const stylePromise = fetch('../template/game-element-template.css')
  .then(response => response.text());



class SteamGame extends HTMLElement{
  constructor(){
    super();
    templatePromise.then(template =>{
      const templateContent = template.content;

      const shadowRoot = this.attachShadow({mode : "open"});
      const instance = templateContent.cloneNode(true);
      shadowRoot.appendChild(instance)

      this.updateContent();
    })

    stylePromise.then(css =>{
      const styleElement = document.createElement('style');
      styleElement.textContent = css;
      this.shadowRoot.appendChild(styleElement);
    })
  }

  connectedCallback(){
    console.log("Steam Game Connected to the Body!")
  }



  updateContent(){
    console.log("Realizando los cambios")
    const nameElement = this.shadowRoot.querySelector("#name");
    const saleElement = this.shadowRoot.querySelector("#onSale");
    const priceElement = this.shadowRoot.querySelector("#price");
    const currencyElement = this.shadowRoot.querySelector("#currency");
    const saleDiv = this.shadowRoot.querySelector("#oferta");

    nameElement.textContent = this.getAttribute('name') || 'Default Title';
    nameElement.href = this.getAttribute('url') || "https://www.youtube.com/watch?v=dQw4w9WgXcQ";
    saleElement.textContent = this.getAttribute('onSale') || 'No';
    priceElement.textContent = this.getAttribute('price') || 'Default Price';
    currencyElement.textContent = this.getAttribute('currency') || 'Default Currency';

    if(this.getAttribute('onSale') == "YES"){
      saleDiv.style.backgroundColor = '#73AD21';
    }
    else{
      saleDiv.style.backgroundColor = '#b90505';
    }
  }


}

customElements.define("steam-game", SteamGame)