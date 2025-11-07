import json
import os
from datetime import timedelta, date
from typing import List, Iterable, Type

from pydantic import BaseModel
from tinydb import TinyDB, Query


class TinyDBCache(object):
    def __init__(self, db_path: str, model: Type[BaseModel], id_field: str = "abs_url"):
        self.db = TinyDB(db_path)
        self.model = model
        self.id_field = id_field  # unique key (e.g. abs_url or arxiv_id)

    def _to_model(self, doc):
        return self.model.model_validate(doc)

    def exists(self, paper_id: str) -> bool:
        Paper = Query()
        return self.db.contains(Paper[self.id_field] == paper_id)

    def add(self, paper: BaseModel) -> bool:
        key = getattr(paper, self.id_field)
        if self.exists(key):
            return False
        self.db.insert(paper.model_dump())
        return True

    def bulk_add(self, papers: Iterable[BaseModel]) -> int:
        count = 0
        for p in papers:
            if self.add(p):
                count += 1
        return count

    def get(self, **query) -> List[BaseModel]:
        Paper = Query()
        q = None
        for k, v in query.items():
            cond = Paper[k] == v
            q = cond if q is None else (q & cond)
        docs = self.db.search(q) if q else self.db.all()
        return [self._to_model(doc) for doc in docs]

    def update(self, paper_id: str, **fields) -> bool:
        Paper = Query()
        modified = self.db.update(fields, Paper[self.id_field] == paper_id)
        return modified != []

    def all(self) -> List[BaseModel]:
        return [self._to_model(doc) for doc in self.db.all()]

    def export_jsonl(self, file_path: str) -> None:
        with open(file_path, "w", encoding="utf-8") as f:
            for doc in self.db.all():
                f.write(self.model(**doc).model_dump_json() + "\n")


class ArxivPaper(BaseModel):
    title: str
    authors: List[str]
    abstract: str
    categories: List[str]
    abs_url: str
    pdf_url: str
    publish_date: str = None
    is_interesting: bool = False
    is_interesting_2nd_pass: object = None
    review: object = None

def upwrap_md_json(text):
    if text.startswith("```json") and text.endswith("```"):
        text = text[len("```json"):-3].strip()
    return text

db = "./arxiv_cache.db"
cache = TinyDBCache(db, model=ArxivPaper, id_field="abs_url")


front_matter = """---
layout: default
---

"""

if not os.path.exists("_posts"):
    os.mkdir("_posts")

base_date = date(1900, 1, 1)

for idx, paper in enumerate(cache.all()):
    if paper.is_interesting and paper.is_interesting_2nd_pass['is_autonomous_driving_related']:
        # print(paper.review)
        # idx_str = f'{idx + 10101:08d}'
        front_matter = f"""---
        layout: default
        title: {paper.title}
        ---
        
        """
        post_date = base_date + timedelta(days=idx)
        if paper.review is None:
            continue
        review = json.loads(upwrap_md_json(paper.review))
        text = f"{front_matter}\n# [{review['score']}] {paper.title}\n\n"
        authors = f"- Authors: {', '.join(paper.authors)}\n"
        if len(authors) > 100:
            authors = f"{authors[:100]}...\n"
        text += authors
        # text += f"- Published Date: {paper.publish_date}\n"
        # text += f"- Categories: {', '.join(paper.categories)}\n"
        text += f"- [arXiv Link]({paper.abs_url})\n"
        text += f"- [PDF Link]({paper.pdf_url})\n\n"
        text += f"## Subfields\n {review['subfield']}\n"
        text += f"## Reason for Interest\n\n{review['reason']}\n"
        text += f"## Abstract: \n{"\n".join(paper.abstract.strip().split("\n")[1:])}\n ```\n"
        fn = f"_posts/{post_date.strftime('%Y-%m-%d')}-[{review['score']}]{paper.title}.md"

        with open(fn, "w", encoding="utf-8") as f:
            f.write(text)
        print(paper.title, fn)



