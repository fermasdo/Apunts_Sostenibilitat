# Sistema editorial de Sostenibilitat DAW

## Objectiu

Este projecte produïx apunts en valencià del mòdul professional 1708,
Sostenibilitat aplicada al sistema productiu, per a segon de CFGS DAW en règim
semipresencial a la Comunitat Valenciana durant el curs 2026-2027.

## Regles comunes

- Carrega la skill `sostenibilitat-daw-cv` abans de planificar, investigar,
  redactar o revisar materials.
- Tracta `referencies/marc-normatiu.md` com un registre inicial que s'ha de
  comprovar, no com un substitut de les normes oficials.
- Mantín separats els requisits oficials, les decisions pedagògiques i les
  decisions pròpies del centre.
- No inventes calendari de centre, ponderacions, dates d'examen, presencialitat,
  recursos disponibles ni coneixements previs de l'alumnat.
- Tota afirmació normativa, quantitativa o susceptible de canvi ha de ser
  traçable a una font identificada.
- No declares una unitat aprovada si `validacio.md` no marca com a `APTA` la
  mateixa revisió que figura en `apunts.md`.
- No uses contingut generat per un agent com a font primària. Verifica'l.

## Propietat dels artefactes

| Artefacte | Agent responsable |
| --- | --- |
| `materials/curs/pla-curs.md` | `coordinacio` |
| `materials/curs/matriu-curricular.md` | `documentalista` |
| `materials/curs/estat.yaml` | `coordinacio` |
| `materials/unitats/*/encarrec.md` | `coordinacio` |
| `materials/unitats/*/dossier.md` | `documentalista` |
| `materials/unitats/*/apunts.md` | `redaccio` |
| `materials/unitats/*/validacio.md` | `auditoria` |
| `materials/unitats/*/estat.yaml` | `coordinacio` |
| `mkdocs.yml`, `docs/**`, `scripts/**` | `mkdocs` |
| `docs/assets/**`, `materials/imatges/**`, `guia-estil-visual.md` | `disseny` |

Els agents no han de modificar artefactes assignats a un altre rol. Les
plantilles de `plantilles/` definixen el contracte mínim de cada artefacte.

## Flux obligatori

1. `coordinacio` crea un encàrrec complet i obri l'estat de la unitat.
2. `documentalista` prepara un dossier i només el declara `APTE` amb fonts
   suficients i vigents.
3. `redaccio` redacta exclusivament des d'un dossier `APTE`.
4. `auditoria` contrasta encàrrec, dossier i apunts, i emet `APTA` o `NO_APTA`.
5. `coordinacio` retorna cada incidència al propietari correcte i repetix
   l'auditoria. Després de dos cicles fallits, marca la unitat `bloquejada`.

Estats admesos: `pendent`, `documentant`, `documentada`, `redactant`,
`en-revisio`, `aprovada` i `bloquejada`.
