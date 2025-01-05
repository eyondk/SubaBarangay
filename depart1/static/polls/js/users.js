//close and open add user modals only.
const displayUserModal = document.getElementById("addUserModal");
const addUserBtn = document.getElementById("addUserBtn");
const closeModalBtn = document.getElementById("cancel-add-user-btn");

addUserBtn.addEventListener("click", function(event) {
    event.preventDefault(); 
    displayUserModal.style.display = "block";

    const url = new URL(window.location)
    url.searchParams.set('action', 'add'); 
    window.history.pushState({}, '', url);

});

closeModalBtn.addEventListener("click", function() {
    displayUserModal.style.display = "none";

    const url = new URL(window.location)
    url.searchParams.delete('action');
    window.history.pushState({}, '', url);
});


//close edit and view modals only.
document.getElementById("closemodalBtn").addEventListener("click", function() {
    document.getElementById("modal").classList.remove("show");
    document.getElementById("modalOverlay").classList.remove("show");

    const url = new URL(window.location);
    url.searchParams.delete('action');
    window.history.pushState({}, '', url); 
});

document.getElementById("modalOverlay").addEventListener("click", function(event) {
    if (event.target === document.getElementById("modalOverlay")) {
        document.getElementById("modal").classList.remove("show");
        document.getElementById("modalOverlay").classList.remove("show");

        const url = new URL(window.location);
        url.searchParams.delete('action');
        window.history.pushState({}, '', url); 
    }
});

