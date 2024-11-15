'use strict';

function fetchFullTimeJob(){
    fetch('./full.json')
    .then((response)=>{
        if(!response.ok){
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => addJobs(data))
    .catch(error =>{
        console.error('There is an error: ', error);
    });


}

function fetchPartTimeJob(){
    fetch('./part.json')
    .then((response)=>{
        if(!response.ok){
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => addJobs(data))
    .catch(error =>{
        console.error('There is an error: ', error);
    });


}

function fetchInternship(){
    fetch('./internship.json')
    .then((response)=>{
        if(!response.ok){
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => addJobs(data))
    .catch(error =>{
        console.error('There is an error: ', error);
    });


}


function addJobs(jobs){
    // select all containers
    const allContainers = document.querySelectorAll('.card-container');
    // select the full time job container class
    const fullTimeContainer = allContainers[0];
    // select the part time job container class
    const partTimeContainer = allContainers[1];
    // select the internship container class
    const internshipContainer = allContainers[2];
    // create article element with 'card' class
    const articleElement = document.createElement('article');
    articleElement.classList.add('card');
    // add article element as children to full time container
    fullTimeContainer.appendChild(articleElement);


}

