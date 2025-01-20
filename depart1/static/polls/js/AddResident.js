
//====================== end delete confiramtion modal =========================
let deleteAction = null; // To store the action to perform (deleteAll or deleteSelected)

// Set the action and message
function openModal(action, message) {
    deleteAction = action;
    document.getElementById("modalMessage").textContent = message;
    document.getElementById("confirmationModal").style.display = "flex";
}

function closeConfirmationModal() {
    document.getElementById("confirmationModal").style.display = "none";
    deleteAction = null;
}

function confirmDelete() {
    if (deleteAction) {
        deleteAction();
    }
    closeConfirmationModal();
    deselectAll();
}

function toggleAllCheckboxesTB(source) {
    const checkboxes = document.querySelectorAll(".rowCheckbox");

    checkboxes.forEach((checkbox) => {
        checkbox.checked = source.checked;
    });

    toggleDeleteButtonTB();
}

function toggleDeleteButtonTB() {
    const checkboxes = document.querySelectorAll(".rowCheckbox");
    const deleteAllButton = document.getElementById("deleteAll");
    const deleteOneButton = document.getElementById("deleteOne");
    const deselectAllButton = document.getElementById("deselectAll");

    const checkedBoxes = Array.from(checkboxes).filter((checkbox) => checkbox.checked);

    deleteAllButton.style.display = checkedBoxes.length === checkboxes.length && checkedBoxes.length > 1 ? "inline-block" : "none";
    deselectAllButton.style.display = checkedBoxes.length > 0 ? "inline-block" : "none";
    deleteOneButton.style.display = checkedBoxes.length === 1 ? "inline-block" : "none";
}

function deleteAll() {
    const checkboxes = document.querySelectorAll(".rowCheckbox:checked");

    checkboxes.forEach((checkbox) => {
        checkbox.closest("tr").remove(); 
    });

    // Update button visibility
    toggleDeleteButtonTB();
}

function deleteSelected() {
    const checkboxes = document.querySelectorAll(".rowCheckbox:checked");

    if (checkboxes.length === 1) {
        checkboxes[0].closest("tr").remove(); // Remove the selected row
    }

    toggleDeleteButtonTB();
}

function deselectAll() {
    const checkboxes = document.querySelectorAll(".rowCheckbox");
    checkboxes.forEach((checkbox) => (checkbox.checked = false));
    document.getElementById("selectAll").checked = false;
    toggleDeleteButtonTB();
}
//====================== end delete confiramtion modal =========================


//===================== add household members page ===================== 
function toggleConditionalFields() {
    var sex = document.getElementById('sex').value;
    var conditionalFields = document.querySelectorAll('.conditional');
    if (sex === 'female') {
        conditionalFields.forEach(function(field) {
            field.style.display = 'grid';
        });
    } else {
        conditionalFields.forEach(function(field) {
            field.style.display = 'none';
        });
    }
}

// Function to simulate adding a household member
function addHouseholdMember() {
    // Simulate the success process (you can replace this with your actual logic)
    setTimeout(() => {
        openSuccessModal();
    }, 500); // Simulate delay for effect
}

function openSuccessModal() {
    const modal = document.getElementById('successModal');
    modal.style.display = 'flex'; 
}

function closeSuccessModal() {
    const modal = document.getElementById('successModal');
    modal.style.display = 'none'; }

// Optional: Close the modal when clicking outside of it
window.onclick = function (event) {
    const modal = document.getElementById('successModal');
    if (event.target === modal) {
        modal.style.display = 'none';
    }
};
//===================== add household members page ===================== 



//check box for non-com diease table
document.getElementById('select-all-iii').addEventListener('change', function() {
    const checkboxes = document.querySelectorAll('input[id^="select-row-iii"]');
    checkboxes.forEach(checkbox => checkbox.checked = this.checked);
});

//if others is selected an input text will show
function handleDropdownChange(selectElement) {
    const inputElement = selectElement.nextElementSibling; 
    if (selectElement.value === "Others") {
        selectElement.style.display = "none";
        inputElement.style.display = "block";
        inputElement.focus(); 
    }
}

//display the select input when the text is empty
function checkSakitInput(inputElement) {
    const selectElement = inputElement.previousElementSibling; 

    if (inputElement.value.trim() === "") {
        inputElement.style.display = "none";
        selectElement.style.display = "block";
        selectElement.value = ""; 
    }
}


// Uncheck the other checkbox when anothers are clicked in the same row
function toggleCheckbox(checkbox) {
    const row = checkbox.closest('tr'); 
    const otherCheckbox = row.querySelector(
        checkbox.name === "YESmaintenance" 
            ? 'input[name="NOmaintenance"]' 
            : 'input[name="YESmaintenance"]'
    );

    if (checkbox.checked) {
        otherCheckbox.checked = false; 
    }
}


// Function to open the modal and display member info
function openMemModal(name, sex, age, riskClass) {
    document.getElementById("memName").innerText = name;
    document.getElementById("memSex").innerText = sex;
    document.getElementById("memAge").innerText = age;
    document.getElementById("memRiskClass").innerText = riskClass;

    document.getElementById("modalOverlay").style.display = "block";
    document.getElementById("displayMemModal").style.display = "flex";
}

function closeModal() {
    document.getElementById("modalOverlay").style.display = "none";
    document.getElementById("displayMemModal").style.display = "none";
}

// Function to handle adding the member to a table
function addToTable() {
    const name = document.getElementById("memName").innerText;
    const sex = document.getElementById("memSex").innerText;
    const age = document.getElementById("memAge").innerText;
    const riskClass = document.getElementById("memRiskClass").innerText; //(optional), not working in the select

    const table = document.getElementById("membersTable");  
    const row = table.insertRow();

    const cell0 = row.insertCell(0);
    const cell1 = row.insertCell(1);
    const cell2 = row.insertCell(2);
    const cell3 = row.insertCell(3);
    const cell4 = row.insertCell(4);
    const cell5 = row.insertCell(5);
    const cell6 = row.insertCell(6);
    const cell7 = row.insertCell(7);


    cell0.innerHTML = '<input type="checkbox" id="select-row-iii">';
    cell1.innerText = name;
    cell2.innerText = age;
    cell3.innerText = sex;
    cell4.innerHTML = `
        <select name="health-risk">
            <option value=""></option>
            <option value="newborn">Newborn (0-28 days)</option>
            <option value="infant">Infant (29 days - 11 months)</option>
            <option value="underfive">Under Five (1-4 y/o)</option>
            <option value="school-age">School-aged Children (5-9 y/o)</option>
            <option value="adolescent">Adolescent (10-19 y/o)</option>
            <option value="adult">Adult (20-59 y/o)</option>
            <option value="senior">Senior Citizen (60+ y/o)</option>
            <option value="PWD">Person With Disability</option>
            <option value="AP">Adoloscent-Pregnant</option>
            <option value="P">Pregnant</option>
            <option value="PP">Post Partum</option>
        </select>
    `;
    cell5.innerHTML = `
        <select class="sakit-dropdown" onchange="handleDropdownChange(this)">
            <option value=""></option>
            <option value="HPN">HPN</option>
            <option value="DM">DM</option>
            <option value="BA">BA</option>
            <option value="CA">CA</option>
            <option value="DL">DL</option>
            <option value="CKD">CKD</option>
            <option value="MHI">MHI</option>
            <option value="Others">Others</option>
        </select>
        <input type="text" class="sakit-input" placeholder="Specify Others" id="otherSakit" style="display: none;" oninput="checkSakitInput(this)">
    `;
    cell6.innerHTML = `
        <select name="lifestylerisk">
            <option value=""></option>
            <option value="smoker">Smoker</option>
            <option value="alcoholic">Alcoholic</option>
            <option value="others">Others</option>
        </select>
    `;
    cell7.innerHTML = `
        <div class="checkbox-group">
            <input type="checkbox" name="YESmaintenance" id="YESmaintenance" onclick="toggleCheckbox(this)">
            <label for="YESmaintenance">Yes</label>
            
            <input type="checkbox" name="NOmaintenance" id="NOmaintenance" onclick="toggleCheckbox(this)">
            <label for="NOmaintenance">No</label>
        </div>
    `;

    closeModal();
}

// Simulating a search function. para mo display ang modals ig search
function simulateSearch() {
    // In a real app, you would fetch data from the backend
    const searchTerm = document.getElementById("searchInput").value;
    if (searchTerm.length > 2) { // Trigger search if input is at least 3 characters
        const memberData = {
            name: "Juan Dela Cruz",
            sex: "Male",
            age: 32,
            riskClass: "Moderate"
        };

        // Open the modal with the dummy data
        openMemModal(memberData.name, memberData.sex, memberData.age, memberData.riskClass);
    }
}