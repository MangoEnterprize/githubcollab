// Add event listener to the 'Add another Job' button
document.querySelector('.add-job').addEventListener('click', function() {
    // Get the job experience container
    const jobExperienceContainer = document.getElementById('job-experience-container');

    // Clone the first job experience div
    const newJobExperience = jobExperienceContainer.querySelector('.job-experience').cloneNode(true);

    // Clear the input fields in the cloned job experience
    const inputs = newJobExperience.querySelectorAll('input[type="text"]');
    inputs.forEach(input => input.value = '');

    // Reset any selected options in the dropdowns
    const selects = newJobExperience.querySelectorAll('select');
    selects.forEach(select => {
        select.selectedIndex = 0; // Set to the first option (disabled selected)
    });

    // Append the new job experience to the container
    jobExperienceContainer.appendChild(newJobExperience);

    // Create a spacer element
    const spacer = document.createElement('div');
    spacer.style.height = '20px'; // Adjust the height for spacing
    jobExperienceContainer.appendChild(spacer); // Insert the spacer after the new job experience
});

fetch('/submit-job-experience', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(jobExperiences),
})
.then(response => response.json())
.then(data => {
    console.log('Success:', data);
})
.catch((error) => {
    console.error('Error:', error);
});

fetch('/submit-major', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(selectedMajor),
})
.then(response => response.json())
.then(data => {
    console.log('Success:', data);
})
.catch((error) => {
    console.error('Error:', error);
});

document.addEventListener("DOMContentLoaded", function() {
    // Select the button and volunteer work section
    const addVolunteerButton = document.querySelector(".add-volunteer");
    const volunteerWorkSection = document.querySelector(".volunteer-section");

    // Function to duplicate the volunteer work section
    addVolunteerButton.addEventListener("click", function() {
        const newVolunteerWork = volunteerWorkSection.cloneNode(true);
        // Optionally clear input fields
        newVolunteerWork.querySelectorAll("input, select").forEach(input => input.value = "");

        // Insert a space or margin for the new section
        newVolunteerWork.style.marginTop = "20px";

        // Insert the new volunteer work section after the last one
        volunteerWorkSection.parentNode.appendChild(newVolunteerWork);
    });
});
