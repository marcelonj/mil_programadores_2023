# 🎵 Aplicación de Tour Musical 🎵

## 🚀 DescripcióndelProblema

Los amantes de la música a menudo se enfrentan a desafíos al tratar de descubrir y
asistir a eventos y conciertos musicales.
La información sobre estos eventos puede estar dispersa yser difícil de encontrar.
Además,la planificación de la ruta y el horario para asistir a varios eventos puede 
ser compleja y consumir mucho tiempo.

## 🎯 ObjetivodelProyecto

Desarrollar una aplicación de escritorio que permita a los usuarios descubrir eventos 
musicales, planificar rutas y compartir su experiencia de manera eficiente y agradable.

## 💼 EstudiodelNegocio

Basándonos en nuestra comprensión de las necesidades del cliente, hemos
Identificado las siguientes características clave para la aplicación

## CaracterísticasPrincipales

**1. Índice de Eventos** 📑:Lista de eventos musicales con detalles esenciales
como el nombre del evento, el artista, el género musical y la ubicación.
**2. BúsquedayFiltrado deEventos** 🔍:Permite a los usuarios buscar eventos.
   Por nombre, género y artista, y filtrar eventos por ubicación y horario.
**3. MapayPlanificadodeRutas** 🗺:Visualización de la ubicación de los eventos.
    en un mapa y unaherramienta paraplanificar rutas paraasistir avarios
    eventos.
**4. ReseñasyCalificaciones** ⭐:Los usuarios pueden escribir reseñas y calificar
los eventos a los que han asistido, proporcionando valiosos comentarios
    otrosusuarios.
**5. HistorialdeEventosAsistidos** 📖:Los usuarios pueden ver un registro de los
 eventos a los que han asistido en el pasado.
**6. SeñaladordeÁnimodelComentario** 😃 **/** 😔:Los usuarios pueden indicar si su 
comentario sobre la experiencia es positivo o negativo.
**7. Experiencia, Información que Puede Contener Spoilers** 󰡷: Los usuarios
    pueden compartir detalles sobre su experiencia en el evento.


## CaracterísticasOpcionales

1. **CompartirenRedesSociales** 🚀:Permite a los usuarios compartir eventos y
 ubicaciones en sus redes sociales.
2. **DestacadodeEventosPróximos** 🕒:Resalta los eventos que están a punto de 
comenzar.

## DiseñoUI

Para la interfaz de usuario, buscamos un diseño limpio y moderno que se alinee con
la estética de los eventos musicales.

## Tipografía

Para la tipografía, proponemos usar una combinación de fuentes Sans Serif para un aspecto
moderno y limpio. Podemos usar 'Roboto' para los títulos y 'OpenSans' para el texto 
del cuerpo. Estas son legibles y se ven bien en una variedad de tamaños de pantalla.

## PaletadeColores

Nuestra paleta de colores se inspira en el mundo de la música y busca equilibrar la energía y
la calma. Proponemos los siguientes colores:

## PúrpuraOscuro ( #2F242C ) ♫ Este color se utilizará para los títulos y el texto.

```
Importante. El púrpura oscuro es un color relajante que también proporciona un buen contraste
con el fondo.
```
## GrisClaro ( #E5E5E5 ) ♫ Este color se utilizará para el texto del cuerpo

```
Fondos de las tarjetas de eventos (si se utilizan). El gris claro proporciona alto contraste con
el púrpura oscuro, lo que facilita la lectura
```
## Amarillo (#E6D884 ) ♫ : Este color se utilizará para resaltar información

```
Importante y botones interactivos. El amarillo es un color energético que atrae la atención del usuario.
```
## Verde Claro ( #A1A892 ) ♫ : Este color se utilizará paralos bordes y los

```
Elementos de la interfaz de usuario secundarios. El verde claro proporciona un contraste suave con el
blanco y el azul oscuro
```

Se ofrece la posibilidad de elegir una paleta alternativa para tener una imagen más diferenciada
utilizando sitios como

```
● http://colormind.io/
● https://coolors.co/
● https://colorhunt.co/
● https://realtimecolors.com/
```
## FlujodeUsuario

La pantalla principal contará con tres botones que separan las secciones más importantes de la aplicación.
Estos son, el índice de eventos, la herramienta de búsqueda y filtrado de eventos, y el historial de eventos.


La segunda pantalla con opciones es la de los detalles del evento. Aquí, el usuario tiene la posibilidad de 
utilizar mapas para ubicar visualmente los eventos, y por otro lado, las reviews donde se puede calificar 
un evento dejando un comentario y el estado de ánimo respecto al evento asistido.

El cliente propondrá aplicaciones de funcionamiento similar para utilizar como guía para el diseño de la
interfaz gráfica de la aplicación

Se propone la siguiente estructura de proyecto:

/raíz del proyecto
/views
archivos.py que definen la interfaz con Tkinter
/models
archivos.py que definen cada uno de los modelos
/data
archivos.json con la información almacenada
/assets
recursos gráficos como imágenes, fuentes, íconos, etc.
main.py (Archivo principal que iniciará la aplicación)



## RequerimientosdeModelo

Los modelos principales propuestos a crear para almacenar los datos son los
siguientes.

### Evento

```
➔ id (int):Elidentificadorúnicodelevento.
➔ nombre (str):Elnombredelevento.
➔ artista (str):Elartistaobandaquepresentaelevento.
➔ genero (str):Elgéneromusicaldelevento.
➔ id_ubicacion (int):Elidentificadordellugardondesellevaacaboelevento.
➔ hora_inicio (str: datetime ISO 8601): Lahora en que comienza el evento,
almacenada como un string en formato ISO 8601. Ejemplo:
2023-07-04T09:00:00.
➔ hora_fin (str:datetimeISO8601):Lahoraenquefinalizaelevento.
➔ descripcion (str):Unabrevedescripcióndelevento.
➔ imagen (str): URL de la imagen del evento. Es posible utilizar
implementacionesalternativasconimágeneslocales.
```

### RutaVisita

```
➔ id (int):Elidentificadorúnicodelarutadevisita.
➔ nombre (str):Elnombredelarutadevisita.
➔ destinos (List[int]):Losidentificadoresdelosdestinosmusicalesqueforman
partedelarutadevisita.
```
### Ubicación

```
➔ id (int):Elidentificadorúnicodelaubicación.
➔ nombre (str):Elnombredelaubicación.
➔ direccion (str):Ladireccióndelaubicación.
➔ coordenadas (List[float]): Las coordenadas geográficas de la ubicación,
almacenadascomounalistadenúmerosflotantes.
```
### Usuario

```
➔ id (int):Elidentificadorúnicodelusuario.
➔ nombre (str):Elnombredelusuario.
➔ apellido (str):Elapellidodelusuario.
➔ historial_eventos (List[int]):UnalistadeIDsdeeventosalosquehaasistido
elusuario.
```
### Review

```
➔ id (int):Elidentificadorúnicodelareview.
➔ id_evento (int):ElIDdeleventoqueseestácalificando.
➔ id_usuario (int):ElIDdelusuarioqueescribiólareview.
➔ calificacion (int):La calificación del evento porparte del usuario, en una
escalade 1 a5.
➔ comentario (str):Elcomentariotextualsobreelevento.
➔ animo (str):Elánimodelcomentario,puedeser‘Positivo’o‘Negativo’.
```

## TecnologíasaUtilizar

```
● Archivos JSON paraalmacenardatos
● Tkinter parainterfazgráficadeescritorio
● CustomTkinter paraaplicarestiloalainterfaz
● TkinterMapView paraintegrarmapasalaaplicación
```
## MetodologíadeTrabajo

Elproyectotendráunmáximode 4 integrantesquetrabajaránenelproyecto.
Lastareas aimplementarestándisponibles enunaplantillade **Notion** lacualse
debeduplicaryasignartareasacadaintegrante.

Utilizaremos un tablero Kanban para realizar un seguimiento del avance de
proyectos.Elprofesordedicaráunespaciodelaclaseaconsultarconlosgrupos
unoporunoencuantoalavance.

Losestudiantestienenlaposibilidadderealizarsusreunionesenelservidoroficial
deAcademiaCIMNE-IBER. Allítambiéntendránel espaciodeforosparapublicar
consultasdemaneraasincrónicaparaserrespondidasporlosprofesores.

## EntregadelTrabajo

Elproyectoestará alojado enGitHubenunrepositorio.Allísetendráregistrosde
envíodecódigoporcadaunodelosintegrantesdelequipo.

Según disponibilidad de tiempo, la presentación del proyecto serealizará en la
últimasemanadejulioylasemanadeagosto(últimasemanadecursada).

Elcumplimientodelastareasmínimassupondrálaaprobacióndelcursodadoque
nohayundesafíosobreelcontenidodelMódulo5.


