// ---------- MODAL ----------
function abrirModal() {
  document.getElementById("modal").style.display = "flex"
  document.querySelector(".fab").style.display = "none" // esconde botão +
}

function fecharModal() {
  document.getElementById("modal").style.display = "none"
  document.querySelector(".fab").style.display = "flex" // mostra botão +
}

// ---------- CATEGORIAS ----------
function abrirCategoria() {
  const popup = document.getElementById("categoria-popup")
  popup.style.display = popup.style.display === "flex" ? "none" : "flex"
}

function selecionarCategoria(categoria) {
  document.getElementById("categoria-input").value = categoria
  document.getElementById("btn-categoria").innerText = categoria
  document.getElementById("categoria-popup").style.display = "none"
}

// ---------- CALENDÁRIO ----------
let hoje = new Date()
let mesAtual = hoje.getMonth()
let anoAtual = hoje.getFullYear()

const meses = [
  "Janeiro",
  "Fevereiro",
  "Março",
  "Abril",
  "Maio",
  "Junho",
  "Julho",
  "Agosto",
  "Setembro",
  "Outubro",
  "Novembro",
  "Dezembro",
]

function abrirCalendario() {
  document.getElementById("calendario-popup").style.display = "block"
}

function fecharCalendario() {
  document.getElementById("calendario-popup").style.display = "none"
}

function gerarCalendario(mes, ano) {
  const diasEl = document.getElementById("dias")
  const mesAnoEl = document.getElementById("mes-ano")
  diasEl.innerHTML = ""
  mesAnoEl.innerText = `${meses[mes]} ${ano}`

  const primeiroDia = new Date(ano, mes, 1).getDay()
  const totalDias = new Date(ano, mes + 1, 0).getDate()

  // preenche espaços vazios antes do primeiro dia
  for (let i = 0; i < primeiroDia; i++) {
    const vazio = document.createElement("span")
    diasEl.appendChild(vazio)
  }

  for (let dia = 1; dia <= totalDias; dia++) {
    const diaEl = document.createElement("span")
    diaEl.innerText = dia
    diaEl.onclick = () => selecionarData(dia, mes, ano)
    diasEl.appendChild(diaEl)
  }
}

function prevMes() {
  mesAtual--
  if (mesAtual < 0) {
    mesAtual = 11
    anoAtual--
  }
  gerarCalendario(mesAtual, anoAtual)
}

function nextMes() {
  mesAtual++
  if (mesAtual > 11) {
    mesAtual = 0
    anoAtual++
  }
  gerarCalendario(mesAtual, anoAtual)
}

function selecionarData(dia, mes, ano) {
  const dataFormatada = `${dia.toString().padStart(2, "0")}/${(mes + 1)
    .toString()
    .padStart(2, "0")}/${ano}`
  document.querySelector(".btn-data").innerText = "📅 " + dataFormatada
  document.getElementById("data-input").value = `${ano}-${(mes + 1)
    .toString()
    .padStart(2, "0")}-${dia.toString().padStart(2, "0")}`
  fecharCalendario()
}

// Inicializa calendário ao carregar página
gerarCalendario(mesAtual, anoAtual)
