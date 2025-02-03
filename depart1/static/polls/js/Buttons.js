// Js file for the buttons [tables] sa Bresident.html file and Tresident.html

//change style when filter by household btn is clicked
document.getElementById('filterButton').addEventListener('click', function() {
    this.classList.toggle('clicked');
});

// ================= start delete function & confirmation modal  ===============

function openModal(action, message) {
    document.getElementById("modalMessage").textContent = message;
    document.getElementById("confirmationModal").style.display = "flex";
}

function closeConfModal() {
    document.getElementById("confirmationModal").style.display = "none";
}



function toggleAllCheckboxesResident(source) {
    const checkboxes = document.querySelectorAll('input[id^="select-row-resident"]');

    checkboxes.forEach((checkbox) => {
        checkbox.checked = source.checked;
    });

    toggleDeleteButtonResident();
}

function toggleDeleteButtonResident() {
    const checkboxes = document.querySelectorAll(".row-checkbox");
    const deleteAllButton = document.getElementById("delete-All");
    const deleteOneButton = document.getElementById("delete-One");
    const deselectAllButton = document.getElementById("deselect-All");


    const checkedBoxes = Array.from(checkboxes).filter((checkbox) => checkbox.checked);

    deselectAllButton.style.display = checkedBoxes.length > 0 ? "inline-block" : "none";
    deleteAllButton.style.display = checkedBoxes.length === checkboxes.length || checkedBoxes.length > 1 ? "inline-block" : "none";
    deleteOneButton.style.display = checkedBoxes.length === 1 ? "inline-block" : "none";
}

function deleteAll() {
    const checkboxes = document.querySelectorAll(".row-checkbox:checked");

    checkboxes.forEach((checkbox) => {
        checkbox.closest("tr").remove(); 
    });

    // Update button visibility
    toggleDeleteButtonResident();
}

function deleteSelected() {
    const checkboxes = document.querySelectorAll(".row-checkbox:checked");

    if (checkboxes.length === 1) {
        checkboxes[0].closest("tr").remove(); // Remove the selected row
    }

    toggleDeleteButtonResident();
}


function deselectAll() {
    const checkboxes = document.querySelectorAll(".row-checkbox:checked");
    checkboxes.forEach((checkbox) => (checkbox.checked = false));
    document.getElementById("select-all-resident").checked = false;
    toggleDeleteButtonResident();
}

// ================= end delete function & confirmation modal  ===============


// ======================== TREASURER'S =================================

function toggleButtons_Treasurer() {
    const checkboxes = document.querySelectorAll(".select-row-checkbox");
    const addButton = document.getElementById("add-org-all");
    const updateButton = document.getElementById("update-org-all");
    const deselectAllButton = document.getElementById("deselect-all");


    const checkedBoxes = Array.from(checkboxes).filter((checkbox) => checkbox.checked);
    deselectAllButton.style.display = checkedBoxes.length > 0 ? "inline-block" : "none";
    updateButton.style.display = checkedBoxes.length === checkboxes.length || checkedBoxes.length > 0 ? "inline-block" : "none";
    addButton.style.display = checkedBoxes.length === checkboxes.length || checkedBoxes.length > 0 ? "inline-block" : "none";

}

function toggleAllCheckboxesResident_treasurer(source) {
    const checkboxes = document.querySelectorAll(".select-row-checkbox");

    checkboxes.forEach((checkbox) => {
        checkbox.checked = source.checked;
    });

    toggleButtons_Treasurer();
}



function deselectAllRes(){
    const tre_checkboxes = document.querySelectorAll(".select-row-checkbox:checked");
    tre_checkboxes.forEach((checkbox) => (checkbox.checked = false));
    document.getElementById("select-all-res").checked = false;
    toggleButtons_Treasurer();
}
