document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".contact-checkbox").forEach(checkbox => {
        checkbox.addEventListener('change', toggleDeleteButton)
    });

    document.querySelector("#check-all").addEventListener("click", checkAll);
    document.querySelector("#uncheck-all").addEventListener("click", uncheckAll);
});

function toggleDeleteButton() {
    let delButton = document.querySelector("#delete-btn");
    delButton.disabled = true;

    document.querySelectorAll(".contact-checkbox").forEach(checkbox => {
        if (checkbox.checked) {
            delButton.disabled = false;
        }
    });
}

function checkAll() {
    document.querySelectorAll(".contact-checkbox").forEach(checkbox => {
        checkbox.checked = true;
    });
}

function uncheckAll() {
    document.querySelectorAll(".contact-checkbox").forEach(checkbox => {
        checkbox.checked = false;
    });
}