function expand(clickedElement) {
    const hiddenInfo = clickedElement.querySelector('.div-oculta');
    clickedElement.classList.toggle('expanded');

    if (clickedElement.classList.contains('expanded')) {
        // Mostrar as informações ocultas
        hiddenInfo.style.display = 'block';
    } else {
        // Ocultar as informações quando a div for recolhida novamente
        hiddenInfo.style.display = 'none';
    }
}

function confirmDelete(id) {
    var resp = confirm('tem certeza que deseja deletar?')

    if (resp) {
        window.location.href = "excluir/" + id

        alert("Exclusão concluída com sucesso!")

    }
}