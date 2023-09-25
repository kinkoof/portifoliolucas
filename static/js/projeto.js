
function excluirProjeto(id) {
    var resp = confirm('tem certeza que deseja deletar?')

    if (resp) {
        window.location.href = "excluir/" + id

        alert("Exclusão concluída com sucesso!")

    }
}