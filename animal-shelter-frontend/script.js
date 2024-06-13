"use strict";

document.addEventListener("DOMContentLoaded", async () => {
  const baseUrl = "http://127.0.0.1:8000";

  const response = await fetch(`${baseUrl}/shelters`);
  const shelters = await response.json();

  const contentElement = document.getElementById("shelters");

  for (let i = 0; i < shelters.length; i++) {
    const shelterElement = createShelterElement(shelters[i]);
    contentElement.appendChild(shelterElement);
  }
});

const createShelterElement = function (shelter) {
  const section = document.createElement("section");
  section.className = "shelter-card";

  section.innerHTML = `
    <h3>${shelter.name}</h3>
    <address>${shelter.address}</address>
    <p>number of dogs: ${shelter.animals.dogs}</p>
    <p>number of cats: ${shelter.animals.cats}</p>`;
  return section;
};
