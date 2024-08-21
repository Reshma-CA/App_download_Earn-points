document.addEventListener("DOMContentLoaded", function() {
    // Function to populate categories
    function populateCategories() {
        fetch('http://127.0.0.1:8000/djadmin/api/categories/')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const categorySelect = document.getElementById('app_category');
            categorySelect.innerHTML = '<option value="">Select Category</option>'; // Default option

            data.forEach(category => {
                const option = document.createElement('option');
                option.value = category.id;
                option.textContent = category.name;
                categorySelect.appendChild(option);
            });
        })
        .catch(error => console.error('Error fetching categories:', error));
    }

    // Function to populate subcategories based on selected category
    function populateSubCategories(categoryId) {
        fetch(`http://127.0.0.1:8000/djadmin/api/subcategories/?category_id=${categoryId}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const subCategorySelect = document.getElementById('sub_category');
            subCategorySelect.innerHTML = '<option value="">Select Sub Category</option>'; // Default option

            data.forEach(subcategory => {
                const option = document.createElement('option');
                option.value = subcategory.id;
                option.textContent = subcategory.name;
                subCategorySelect.appendChild(option);
            });
        })
        .catch(error => console.error('Error fetching subcategories:', error));
    }

    // Initialize categories on page load
    populateCategories();

    // Event listener for category change to update subcategories
    document.getElementById('app_category').addEventListener('change', function(event) {
        const selectedCategoryId = event.target.value;
        if (selectedCategoryId) {
            populateSubCategories(selectedCategoryId);
        } else {
            document.getElementById('sub_category').innerHTML = '<option value="">Select Sub Category</option>'; // Default option
        }
    });

    // Handle form submission
    document.getElementById('app-form').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        const formData = new FormData(this);

        fetch('http://127.0.0.1:8000/djadmin/api/admin_dash/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken') // Ensure CSRF token is included
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.errors) {
                // Show validation errors to the user
                document.getElementById('error-message').textContent = data.errors;
                document.getElementById('error-message').style.display = 'block';
                
                // Hide success message if it was previously shown
                document.getElementById('success-message').style.display = 'none';
            } else {
                // Success - Show a success message and optionally clear the form
                document.getElementById('success-message').textContent = 'App added successfully!';
                document.getElementById('success-message').style.display = 'block';
                
                // Optionally, reset the form
                document.getElementById('app-form').reset();
                
                // Hide the error message if it was previously shown
                document.getElementById('error-message').style.display = 'none';
            }
        })
        .catch(error => {
            // Error during form submission
            console.error('Error adding app:', error);
            document.getElementById('error-message').textContent = 'There was an error submitting the form.';
            document.getElementById('error-message').style.display = 'block';

            // Hide the success message if it was previously shown
            document.getElementById('success-message').style.display = 'none';
        });
    });

    // Utility function to get CSRF token from cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Handle image preview functionality
    document.getElementById('app_image').onclick = function() {
        document.getElementById('file').click();
    };

    document.getElementById('file').onchange = function(event) {
        var reader = new FileReader();
        reader.onload = function() {
            var img = document.getElementById('app_image');
            img.src = reader.result;
        };
        reader.readAsDataURL(event.target.files[0]);

        // Prepare the file data to be sent to the server
        var formData = new FormData();
        formData.append('image', event.target.files[0]);

        // Send the image to the server via AJAX
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '{% url "upload_image_url" %}', true); // Replace 'upload_image_url' with your actual URL
        xhr.setRequestHeader('X-CSRFToken', '{{ csrf_token }}'); // CSRF token for security

        xhr.onload = function() {
            if (xhr.status === 200) {
                // Success - Handle response if needed
                console.log('Image uploaded successfully.');
            } else {
                // Error - Handle the error
                console.error('Error uploading image.');
            }
        };

        xhr.send(formData);
    };
});
