const productcontainer=document.querySelector('#product-container');
console.log(product-container)
async function
fetchAndDisplaySingleLaptops(){
    const laptopsId =new URLSearchParams(window.location.search).get('id')
    const response=await fetch(`https://file:///C:/Users/memelasr/Desktop/Apllied%20Ecomm%20Project/ecomapp/templates/products.html.com/products/${laptopsId}`);
    const laptops=await response.json();
    console.log(laptops, laptopsId);
    displayLaptops(laptops);
      
}
function displayLaptops(laptops){
productcontainer.innerHTML=`<div class="laptops">
    <a href="description.html"><img src=${laptops,image}></a>
    </div>
   `;
}

fetchAndDisplaySingleLaptops();

