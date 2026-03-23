// Custom JavaScript for the Flask application

document.addEventListener('DOMContentLoaded', function() {
    console.log('Application loaded successfully!');

    // Initialize tooltips if needed
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});
