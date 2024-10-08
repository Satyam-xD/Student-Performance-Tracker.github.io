document.addEventListener('DOMContentLoaded', function() {
    console.log("Document ready.");

    // Example of form submission handling
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            const nameInput = this.querySelector('input[name="name"]');
            const rollNumberInput = this.querySelector('input[name="roll_number"]');

            if (nameInput && !nameInput.value.trim()) {
                event.preventDefault();
                alert('Please enter a name.');
            }

            if (rollNumberInput && !rollNumberInput.value.trim()) {
                event.preventDefault();
                alert('Please enter a roll number.');
            }
        });
    });
});
