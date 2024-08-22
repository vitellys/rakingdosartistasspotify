document.addEventListener('DOMContentLoaded', () => {
    async function fetchData() {
        try {
            const response = await fetch('/data');
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            console.log("Data fetched:", data);
            displayData(data);
        } catch (error) {
            console.error("Erro ao carregar dados:", error);
        }
    }

    function displayData(data) {
        const artistList = document.getElementById('artist-list');
        artistList.innerHTML = ''; // Limpa a lista existente

        data.pop_ranking.forEach(artist => {
            const li = document.createElement('li');
            li.textContent = `${artist.name} - Seguidores: ${artist.followers} - Popularidade: ${artist.popularity}`;
            artistList.appendChild(li);
        });

        const genreList = document.getElementById('genre-list');
        genreList.innerHTML = ''; // Limpa a lista existente

        data.genre_ranking.forEach(genre => {
            const li = document.createElement('li');
            li.textContent = genre;
            genreList.appendChild(li);
        });
    }

    fetchData();
});
