# 🎵 Aplicación de Tour Musical 🎵

## 🚀 DescripcióndelProblema

Losamantesdelamúsicaamenudoseenfrentanadesafíosaltratardedescubriry
asistiraeventosyconciertosmusicales.Lainformaciónsobreestoseventospuede
estar dispersa yser difícil de encontrar. Además,la planificacióndela rutayel
horarioparaasistiravarioseventospuedesercomplejayconsumirmuchotiempo.

## 🎯 ObjetivodelProyecto

Desarrollarunaaplicacióndeescritorioquepermitaalosusuariosdescubrireventos
musicales, planificar rutas y compartir su experiencia de manera eficiente y
agradable.

## 💼 EstudiodelNegocio

Basándonos en nuestra comprensión de las necesidades del cliente, hemos
identificadolassiguientescaracterísticasclaveparalaaplicación:

## CaracterísticasPrincipales

**1. Índice de Eventos** 📑:Listadeeventosmusicales condetallesesenciales
    comoelnombredelevento,elartista,elgéneromusicalylaubicación.
**2. BúsquedayFiltrado deEventos** 🔍:Permitealosusuariosbuscareventos
    pornombre,géneroyartista,yfiltr areventosporubicaciónyhorario.
**3. MapayPlanificadodeRutas** 🗺:Visualizacióndelaubicacióndeloseventos
    en un mapa y unaherramienta paraplanificar rutas paraasistir avarios
    eventos.
**4. ReseñasyCalificaciones** ⭐:Losusuariospuedenescribirreseñasycalificar
    loseventosalosquehanasistido,proporcionandovaliososcomentariosa
    otrosusuarios.
**5. HistorialdeEventosAsistidos** 📖:Losusuariospuedenverunregistrodelos
    eventosalosquehanasistidoenelpasado.
**6. SeñaladordeÁnimodelComentario** 😃 **/** 😔:Losusuariospuedenindicarsisu
    comentariosobrelaexperienciaespositivoonegativo.
**7. Experiencia, Información que Puede Contener Spoilers** 󰡷: Los usuarios
    puedencompartirdetallessobresuexperienciaenelevento.


## CaracterísticasOpcionales

1. **CompartirenRedesSociales** 🚀:Permitealosusuarioscompartireventosy
    ubicacionesensusredessociales.
2. **DestacadodeEventosPróximos** 🕒:Resaltaloseventosqueestánapuntode
    comenzar.

## DiseñoUI

Paralainterfazdeusuario,buscamosundiseñolimpioymodernoquesealineecon
laestéticadeloseventosmusicales.

## Tipografía

Paralatipografía,proponemosusarunacombinacióndefuentesSansSerifparaun
aspectomodernoylimpio.Podemosusar **‘Roboto’** paralostítulosy **‘OpenSans’**
para el texto del cuerpo. Estas son legibles yse ven bienen una variedadde
tamañosdepantalla.

## PaletadeColores

Nuestrapaletadecoloresseinspiraenelmundodelamúsicaybuscaequilibrarla
energíaylacalma.Proponemoslossiguientescolores:

## PúrpuraOscuro ( #2F242C ) ♫ :Estecolorseutilizaráparalostítulosyeltexto

```
importante.Elpúrpuraoscuroesuncolorrelajantequetambiénproporciona
unbuencontrasteconelfondo.
```
## GrisClaro ( #E5E5E5 ) ♫ :Estecolorseutilizaráparaeltextodelcuerpoylos

```
fondosdelastarjetasdeeventos(siseutilizan).Elgrisclaroproporcionaalto
contrasteconelpúrpuraoscuro,loquefacilitalalectura.
```
## Amarillo (#E6D884 ) ♫ : Este color se utilizará para resaltar información

```
importanteybotonesinteractivos.Elamarilloesuncolorenérgicoqueatrae
laatencióndelusuario.
```
## Verde Claro ( #A1A892 ) ♫ : Este color se utilizará paralos bordes y los

```
elementosdelainterfazdeusuariosecundarios.Elverdeclaroproporciona
uncontrastesuaveconelblancoyelazuloscuro.
```

Seofrecelaposibilidaddeelegirunapaletaalternativaparatenerunaimagenmás
diferenciadautilizandositioscomo:

```
● http://colormind.io/
● https://coolors.co/
● https://colorhunt.co/
● https://realtimecolors.com/
```
## FlujodeUsuario

La pantalla principal contará con tres botones que separanlas secciones más
importantes de la aplicación. Estos son, el índice deeventos, laherramienta de
búsquedayfiltr adodeeventos,yelhistorialdeeventos.


Lasegundapantallaconopcionesesladelosdetallesdelevento.Aquíelusuario
tienelaposibilidaddeutilizarmapasparaubicarvisualmenteloseventos,yporotro
ladolasreviewsendondesepuedecalificaruneventodejandouncomentarioyel
estadodeánimorespectoaleventoasistido.

Elclientepropondráaplicacionesdefuncionamientosimilarparautilizarcomoguía
paraeldiseñodelainterfazgráficadelaaplicación.

Seproponelasiguienteestructuradeproyecto:

/raíz del proyecto
/views
archivos.pyquedefinenlainterfazconTkinter
/models
archivos.pyquedefinencadaunodelosmodelos
/data
archivos.jsonconlainformaciónalmacenada
/assets
recursosgráficoscomoimágenes,fuentes,íconos,etc.
main.py(Archivoprincipalqueiniciarálaaplicación)


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


