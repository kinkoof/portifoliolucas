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