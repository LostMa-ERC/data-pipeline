# LostMa Data Pipeline

Data pipeline for the LostMa ERC project, which extracts, transforms, and loads the contents of the Heurist database into local, embedded database files. These local files, having been modelled according to the final, public version of the data, are then used to create artifacts, including JSON and TEI-XML files.

## Table of Contents

- [Architecture](#architecture)
- [Set up](#set-up-)
- [Run](#launch-pipeline-)
    - [Download Heurist data](#1-download-heurist-data)
    - [Model as graph](#2-model-as-graph)
    - [Write witnesses to JSON](#3-write-nested-witness-metadata-to-json)
- [Contributing](./CONTRIBUTING.md)
- [Acknowledgements](#acknowledgements)

## Architecture

```mermaid
architecture-beta
    group cloud(server)[Server]
    service heurist(database)[Heurist RDBMS] in cloud
    service api(server)[Heurist API] in cloud
    service duckdb(database)[DuckDB RDBMS] in local

    group local(database)[Data Modelling]
    service kuzu(database)[Kuzu GDBMS] in local

    group staticFiles(disk)[Output]
    service witnessTrees(disk)[Witness JSON] in staticFiles
    service tei(disk)[Witness TEI] in staticFiles


    heurist:R -- L:api
    api:R -- L:duckdb
    duckdb:R -- L:kuzu
    kuzu:R -- L:witnessTrees
    kuzu:R -- L:tei

```

## Set up 📐

1. Download the code: `git clone https://github.com/LostMa-ERC/data-pipeline.git`

2. Change into the directory: `cd data-pipeline`.

3. Save Heurist login credentials in a `.env` file.

    1. Copy the example [`.env.example`](./.env.example), renaming it `.env`.

    2. Fill in the 2 parameters: `HEURIST_LOGIN`, `HEURIST_PASSWORD`

4. Create and activate a virtual Python environment, version 3.12 or greater.

5. Install the project: `pip install .`

## Launch pipeline 🚀

You can run the full workflow or run steps individually, as long as you make sure to have satisfied each step's prerequesites.

### Full workflow

```shell

```

### Step by step

#### 1. Download Heurist data

- Prerequisites: _None_

- Output:

    - `databases/heurist.duckdb` : [Duckdb](https://duckdb.org/) relational database

```shell
```

#### 2. Model as graph

- Prerequisites:

    - `databases/heurist.duckdb` : [Duckdb](https://duckdb.org/) relational database

- Output:

    - `databases/kuzu_db` : [Kùzu](https://kuzudb.com/) graph database

```shell
```

#### 3. Write nested `Witness` metadata to JSON

- Prerequisites:

    - `databases/kuzu_db` : [Kùzu](https://kuzudb.com/) graph database

- Output:

    - `static/*.json` : 1 JSON file per Witness, including the following metadata:

        - Witness's metadata
        - Witness's documents
            - Document's metadata
            - Document's parts & physical descriptions
            - Document's repository & location

```shell
```

```json
{
    "type": "witness",
    "id": 47375,
    "is_unobserved": false,
    "is_excerpt": false,
    "siglum": "Ltk. 195",
    "alternative_sigla": [],
    "status": "complete",
    "creation_date_min": "1326-01-01",
    "creation_date_max": "1360-12-31",
    "creation_date_certainty": "2. Probable (33%-66%)",
    "creation_date_text": "'<=1350'.",
    "urls": [
        "https://www.handschriftencensus.de/20258"
    ],
    "scripta": {
        "id": 46312,
        "name": "Brabants",
        "description": "Dialect of Brabant.",
        "urls": []
    },
    "manuscripts": [
        {
            "id": 47370,
            "shelfmark": "Ltk. 195",
            "old_shelfmarks": [],
            "is_hypothetical": false,
            "collection_of_fragments": "No",
            "urls": [
                "https://www.handschriftencensus.de/20258"
            ],
            "witness_parts": [
                {
                    "id": 47376,
                    "div_order": 1,
                    "number_of_verses": 21844,
                    "part_of_text": "Full text",
                    "verses_per_line": "continuous",
                    "lines_are_incomplete": "No",
                    "page_ranges": [
                        "1r-120v"
                    ],
                    "has_initials": false,
                    "has_rubrication": false,
                    "has_incomplete_decoration": false,
                    "has_no_decoration": false,
                    "has_pictorial_designs": false,
                    "decoration_is_unknown": false
                }
            ],
            "repository": {
                "id": 43873,
                "name": "Universitaire Bibliotheken Leiden",
                "alternative_names": [
                    "Rijksuniversiteit te Leiden., Bibliotheek",
                    "Leiden University Library",
                    "Bibliotheek der Rijksuniversiteit Leiden",
                    "Universiteitsbibliotheek (Lejda).",
                    "Universiteitsbibliotheek (Leyde, Pays-Bas)",
                    "Rijksuniversiteit Leiden Bibliotheek"
                ],
                "viaf": "133132602.000000",
                "isni": "0000000122932800",
                "settlement": {
                    "id": 43362,
                    "name": "Leiden",
                    "region": "South Holland",
                    "country": "Netherlands",
                    "location_mappable": "POINT(4.49306 52.15833)",
                    "geonames_id": 2751773
                }
            }
        }
    ]
}
```

## Acknowledgements

Funded by the European Union (ERC, LostMA, 101117408). Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Research Council. Neither the European Union nor the granting authority can be held responsible for them.