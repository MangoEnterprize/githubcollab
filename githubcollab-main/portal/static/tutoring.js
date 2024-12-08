document.addEventListener("DOMContentLoaded", () => {
    const subjectSelect = document.getElementById("subject");
    const classSelect = document.getElementById("class");

    // Define the class options based on the subject
    const classesOptions = {
        Mathematics: ["Calculus 1", "Calculus 2", "Linear Algebra", "Geometry"],
        Science: ["Physics", "Chemistry", "Biology"],
        English: ["English 1", "English 2", "English 3"]
    };

    // Event listener to filter class options based on subject selection
    subjectSelect.addEventListener("change", () => {
        const selectedSubject = subjectSelect.value;

        // Reset the class dropdown
        classSelect.innerHTML = '<option value="">Select Class</option>';

        // Populate the class dropdown with options for the selected subject
        if (classesOptions[selectedSubject]) {
            classesOptions[selectedSubject].forEach((className) => {
                const option = document.createElement("option");
                option.value = className;
                option.textContent = className;
                classSelect.appendChild(option);
            });
        }
    });

    // Event listener for form submission
    document.getElementById("reservationForm").addEventListener("submit", (event) => {
        event.preventDefault(); // Prevent form from refreshing the page

        // Get form data
        const date = document.getElementById("date").value;
        const time = document.getElementById("time").value;
        const subject = subjectSelect.value;
        const classValue = classSelect.value;

        // Check if all fields are filled
        if (!date || !time || !subject || !classValue) {
            alert("Please fill out all fields.");
            return;
        }

        // Display confirmation message
        const confirmationMessage = document.getElementById("confirmationMessage");
        confirmationMessage.textContent = `Reservation confirmed for ${subject} (${classValue}) on ${date} at ${time}.`;
    });
});
