document.addEventListener("DOMContentLoaded", function() {
    const safespacesContainer = document.getElementById('safespaces-container');

    const safespaces = [
        {
            name: "Forest Retreat",
            type: "image",
            url: "/static/images/UnderTheTree.jpg"
        },
        {
            name: "Floating through the Sky",
            type: "image",
            url: "/static/images/clouds.jpg"
        },
        {
            name: "Meadow of Peace",
            type: "image",
            url: "/static/images/solitude.jpg"
        }
    ];

    safespaces.forEach((safespace) => {
        const div = document.createElement('div');
        div.classList.add('safespace');

        const img = document.createElement('img');
        img.src = safespace.url;
        img.alt = safespace.name;

        img.addEventListener('click', () => {
            // Redirect to the chatbot page with the safespace name as a query parameter
            window.location.href = `/chatbot/${encodeURIComponent(safespace.name)}`;
        });

        div.appendChild(img);
        const p = document.createElement('p');
        p.textContent = safespace.name;
        div.appendChild(p);

        safespacesContainer.appendChild(div);
    });
});
