import re
from collections import defaultdict


def clean_keyword(k: str) -> str:
    """Lowercase, strip, remove extra whitespace and punctuation."""
    if not k:
        return ""
    k = k.lower().strip()
    k = re.sub(r"[^a-z0-9\s-]", "", k)
    k = re.sub(r"\s+", " ", k)
    return k


def deduplicate(keywords):
    seen = set()
    out = []
    for k in keywords:
        c = clean_keyword(k)
        if c and c not in seen:
            seen.add(c)
            out.append(c)
    return out


def group_keywords(keywords, threshold=0.6):
    """Naive grouping: cluster by exact token overlap.

    Returns list of clusters (list of keywords).
    """
    cleaned = deduplicate(keywords)
    clusters = []
    used = set()
    for i, k in enumerate(cleaned):
        if i in used:
            continue
        group = [k]
        ki = set(k.split())
        used.add(i)
        for j, kj in enumerate(cleaned[i + 1 :], start=i + 1):
            if j in used:
                continue
            kj_set = set(kj.split())
            overlap = len(ki & kj_set) / max(1, min(len(ki), len(kj_set)))
            if overlap >= threshold:
                group.append(kj)
                used.add(j)
        clusters.append(group)
    return clusters
