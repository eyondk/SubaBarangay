const modal = document.getElementById("logout-modal");
const logoutBtn = document.querySelector(".logout-btn");
const closeBtn = document.querySelector(".close-logout-btn");
const confirmLogoutBtn = document.getElementById("logout-confirm");
const cancelLogoutBtn = document.getElementById("logout-cancel");

logoutBtn.addEventListener("click", (e) => {
    e.preventDefault();
    modal.style.display = "block";
});

closeBtn.addEventListener("click", () => {
    modal.style.display = "none";
});

cancelLogoutBtn.addEventListener("click", () => {
    modal.style.display = "none";
});

confirmLogoutBtn.addEventListener("click", (e) => {
    e.preventDefault();
    // Add any logout confirmation logic here
    console.log("User logged out");
    modal.style.display = "none"; 
});

window.addEventListener("click", (e) => {
    if (e.target === modal) {
        modal.style.display = "none";
    }
});
