
(function () {
    "use strict";

    // SVG icons for different product categories
    const categoryIcons = {
        "safety helmets": `
            <svg viewBox="0 0 24 24" fill="none">
                <path d="M3 16V12C3 7 7 3 12 3C17 3 21 7 21 12V16H3Z"
                    stroke="currentColor" stroke-width="1.8"
                    stroke-linejoin="round"/>
                <path d="M12 3V12M3 12H21"
                    stroke="currentColor" stroke-width="1.8"/>
            </svg>
        `,

        "safety shoes": `
            <svg viewBox="0 0 24 24" fill="none">
                <path d="M3 16L8 14L12 8L15 12L21 15V20H3V16Z"
                    stroke="currentColor" stroke-width="1.8"
                    stroke-linejoin="round"/>
            </svg>
        `,

        "safety gloves": `
            <svg viewBox="0 0 24 24" fill="none">
                <path d="M7 12V5C7 3 10 3 10 5V10V4C10 2 13 2 13 4V10V5C13 3 16 3 16 5V11V8C16 6 19 6 19 8V16C19 20 16 22 12 22H10C7 22 5 19 5 16V13C5 11 7 11 7 12Z"
                    stroke="currentColor" stroke-width="1.5"/>
            </svg>
        `,

        "safety goggles": `
            <svg viewBox="0 0 24 24" fill="none">
                <path d="M2 9H22L20 17H14L12 14L10 17H4L2 9Z"
                    stroke="currentColor" stroke-width="1.8"
                    stroke-linejoin="round"/>
            </svg>
        `,

        "safety jackets": `
            <svg viewBox="0 0 24 24" fill="none">
                <path d="M8 3L4 6L2 13L6 15L7 12V21H17V12L18 15L22 13L20 6L16 3L12 7L8 3Z"
                    stroke="currentColor" stroke-width="1.8"
                    stroke-linejoin="round"/>
                <path d="M12 7V21M8 11H10M14 11H16"
                    stroke="currentColor" stroke-width="1.5"/>
            </svg>
        `,

        "safety masks": `
            <svg viewBox="0 0 24 24" fill="none">
                <path d="M4 9L12 6L20 9V16L12 19L4 16V9Z"
                    stroke="currentColor" stroke-width="1.8"
                    stroke-linejoin="round"/>
                <path d="M4 10L1 8M20 10L23 8"
                    stroke="currentColor" stroke-width="1.8"/>
            </svg>
        `
    };

    // Default icon for categories without a matching icon
    const defaultIcon = `
        <svg viewBox="0 0 24 24" fill="none">
            <path d="M4 7L12 3L20 7V17L12 21L4 17V7Z"
                stroke="currentColor" stroke-width="1.8"
                stroke-linejoin="round"/>
            <path d="M4 7L12 11L20 7M12 11V21"
                stroke="currentColor" stroke-width="1.8"/>
        </svg>
    `;

    // Initialize category icons
    function initializeCategoryIcons() {
        document.querySelectorAll("[data-category-card]").forEach(
            function (card) {

                const categoryName = card
                    .querySelector("[data-category-name]")
                    ?.textContent
                    .trim()
                    .toLowerCase();

                const iconContainer = card.querySelector(
                    "[data-category-icon]"
                );

                if (!iconContainer || !categoryName) {
                    return;
                }

                iconContainer.innerHTML =
                    categoryIcons[categoryName] || defaultIcon;
            }
        );
    }

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
                String(!isOpen)
            );

            menu.classList.toggle("hidden", isOpen);
        });

        menu.querySelectorAll("a").forEach(function (link) {
            link.addEventListener("click", function () {
                button.setAttribute("aria-expanded", "false");
                menu.classList.add("hidden");
            });
        });
    }

    function initializeYear() {
        document.querySelectorAll("[data-current-year]").forEach(
            function (element) {
                element.textContent = String(
                    new Date().getFullYear()
                );
            }
        );
    }

    document.addEventListener("DOMContentLoaded", function () {
        initializeMobileMenu();
        initializeYear();
        initializeCategoryIcons();
    });

})();


/* ==========================================
   GET QUOTE POPUP FUNCTIONALITY
========================================== */

function initializeQuotePopup() {

    const modal = document.getElementById("quoteModal");

    if (!modal) return;

    const productName = document.getElementById("quoteProductName");
    const productCategory = document.getElementById("quoteProductCategory");
    const productImage = document.getElementById("quoteProductImage");
    const imagePlaceholder = document.getElementById("quoteImagePlaceholder");

    const productIdInput = document.getElementById("quoteProductId");
    const hiddenNameInput = document.getElementById("quoteProductHiddenName");

    const productInfoName = document.getElementById("quoteProductInfoName");
    const productPrice = document.getElementById("quoteProductPrice");

    const mobileInput = document.getElementById("quoteMobile");

    // OPEN POPUP
    document.addEventListener("click", function (event) {

        const button = event.target.closest("[data-quote-button]");

        if (!button) return;

        const name = button.dataset.productName || "Product";
        const category = button.dataset.productCategory || "";
        const image = button.dataset.productImage || "";
        const price = button.dataset.productPrice || "";

        const id = button.dataset.productId || "";

        // Set product information
        productName.textContent = name;
        productCategory.textContent = category;

        productInfoName.textContent = name;
        productPrice.textContent = price ? "INR " + price : "Contact for Price";

        productIdInput.value = id;
        hiddenNameInput.value = name;

        // Set product image
        if (image) {

            productImage.src = image;
            productImage.alt = name;
            productImage.hidden = false;
            imagePlaceholder.hidden = true;

            productImage.onerror = function () {
                productImage.hidden = true;
                imagePlaceholder.hidden = false;
            };

        } else {

            productImage.hidden = true;
            imagePlaceholder.hidden = false;

        }

        // Show popup
        modal.classList.add("active");
        modal.setAttribute("aria-hidden", "false");

        document.body.style.overflow = "hidden";

        // Focus mobile field
        setTimeout(function () {
            mobileInput.focus();
        }, 100);

    });


    // CLOSE POPUP
    function closeQuotePopup() {

        modal.classList.remove("active");
        modal.setAttribute("aria-hidden", "true");

        document.body.style.overflow = "";

    }

    modal.querySelectorAll("[data-quote-close]").forEach(function (element) {

        element.addEventListener("click", closeQuotePopup);

    });


    // CLOSE ON ESCAPE
    document.addEventListener("keydown", function (event) {

        if (
            event.key === "Escape" &&
            modal.classList.contains("active")
        ) {
            closeQuotePopup();
        }

    });


    // MOBILE NUMBER VALIDATION
    mobileInput.addEventListener("input", function () {

        this.value = this.value.replace(/\D/g, "").slice(0, 10);

    });

}


// INITIALIZE
document.addEventListener("DOMContentLoaded", function () {

    initializeQuotePopup();

});