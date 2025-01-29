document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM Content Loaded'); // Debug log

    // Initialize dropdowns
    const dropdowns = document.querySelectorAll('.language-switcher .dropdown-toggle');
    console.log('Found dropdowns:', dropdowns.length); // Debug log

    dropdowns.forEach(function (dropdown) {
        dropdown.addEventListener('click', function (event) {
            event.stopPropagation();
            console.log('Dropdown clicked'); // Debug log

            const menu = this.nextElementSibling;
            const isExpanded = menu.classList.contains('show');

            // Close all other dropdowns
            document.querySelectorAll('.dropdown-menu.show').forEach(function (openMenu) {
                if (openMenu !== menu) {
                    openMenu.classList.remove('show');
                    openMenu.previousElementSibling.setAttribute('aria-expanded', 'false');
                }
            });

            // Toggle current dropdown
            menu.classList.toggle('show');
            this.setAttribute('aria-expanded', !isExpanded);
        });
    });

    // Close dropdowns when clicking outside
    document.addEventListener('click', function (event) {
        if (!event.target.closest('.language-switcher')) {
            document.querySelectorAll('.dropdown-menu.show').forEach(function (menu) {
                menu.classList.remove('show');
                menu.previousElementSibling.setAttribute('aria-expanded', 'false');
            });
        }
    });
});