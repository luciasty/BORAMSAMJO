"use strict";




// Show "arrow up" button when scrolling down
const arrowUp = document.querySelector('.arrow-up');
document.addEventListener('scroll', () => {
    if (window.scrollY > homeHeight / 2) {
        arrowUp.classList.add('visible');
    } else {
        arrowUp.classList.remove('visible');
    }
});
        
// Handle click on the "arrow up" button
arrowUp.addEventListener('click', () => {
    scrollIntoView('.title');
});

// main
const tabber = document.querySelector(".tabber");

tabber.addEventListener("click", (e) => {
  if (e.target.classList.contains("tab-trigger")) {
    e.preventDefault();
    const tab = e.target;
    const panels = e.target.parentElement.parentElement.parentElement.querySelectorAll(
      ".tab-panel"
    );
    Array.from(tab.parentElement.parentElement.children)
      .filter((tabF) => tab !== tabF)
      .forEach((tab) => tab.classList.remove("active"));
    tab.parentElement.classList.add("active");
    panels.forEach((panel) =>
      tab.href.split("#").pop() === panel.getAttribute("content-id")
        ? panel.classList.add("active")
        : panel.classList.remove("active")
    );
  }
});

