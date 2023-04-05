const templatePromise = fetch('../template/my-template.html')
  .then(response => response.text())
  .then(html => new DOMParser().parseFromString(html, 'text/html'))
  .then(doc => doc.getElementById('my-template'));

const stylePromise = fetch('../template/my-template.css')
  .then(response => response.text());

class MyCustomElement extends HTMLElement {
  constructor() {
    super();
    templatePromise.then(template =>{
      const templateContent = template.content;

      const shadowRoot = this.attachShadow({mode : "open"});
      const instance = templateContent.cloneNode(true);
      shadowRoot.appendChild(instance);
    })

    stylePromise.then(css =>{
      const styleElement = document.createElement('style');
      styleElement.textContent = css;
      this.shadowRoot.appendChild(styleElement)
    })
  }


  connectedCallback() {
    console.log("Connected to the Body!")
    // Before, this used to assign the inner html of the element once it was connected, not anymore
    // still, we can use this function to run some lines of code once it connects to the body
    // this.innerHTML = "<h1>This is a great example</h1>";
  }
}

customElements.define("my-custom-element", MyCustomElement);