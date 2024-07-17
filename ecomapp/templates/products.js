const laptopsContainer=document.querySelector(".images-container")
console.log(images-container)
const API="https://file:///C:/Users/memelasr/Desktop/Apllied%20Ecomm%20Project/ecomapp/templates/products.html.com/products";

async function fetchAndDisplayData(){
    try{
        //fetch data
    const response =await fetch(API);
    const data = await response.json();
console.log(data)
    //display data
    displayData(data)
   
    }catch(err){
        console.log("something went wrong", err)
    }
}
fetchAndDisplayData(); 
function displayData(data){
    data.forEach((product)=>{
        const laptopsTemplate=`
        <div class="images-container">
    <div class="laptops">
      <a href="description.html?id={laptops.id}"><img src=${laptops.image}></a>
        </div>
      </div>
        `;
        imagesContainer.insertAdjacentHTML('beforeend',laptopsTemplate);
    });
}
