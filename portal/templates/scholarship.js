// Sample scholarship data (or fetch from an external JSON file)
const scholarships = [
    {
        "title": "Gates Scholarship",
        "description": "A highly selective, full scholarship for exceptional minority high school seniors.",
        "category": "university",
        "url": "https://www.thegatesscholarship.org/scholarship"
    },
    {
        "title": "Coca-Cola Scholars Program",
        "description": "An achievement-based scholarship awarded to graduating high school seniors.",
        "category": "private",
        "url": "https://www.coca-colascholarsfoundation.org/apply/"
    },
    {
        "title": "Pell Grant",
        "description": "A federal grant for undergraduate students with financial need.",
        "category": "grant",
        "url": "https://studentaid.gov/understand-aid/types/grants/pell"
    },
    {
        "title": "Jack Kent Cooke Foundation College Scholarship",
        "description": "A scholarship for high-achieving high school seniors with financial need.",
        "category": "university",
        "url": "https://www.jkcf.org/our-scholarships/college-scholarship-program/"
    }
];

// Load scholarships on page load
document.addEventListener("DOMContentLoaded", () => {
    loadScholarships(scholarships);
});

// Function to dynamically load scholarships
function loadScholarships(scholarships) {
    const scholarshipContainer = document.getElementById("scholarship-cards");
    scholarshipContainer.innerHTML = ""; // Clear any existing scholarships

    scholarships.forEach(scholarship => {
        const card = document.createElement("div");
        card.classList.add("card", scholarship.category);

        card.innerHTML = `
            <h3>${scholarship.title}</h3>
            <p>${scholarship.description}</p>
            <a href="${scholarship.url}" target="_blank" class="apply-button">Apply</a>
        `;

        scholarshipContainer.appendChild(card);
    });
}

// Filter scholarships by category
function filterScholarships(type) {
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        if (card.classList.contains(type)) {
            card.style.display = card.style.display === 'none' ? 'block' : 'none';
        } else {
            card.style.display = 'none';
        }
    });
}
