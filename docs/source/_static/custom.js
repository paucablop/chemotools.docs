document.addEventListener('DOMContentLoaded', function() {
    // Initialize all dropdowns
    var dropdowns = document.querySelectorAll('.dropdown-toggle');
    dropdowns.forEach(function(dropdown) {
        dropdown.addEventListener('click', function() {
            var menu = this.nextElementSibling;
            menu.classList.toggle('show');
            this.setAttribute('aria-expanded', menu.classList.contains('show'));
        });
    });

    // Close dropdowns when clicking outside
    document.addEventListener('click', function(event) {
        if (!event.target.matches('.dropdown-toggle')) {
            var dropdowns = document.querySelectorAll('.dropdown-menu.show');
            dropdowns.forEach(function(dropdown) {
                dropdown.classList.remove('show');
                dropdown.previousElementSibling.setAttribute('aria-expanded', 'false');
            });
        }
    });
});
