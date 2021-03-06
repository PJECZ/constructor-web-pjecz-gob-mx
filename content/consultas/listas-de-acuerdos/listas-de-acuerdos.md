Title: Listas de Acuerdos
Summary: Actuaciones que realiza diariamente el Poder Judicial del Estado de Coahuila de Zaragoza y que por ley de acuerdo al Código Procesal Civil deben de ser publicadas; en donde se incluyen autos, acuerdos, sentencias, exhortos y audiencias.
Slug: consultas-listas-de-acuerdos
URL: consultas/listas-de-acuerdos/
Save_As: consultas/listas-de-acuerdos/index.html
Date: 2020-05-11 16:00
Modified: 2020-05-20 12:32
JavaScripts: consultas-listas-de-acuerdos.js


<nav aria-label="breadcrumb">
<ol class="breadcrumb">
<li class="breadcrumb-item"><a href="../">Consultas</a></li>
<li class="breadcrumb-item active" aria-current="page">Listas de Acuerdos</li>
</ol>
</nav>

## Instrucciones

1. Favor de seleccionar el **Distrito Judicial** (lista desplegable con los 8 distritos incluyendo tribunales salas y pleno).
2. Seleccione el **Juzgado de la Materia,** donde encontará los de ese distrito.
3. Posteriormente presione el botón **Mostrar** y espere a que se carguen las listas de acuerdo. Esta opción las desplegará por fecha reciente.
4. Para buscar por fecha favor de ingresar en la opción **Filtrar** el Año–Mes-Dia que desee encontrar; por ejemplo **2020-05-20** es 20 de mayo 2020.
5. **Nota:** Si la lista de acuerdo de una fecha en particular no se encuentra en el listado favor de revisar con el juzgado correspondiente.

<div id="elegirListaDeAcuerdos" class="form-row mb-3">
<div class="col"><select id="distritoSelect"></select></div>
<div class="col"><select id="autoridadSelect"></select></div>
<div class="col"><button id="mostrarButton" type="button" class="btn btn-primary">Mostrar</button></div>
</div>

<table id="listaDeAcuerdos" class="table" style="width:100%">
<thead>
<th>Fecha</th>
<th>Descripción</th>
<th>Archivo</th>
</thead>
</table>
