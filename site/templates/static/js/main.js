function renderizar_total_vendido(url){
    fetch(url,{
        method: "GET",
    }).then (function (result){
        return result.json()
    }).then (function (data){
        document.getElementById('total_investido').innerHTML = data.total
    })
}
function lucro_investido(url){
    fetch(url,{
        method: "GET",
    }).then (function (result){
        return result.json()
    }).then (function (data){
        document.getElementById('lucro').innerHTML = data.rendimento
    })
}

