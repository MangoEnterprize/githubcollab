document.getElementById('add-job-button').addEventListener('click', addJobEntry);

function addJobEntry() {
    // Select the job experience section
    const jobExperienceSection = document.getElementById('job-experience-section');
    
    // Create a new job entry
    const newJobEntry = document.createElement('div');
    newJobEntry.classList.add('job-entry');
    
    newJobEntry.innerHTML = `
        <label>Title:</label>
        <input type="text" placeholder="Job Title" name="title[]">
        
        <label>Description:</label>
        <input type="text" placeholder="Job Description" name="description[]">
        
        <label>Date started:</label>
        <select name="start-month[]">
            <option value="" disabled selected>Month</option>
            <option>January</option>
            <option>February</option>
            <option>March</option>
            <!-- ... more months ... -->
        </select>
        <select name="start-year[]">
            <option value="" disabled selected>Year</option>
            <option>2024</option>
            <option>2023</option>
            <!-- ... more years ... -->
        </select>
        
        <label>Date ended:</label>
        <select name="end-month[]">
            <option value="" disabled selected>Month</option>
            <option>January</option>
            <option>February</option>
            <option>March</option>
            <!-- ... more months ... -->
        </select>
        <select name="end-year[]">
            <option value="" disabled selected>Year</option>
            <option>2024</option>
            <option>2023</option>
            <!-- ... more years ... -->
        </select>
        
        <label>
            <input type="checkbox" name="still-working[]"> Still Working Here
        </label>
        <button type="button" class="remove-job">Remove Job</button>
    `;
    
    // Append the new job entry to the section
    jobExperienceSection.appendChild(newJobEntry);

    // Add event listener to the "Remove Job" button
    newJobEntry.querySelector('.remove-job').addEventListener('click', function() {
        jobExperienceSection.removeChild(newJobEntry);
    });
}
