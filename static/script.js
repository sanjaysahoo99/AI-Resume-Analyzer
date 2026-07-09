document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");
    const fileInput = document.querySelector('input[type="file"]');
    const textarea = document.querySelector("textarea");
    const button = document.querySelector("button");
    const fileName = document.getElementById("fileName");

    fileInput.addEventListener("change", () => {

        if (fileInput.files.length > 0) {
            fileName.textContent = "Selected: " + fileInput.files[0].name;
        } else {
            fileName.textContent = "No file selected";
        }

    });

    form.addEventListener("submit", (e) => {

        if (fileInput.files.length === 0) {
            alert("Please upload a resume.");
            e.preventDefault();
            return;
        }

        if (textarea.value.trim() === "") {
            alert("Please enter the Job Description.");
            e.preventDefault();
            return;
        }

        button.textContent = "Analyzing Resume...";
        button.disabled = true;

    });

});