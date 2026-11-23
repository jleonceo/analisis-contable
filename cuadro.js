/* Cuadro de mando de contabilidad de gestión.
   Lee los CSV de datos/ (los mismos que lee el informe de Power BI), dibuja tres pestañas y guarda la pestaña y el
   filtro en la dirección de la página. Sin librerías: SVG dibujado aquí. Todo texto que viene de los datos entra con
   textContent. */
"use strict";

// ===== Paleta y textos fijos =====
const AZUL = "#2a78d6", NARANJA = "#eb6834", VERDE = "#1baf7a", GRIS = "#898781";
const REJILLA = "#e1e0d9", EJE = "#c3c2b7";
const ANOS = ["2023", "2024", "2025", "2026"];
const MESES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"];
const FICHEROS = ["d_ventas_resultado", "d_margenes", "d_margen_bruto_mensual", "d_punto_muerto", "d_flujos",
  "d_rentabilidad", "d_concentracion_clientes", "d_puente_presupuesto", "c_objetivos", "c_presupuesto_real",
  "c_ingresos_linea", "c_coste_centro", "c_coste_laboral", "c_variaciones", "c_clientes", "o_comprobaciones"];
const ESTADO = { OK: "En orden", AVISO: "Aviso", SIN_DATO: "Sin dato" };

let D = {};                       // los CSV leídos, por nombre
const estado = { pestana: "direccion", ano: "Todos" };

// ===== Números y textos a la española =====
function miles(entero) { return String(entero).replace(/\B(?=(\d{3})+(?!\d))/g, "."); }
function num(x, dec = 0) {
  const v = Number(x);
  const signo = v < 0 ? "−" : "";
  const [e, d] = Math.abs(v).toFixed(dec).split(".");
  return signo + miles(e) + (d ? "," + d : "");
}
function eur(x) { return num(x, 0) + " €"; }
function pct(x, dec = 1) { return num(x, dec) + " %"; }
function conSigno(texto, x) { return (Number(x) > 0 ? "+" : "") + texto; }
function millones(x) { return num(Number(x) / 1e6, 2) + " M€"; }
function mesLargo(aaaamm) { const [a, m] = aaaamm.split("-"); return MESES[Number(m) - 1] + " " + a; }

// ===== Lectura de los CSV =====
function leerCSV(texto) {
  const filas = []; let fila = [], campo = "", comillas = false;
  for (let i = 0; i < texto.length; i++) {
    const c = texto[i];
    if (comillas) {
      if (c === '"' && texto[i + 1] === '"') { campo += '"'; i++; }
      else if (c === '"') comillas = false;
      else campo += c;
    } else if (c === '"') comillas = true;
    else if (c === ",") { fila.push(campo); campo = ""; }
    else if (c === "\n") { fila.push(campo); filas.push(fila); fila = []; campo = ""; }
    else if (c !== "\r") campo += c;
  }
  if (campo !== "" || fila.length) { fila.push(campo); filas.push(fila); }
  const cabecera = filas.shift();
  return filas.filter(f => f.length === cabecera.length).map(f => Object.fromEntries(cabecera.map((k, i) => [k, f[i]])));
}
async function cargar() {
  const textos = await Promise.all(FICHEROS.map(f => fetch("datos/" + f + ".csv").then(r => {
    if (!r.ok) throw new Error(f + ".csv no se pudo leer (" + r.status + ")");
    return r.text();
  })));
  FICHEROS.forEach((f, i) => { D[f] = leerCSV(textos[i]); });
}

// ===== Piezas de la página =====
function el(etiqueta, atributos = {}, texto) {
  const n = document.createElement(etiqueta);
  for (const [k, v] of Object.entries(atributos)) n.setAttribute(k, v);
  if (texto !== undefined) n.textContent = texto;
  return n;
}
function svgEl(etiqueta, atributos = {}, texto) {
  const n = document.createElementNS("http://www.w3.org/2000/svg", etiqueta);
  for (const [k, v] of Object.entries(atributos)) n.setAttribute(k, v);
  if (texto !== undefined) n.textContent = texto;
  return n;
}
function cifras(id, lista) {
  const caja = document.getElementById(id); caja.replaceChildren();
  for (const c of lista) {
    const d = el("div", { class: "cifra", tabindex: "0", "data-tip": c.tip, "data-valor": c.valor });
    d.append(el("p", { class: "numero" }, c.numero), el("p", { class: "etiqueta" }, c.etiqueta),
      el("p", { class: "contexto" }, c.contexto));
    caja.append(d);
  }
}
function cabeceraGrafico(fig, titulo, subtitulo, leyenda) {
  fig.replaceChildren(el("h2", {}, titulo), el("p", { class: "subtitulo" }, subtitulo));
  if (leyenda && leyenda.length) {
    const ul = el("ul", { class: "leyenda" });
    for (const l of leyenda) {
      const li = el("li");
      li.append(el("span", { class: l.raya ? "raya" : "marca", style: "background:" + l.color }), document.createTextNode(l.nombre));
      ul.append(li);
    }
    fig.append(ul);
  }
}
function dato(grupo, tip) { grupo.setAttribute("class", "dato"); grupo.setAttribute("tabindex", "0"); grupo.setAttribute("data-tip", tip); grupo.setAttribute("aria-label", tip); return grupo; }
function escalaLimpia(max) {
  const paso = Math.pow(10, Math.floor(Math.log10(max)));
  for (const m of [1, 2, 2.5, 5, 10]) if (m * paso >= max) return m * paso;
  return 10 * paso;
}

// ===== Gráficos =====
// Columnas agrupadas: categorías en el eje x, una barra por serie; cada barra con su cifra (G4).
function columnas(fig, categorias, series, formato, formatoTip) {
  const W = 500, H = 270, m = { t: 22, r: 8, b: 30, l: 8 };
  const max = escalaLimpia(Math.max(...series.flatMap(s => s.valores.map(Number))));
  const y = v => m.t + (H - m.t - m.b) * (1 - v / max);
  const banda = (W - m.l - m.r) / categorias.length;
  const ancho = Math.min(24 * series.length + 2 * (series.length - 1), banda * 0.7) / series.length;
  const svg = svgEl("svg", { viewBox: `0 0 ${W} ${H}`, role: "img" });
  svg.append(svgEl("line", { x1: m.l, x2: W - m.r, y1: y(0), y2: y(0), stroke: EJE }));
  categorias.forEach((cat, i) => {
    const x0 = m.l + banda * i + banda / 2 - (ancho * series.length + 2 * (series.length - 1)) / 2;
    series.forEach((s, j) => {
      const v = Number(s.valores[i]), x = x0 + j * (ancho + 2);
      const g = dato(svgEl("g"), `${s.nombre}, ${cat.tip}: ${formatoTip(v)}`);
      g.append(svgEl("rect", { x, y: y(v), width: ancho, height: Math.max(0, y(0) - y(v)), fill: s.color, rx: 2 }));
      g.append(svgEl("text", { class: "valor", x: x + ancho / 2, y: y(v) - 4, "text-anchor": "middle" }, formato(v)));
      svg.append(g);
    });
    svg.append(svgEl("text", { x: m.l + banda * i + banda / 2, y: H - 10, "text-anchor": "middle" }, cat.nombre));
  });
  fig.append(svg);
}

// Línea en el tiempo: uno o dos series con puntos que llevan su etiqueta; referencia opcional rotulada.
function lineas(fig, etiquetas, series, opciones) {
  const W = 500, H = 270, m = { t: 14, r: 46, b: 30, l: 40 };
  const valores = series.flatMap(s => s.valores.filter(v => v !== null).map(Number));
  if (opciones.referencia !== undefined) valores.push(opciones.referencia);
  const bruto = Math.max(...valores) - Math.min(...valores);
  const paso = [5, 10, 15, 20, 25, 50].find(p => bruto / p <= 5) || 100;
  const min = opciones.desdeCero ? 0 : Math.floor(Math.min(...valores) / paso) * paso;
  const max = Math.ceil(Math.max(...valores) / paso) * paso;
  const x = i => m.l + (W - m.l - m.r) * (etiquetas.length === 1 ? 0.5 : i / (etiquetas.length - 1));
  const y = v => m.t + (H - m.t - m.b) * (1 - (v - min) / (max - min));
  const svg = svgEl("svg", { viewBox: `0 0 ${W} ${H}`, role: "img" });
  for (let v = min; v <= max + 1e-9; v += paso) {
    const k = v - min;
    svg.append(svgEl("line", { x1: m.l, x2: W - m.r, y1: y(v), y2: y(v), stroke: k === 0 ? EJE : REJILLA }));
    svg.append(svgEl("text", { x: m.l - 6, y: y(v) + 4, "text-anchor": "end" }, num(v, 0) + opciones.unidad));
  }
  if (opciones.referencia !== undefined) {
    svg.append(svgEl("line", { x1: m.l, x2: W - m.r, y1: y(opciones.referencia), y2: y(opciones.referencia), stroke: "#0b0b0b", "stroke-width": 1 }));
    svg.append(svgEl("text", { x: W - m.r + 4, y: y(opciones.referencia) + 4 }, opciones.rotuloReferencia));
  }
  const cada = etiquetas.length <= 12 ? 1 : Math.ceil(etiquetas.length / 8);
  etiquetas.forEach((e, i) => { if (i % cada === 0 || i === etiquetas.length - 1) svg.append(svgEl("text", { x: x(i), y: H - 10, "text-anchor": "middle" }, e.corta)); });
  for (const s of series) {
    const puntos = s.valores.map((v, i) => v === null ? null : [x(i), y(Number(v))]).filter(Boolean);
    svg.append(svgEl("polyline", { points: puntos.map(p => p.join(",")).join(" "), fill: "none", stroke: s.color, "stroke-width": 2, "stroke-linejoin": "round", "stroke-linecap": "round" }));
    s.valores.forEach((v, i) => {
      if (v === null) return;
      const g = dato(svgEl("g"), `${s.nombre}, ${etiquetas[i].larga}: ${num(v, 1)}${opciones.unidad}`);
      g.append(svgEl("circle", { cx: x(i), cy: y(Number(v)), r: 12, fill: "transparent" }));
      g.append(svgEl("circle", { cx: x(i), cy: y(Number(v)), r: 3.5, fill: s.color, stroke: "#ffffff", "stroke-width": 2 }));
      svg.append(g);
    });
    const u = s.valores.length - 1;
    if (s.valores[u] !== null && opciones.rotularFinal) svg.append(svgEl("text", { class: "valor", x: x(u) + 6, y: y(Number(s.valores[u])) + 4 }, num(s.valores[u], 1) + opciones.unidad));
  }
  fig.append(svg);
}

// Cascada: el primer y el último escalón son totales; los demás suben o bajan desde el acumulado anterior.
function cascada(fig, pasos) {
  const W = 500, H = 300, m = { t: 22, r: 8, b: 74, l: 8 };
  const max = Math.max(...pasos.map(p => Math.max(p.desde, p.hasta))) * 1.06;
  const y = v => m.t + (H - m.t - m.b) * (1 - v / max);
  const banda = (W - m.l - m.r) / pasos.length, ancho = Math.min(24, banda * 0.7);
  const svg = svgEl("svg", { viewBox: `0 0 ${W} ${H}`, role: "img" });
  svg.append(svgEl("line", { x1: m.l, x2: W - m.r, y1: y(0), y2: y(0), stroke: EJE }));
  pasos.forEach((p, i) => {
    const xc = m.l + banda * i + banda / 2, arriba = Math.max(p.desde, p.hasta), abajo = Math.min(p.desde, p.hasta);
    const g = dato(svgEl("g"), p.tip);
    g.append(svgEl("rect", { x: xc - ancho / 2, y: y(arriba), width: ancho, height: Math.max(1, y(abajo) - y(arriba)), fill: p.color, rx: 2 }));
    g.append(svgEl("text", { class: "valor", x: xc, y: y(arriba) - 4, "text-anchor": "middle" }, p.cifra));
    svg.append(g);
    const t = svgEl("text", { x: xc, y: H - m.b + 12, "text-anchor": "end", transform: `rotate(-40 ${xc} ${H - m.b + 12})` }, p.corta);
    svg.append(t);
  });
  fig.append(svg);
}

// ===== Tablas =====
function tabla(destino, titulo, columnasTabla, filas, total) {
  const caja = el("div", { class: "tabla-caja" });
  const t = el("table");
  t.append(el("caption", {}, titulo));
  const cab = el("tr");
  for (const c of columnasTabla) cab.append(el("th", c.num ? { class: "num" } : {}, c.nombre));
  const cabeza = el("thead"); cabeza.append(cab); t.append(cabeza);
  const cuerpo = el("tbody");
  for (const f of filas) {
    const tr = el("tr");
    for (const c of columnasTabla) {
      const clases = [c.num ? "num" : "", c.clase ? c.clase(f) : ""].filter(Boolean).join(" ");
      tr.append(el("td", clases ? { class: clases } : {}, c.valor(f)));
    }
    cuerpo.append(tr);
  }
  if (total) {
    const tr = el("tr", { class: "total" });
    for (const c of columnasTabla) tr.append(el("td", c.num ? { class: "num" } : {}, total(c) ?? ""));
    cuerpo.append(tr);
  }
  t.append(cuerpo); caja.append(t); destino.append(caja);
}

// ===== Selección =====
function anosSel() { return estado.ano === "Todos" ? ANOS : [estado.ano]; }
function textoViendo() {
  if (estado.ano === "Todos") return "Viendo: todos los años, de enero de 2023 a julio de 2026";
  if (estado.ano === "2026") return "Viendo: 2026, de enero a julio";
  return "Viendo: " + estado.ano + ", año completo";
}
function porAno(nombre) { return Object.fromEntries(D[nombre].map(f => [f.ano, f])); }
function etiquetaAno(a) { return a === "2026" ? "2026 (ene-jul)" : a; }

// ===== Pestaña Dirección =====
// Solo el ejercicio del corte (Juan, 23/11/2026): la rentabilidad de 2023 a 2025 sale de un dato generado irreal y
// no se publica. Por eso esta pestaña no usa el filtro de año.
const ANO_DIRECCION = "2026";
function dibujarDireccion() {
  const a = ANO_DIRECCION;
  const v = porAno("d_ventas_resultado")[a], mg = porAno("d_margenes")[a], fl = porAno("d_flujos")[a];
  const pm = porAno("d_punto_muerto")[a], rt = porAno("d_rentabilidad")[a];
  cifras("dir-cifras", [
    { numero: eur(v.ventas), etiqueta: "Ventas", contexto: "de enero a julio de " + a,
      valor: v.ventas, tip: "Ventas de mercaderías de enero a julio de " + a + ": " + eur(v.ventas) + ". Haber menos debe de las cuentas de ventas." },
    { numero: eur(v.resultado), etiqueta: "Resultado", contexto: "de enero a julio de " + a + ", antes de impuestos",
      valor: v.resultado, tip: "Resultado de enero a julio de " + a + ": " + eur(v.resultado) + ". Ingresos menos gastos; el diario no registra el impuesto sobre beneficios." },
    { numero: pct(mg.margen_bruto_pct), etiqueta: "Margen bruto", contexto: "de enero a julio de " + a,
      valor: mg.margen_bruto_pct, tip: "Margen bruto de enero a julio de " + a + ": " + pct(mg.margen_bruto_pct, 2) + ". Ventas menos compras y variación de existencias, sobre las ventas." },
    { numero: eur(fl.caja_libre), etiqueta: "Flujo de caja libre", contexto: "de enero a julio de " + a,
      valor: fl.caja_libre, tip: "Flujo de caja libre de enero a julio de " + a + ": " + eur(fl.caja_libre) + ". Caja que deja la operación después de pagar las inversiones." },
  ]);
  document.getElementById("dir-texto").textContent =
    "De enero a julio de " + a + " la empresa vendió " + eur(v.ventas) + " con un margen bruto del " + pct(mg.margen_bruto_pct) +
    ". El resultado antes de impuestos fue de " + eur(v.resultado) + ", el " + pct(rt.margen_neto_pct) + " de las ventas.";

  const meses = D.d_margen_bruto_mensual.filter(f => f.mes.startsWith(a + "-"));
  const fig1 = document.getElementById("dir-g1");
  cabeceraGrafico(fig1, "Ventas y aprovisionamientos de cada mes",
    "En miles de €; de enero a julio de " + a,
    [{ nombre: "Ventas", color: AZUL }, { nombre: "Aprovisionamientos", color: NARANJA }]);
  columnas(fig1, meses.map(f => ({ nombre: MESES[Number(f.mes.slice(5)) - 1], tip: mesLargo(f.mes) })),
    [{ nombre: "Ventas", color: AZUL, valores: meses.map(f => f.ventas) },
     { nombre: "Aprovisionamientos", color: NARANJA, valores: meses.map(f => f.aprovisionamientos) }],
    x => num(x / 1000, 0), eur);

  const fig2 = document.getElementById("dir-g2");
  const todosBajo50 = meses.length > 0 && meses.every(f => Number(f.margen_bruto_pct) < 50);
  cabeceraGrafico(fig2, todosBajo50 ? "El margen bruto no llegó al 50 % en ningún mes" : "Margen bruto de cada mes",
    "Margen bruto sobre ventas de cada mes, en %; de enero a julio de " + a, []);
  lineas(fig2, meses.map(f => ({ corta: MESES[Number(f.mes.slice(5)) - 1], larga: mesLargo(f.mes) })),
    [{ nombre: "Margen bruto", color: AZUL, valores: meses.map(f => Number(f.margen_bruto_pct)) }],
    { unidad: " %", referencia: 50, rotuloReferencia: "50 %", rotularFinal: true, desdeCero: true });

  const det = document.getElementById("dir-detalle");
  det.replaceChildren(el("summary", {}, "Detalle de " + a));
  tabla(det, "Las cifras de enero a julio de " + a, [
    { nombre: "Ventas (€)", num: true, valor: () => num(v.ventas) },
    { nombre: "Resultado (€)", num: true, valor: () => num(v.resultado) },
    { nombre: "Margen bruto (%)", num: true, valor: () => num(mg.margen_bruto_pct, 1) },
    { nombre: "Margen de explotación (%)", num: true, valor: () => num(mg.margen_explotacion_pct, 1) },
    { nombre: "Punto muerto (€ de ventas)", num: true, valor: () => pm ? num(pm.punto_muerto) : "" },
    { nombre: "Flujo de caja libre (€)", num: true, valor: () => num(fl.caja_libre) },
    { nombre: "Rentabilidad del capital (%)", num: true, valor: () => num(rt.roe_pct, 1) },
  ], [{}]);
  const conc = D.d_concentracion_clientes;
  det.append(el("p", { class: "nota" },
    "Solo se publica " + a + ": las series de 2023 a 2025 salen de un dato generado en el que las compras no siguen a las ventas, y sus márgenes no son los de una pyme real. " +
    "El punto muerto es lo que hay que vender para no perder. La rentabilidad del capital es el resultado sobre el patrimonio medio, sin anualizar, y no se ha comprobado por otra vía. " +
    "En los doce meses hasta julio de " + a + ", el primer cliente reúne el " + pct(conc[0].peso_pct) + " de lo facturado y los cinco primeros, el " + pct(conc[4].peso_acumulado_pct) + "."));
}

// ===== Pestaña Controller =====
function dibujarController() {
  const acum = Object.fromEntries(D.c_objetivos.filter(f => f.periodo.includes(" a ")).map(f => [f.indicador, f]));
  const puente = D.d_puente_presupuesto, ini = puente[0], fin = puente[puente.length - 1];
  const sin = puente.find(p => p.partida === "Partidas sin presupuesto");
  const periodo = acum.Ingresos_Totales_Mes.periodo;
  cifras("con-cifras", [
    { numero: pct(acum.Ingresos_Totales_Mes.cumplimiento_pct), etiqueta: "Ingresos frente a su objetivo", contexto: "de enero a julio de 2026",
      valor: acum.Ingresos_Totales_Mes.cumplimiento_pct, tip: "Ingresos de enero a julio de 2026: " + eur(acum.Ingresos_Totales_Mes.real) + " frente a un objetivo de " + eur(acum.Ingresos_Totales_Mes.objetivo) + "." },
    { numero: pct(acum.Gasto_Total_Mes.cumplimiento_pct), etiqueta: "Gasto frente a su objetivo", contexto: "de enero a julio de 2026",
      valor: acum.Gasto_Total_Mes.cumplimiento_pct, tip: "Gasto de enero a julio de 2026: " + eur(acum.Gasto_Total_Mes.real) + " frente a un objetivo de " + eur(acum.Gasto_Total_Mes.objetivo) + "." },
    { numero: eur(fin.acumulado), etiqueta: "Resultado real", contexto: eur(ini.acumulado) + " presupuestados",
      valor: fin.acumulado, tip: "Resultado real de enero a julio de 2026: " + eur(fin.acumulado) + ". Presupuestado: " + eur(ini.acumulado) + "." },
    { numero: eur(sin.efecto), etiqueta: "Partidas sin presupuesto", contexto: "lo que el presupuesto no recoge",
      valor: sin.efecto, tip: "Resultado de las partidas sin presupuesto, de enero a julio de 2026: " + eur(sin.efecto) + "." },
  ]);
  document.getElementById("con-texto").textContent =
    "Hasta julio, los ingresos cumplen su objetivo y el gasto lo supera. Tres partidas parecen gastar menos de lo presupuestado, pero su gasto está apuntado en otro centro. Ese gasto reaparece en las partidas sin presupuesto y deja el resultado real por debajo del presupuestado.";

  const fig1 = document.getElementById("con-g1");
  cabeceraGrafico(fig1, "Las partidas sin presupuesto dejan el resultado por debajo de lo previsto",
    "Del resultado presupuestado al real, en €, de enero a julio de 2026",
    [{ nombre: "Resultado", color: AZUL }, { nombre: "Partida con presupuesto", color: GRIS }, { nombre: "Partidas sin presupuesto", color: NARANJA }]);
  let previo = 0;
  const pasos = puente.map((p, i) => {
    const total = i === 0 || i === puente.length - 1;
    const desde = total ? 0 : previo, hasta = Number(p.acumulado);
    previo = hasta;
    const color = total ? AZUL : (p.partida === "Partidas sin presupuesto" ? NARANJA : GRIS);
    const efecto = Number(p.efecto);
    const corta = ({ "Resultado presupuestado": "Presupuestado", "Resultado real": "Real", "Partidas sin presupuesto": "Sin presupuesto" })[p.partida] || p.partida.replace(/ \(.*\)$/, "").replace("Publicidad, propaganda y relaciones públicas", "Publicidad").replace("Seguridad Social a cargo de la empresa", "Seguridad Social").replace("Arrendamientos y cánones", "Arrendamientos");
    return { desde, hasta, color, corta: corta.length > 22 ? corta.slice(0, 21) + "…" : corta,
      cifra: total ? num(hasta / 1000, 0) + " mil" : (Math.abs(efecto) < 0.5 ? "0" : Math.abs(efecto) < 1000 ? num(efecto, 0) : conSigno(num(efecto / 1000, 0) + " mil", efecto)),
      tip: p.partida + ": " + (total ? eur(hasta) : conSigno(num(efecto, 2) + " €", efecto) + " sobre el resultado") };
  });
  cascada(fig1, pasos);

  const meses = D.c_objetivos.filter(f => !f.periodo.includes(" a ") && f.real !== "");
  const ing = meses.filter(f => f.indicador === "Ingresos_Totales_Mes"), gas = meses.filter(f => f.indicador === "Gasto_Total_Mes");
  const fig2 = document.getElementById("con-g2");
  const porEncima = gas.filter(f => Number(f.cumplimiento_pct) > 100).length;
  cabeceraGrafico(fig2, "El gasto pasó de su objetivo en " + porEncima + " de los " + gas.length + " meses",
    "Cumplimiento de cada mes frente a su objetivo, en %, de enero a julio de 2026",
    [{ nombre: "Ingresos", color: AZUL, raya: true }, { nombre: "Gasto", color: VERDE, raya: true }]);
  lineas(fig2, ing.map(f => ({ corta: MESES[Number(f.periodo.slice(5)) - 1], larga: mesLargo(f.periodo) })),
    [{ nombre: "Ingresos", color: AZUL, valores: ing.map(f => Number(f.cumplimiento_pct)) },
     { nombre: "Gasto", color: VERDE, valores: gas.map(f => Number(f.cumplimiento_pct)) }],
    { unidad: " %", referencia: 100, rotuloReferencia: "objetivo" });

  const det = document.getElementById("con-detalle");
  det.replaceChildren(el("summary", {}, "Detalle: partidas, líneas, centros, personal y clientes"));
  if (estado.ano !== "Todos" && estado.ano !== "2026") det.append(el("p", { class: "nota" }, "El presupuesto y los objetivos solo existen para 2026: el filtro de año cambia las tablas de líneas, centros y personal."));

  // Desviación por partida, sumada de enero a julio
  const partidas = {};
  for (const f of D.c_presupuesto_real) {
    const k = f.cuenta + "|" + f.centro;
    partidas[k] ??= { nombre: f.nombre_cuenta, centro: f.centro, presupuesto: 0, real: 0, desviacion: 0 };
    partidas[k].presupuesto += Number(f.presupuesto); partidas[k].real += Number(f.real); partidas[k].desviacion += Number(f.desviacion);
  }
  const lista = Object.values(partidas).sort((p, q) => Math.abs(q.desviacion) - Math.abs(p.desviacion));
  tabla(det, "Presupuesto frente a real por partida, de enero a julio de 2026", [
    { nombre: "Cuenta", valor: p => p.nombre }, { nombre: "Centro", valor: p => p.centro || "toda la empresa" },
    { nombre: "Presupuesto (€)", num: true, valor: p => num(p.presupuesto) }, { nombre: "Real (€)", num: true, valor: p => num(p.real) },
    { nombre: "Real menos presupuesto (€)", num: true, valor: p => num(p.desviacion) },
  ], lista);
  det.append(el("p", { class: "nota" }, "El real de cada partida es el de esa cuenta en ese centro. Lo apuntado en otro centro, o en una cuenta sin presupuesto, cae en las partidas sin presupuesto."));

  const lineasNeg = D.c_ingresos_linea.filter(f => anosSel().includes(f.ano));
  tabla(det, "Ingresos por línea de negocio", [
    { nombre: "Año", valor: f => etiquetaAno(f.ano) }, { nombre: "Línea", valor: f => f.linea }, { nombre: "Ingresos (€)", num: true, valor: f => num(f.ingresos) },
  ], lineasNeg);
  det.append(el("p", { class: "nota" }, "El gasto no se reparte entre líneas porque todo se apunta como común. Repartirlo por ventas daría a las dos el mismo margen."));

  const centros = {};
  for (const f of D.c_coste_centro.filter(f => anosSel().includes(f.mes.slice(0, 4)))) {
    const k = f.mes.slice(0, 4) + "|" + f.centro;
    centros[k] ??= { ano: f.mes.slice(0, 4), centro: f.centro, coste: 0 };
    centros[k].coste += Number(f.coste);
  }
  tabla(det, "Coste por centro", [
    { nombre: "Año", valor: f => etiquetaAno(f.ano) }, { nombre: "Centro", valor: f => f.centro }, { nombre: "Coste (€)", num: true, valor: f => num(f.coste) },
  ], Object.values(centros).sort((p, q) => p.ano.localeCompare(q.ano) || q.coste - p.coste));
  det.append(el("p", { class: "nota" }, "El reparto de una misma cuenta entre centros cambia de un año a otro, así que el coste de un centro se lee dentro de cada año y no se compara entre años."));

  tabla(det, "Coste de personal", [
    { nombre: "Año", valor: f => etiquetaAno(f.ano) }, { nombre: "Personas", num: true, valor: f => f.personas },
    { nombre: "Sueldos (€)", num: true, valor: f => num(f.sueldos) }, { nombre: "Seguridad Social (€)", num: true, valor: f => num(f.seguridad_social) },
    { nombre: "Coste total (€)", num: true, valor: f => num(f.coste_total) },
  ], D.c_coste_laboral.filter(f => anosSel().includes(f.ano)));
  det.append(el("p", { class: "nota" }, "Solo el total: por departamento quedarían grupos de menos de cinco personas, en los que se vería el sueldo de alguien."));

  tabla(det, "Clientes: días de cobro y límite de crédito al corte", [
    { nombre: "Cliente", valor: f => f.cuenta }, { nombre: "Días pactados", num: true, valor: f => f.dias_pactados ? num(f.dias_pactados) : "" },
    { nombre: "Días reales (mediana)", num: true, valor: f => f.dias_reales_mediana ? num(f.dias_reales_mediana) : "" },
    { nombre: "Saldo (€)", num: true, valor: f => f.saldo ? num(f.saldo) : "" }, { nombre: "Límite (€)", num: true, valor: f => f.limite ? num(f.limite) : "" },
    { nombre: "Uso del límite (%)", num: true, valor: f => f.uso_limite_pct ? num(f.uso_limite_pct, 0) : "", clase: f => Number(f.uso_limite_pct) > 100 ? "aviso" : "" },
    { nombre: "Ha dejado de comprar", valor: f => f.apagado === "true" ? "sí" : (f.apagado === "false" ? "no" : "") },
  ], [...D.c_clientes].sort((p, q) => Number(q.uso_limite_pct || -1) - Number(p.uso_limite_pct || -1)));
  det.append(el("p", { class: "nota" }, "Los clientes van por su código de cuenta. El uso del límite queda en blanco cuando el saldo es a favor del cliente; en negrita, por encima del 100 %."));
}

// ===== Pestaña Contabilidad =====
function dibujarContabilidad() {
  const c = D.o_comprobaciones;
  const avisos = c.filter(f => f.estado === "AVISO"), bien = c.filter(f => f.estado === "OK");
  const d08 = c.find(f => f.analisis === "D08"), a08 = c.find(f => f.analisis === "A08");
  const sinDotar = (d08.cifra.match(/([0-9.]+,[0-9]{2})/) || [])[1] || "";
  const sinUsar = (a08.cifra.match(/números sin usar: ([0-9.]+)/) || [])[1] || "";
  cifras("ope-cifras", [
    { numero: bien.length + " de " + c.length, etiqueta: "Comprobaciones en orden", contexto: "a 31/07/2026", valor: bien.length, tip: bien.length + " de las " + c.length + " comprobaciones del libro diario no encuentran nada que revisar." },
    { numero: String(avisos.length), etiqueta: "Comprobaciones con aviso", contexto: "cada una con lo que encontró", valor: avisos.length, tip: avisos.length + " comprobaciones encuentran algo que una persona tiene que mirar." },
    { numero: sinDotar.replace(/,00$/, "") + " €", etiqueta: "Reserva legal sin dotar", contexto: "lo que falta hasta el 20 % del capital", valor: sinDotar.replace(/\./g, "").replace(",", "."), tip: "Reserva legal que falta por dotar a 31/07/2026: " + sinDotar + " €." },
    { numero: sinUsar, etiqueta: "Números de asiento sin usar", contexto: "en la numeración del 1 al 8.672", valor: sinUsar.replace(/\./g, ""), tip: sinUsar + " números de asiento sin usar entre el primero y el último." },
  ]);
  document.getElementById("ope-texto").textContent =
    "El diario cuadra al céntimo. Los cierres traspasan bien el saldo de un ejercicio al siguiente y ninguna cuenta queda fuera del plan contable. Los avisos piden una revisión a mano: la reserva legal sin dotar, los huecos de la numeración y las cuentas que se comportan distinto de lo habitual.";

  const caja = document.getElementById("ope-tabla"); caja.replaceChildren();
  const orden = [...avisos, ...c.filter(f => f.estado !== "AVISO" && f.estado !== "OK"), ...bien];
  tabla(caja, "Comprobaciones del libro diario, primero las que tienen aviso", [
    { nombre: "Qué se comprueba", valor: f => f.que_mira }, { nombre: "Tema", valor: f => f.bloque },
    { nombre: "Estado", valor: f => ESTADO[f.estado] || f.estado, clase: f => f.estado === "AVISO" ? "aviso" : "" },
    { nombre: "Lo que se ve", valor: f => f.cifra },
  ], orden);
  const p = el("p", { class: "descarga" });
  const b = el("button", { type: "button" }, "Descargar la lista en CSV");
  b.addEventListener("click", () => descargarComprobaciones(orden));
  p.append(b); caja.append(p);
}
function descargarComprobaciones(filas) {
  const campo = x => '"' + String(x).replace(/"/g, '""') + '"';
  const lineas = ["Comprobaciones del libro diario a 31/07/2026",
    ["Qué se comprueba", "Tema", "Estado", "Lo que se ve"].map(campo).join(";"),
    ...filas.map(f => [f.que_mira, f.bloque, ESTADO[f.estado] || f.estado, f.cifra].map(campo).join(";"))];
  const blob = new Blob(["﻿" + lineas.join("\r\n")], { type: "text/csv;charset=utf-8" });
  const a = el("a", { href: URL.createObjectURL(blob), download: "comprobaciones_libro_diario_datos-2026-07-31.csv" });
  document.body.append(a); a.click(); a.remove();
}

// ===== Dirección de la página, pestañas y filtros =====
function leerDireccion() {
  const p = new URLSearchParams(location.hash.slice(1));
  if (["direccion", "controller", "contabilidad"].includes(p.get("pestana"))) estado.pestana = p.get("pestana");
  if (["Todos", ...ANOS].includes(p.get("ano"))) estado.ano = p.get("ano");
}
function escribirDireccion() { history.replaceState(null, "", "#pestana=" + estado.pestana + "&ano=" + estado.ano); }
function pintar() {
  for (const b of document.querySelectorAll(".pestanas button")) {
    const sel = b.dataset.pestana === estado.pestana;
    b.setAttribute("aria-selected", String(sel)); b.tabIndex = sel ? 0 : -1;
    document.getElementById(b.dataset.pestana).hidden = !sel;
  }
  document.getElementById("filtro-ano").value = estado.ano;
  document.getElementById("viendo").textContent = textoViendo();
  document.getElementById("quitar").disabled = estado.ano === "Todos";
  ({ direccion: dibujarDireccion, controller: dibujarController, contabilidad: dibujarContabilidad })[estado.pestana]();
  escribirDireccion();
}
function preparar() {
  const sel = document.getElementById("filtro-ano");
  for (const a of ["Todos", ...ANOS]) sel.append(el("option", { value: a }, a === "2026" ? "2026 (ene-jul)" : a));
  sel.addEventListener("change", () => { estado.ano = sel.value; pintar(); });
  document.getElementById("quitar").addEventListener("click", () => { estado.ano = "Todos"; pintar(); });
  const botones = [...document.querySelectorAll(".pestanas button")];
  botones.forEach((b, i) => {
    b.addEventListener("click", () => { estado.pestana = b.dataset.pestana; pintar(); });
    b.addEventListener("keydown", e => {
      if (e.key !== "ArrowRight" && e.key !== "ArrowLeft") return;
      const otro = botones[(i + (e.key === "ArrowRight" ? 1 : botones.length - 1)) % botones.length];
      estado.pestana = otro.dataset.pestana; pintar(); otro.focus();
    });
  });
  // Etiqueta al pasar el ratón y con el tabulador
  const tip = document.getElementById("etiqueta");
  const mostrar = (n, x, y) => {
    tip.textContent = n.getAttribute("data-tip"); tip.hidden = false;
    const r = tip.getBoundingClientRect();
    tip.style.left = Math.min(x + 12, innerWidth - r.width - 8) + "px";
    tip.style.top = (y + 16 + r.height > innerHeight ? y - r.height - 12 : y + 16) + "px";
  };
  document.addEventListener("pointermove", e => { const n = e.target.closest("[data-tip]"); if (n) mostrar(n, e.clientX, e.clientY); else tip.hidden = true; });
  document.addEventListener("focusin", e => { const n = e.target.closest("[data-tip]"); if (n) { const r = n.getBoundingClientRect(); mostrar(n, r.left, r.bottom); } else tip.hidden = true; });
  document.addEventListener("focusout", () => { tip.hidden = true; });
  document.addEventListener("keydown", e => { if (e.key === "Escape") tip.hidden = true; });
}

preparar();
leerDireccion();
cargar().then(pintar).catch(err => {
  document.querySelector("main").replaceChildren(el("p", { class: "error" }, "No se pudieron leer los datos: " + err.message + ". Si has abierto el fichero desde el disco, sírvelo con «python -m http.server» y abre http://localhost:8000."));
});
