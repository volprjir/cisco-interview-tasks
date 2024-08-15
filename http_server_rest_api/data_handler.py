from typing import List

from mocked_db import documents_by_tag, tag_hierarchy


def get_documents_for_tag(tag: str) -> List[str]:
    """
    Get all documents for a given tag, including documents from sub-tags
    :param tag: tag to get documents for
    :return:
        List of documents for the given tag
    """
    if tag not in documents_by_tag:
        return []
    documents = set(documents_by_tag.get(tag, []))

    # Recursively gather documents from sub-tags
    for sub_tag in tag_hierarchy.get(tag, []):
        documents.update(get_documents_for_tag(sub_tag))

    return list(documents)