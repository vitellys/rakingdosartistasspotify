document.addEventListener('DOMContentLoaded', () => { // espera a pagina carregar para rodar o código
    async function fetchData() {  // buscar dados na api
        try {
            const response = await fetch('/data');
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`); // retorna caso dê errado
            }
            const data = await response.json(); // aguarda até que o json esteja pronto
            console.log("Data fetched:", data); // mostra os dados 
            displayData(data); // mostra os dados na página
        } catch (error) { // mostra caso dê errado
            console.error("Erro ao carregar dados:", error);
        }
    }

    function displayData(data) {
        const artistList = document.getElementById('artist-list'); // lugar onde mostrará os artistas
        artistList.innerHTML = ''; // limpa o que estiver para não se misturar

        data.pop_ranking.forEach(artist => { // cria um item para cada artista
            const li = document.createElement('li'); // cria um novo item na lista
            li.textContent = `${artist.name} - Seguidores: ${artist.followers} - Popularidade: ${artist.popularity}`; // define o texto da lista
            artistList.appendChild(li); // adiciona o item na lista da página
        });

        const genreList = document.getElementById('genre-list'); // lugar onde mostrará os gêneros mais comuns
        genreList.innerHTML = ''; // limpa o que estiver para não se misturar, igual na lista dos artistas

        data.genre_ranking.forEach(genre => {
            const li = document.createElement('li');
            li.textContent = genre;
            genreList.appendChild(li);
        });
    }

    fetchData();
});

/* o resto do código pode ser justificado mesmo modo da lista dos artistas, é a mesma função, 
muda apenas o que será mostrado */