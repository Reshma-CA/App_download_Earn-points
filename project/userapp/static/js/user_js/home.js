document.addEventListener("DOMContentLoaded", function() {
    fetch('http://127.0.0.1:8000/api/home/')
    .then(response => response.json())
    .then(data => {
        console.log('Fetched data:', data);  // Log the data to the console

        const appsList = document.getElementById('home');
        appsList.innerHTML = '';  // Clear existing content

        data.forEach(app => {
            const itemDiv = document.createElement('div');
            itemDiv.className = 'item';

            // Dynamically add the image and other details
            itemDiv.innerHTML = `
          
                <img src="${app.app_image}" id="app_images" alt="${app.name} Image">
                <h2>App Name: ${app.name}</h2>
                <h3>Category:${app.category.name}</h3>
                <h4>Sub category:${app.sub_category.name}</h4>
                <button>Points: ${app.points}</button>
                   
            `;

            appsList.appendChild(itemDiv);
        });
    })
    .catch(error => console.error('Error fetching data:', error));
});
