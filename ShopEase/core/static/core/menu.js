const btn = document.querySelector("button.mobile-menu-button");
const menu = document.querySelector(".mobile-menu");

btn.addEventListener("click", () => {
    menu.classList.toggle("hidden");
});

// document.querySelectorAll('.dropdown-toggle').forEach(button => {
//     button.addEventListener('click', function (event) {
//         event.preventDefault();

//         // Close all dropdown menus
//         document.querySelectorAll('.dropdown-menu').forEach(menu => {
//             if (menu !== this.nextElementSibling) {
//                 menu.style.display = 'none';
//             }
//         });

//         // Toggle the clicked dropdown menu
//         const dropdown = this.nextElementSibling;
//         dropdown.style.display = (dropdown.style.display === 'block') ? 'none' : 'block';
//     });
// });

// // Close dropdowns when clicking outside
// document.addEventListener('click', function (event) {
//     if (!event.target.classList.contains('dropdown-toggle')) {
//         document.querySelectorAll('.dropdown-menu').forEach(menu => menu.style.display = 'none');
//     }
// });

// // Prevent click events inside dropdowns from closing them
// document.querySelectorAll('.dropdown-menu').forEach(menu => {
//     menu.addEventListener('click', function (event) {
//         event.stopPropagation();
//     });
// });