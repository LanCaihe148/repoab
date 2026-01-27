function mostrarCarta(id, titulo, cuerpo, fecha) {
    document.getElementById('detalle-titulo').textContent = titulo;
    document.getElementById('detalle-fecha').textContent = `Fecha: ${fecha}`;
    document.getElementById('detalle-cuerpo').textContent = cuerpo;

    document.getElementById('detalle-carta').style.display = 'block';

    document.getElementById('detalle-carta').scrollIntoView({
        behavior: 'smooth'
    });
}

function mostrarNota(id, cuerpo){
    document.getElementById('detalle-cuerpo'),textContent = cuerpo;
}