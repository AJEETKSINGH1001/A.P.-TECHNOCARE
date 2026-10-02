(function () {
    "use strict";

    function initializeMobileMenu() {
        const button = document.querySelector("[data-mobile-menu-button]");
        const menu = document.querySelector("[data-mobile-menu]");

        if (!button || !menu) {
            return;
        }

        button.addEventListener("click", function () {
            const isOpen =
                button.getAttribute("aria-expanded") === "true";

            button.setAttribute(
                "aria-expanded",
                String(!isOpen),
            );

            menu.classList.toggle("hidden", isOpen);
        });

        menu.querySelectorAll("a").forEach(function (link) {
            link.addEventListener("click", function () {
                button.setAttribute(
                    "aria-expanded",
                    "false",
                );

                menu.classList.add("hidden");
            });
        });
    }

    function initializeYear() {
        document.querySelectorAll("[data-current-year]").forEach(
            function (element) {
                element.textContent = String(
                    new Date().getFullYear(),
                );
            },
        );
    }

    document.addEventListener(
        "DOMContentLoaded",
        function () {
            initializeMobileMenu();
            initializeYear();
        },
    );
})();