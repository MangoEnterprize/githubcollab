document.addEventListener('DOMContentLoaded', () => {
    const sortByButton = document.getElementById('sort-by');
    const essayFilter = document.getElementById('essay');
    const noEssayFilter = document.getElementById('no-essay');
    const allListings = document.querySelectorAll('.listing > div');

    sortByButton.addEventListener('click', () => {
        // Reset all listings to be visible initially
        allListings.forEach(listing => {
            listing.style.display = 'block';
        });

        // Filter based on selected radio button
        if (essayFilter.checked) {
            allListings.forEach(listing => {
                if (!listing.classList.contains('essay')) {
                    listing.style.display = 'none';
                }
            });
        } else if (noEssayFilter.checked) {
            allListings.forEach(listing => {
                if (!listing.classList.contains('no-essay')) {
                    listing.style.display = 'none';
                }
            });
        }
    });
});
