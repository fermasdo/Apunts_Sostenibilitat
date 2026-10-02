# Guia d'estil visual — Sostenibilitat DAW

Revisió visual: **2026-08-04**.

## 1. Intenció i criteris

El sistema visual explica **sistemes, decisions, relacions i límits**. No usa
fulles, planetes, color verd ni fotografies genèriques com a prova de
sostenibilitat. Cada unitat ha de publicar **dos o tres fitxers diferents** amb
funció didàctica; repetir un fitxer en la capçalera i dins del contingut continua
sent un únic recurs i es considera una duplicació editorial.

- **Tinta:** `#0F172A`; **secundària:** `#334155`; **fons:** `#F8FAFC` i
  `#FFFFFF`; **procés i fletxes:** `#2563EB`; **suport:** `#DBEAFE`.
- El color reforça, però no codifica cap significat sense número, rètol, tipus de
  traç o posició en una seqüència.
- Tipografia sans-serif del sistema. En els SVG d'unitat revisats: `viewBox` de
  640 px d'amplària, títols de 34 px i text de 24–26 px. La composició vertical
  evita reduir cinc o huit targetes a una fila il·legible en mòbil.
- Fletxes blaves amb punta visible i passos numerats. Els bucles tenen una
  fletxa de retorn; els límits usen també contorn discontinu o un rètol.
- Tot SVG didàctic conserva `title`, `desc`, `metadata`, text real i `viewBox`;
  no usa text convertit en traços.
- El text alternatiu descriu la relació o conclusió útil, no els colors. El peu
  identifica funció, autoria, procedència i llicència.
- La figura complementa una llista, taula o explicació adjacent. No és la font
  única d'una instrucció, una dada, una obligació o una conclusió.

## 2. Manifest d'integració exacte

Les rutes següents partixen de `docs/unitats/*.md`. Els SVG originals són de
l'equip de disseny del projecte i es publiquen amb **CC0 1.0**.

### U01 — dos recursos

| Fitxer | Ubicació editorial exacta | Text alternatiu | Peu proposat | Funció didàctica | Llicència |
| --- | --- | --- | --- | --- | --- |
| `../assets/sostenibilitat/asg-materialitat.svg` | Secció **3.2. Procés inicial de materialitat**, després de l'esquema textual/alternativa de la figura 1 i abans de «La figura repetix la seqüència…». | `Procés inicial de materialitat en sis passos: delimitar el context, identificar grups d'interés, formular assumptes ASG, separar impactes riscos i oportunitats, prioritzar i seleccionar mètriques; la revisió de dades i límits pot canviar la prioritat.` | *Figura. Seqüència de treball per passar del context a mètriques revisables; la llista numerada adjacent n'és l'alternativa textual. Il·lustració original, equip de disseny del projecte, CC0 1.0.* | Organitzar el procés de materialitat sense convertir-lo en una puntuació automàtica. | CC0 1.0 |
| `../assets/sostenibilitat/u01-metrica-tracable.svg` | Secció **4.2. Com construir una mètrica reproduïble**, immediatament després de la llista de camps mínims i abans de la taula d'exemples. | `Fitxa d'una mètrica traçable en quatre blocs: finalitat, definició, context i traçabilitat; un indicador operatiu no prova per si sol un impacte final.` | *Figura. Llista de control per documentar una mètrica amb finalitat, definició, context, procedència i límits. Il·lustració original, equip de disseny del projecte, CC0 1.0.* | Permetre revisar si una mètrica conserva els camps que la fan interpretable. | CC0 1.0 |

### U02 — dos recursos

| Fitxer | Ubicació editorial exacta | Text alternatiu | Peu proposat | Funció didàctica | Llicència |
| --- | --- | --- | --- | --- | --- |
| `../assets/sostenibilitat/u02-frontera-servei-web.svg` | Secció **1. Delimita el servici abans d'opinar**, després de la cadena textual que acaba en «resposta» i de «L'esquema orienta, però no fixa una arquitectura universal», abans de «Pas a pas». | `Cadena del servici des de la necessitat de la persona fins a la resposta, dins d'una frontera declarada; cal indicar unitat funcional, estat de les dades i exclusions.` | *Figura. Mapa per declarar què s'inclou i què s'exclou en l'anàlisi d'un servici web; la cadena i els passos adjacents en són l'alternativa textual. Il·lustració original, equip de disseny del projecte, CC0 1.0.* | Evitar analitzar només el codi o canviar la frontera durant la comparació. | CC0 1.0 |
| `../assets/sostenibilitat/u02-cadena-diagnostic.svg` | Secció **2. Relaciona reptes, activitat i efectes**, després de la cadena textual `activitat o decisio -> ... -> limit o evidencia` i abans de «Pas a pas». | `Cadena de diagnòstic en cinc passos: activitat o decisió, recurs o relació, impacte potencial, persones i sectors afectats, i evidència o límit; acaba en una mesura amb responsable i seguiment.` | *Figura. Bastida per connectar un repte ambiental o social amb afectacions, evidència i una mesura inicial. Il·lustració original, equip de disseny del projecte, CC0 1.0.* | Convertir una llista de reptes en un diagnòstic causal i prudent. | CC0 1.0 |

### U03 — dos recursos

| Fitxer | Ubicació editorial exacta | Text alternatiu | Peu proposat | Funció didàctica | Llicència |
| --- | --- | --- | --- | --- | --- |
| `../assets/sostenibilitat/u03-accio-verificable.svg` | Al començament de **3. De la intenció a l'acció verificable**, després del primer paràgraf definitori i abans de la taula «Camp / Pregunta». Mantindre una sola inserció. | `Seqüència de cinc passos des d'una decisió DAW fins a una acció verificable: justificar repte afectació i meta, delimitar l'acció, conservar línia base i evidència, i declarar límits; risc i oportunitat condicionada queden separats.` | *Figura. Guia per justificar una meta ODS i transformar-la en una acció comprovable sense confondre risc amb benefici garantit. Il·lustració original, equip de disseny del projecte, CC0 1.0.* | Fer visible la cadena decisió–meta–acció–evidència i els límits. | CC0 1.0 |
| `../assets/context-wikimedia/u03-accessible-keyboard.jpg` | **Cas guiat DAW**, immediatament abans de «Situació hipotètica». | `Mà d'una persona amb baixa visió sobre un teclat d'alt contrast.` | *Fotografia de context per a l'anàlisi d'una barrera de teclat. Francisclarke, 2016, [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?title=File:Hand-on-high-contrast-accessible-computer-keyboard.jpg&oldid=1211953052), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); còpia local redimensionada, sense retall.* | Situar l'accessibilitat com una relació entre persones, tasques i decisions DAW, no com una etiqueta ODS. | CC BY-SA 4.0 |

### U04 — dos recursos

| Fitxer | Ubicació editorial exacta | Text alternatiu | Peu proposat | Funció didàctica | Llicència |
| --- | --- | --- | --- | --- | --- |
| `../assets/sostenibilitat/u04-decisio-ecodisseny.svg` | Secció **4.1. Registre d'una decisió d'ecodisseny**, després de la taula de l'exemple breu i abans del paràgraf sobre memòria cau HTTP. Mantindre una sola inserció. | `Registre d'ecodisseny en cinc passos: problema, decisió, criteri, prova i límit; la comparació conserva funció, frontera i mètode.` | *Figura. Llista de control per justificar i provar una decisió d'ecodisseny sense atribuir-li un impacte final no mesurat. Il·lustració original, equip de disseny del projecte, CC0 1.0.* | Evitar propostes sense problema observat, prova o salvaguarda. | CC0 1.0 |
| `../assets/sostenibilitat/cicle-vida-servei-web.svg` | Secció **5.1. Mapa textual accessible**, després del text alternatiu proposat i abans de **5.2. Fitxa d'anàlisi qualitativa**. | `Cicle de vida d'un servici web en set fases: concepció, disseny, desenrotllament, infraestructura i desplegament, transferència i ús, manteniment i retirada; la interpretació manté funció, frontera i dades pendents visibles.` | *Figura. Bucle qualitatiu del cicle de vida del servici web; la llista ordenada anterior és l'alternativa textual completa. Il·lustració original, equip de disseny del projecte, CC0 1.0.* | Ajudar a detectar trasllats d'impacte entre fases sense presentar la figura com una ACV. | CC0 1.0 |

### U05 — tres recursos

| Fitxer | Ubicació editorial exacta | Text alternatiu | Peu proposat | Funció didàctica | Llicència |
| --- | --- | --- | --- | --- | --- |
| `../assets/sostenibilitat/u05-auditoria-proxy-impacte.svg` | Final de **2.4. Del rendiment a l'impacte: un límit essencial**, després de «Un resultat parcial s'ha d'anomenar parcial» i abans de **2.5. Impacte personal i professional**. | `Dos recorreguts d'una auditoria compartixen funció, unitat, frontera, línia base i mètode: un registra inventari i indicadors intermedis; l'altre avalua impactes amb dades, absències, incertesa i una conclusió delimitada.` | *Figura. Separació entre proxies de rendiment i avaluació d'impactes; el text d'U05 conserva els camps i límits complets. Il·lustració original, equip de disseny del projecte, CC0 1.0.* | Impedir la conversió automàtica de bytes, peticions o temps en impactes finals. | CC0 1.0 |
| `../assets/sostenibilitat/u05-flux-auditoria-millora.svg` | Activitat asíncrona, al començament de **6.3. Passos**, abans de la llista numerada. | `Flux d'auditoria en sis passos: fixar funció i unitat funcional, declarar límit i exclusions, registrar línia base i procedència, comparar amb el mateix mètode, proposar accions amb salvaguardes i revisar seguiment, rebot i final de vida.` | *Figura. Vista general del procés que l'activitat desplega pas a pas; la llista numerada és l'alternativa textual completa. Il·lustració original, equip de disseny del projecte, CC0 1.0.* | Servir de mapa de treball per a una activitat llarga i semipresencial. | CC0 1.0 |
| `../assets/context-wikimedia/u05-ewaste-recycling.jpg` | **Cas guiat DAW: optimització d'un formulari i retirada d'un monitor**, immediatament abans de **5.1. Enunciat i dades**. | `Components d'aparells electrònics separats en una mostra sobre reciclatge.` | *Fotografia de context sobre final de vida d'equips. Syced, 2024, [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?title=File:Electronic_junk_separation_in_view_of_recycling.jpg&oldid=956498563), [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/); còpia local redimensionada, sense retall.* | Recordar que RAEE es referix a equips materials i no al codi o a les dades. | CC0 1.0 |

### U06 — dos recursos

| Fitxer | Ubicació editorial exacta | Text alternatiu | Peu proposat | Funció didàctica | Llicència |
| --- | --- | --- | --- | --- | --- |
| `../assets/sostenibilitat/u06-pla-tracable.svg` | Secció **1. De la llista d'assumptes al pla coherent**, després de la llista de set passos i abans del paràgraf que comença «ESRS 1 diferencia…». Mantindre una sola inserció. | `Traça d'un pla de sostenibilitat: grups d'interés, aspecte ASG, anàlisi d'impacte risc o oportunitat, acció, indicador i informe equilibrat; la revisió torna al diagnòstic.` | *Figura. Cadena de traçabilitat des dels grups fins a l'informe, amb omissions i límits visibles. Il·lustració original, equip de disseny del projecte, CC0 1.0.* | Comprovar que cada acció i indicador respon a una anàlisi prèvia. | CC0 1.0 |
| `../assets/sostenibilitat/pla-sostenibilitat-web.svg` | Secció **6.1. Prova contra el blanqueig ecològic**, després de la llista de comprovacions i abans de «Substituïx “els nostres webs són verds”…». | `Bucle de huit passos d'un pla: delimitar, escoltar, analitzar, prioritzar, actuar, mesurar, informar i revisar; una mètrica necessita abast, font, període i incertesa.` | *Figura. Bucle de revisió per comprovar el pla i les afirmacions abans de publicar-les. Il·lustració original, equip de disseny del projecte, CC0 1.0.* | Fer visible que informar no tanca el procés i que la revisió pot canviar prioritats. | CC0 1.0 |

## 3. Duplicacions i insercions que s'han de retirar

Auditoria de `docs/unitats/*.md` en la revisió publicada actual:

| Unitat | Duplicació o recurs prescindible detectat | Acció exacta per a la integració |
| --- | --- | --- |
| U01 | `u01-metrica-tracable.svg` apareix en la capçalera (línia actual 15) i en 4.3 (línia actual 575). | Eliminar la inserció de capçalera; moure/conservar una sola inserció en 4.2 segons el manifest. Afegir `asg-materialitat.svg`. |
| U02 | No hi ha fitxer duplicat. La foto genèrica `u02-people-using-laptops.jpg` de capçalera i `u02-optic-fiber.jpg` no expliquen una decisió del diagnòstic. | Eliminar les dos insercions, no comptar-les com a recursos i integrar només els dos SVG del manifest. No esborrar encara els JPG mentre hi haja referències publicades. |
| U03 | `u03-accio-verificable.svg` apareix en la capçalera (línia actual 15) i en la secció 3 (línia actual 420). | Eliminar la inserció de capçalera i mantindre una sola inserció didàctica en la secció 3. Mantindre la fotografia del teclat en el cas. |
| U04 | `u04-decisio-ecodisseny.svg` apareix en la capçalera (línia actual 15) i en 4.1 (línia actual 498). | Eliminar la inserció de capçalera, mantindre la de 4.1 i afegir el cicle de vida en 5.1. |
| U05 | `u05-auditoria-proxy-impacte.svg` apareix en la capçalera (línia actual 15) i en 2.5 (línia actual 494). | Eliminar la inserció de capçalera; moure/conservar una sola inserció al final de 2.4. Afegir el flux d'auditoria en 6.3 i mantindre la fotografia RAEE. |
| U06 | `u06-pla-tracable.svg` apareix en la capçalera (línia actual 15) i en la secció 1 (línia actual 310). | Eliminar la inserció de capçalera, mantindre la de la secció 1 i afegir el bucle de revisió en 6.1. |

`ods-decisio-accio-evidencia.svg` **no s'ha d'integrar en U03**: solapa la
mateixa cadena que `u03-accio-verificable.svg` amb menys camps. Es conserva com
un recurs anterior no seleccionat, igual que les fotografies contextuals no
incloses en este manifest. `portada-sostenibilitat-daw.svg` és només la portada
general del curs i no compta per a cap unitat.

## 4. Patró MkDocs

```md
<div class="recurs-visual" markdown="1">

![TEXT ALTERNATIU EXACTE](../assets/sostenibilitat/FITXER.svg)

*PEU EXACTE DEL MANIFEST*

</div>
```

Per a les fotografies, canvia només la subcarpeta a `context-wikimedia`. No uses
el mateix recurs com a `unitat-hero`. Les figures verticals no s'han de forçar a
una altura fixa; `max-width: 100%` i `height: auto` han de conservar la relació
d'aspecte. En escriptori es pot limitar l'amplària visual a 720 px i centrar-les.

## 5. Traçabilitat de fotografies seleccionades

| Fitxer local | Original i revisió consultada | Autoria i data | Llicència | Transformació local | Verificació |
| --- | --- | --- | --- | --- | --- |
| `docs/assets/context-wikimedia/u03-accessible-keyboard.jpg` | [Wikimedia Commons, oldid 1211953052](https://commons.wikimedia.org/w/index.php?title=File:Hand-on-high-contrast-accessible-computer-keyboard.jpg&oldid=1211953052) | Francisclarke, 28-11-2016 | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) | Redimensionada a 1400 × 1048 px, sense retall ni alteració de contingut. | Autoria, descripció i llicència comprovades el 04-08-2026. |
| `docs/assets/context-wikimedia/u05-ewaste-recycling.jpg` | [Wikimedia Commons, oldid 956498563](https://commons.wikimedia.org/w/index.php?title=File:Electronic_junk_separation_in_view_of_recycling.jpg&oldid=956498563) | Syced, 10-02-2024 | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) | Redimensionada a 1400 × 1054 px, sense retall ni alteració de contingut. | Autoria, descripció i llicència comprovades el 04-08-2026. |

La fotografia de teclat requerix atribució, enllaç a la llicència i indicació de
la redimensió. No suggerix que l'autoria avala el material. La fotografia de
RAEE és CC0, però es conserva el crèdit per traçabilitat.

### Fotografies existents no seleccionades per al manifest

Es conserva el registre anterior perquè els fitxers encara existixen i dos
d'ells apareixen en la publicació actual d'U02. S'han de retirar les insercions
segons l'apartat 3; estos recursos no compten en l'inventari final.

| Fitxer local | Font original | Autoria | Llicència | Estat editorial |
| --- | --- | --- | --- | --- |
| `docs/assets/context-wikimedia/u02-optic-fiber.jpg` | <https://commons.wikimedia.org/wiki/File:Fujikura_optic_fiber_at_Science_Museum.jpg> | Syced | CC0 1.0 | No integrar: context físic sense una decisió observable. |
| `docs/assets/context-wikimedia/u02-fiber-connectors.jpg` | <https://commons.wikimedia.org/wiki/File:Optical_fiber_connectors-optical_patch_cable-01ASD.jpg> | Asurnipal | CC BY-SA 4.0 | No integrar. |
| `docs/assets/context-wikimedia/u02-people-using-laptops.jpg` | <https://commons.wikimedia.org/wiki/File:People_using_laptops.jpg> | mdemon | CC BY-SA 2.0 | Retirar de la capçalera: fotografia genèrica i decorativa per a l'objectiu d'U02. |
| `docs/assets/context-wikimedia/u02-data-center-unc.jpg` | <https://commons.wikimedia.org/wiki/File:Data_Center_2_(UNC).jpg> | Ana Las Heras | CC BY-SA 4.0 | No integrar. |

La procedència d'estos quatre fitxers constava en el registre visual anterior
amb data de consulta 04-08-2026. No s'han modificat en esta revisió.

## 6. Control tècnic abans de publicar

1. Validar XML de tots els SVG amb `xmllint --noout`.
2. Comprovar automàticament `viewBox`, `title`, `desc`, `metadata`, text real i
   absència d'elements `image`, `script` o enllaços externs en els SVG originals.
3. Renderitzar els SVG seleccionats a 640 px i 320 px. Revisar que no hi haja text
   tallat, solapaments, targetes fora del `viewBox` ni fletxes sense punta.
4. Comprovar contrast: tinta sobre blanc/fons clar, blanc sobre blau nit i traç
   blau sobre fons clar. Cap categoria es deduïx només del color.
5. Comprovar els JPG amb `file` i `sips`: dimensions, format i pes. Objectiu de
   publicació: màxim 1400 px en el costat llarg i pes orientatiu inferior a
   400 KiB per fotografia contextual.
6. Executar la construcció estricta de MkDocs i revisar a amplàries de 320 px i
   d'escriptori. Verificar també que cada fitxer apareix una sola vegada en la
   unitat indicada.

## 7. Mini guia d'icones de Material for MkDocs

| Apartat | Icona Markdown |
| --- | --- |
| Orientació | `:material-compass-outline:` |
| Cas guiat | `:material-school-outline:` |
| Activitat | `:material-clipboard-edit-outline:` |
| Autoavaluació | `:material-check-decagram-outline:` |
| Resum | `:material-text-box-check-outline:` |
| Annex | `:material-folder-information-outline:` |
| Glossari | `:material-book-open-variant:` |
| Referències | `:material-link-variant:` |

No poses icones en encapçalaments numerats, usa'n una com a màxim per
encapçalament i no les convertisques en l'única indicació del tipus de secció.
