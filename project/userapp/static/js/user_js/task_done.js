// function displayImage(event) {
//     const fileInput = event.target;
//     const file = fileInput.files[0];
//     if (file) {
//         const reader = new FileReader();
//         reader.onload = function(e) {
//             document.getElementById('uploaded-image').src = e.target.result;
//         };
//         reader.readAsDataURL(file);
//     }
// }

// const dropArea = document.getElementById('drop-zone');
// const inputFile = document.getElementById('file-input'); 
// const imageview = document.getElementById('uploaded-image');

// inputFile.addEventListener('change',uploadImage);

// function uploadImage(){
    
//     let imgLink = URL.createObjectURL(inputFile.files[0]);
//     imageview.style.backgroundImage = `url(${imgLink })`;
    


// }

// dropArea.addEventListener("dragover",function(e){
//     e.preventDefault();
// });

// dropArea.addEventListener("drop",function(e){
//     e.preventDefault();
//     inputFile.files = e.dataTransfer.files;
//     uploadImage();
// });


function displayImage(event) {
    const fileInput = event.target;
    const file = fileInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('uploaded-image').src = e.target.result;
        };
        reader.readAsDataURL(file);
    }
}

const dropArea = document.getElementById('drop-zone');
const inputFile = document.getElementById('file-input'); 
const imageview = document.getElementById('uploaded-image');

// This function will handle both the input change and drag/drop events
function uploadImage(file) {
    let imgLink = URL.createObjectURL(file);
    imageview.src = imgLink;
}

inputFile.addEventListener('change', function() {
    const file = inputFile.files[0];
    if (file) {
        uploadImage(file);
    }
});

dropArea.addEventListener("dragover", function(e) {
    e.preventDefault();
});

dropArea.addEventListener("drop", function(e) {
    e.preventDefault();
    const file = e.dataTransfer.files[0];
    if (file) {
        uploadImage(file);

        // Manually assign the dropped file to the input element
        inputFile.files = e.dataTransfer.files; 
    }
});
