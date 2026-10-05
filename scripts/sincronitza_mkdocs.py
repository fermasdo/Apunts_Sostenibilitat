#!/usr/bin/env python3
"""Genera la capa MkDocs navegable a partir dels materials editorials.

No edita els originals. Les còpies de ``docs/`` es regeneren en cada execució.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
MATERIALS = ROOT / "materials"
DOCS = ROOT / "docs"
VISUAL_GUIDE = ROOT / "guia-estil-visual.md"
UNITS = ("U01", "U02", "U03", "U04", "U05", "U06")
EXPECTED_VISUAL_COUNTS = {
    "U01": 2,
    "U02": 2,
    "U03": 2,
    "U04": 2,
    "U05": 3,
    "U06": 2,
}
UNIT_TITLES = {
    "U01": "La sostenibilitat en les organitzacions",
    "U02": "Reptes ambientals i socials",
    "U03": "Els ODS en l'acompliment professional i personal",
    "U04": "Economia verda i circular",
    "U05": "Activitats sostenibles i medi ambient",
    "U06": "El pla de sostenibilitat",
}
PUBLIC_UNIT_TITLES = {
    "Sostenibilitat, marcs i criteris ASG": "La sostenibilitat en les organitzacions",
    "Reptes ambientals i socials del sector digital": "Reptes ambientals i socials",
    "ODS i exercici professional en DAW": "Els ODS en l'acompliment professional i personal",
    "Economia circular i ecodisseny de servicis web": "Economia verda i circular",
    "Pràctiques sostenibles en el cicle de vida web": "Activitats sostenibles i medi ambient",
    "Pla de sostenibilitat d'una empresa web": "El pla de sostenibilitat",
}


def section(text: str, heading_pattern: str) -> tuple[str, str] | None:
    """Extrau una secció de nivell 2 sense reescriure el seu contingut."""
    match = re.search(rf"(?ms)^(## {heading_pattern}.*?)(?=^## |\Z)", text)
    if match is None:
        return None
    return match.group(0), text[:match.start()] + text[match.end():]


def unit_learning_guide() -> str:
    """Afig només orientació de navegació a la còpia publicada."""
    return """
<div class="guia-progresiva" markdown="1">

## Com treballar esta unitat

<p class="lectura-clau"><strong>Primer, orienta't; després, practica.</strong>
No cal memoritzar els detalls abans de saber quin producte elaboraràs.</p>

<div class="passos-lectura" markdown="1">

1. **Orientació.** Consulta el propòsit, els prerequisits i el temps orientatiu.
2. **Idees clau.** Llig els blocs de contingut i contrasta'ls amb el cas guiat.
3. **Acció.** Revisa l'activitat i els criteris d'èxit abans de començar el producte.
4. **Comprovació.** Respon l'autoavaluació i obri el solucionari després.

</div>

> **Per a avançar:** conserva els dubtes i usa la proposta de tutoria o el treball
> autònom equivalent. El canal docent concret l'ha de confirmar el centre.

</div>

La informació curricular, la traçabilitat i les referències completes es pot
consultar al final de la pàgina en seccions desplegables.
"""


def insert_learning_guide(text: str) -> str:
    """Situa l'orientació i el resum literal abans del desenrotllament."""
    match = re.search(r"(?m)^# .+$", text)
    if match is None:
        raise RuntimeError("No s'ha localitzat el títol principal de la unitat")
    summary = section(text, r"(?:\d+\. )?Resum")
    if summary is not None:
        summary_text, text = summary
        # El resum és contingut original: només se'n canvia la posició per oferir
        # una entrada ràpida abans del desenvolupament complet.
        quick_start = (
            "\n> **Idees clau per començar.** Este resum procedeix literalment del "
            "material de la unitat; el desenrotllament complet apareix més avall.\n\n"
            + summary_text
        )
        match = re.search(r"(?m)^# .+$", text)
        assert match is not None
    else:
        quick_start = ""
    return text[:match.end()] + "\n" + unit_learning_guide() + quick_start + text[match.end():]


def reorganize_unit(text: str) -> str:
    """Desplaça la informació curricular i docent a un annex de la còpia publicada.

    Els fragments es traslladen literalment: no se n'altera el text, les cites,
    les taules ni les capçaleres internes.
    """
    extracted: list[str] = []
    for pattern in (
        r"(?:\d+\. )?Orientació",
        r"(?:\d+\. )?Resultat(?:s)? i criteris treballats",
        r"(?:\d+\. )?Mapa de traçabilitat",
    ):
        result = section(text, pattern)
        if result is not None:
            fragment, text = result
            # L'encapçalament passa a ser fill semàntic de l'annex; el text es
            # conserva de manera literal.
            extracted.append(fragment.replace("## ", "### ", 1))

    if extracted:
        annex = (
            "\n\n<details class=\"publicacio-desplegable curricular\" markdown=\"1\">\n"
            "<summary>Informació curricular i traçabilitat</summary>\n\n"
            + "\n\n".join(extracted)
            + "\n\n</details>"
        )
        reference = re.search(r"(?m)^## (?:\d+\. )?Referències\b", text)
        if reference is None:
            text += annex
        else:
            text = text[:reference.start()] + annex + "\n\n" + text[reference.start():]
    return text


def collapse_section(text: str, heading_pattern: str, summary: str) -> str:
    """Conserva una secció literal dins d'un desplegable semàntic."""
    result = section(text, heading_pattern)
    if result is None:
        return text
    fragment, remaining = result
    # Manté un encapçalament cercable dins del contingut desplegable, sense crear
    # un segon títol de primer nivell en la pàgina publicada.
    fragment = fragment.replace("## ", "### ", 1)
    folded = (
        f"<details class=\"publicacio-desplegable\" markdown=\"1\">\n"
        f"<summary>{summary}</summary>\n\n{fragment}\n\n</details>"
    )
    insertion = re.search(r"(?m)^## Informació curricular i traçabilitat|^<details class=\"publicacio-desplegable curricular\"", remaining)
    if insertion is None:
        return remaining.rstrip() + "\n\n" + folded + "\n"
    return remaining[:insertion.start()].rstrip() + "\n\n" + folded + "\n\n" + remaining[insertion.start():]


def progressive_disclosure(text: str) -> str:
    """Plecs no essencials sense eliminar-los del HTML ni de la cerca."""
    text = collapse_section(text, r"(?:\d+\. )?Solucionari raonat", "Solucionari raonat (obri'l després de respondre)")
    text = collapse_section(text, r"(?:\d+\. )?Glossari", "Glossari de consulta")
    text = collapse_section(text, r"(?:\d+\. )?Referències\b", "Referències completes i fonts")
    return text


def callout_kind(label: str) -> str:
    normalized = label.lower()
    if "pas a pas" in normalized or "pregunta de control" in normalized:
        return "question"
    if "error habitual" in normalized:
        return "warning"
    if "exemple" in normalized:
        return "example"
    if "idea clau" in normalized or "clau del cas" in normalized or "per a avançar" in normalized:
        return "tip"
    return "note"


def quote_block_to_admonition(block: str) -> str:
    lines = [re.sub(r"^>\s?", "", line) for line in block.splitlines()]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    if not lines:
        return block
    first = lines[0].strip()
    match = re.match(r"^\*\*(.+?)\*\*\s*:?\s*(.*)$", first)
    if match is None:
        return block
    label = match.group(1).strip()
    first_body = match.group(2).strip()
    body = ([first_body] if first_body else []) + lines[1:]
    while body and not body[0].strip():
        body.pop(0)
    kind = callout_kind(label)
    title = label.rstrip(".")
    if not body:
        return f'!!! {kind} "{title}"\n'
    indented = "\n".join((f"    {line}" if line.strip() else "") for line in body)
    return f'!!! {kind} "{title}"\n{indented}\n'


def materialize_admonitions(text: str) -> str:
    """Converteix avisos pedagògics en admonitions de MkDocs Material."""
    lines = text.splitlines()
    output: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.startswith(">"):
            output.append(line)
            i += 1
            continue

        block_lines = [line]
        i += 1
        while i < len(lines) and lines[i].strip():
            current = lines[i]
            if current.startswith(">"):
                block_lines.append(current)
                i += 1
                continue
            if current.lstrip().startswith(("##", "#", "- ", "* ", "|", "```", "!!! ", "<")):
                break
            # Continuació laxa de blockquote en Markdown.
            block_lines.append("> " + current)
            i += 1

        converted = quote_block_to_admonition("\n".join(block_lines)).rstrip("\n")
        output.append(converted)

    return "\n".join(output)


ICON_HEADING_RULES = (
    ("orientació", ":material-compass-outline:"),
    ("cas guiat", ":material-school-outline:"),
    ("activitat central", ":material-clipboard-edit-outline:"),
    ("activitats d'aprenentatge", ":material-clipboard-edit-outline:"),
    ("autoavaluació", ":material-check-decagram-outline:"),
    ("resum", ":material-text-box-check-outline:"),
    ("annex", ":material-folder-information-outline:"),
    ("glossari", ":material-book-open-variant:"),
    ("referències", ":material-link-variant:"),
)


def icon_for_heading(title: str) -> str | None:
    normalized = title.lower().strip()
    for token, icon in ICON_HEADING_RULES:
        if token in normalized:
            return icon
    return None


def decorate_non_numbered_headings(text: str) -> str:
    """Afig icones als apartats principals no numerats, reutilitzables entre unitats."""
    decorated: list[str] = []
    for line in text.splitlines():
        match = re.match(r"^(## )(.+)$", line)
        if match is None:
            decorated.append(line)
            continue

        title = match.group(2).strip()
        if re.match(r"^\d+[\.)]?\s", title):
            decorated.append(line)
            continue
        if title.startswith(":material-"):
            decorated.append(line)
            continue

        icon = icon_for_heading(title)
        if icon is None:
            decorated.append(line)
            continue
        decorated.append(f"{match.group(1)}{icon} {title}")
    return "\n".join(decorated)


def course_itinerary(plan_text: str) -> str:
    result = section(plan_text, r"Seqüència d'unitats")
    if result is None:
        raise RuntimeError("No s'ha localitzat la seqüència d'unitats del pla")
    sequence, _ = result
    # La planificació conserva títols de treball interns; la publicació mostra la
    # denominació de les unitats comunicada a l'alumnat en la fitxa del mòdul.
    for internal_title, public_title in PUBLIC_UNIT_TITLES.items():
        sequence = sequence.replace(f"| {internal_title} |", f"| {public_title} |")
    return (
        "<!-- Fitxer generat per scripts/sincronitza_mkdocs.py; no l'edites manualment. -->\n"
        "# Itinerari i càrrega orientativa\n\n"
        "Consulta les unitats en este ordre. Les hores són una estimació de treball, "
        "no sessions ni dates del centre.\n\n"
        + sequence
    )


def publication_status(statuses: dict[str, str]) -> str:
    rows = []
    for unit in UNITS:
        source = MATERIALS / "unitats" / unit / "apunts.md"
        source_revision = yaml_value(source.read_text(encoding="utf-8"), "revision") or "no indicada"
        unit_state = yaml_value(statuses[unit], "estat") or "no indicat"
        gate = yaml_value(statuses[unit], "porta_superada") or "no indicada"
        audited_revision = yaml_value(statuses[unit], "revision_auditada") or "no indicada"
        rows.append(
            f"| {unit} | `{unit_state}` | `{gate}` | `{source_revision}` | `{audited_revision}` |"
        )
    return "\n".join((
        "<!-- Fitxer generat per scripts/sincronitza_mkdocs.py; no l'edites manualment. -->",
        "# Estat de publicació",
        "",
        "Esta pàgina mostra metadades tècniques de les fonts. No modifica ni "
        "interpreta els estats editorials o d'auditoria.",
        "",
        "| Unitat | Estat de la unitat | Porta registrada | Revisió font (`apunts.md`) | Revisió auditada |",
        "| --- | --- | --- | --- | --- |",
        *rows,
    )) + "\n"

def yaml_value(text: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*([^#\n]+)", text)
    return match.group(1).strip().strip('"\'') if match else None


def publication_notice(source: Path, source_text: str, status_text: str | None) -> str:
    source_status = yaml_value(source_text, "estat")
    draft = source_status == "esborrany"
    pending_audit = status_text is not None and yaml_value(status_text, "porta_superada") != "G4"
    if draft or pending_audit:
        reasons = []
        if draft:
            reasons.append("l'artefacte d'origen està marcat com a esborrany")
        if pending_audit:
            reasons.append("no consta la porta G4 en l'estat de la unitat")
        return (
            "\n> **Avís de publicació.** Esta còpia prové d'un material editorial "
            f"per al qual {' i '.join(reasons)}. "
            "La publicació no modifica l'estat ni el contingut de l'original.\n"
        )
    return ""


def normalize_unit_asset_paths(text: str) -> str:
    """Adapta només les rutes d'assets de la font a la ubicació en ``docs``."""
    return text.replace("../../../docs/assets/", "../assets/")


def use_public_unit_title(text: str, unit: str) -> str:
    """Mostra a l'alumnat el títol de la fitxa, sense alterar la font editorial."""
    return re.sub(
        rf"(?m)^# {unit}\. .+$",
        f"# {unit}. {UNIT_TITLES[unit]}",
        text,
        count=1,
    )


def visual_manifest() -> dict[str, list[tuple[str, str, str, str]]]:
    """Llig del manifest visual les rutes, els alts, els peus i les llicències."""
    guide = VISUAL_GUIDE.read_text(encoding="utf-8")
    manifest: dict[str, list[tuple[str, str, str, str]]] = {}
    for unit in UNITS:
        section_match = re.search(
            rf"(?ms)^### {unit}\b.*?\n(?P<body>.*?)(?=^### U\d\d\b|^## 3\.)",
            guide,
        )
        if section_match is None:
            raise RuntimeError(f"No s'ha localitzat el manifest visual de {unit}")
        entries: list[tuple[str, str, str, str]] = []
        for line in section_match.group("body").splitlines():
            if not line.startswith("| `"):
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) != 6:
                raise RuntimeError(f"Fila no interpretable en el manifest visual de {unit}")
            path = cells[0].strip("`")
            alt = cells[2].strip("`")
            caption = cells[3]
            licence = cells[5]
            entries.append((path, alt, caption, licence))
        expected_count = EXPECTED_VISUAL_COUNTS[unit]
        if len(entries) != expected_count:
            raise RuntimeError(
                f"El manifest de {unit} conté {len(entries)} recursos; "
                f"se n'esperaven {expected_count}"
            )
        manifest[unit] = entries
    return manifest


def verify_unit_visuals(
    unit: str,
    text: str,
    manifest: dict[str, list[tuple[str, str, str, str]]],
) -> None:
    """Comprova que la còpia publica una sola vegada el manifest, amb crèdits."""
    if "../../../docs/assets/" in text:
        raise RuntimeError(f"{unit} conserva una ruta d'asset pròpia de materials")
    if "unitat-hero" in text:
        raise RuntimeError(f"{unit} conté una imatge hero no permesa")

    references = re.findall(r"!\[[^]]*\]\((\.\./assets/[^)\s]+)\)", text)
    expected_paths = [entry[0] for entry in manifest[unit]]
    if sorted(references) != sorted(expected_paths):
        raise RuntimeError(
            f"Inventari visual incorrecte en {unit}: {references!r}; "
            f"s'esperava {expected_paths!r}"
        )
    if len(set(references)) != EXPECTED_VISUAL_COUNTS[unit]:
        raise RuntimeError(f"{unit} conté recursos visuals duplicats")

    visual_blocks = re.findall(
        r'(?ms)<div class="recurs-visual" markdown="1">\s*(.*?)\s*</div>',
        text,
    )
    for path, alt, caption, licence in manifest[unit]:
        image = f"![{alt}]({path})"
        matching_blocks = [block for block in visual_blocks if image in block]
        if len(matching_blocks) != 1:
            raise RuntimeError(f"{unit}: falta un bloc únic amb alt exacte per a {path}")
        block = matching_blocks[0]
        if caption not in block or licence not in caption:
            raise RuntimeError(f"{unit}: peu o llicència incorrectes per a {path}")
        asset = (DOCS / "unitats" / path).resolve()
        if not asset.is_file():
            raise RuntimeError(f"{unit}: no existix l'asset publicat {path}")

    if unit == "U02" and re.search(
        r"\.\./assets/context-wikimedia/u02-[^)\s]+\.jpg",
        text,
    ):
        raise RuntimeError("U02 conserva una fotografia descartada pel manifest visual")


def copy_markdown(
    source: Path,
    destination: Path,
    status_text: str | None = None,
    unit: str | None = None,
    manifest: dict[str, list[tuple[str, str, str, str]]] | None = None,
) -> None:
    text = source.read_text(encoding="utf-8")
    if unit is not None:
        text = normalize_unit_asset_paths(text)
        text = use_public_unit_title(text, unit)
        text = reorganize_unit(text)
        text = progressive_disclosure(text)
        text = insert_learning_guide(text)
        text = materialize_admonitions(text)
        text = decorate_non_numbered_headings(text)
        verify_unit_visuals(unit, text, manifest or visual_manifest())
    destination.parent.mkdir(parents=True, exist_ok=True)
    generated = "<!-- Fitxer generat per scripts/sincronitza_mkdocs.py; no l'edites manualment. -->\n"
    notice = publication_notice(source, text, status_text)
    if text.startswith("---\n"):
        front_matter_end = text.find("\n---\n", 4)
        if front_matter_end != -1:
            front_matter_end += len("\n---\n")
            text = text[:front_matter_end] + generated + notice + text[front_matter_end:]
        else:
            text = generated + notice + text
    else:
        text = generated + notice + text
    destination.write_text(text, encoding="utf-8")


def verify_approval_contract(unit: str, status_text: str) -> None:
    """Evita publicar G4 si no coincidixen font, estat i validació canònica."""
    source_text = (MATERIALS / "unitats" / unit / "apunts.md").read_text(encoding="utf-8")
    validation_text = (MATERIALS / "unitats" / unit / "validacio.md").read_text(
        encoding="utf-8"
    )
    source_revision = yaml_value(source_text, "revision")
    revisions = {
        source_revision,
        yaml_value(status_text, "revision_apunts"),
        yaml_value(status_text, "revision_auditada"),
        yaml_value(validation_text, "audited_revision"),
    }
    if None in revisions or len(revisions) != 1:
        raise RuntimeError(f"{unit} no és publicable: les revisions no coincidixen")
    if yaml_value(validation_text, "veredicte") != "APTA":
        raise RuntimeError(f"{unit} no és publicable: validacio.md no marca APTA")
    if yaml_value(status_text, "estat") != "aprovada" or yaml_value(
        status_text, "porta_superada"
    ) != "G4":
        raise RuntimeError(f"{unit} no és publicable: cal estat aprovada i porta G4")


def is_publishable(status_text: str) -> bool:
    return yaml_value(status_text, "estat") == "aprovada" and yaml_value(status_text, "porta_superada") == "G4"


def unpublished_unit_page(unit: str, status_text: str) -> str:
    status = yaml_value(status_text, "estat") or "no indicat"
    gate = yaml_value(status_text, "porta_superada") or "no indicada"
    apunts_revision = yaml_value(status_text, "revision_apunts") or "no indicada"
    audited_revision = yaml_value(status_text, "revision_auditada") or "no indicada"
    title = UNIT_TITLES[unit]
    return "\n".join((
        "<!-- Fitxer generat per scripts/sincronitza_mkdocs.py; no l'edites manualment. -->",
        f"# {unit}. {title}",
        "",
        "> **Unitat no publicada.** Els apunts d'esta unitat no es copien a la "
        "> publicació perquè l'estat editorial actual no supera la porta G4.",
        "",
        "| Camp | Valor |",
        "| --- | --- |",
        f"| Estat de la unitat | `{status}` |",
        f"| Porta registrada | `{gate}` |",
        f"| Revisió dels apunts | `{apunts_revision}` |",
        f"| Revisió auditada | `{audited_revision}` |",
        "",
        "Quan `validacio.md` audite la mateixa revisió dels apunts i l'estat "
        "passe a `aprovada` amb porta `G4`, la sincronització publicarà el "
        "contingut d'esta unitat.",
    )) + "\n"


def main() -> None:
    # Només es regeneren directoris que són propietat d'esta publicació.
    for generated_dir in (DOCS / "curs", DOCS / "unitats"):
        if generated_dir.exists():
            shutil.rmtree(generated_dir)

    plan_source = MATERIALS / "curs" / "pla-curs.md"
    plan_text = plan_source.read_text(encoding="utf-8")
    copy_markdown(plan_source, DOCS / "curs" / "pla-curs.md")
    copy_markdown(MATERIALS / "curs" / "matriu-curricular.md", DOCS / "curs" / "matriu-curricular.md")

    (DOCS / "curs" / "itinerari.md").write_text(course_itinerary(plan_text), encoding="utf-8")

    manifest = visual_manifest()
    statuses: dict[str, str] = {}
    for unit in UNITS:
        status_path = MATERIALS / "unitats" / unit / "estat.yaml"
        status_text = status_path.read_text(encoding="utf-8")
        statuses[unit] = status_text
        destination = DOCS / "unitats" / f"{unit.lower()}.md"
        if is_publishable(status_text):
            verify_approval_contract(unit, status_text)
            copy_markdown(
                MATERIALS / "unitats" / unit / "apunts.md",
                destination,
                status_text,
                unit,
                manifest,
            )
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(unpublished_unit_page(unit, status_text), encoding="utf-8")
    (DOCS / "curs" / "estat-publicacio.md").write_text(publication_status(statuses), encoding="utf-8")


if __name__ == "__main__":
    main()
