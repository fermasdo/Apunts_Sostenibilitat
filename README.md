# Apunts de Sostenibilitat aplicada al sistema productiu

Sistema d'agents OpenCode per a elaborar materials del mòdul professional
`1708` amb enfocament CFGS DAW semipresencial, Comunitat Valenciana, curs
2026-2027.

## Agents

| Agent | Funció |
| --- | --- |
| `coordinacio` | Dirigix el flux, delega fases i controla les portes de qualitat. |
| `documentalista` | Verifica currículum, vigència normativa i fonts tècniques. |
| `redaccio` | Crea apunts autocontinguts i contextualitzats en DAW. |
| `auditoria` | Revisa de manera independent la correcció i la cobertura. |

## Ús

1. Reinicia OpenCode després d'instal·lar esta configuració.
2. Executa `/planifica-curs` i indica les dades reals del centre disponibles.
3. Executa `/unitat U01 titol-curt` per iniciar el flux complet d'una unitat.
4. Usa `/estat` o `/estat U01` per consultar el següent pas.
5. Usa `/revisa U01` per forçar una nova auditoria de la revisió actual.

Exemple:

```text
/planifica-curs Centre públic; Aules Semipresencial; sense dates d'examen confirmades
/unitat U01 sostenibilitat-i-asg-en-el-sector-tic
/estat U01
```

## Estructura

```text
.opencode/agent/       rols i permisos
.opencode/command/     ordres de treball
.opencode/skills/      criteris compartits
referencies/           registre inicial de normativa oficial
plantilles/            contractes dels artefactes
materials/curs/        pla, matriu curricular i estat global
materials/unitats/     dossiers, apunts i validacions per unitat
```

Les 34 hores de la seqüenciació DAW no equivalen automàticament a 34 sessions.
La distribució real depén del calendari i de la guia didàctica del centre.
