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

// Add event listener to the 'Add more Volunteer Work' button
document.querySelector('.add-volunteer').addEventListener('click', function() {
    // Get the volunteer work container
    const volunteerWorkContainer = document.getElementById('volunteer-work-container');

    // Clone the first volunteer work div
    const newVolunteerWork = volunteerWorkContainer.querySelector('.volunteer-work').cloneNode(true);

    // Clear the input fields in the cloned volunteer work
    const inputs = newVolunteerWork.querySelectorAll('input[type="text"]');
    inputs.forEach(input => input.value = '');

    // Reset any selected options in the dropdowns
    const selects = newVolunteerWork.querySelectorAll('select');
    selects.forEach(select => {
        select.selectedIndex = 0; // Set to the first option (disabled selected)
    });

    // Append the new volunteer work to the container
    volunteerWorkContainer.appendChild(newVolunteerWork);

    // Create a spacer element
    const spacer = document.createElement('div');
    spacer.style.height = '20px'; // Adjust the height for spacing
    volunteerWorkContainer.appendChild(spacer); // Insert the spacer after the new volunteer work
});