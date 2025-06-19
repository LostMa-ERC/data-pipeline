import json

from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    TextColumn,
    TimeElapsedColumn,
)

from src.config import settings
from src.db.connections import KuzuDB

from .builders.witness import WitnessTreeBuilder


def build_witness_trees(db: KuzuDB):
    dir = settings.STATIC_FILES.joinpath("witness")
    dir.mkdir(exist_ok=True)
    with (
        Progress(
            TextColumn("{task.description}"),
            BarColumn(),
            MofNCompleteColumn(),
            TimeElapsedColumn(),
        ) as p,
    ):
        total = len(db.get_rows("MATCH (w:Witness) RETURN w.id"))
        wtb = WitnessTreeBuilder(db=db)
        t = p.add_task("Building witness trees", total=total)
        for wit in wtb.iter_witnesses():
            json_str = wit.model_dump_json(exclude_unset=True, exclude_none=True)
            obj = json.loads(json_str)
            obj = {"type": "witness"} | obj
            with open(dir.joinpath(f"{wit.id}.json"), "w") as f:
                json.dump(obj=obj, fp=f, indent=4, ensure_ascii=False)
            p.advance(t)
        total_files = len([f for f in dir.iterdir() if "json" in f.suffix])
        assert total == total_files
