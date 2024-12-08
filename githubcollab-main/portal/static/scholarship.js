const fullTimeJobs = [
  {
    "title": "2024 AMVETS Veteran, Active Duty & Guard/Reserve Scholarship",
    "description": "AMVETS offers up to $12,000 scholarships to a qualified Veteran or Active-Duty member of the United States military to include the National Guard or Reserves. The candidate must be in pursuit of a higher education undergrad degree.",
    "location": "Remote",
    "url": "https://apply.mykaleidoscope.com/scholarships/AMVETSactiveduty24"
  },
  {
    "title": "2024 AMVETS Spouse Scholarship",
    "description": "AMVETS offers a $4000 scholarship to a qualified spouse of a Veteran or Active-Duty member of the United States military to include the National Guard or Reserves. The candidate must be in pursuit of a higher education undergrad degree.",
    "location": "Onsite",
    "url": "https://apply.mykaleidoscope.com/scholarships/AMVETSspouse24"
  },
  {
    "title": "2024 AMVETS Children/Grandchildren Scholarship",
    "description": "Scholarships offered up to $4000 are available to a qualified child or grandchild of a Veteran or Active Duty member of the United States military to include the National Guard or Reserves. Candidate must be in pursuit of a higher education undergrad degree.",
    "location": "Remote",
    "url": "https://apply.mykaleidoscope.com/scholarships/AMVETSchildrenandgrandchildren24"
  },
  {
    "title": "Air Force Aid Society General George S. Brown Spouse Tuition Assistance Program",
    "description": "Provides $2,000 grants to selected children of active duty, Title 32 AGR performing full-time active duty, retired, and deceased Air Force members; spouses (stateside) of active duty members; and surviving spouses of deceased personnel for their undergraduate studies.",
    "location": "Remote",
    "url": "https://afas.org/haparnoldgrant/"
  }
];

const partTimeJobs = [
{
  "title": "Student Referee Scholarshipe",
  "description": "This scholarship seeks to reward exceptional student referees who exemplify integrity, dedication, and a passion for sportsmanship. Any high school senior or undergraduate student who is a referee or umpire may apply for this scholarship opportunity or any student enrolled in a sports officiating class.",
  "location": "Remote",
  "url": "https://bold.org/scholarships/student-referee-scholarship/"
},
{
  "title": "Deborah Jean Rydberg Memorial Scholarship",
  "description": "The Deborah Jean Rydberg Memorial Scholarship provides educational resources for Guilford High School students to pursue their dreams through higher education.",
  "location": "Onsite",
  "url": "https://www.scholarships.com/scholarships/deborah-jean-rydberg-memorial-scholarship"
},
{
  "title": "Edward and Marion Petzko Athlete Scholarship",
  "description": "The recipient of the Edward and Marion Petzko Student-Athlete Scholarship will be an above-average student that received a varsity letter in either track or golf.",
  "location": "Remote",
  "url": "https://www.scholarships.com/scholarships/edward-and-marion-petzko-athlete-scholarship"
},
{
  "title": "Can-Amera Games Scholarship",
  "description": "Education is vital to the growth and future of every community. Because of this, the Saginaw Community Foundation administers a variety of scholarship programs for high school, community college, university and vocational students.",
  "location": "Onsite",
  "url": "https://www.scholarships.com/scholarships/can-amera-games-scholarship"
}
];

const internships = [
{
  "title": "Sturz Legacy Scholarship",
  "description": "This scholarship aims to honor the incredible life of Marian Sturz by supporting students who share her kindness, wonder, and strength.",
  "location": "Remote",
  "url": "https://bold.org/scholarships/sturz-legacy-scholarship/"
},
{
  "title": "F.E. Foundation Scholarship",
  "description": "All students should have the ability to pursue a college education so they can enjoy all of the benefits that come with it.Unfortunately, with college costs on the rise, access to higher education is not equal. The cost of tuition, books, and living expenses is now overwhelming for low-income and even middle-income students, requiring individuals with financial need to take on significant debt or opt to forgo a college degree.",
  "location": "Onsite",
  "url": "https://bold.org/scholarships/f-e-foundation-scholarship/"
},
{
  "title": "College Raptor Scholarship",
  "description": "To help students take a thoughtful approach to their college decision process and to help pay for college, College Raptor awards a $2,500 scholarship four times per year.",
  "location": "Remote",
  "url": "https://careers.cmco.com/job/Charlotte-Summer-2025-Data-Analytics-Intern-NC-28277/1212559500/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic"
},
{
  "title": "Ron Brown Scholar Program",
  "description": "Applicants must be African American collegebound high school seniors. Selection is based on academic promise, leadership, communication skills, school and community involvement and financial need.",
  "location": "Onsite",
  "url": "https://www.collegeraptor.com/scholarship/private/detail/Ron%20Brown%20Scholar%20Program--8111"
}
];

// select all containers
const allContainers = document.querySelectorAll('.services');
const list = ["📱","💡","⚙️"];

// Load scholarships on page load
document.addEventListener("DOMContentLoaded", () => {
  loadFullTimeJob(fullTimeJobs);
  loadPartTimeJob(partTimeJobs);
  loadInternship(internships);    

});


// Function to dynamically load full-time jobs
function loadFullTimeJob(fullTimeJobs) {
  const fullTimeContainer = allContainers[0];
  fullTimeContainer.innerHTML = ""; // Clear any existing jobs

  fullTimeJobs.forEach((fullTimeJob, index) => {
    const card = document.createElement("div");
    card.classList.add("service-box", fullTimeJob.location);

    // Create a div with the class name 'service-icon'
    const divElement = document.createElement('div');
    divElement.classList.add('service-icon');
    divElement.textContent = list[index % list.length];

    // Create title, description, apply link
    const title = document.createElement('h3');
    title.textContent = fullTimeJob.title;
    const description = document.createElement('p');
    description.textContent = fullTimeJob.description;
    const ApplyLink = document.createElement('a');
    ApplyLink.textContent = 'APPLY »';
    ApplyLink.classList.add("apply");
    ApplyLink.href = fullTimeJob.url; // Set the hyperlink
    ApplyLink.target = "_blank"; // Open in a new tab

    // Append
    card.append(divElement, title, description, ApplyLink);
    fullTimeContainer.append(card);
  });
}

// Function to dynamically load part-time jobs
function loadPartTimeJob(partTimeJobs) {
  const partTimeContainer = allContainers[1];
  partTimeContainer.innerHTML = ""; // Clear any existing jobs

  partTimeJobs.forEach((partTimeJob, index) => {
    const card = document.createElement("div");
    card.classList.add("service-box", partTimeJob.location);

    // Create a div with the class name 'service-icon'
    const divElement = document.createElement('div');
    divElement.classList.add('service-icon');
    divElement.textContent = list[index % list.length];

    // Create title, description, apply link
    const title = document.createElement('h3');
    title.textContent = partTimeJob.title;
    const description = document.createElement('p');
    description.textContent = partTimeJob.description;
    const ApplyLink = document.createElement('a');
    ApplyLink.textContent = 'APPLY »';
    ApplyLink.classList.add("apply");
    ApplyLink.href = partTimeJob.url; // Set the hyperlink
    ApplyLink.target = "_blank"; // Open in a new tab

    // Append
    card.append(divElement, title, description, ApplyLink);
    partTimeContainer.append(card);
  });
}

// Function to dynamically load internships
function loadInternship(internships) {
  const internshipContainer = allContainers[2];
  internshipContainer.innerHTML = ""; // Clear any existing jobs

  internships.forEach((internship, index) => {
    const card = document.createElement("div");
    card.classList.add("service-box", internship.location);

    // Create a div with the class name 'service-icon'
    const divElement = document.createElement('div');
    divElement.classList.add('service-icon');
    divElement.textContent = list[index % list.length];

    // Create title, description, apply link
    const title = document.createElement('h3');
    title.textContent = internship.title;
    const description = document.createElement('p');
    description.textContent = internship.description;
    const ApplyLink = document.createElement('a');
    ApplyLink.textContent = 'APPLY »';
    ApplyLink.classList.add("apply");
    ApplyLink.href = internship.url; // Set the hyperlink
    ApplyLink.target = "_blank"; // Open in a new tab

    // Append
    card.append(divElement, title, description, ApplyLink);
    internshipContainer.append(card);
  });
}
