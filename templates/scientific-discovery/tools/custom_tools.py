"""Tools for the daily scientific discovery digest."""

from __future__ import annotations

from typing import TypedDict

from grok_install.runtime import arxiv, delivery, x_client


class Paper(TypedDict):
    id: str
    title: str
    authors: list[str]
    abstract: str
    url: str
    categories: list[str]


class PaperSummary(TypedDict):
    paper_id: str
    claim: str
    method: str
    why_it_matters: str


class ExpertTake(TypedDict):
    author: str
    url: str
    excerpt: str


def fetch_arxiv_new(categories: list[str], limit: int = 6) -> list[Paper]:
    """Return the newest papers in the given arXiv categories."""
    return arxiv.latest(categories=categories, limit=max(1, min(limit, 20)))


def summarize_paper(paper_id: str, claim: str, method: str, why_it_matters: str) -> PaperSummary:
    """Attach a structured summary to a paper."""
    return {"paper_id": paper_id, "claim": claim, "method": method, "why_it_matters": why_it_matters}


def search_x_for_paper(arxiv_url: str, limit: int = 30) -> list[dict]:
    """Search X for posts referencing the paper."""
    return x_client.from_env().search(query=arxiv_url, limit=max(1, min(limit, 50)))


def extract_expert_takes(paper_id: str, takes: list[ExpertTake]) -> dict:
    """Record 2-4 credible expert takes on the paper."""
    if not 0 <= len(takes) <= 4:
        raise ValueError("at most 4 takes per paper")
    return {"paper_id": paper_id, "takes": takes}


def compile_digest(papers: list[PaperSummary], takes: list[dict], date: str) -> dict:
    """Build the digest object."""
    return {"date": date, "papers": papers, "takes": takes}


def deliver_digest(digest: dict, channel: str, to: str) -> dict:
    """Deliver the digest over the configured channel."""
    if channel not in ("email", "slack", "stdout"):
        raise ValueError(f"unsupported channel: {channel}")
    return delivery.send(channel=channel, to=to, payload=digest)
