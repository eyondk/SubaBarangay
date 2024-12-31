 // headers for each tab
 const headers = {
    user: ['USER LOG ID', 'LOG DETAILS', 'TIMESTAMP', 'ACTION', 'USER', 'ROLE'],
    resident: ['RESIDENT LOG ID', 'USER','ROLE','RESIDENT', 'ACTIVITY','TIMESTAMP'], //not sure
    payment: ['PAYMENT ID', 'AMOUNT', 'DATE ISSUED', 'CERTIFICATE TYPE', 'REQUESTED', 'IS RESIDENT'], //not sure
    certificateissued: ['CERTIFCATE ISSUED LOG ID', 'RESIDENT REQUESTED', 'CERTIFICATE TYPE', 'DATE ISSUED', 'RESIDENT REQUESTED', 'IS RESIDENT'] //not sure
};

//change headers for different log type
document.querySelectorAll('.tab').forEach(tab => {
    tab.addEventListener('click', () => {
        const type = tab.dataset.type; 
        const tableHeader = document.getElementById('table-header');

        tableHeader.innerHTML = '';

        headers[type].forEach(header => {
            const th = document.createElement('th');
            th.textContent = header;
            tableHeader.appendChild(th);
        });

    });
});


//add active css styling for active tab
document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll('.tab');
    const defaultTab = document.querySelector('.tab[data-type="resident"]');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');

            // (Optional) Load data or perform other actions here
        });
    });

    // Set the resident tab as active by default
    if (defaultTab) {
        defaultTab.classList.add('active'); 
        defaultTab.click(); 
    }
});

