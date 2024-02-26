function previewImage(event) {
    const imageFile = event.target.files[0];
    const imageElement = document.getElementById('imagePreview');
    // Clear previous image preview    
    imageElement.innerHTML = '';

    // Check if the file is an image    
    if (imageFile.type.match('image.*')) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = new Image();
            img.src = e.target.result;
            img.onload = function() { // Display the image in the image preview div                
                if (imageElement.childElementCount === 0) {
                    imageElement.appendChild(img);
                 }
            }; 
        };
        reader.readAsDataURL(imageFile); 
    } else {
        // Display an error message if the file is not an image        
        imageElement.innerHTML = '<p>File is not an image</p>';
    }
}
document.getElementById('imageInput').addEventListener('change', previewImage);

// Select the button and the section containing disease information
document.addEventListener('DOMContentLoaded', function() {
    const viewDiseasesButton = document.querySelector('.btn');
    const diseasesSection = document.getElementById('diseases');
    
    // Function to toggle the visibility of the disease information    
    function toggleDiseaseInfo() {
        diseasesSection.classList.toggle('hidden');
    }
    diseasesSection.classList.add('hidden');
    // Add click event listener to the button    
    viewDiseasesButton.addEventListener('click', toggleDiseaseInfo);
});
function previewImage(event) {
    const imageFile = event.target.files[0];
    const imageElement = document.getElementById('imagePreview');
    
    // Clear previous image preview    
    imageElement.innerHTML = '';

    // Check if the file is an image    
    if (imageFile.type.match('image.*')) {
        const reader = new FileReader();
        
        reader.onload = function(e) { 
            const img = new Image();
            img.src = e.target.result;
            img.onload = function() {
            // Display the image in the image preview div                
            if (imageElement.childElementCount === 0) {
                imageElement.appendChild(img);
            }
        };
    };
    reader.readAsDataURL(imageFile);
    } else {
        // Display an error message if the file is not an image        
        imageElement.innerHTML = '<p>File is not an image</p>';
    }
}
document.getElementById('imageInput').addEventListener('change', previewImage);

// Select the button and the section containing disease information
document.addEventListener('DOMContentLoaded', function() {
    const viewDiseasesButton = document.querySelector('.btn');
    const diseasesSection = document.getElementById('diseases');
    // Function to toggle the visibility of the disease information    
    function toggleDiseaseInfo() {
        diseasesSection.classList.toggle('hidden');
    }
    diseasesSection.classList.add('hidden');
    // Add click event listener to the button    
    viewDiseasesButton.addEventListener('click', toggleDiseaseInfo);
});