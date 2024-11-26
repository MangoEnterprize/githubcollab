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

const fullTimeJobs = [
    {
      "title": "Software Engineer",
      "description": "We are seeking a passionate and skilled Software Engineer to join our team. You will design, develop, and maintain high-quality software solutions while collaborating with cross-functional teams to ensure the best outcomes.",
      "location": "Remote",
      "url": "https://www.example.com/jobs/software-engineer"
    },
    {
      "title": "Product Manager",
      "description": "The Product Manager will oversee the development and launch of new features, ensuring alignment with business goals and customer needs.",
      "location": "Onsite",
      "url": "https://www.example.com/jobs/product-manager"
    },
    {
      "title": "Data Analyst",
      "description": "Analyze large datasets to provide actionable insights, create reports, and collaborate with stakeholders to drive data-driven decision-making.",
      "location": "Remote",
      "url": "https://www.example.com/jobs/data-analyst"
    },
    {
      "title": "UX Designer",
      "description": "Design intuitive and user-friendly interfaces, conduct user research, and work closely with developers to ensure seamless implementation.",
      "location": "Onsite",
      "url": "https://www.example.com/jobs/ux-designer"
    }
  ];

const partTimeJobs = [
  {
    "title": "Customer Support Representative",
    "description": "Provide excellent customer service by responding to inquiries via phone, email, or chat. Assist customers with resolving issues and provide product information.",
    "location": "Remote",
    "url": "https://www.example.com/jobs/customer-support-representative"
  },
  {
    "title": "Barista",
    "description": "Prepare and serve coffee and other beverages in a fast-paced café environment. Maintain a clean workspace and deliver exceptional customer service.",
    "location": "Onsite",
    "url": "https://www.example.com/jobs/barista"
  },
  {
    "title": "Social Media Coordinator",
    "description": "Create and schedule social media posts, engage with followers, and track performance metrics to grow the company's online presence.",
    "location": "Remote",
    "url": "https://www.example.com/jobs/social-media-coordinator"
  },
  {
    "title": "Tutor",
    "description": "Provide one-on-one tutoring sessions to help students improve their understanding of specific subjects. Prepare lesson plans tailored to individual needs.",
    "location": "Onsite",
    "url": "https://www.example.com/jobs/tutor"
  }
];

const internships = [
  {
    "title": "Software Development Intern",
    "description": "Assist in the development and testing of software applications. Collaborate with the engineering team to learn and contribute to projects using modern tools and practices.",
    "location": "Remote",
    "url": "https://www.example.com/internships/software-development-intern"
  },
  {
    "title": "Marketing Intern",
    "description": "Support the marketing team with campaign execution, social media management, and analytics. Gain hands-on experience in digital marketing strategies.",
    "location": "Onsite",
    "url": "https://www.example.com/internships/marketing-intern"
  },
  {
    "title": "Data Science Intern",
    "description": "Work with the data science team to clean, analyze, and visualize datasets. Contribute to machine learning model development and research projects.",
    "location": "Remote",
    "url": "https://www.example.com/internships/data-science-intern"
  },
  {
    "title": "Graphic Design Intern",
    "description": "Create engaging designs for digital and print media, including advertisements, social media posts, and promotional materials. Collaborate with the creative team to enhance brand visuals.",
    "location": "Onsite",
    "url": "https://www.example.com/internships/graphic-design-intern"
  }
];

// select all containers
const allContainers = document.querySelectorAll('.card-container');

// Load scholarships on page load
document.addEventListener("DOMContentLoaded", () => {
    loadFullTimeJob(fullTimeJobs);
    loadPartTimeJob(partTimeJobs);
    loadInternship(internships);    

});


// Function to dynamically load full time jobs
function loadFullTimeJob(fullTimeJobs) {
    
    // select the full time job container class
    const fullTimeContainer = allContainers[0];

    fullTimeContainer.innerHTML = ""; // Clear any existing jobs

    fullTimeJobs.forEach(fullTimeJob => {
        const card = document.createElement("div");
        card.classList.add("card", fullTimeJob.location);

        //create a div class name 'content'
        const divElement = document.createElement('div');
        divElement.classList.add('content');

        // create img element
        const imgElement = document.createElement('img');
        imgElement.src = imageUrl;
        // create two p elements
        const pElementOne = document.createElement('p');
        pElementOne.textContent = fullTimeJob.title;
        const pElementTwo = document.createElement('p');
        pElementTwo.textContent = fullTimeJob.description;
        // create button element
        const Applybtn = document.createElement('button');
        Applybtn.classList.add('btn');
        Applybtn.textContent = 'apply';
        // add append p elemenst and button to div class name 'content'
        divElement.append(imgElement, pElementOne, pElementTwo, Applybtn);
        // append div to 'card'
        card.appendChild(divElement);
        fullTimeContainer.appendChild(card);
    });
}


// Function to dynamically load part time jobs 
function loadPartTimeJob(partTimeJobs) {

  // select the part time job container class
  const partTimeContainer = allContainers[1];

  partTimeJobs.forEach(partTimeJob => {
      const card = document.createElement("div");
      card.classList.add("card", partTimeJob.location);

      //create a div class name 'content'
      const divElement = document.createElement('div');
      divElement.classList.add('content');
      // create img element
      const imgElement = document.createElement('img');
      imgElement.src = imageUrl;
      // create two p elements
      const pElementOne = document.createElement('p');
      pElementOne.textContent = partTimeJob.title;
      const pElementTwo = document.createElement('p');
      pElementTwo.textContent = partTimeJob.description;
      // create button element
      const Applybtn = document.createElement('button');
      Applybtn.classList.add('btn');
      Applybtn.textContent = 'apply';
      // add append p elemenst and button to div class name 'content'
      divElement.append(imgElement, pElementOne, pElementTwo, Applybtn);
      // append div to 'card'
      card.appendChild(divElement);
      partTimeContainer.appendChild(card);
  });
}

// Function to dynamically load internships
function loadInternship(internships) {

  // select internship container class
  const internshipContainer = allContainers[2];

  internships.forEach(internship => {
      const card = document.createElement("div");
      card.classList.add("card", internship.location);

      //create a div class name 'content'
      const divElement = document.createElement('div');
      divElement.classList.add('content');
      // create img element
      const imgElement = document.createElement('img');
      imgElement.src = imageUrl;
      // create two p elements
      const pElementOne = document.createElement('p');
      pElementOne.textContent = internship.title;
      const pElementTwo = document.createElement('p');
      pElementTwo.textContent = internship.description;
      // create button element
      const Applybtn = document.createElement('button');
      Applybtn.classList.add('btn');
      Applybtn.textContent = 'apply';
      // add append p elemenst and button to div class name 'content'
      divElement.append(imgElement, pElementOne, pElementTwo, Applybtn);
      // append div to 'card'
      card.appendChild(divElement);
      internshipContainer.appendChild(card);
  });
}

//Filter jobs by category

document.querySelector('.sort-by').addEventListener('click', (e) => {

  e.preventDefault(); // Prevent the form from actually submitting/reloading the page

  // Get the selected radio button value
  const selectedLocation = document.querySelector('.radio-group input[name="options"]:checked').value;

  // Get all job cards
  const cards = document.querySelectorAll('.card');

  // Filter jobs based on selected location
  cards.forEach(card => {
      if (card.classList.contains(selectedLocation)) {
          card.style.display = 'block'; // Show matching jobs
      } else {
          card.style.display = 'none'; // Hide non-matching jobs
      }
  });
});
