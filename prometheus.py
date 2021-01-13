from itertools import groupby
from typing import Any, Dict, List

from prometheus_client import CollectorRegistry, Summary, write_to_textfile


def parse_filled_rows(
    filled_rows: Dict[str, List[Any]], scenario_name: str, target_file: str
) -> None:
    registry = CollectorRegistry()
    summary = Summary(
        "task_duration",
        "The duration summary of a certain task",
        labelnames=["scenario", "task", "nodes_involved"],
        unit="sec",
        registry=registry,
        namespace="scenario_player",
    )
    k = lambda r: r.task_type
    for key, group in groupby(sorted(filled_rows["csv_rows"], key=k), key=k):
        task = key.split("(", 1)[0]
        group = list(group)
        for entry in group:
            summary.labels(
                scenario=scenario_name, task=task, nodes_involved=entry.nodes_involved
            ).observe(entry.duration)
    write_to_textfile(target_file, registry)
