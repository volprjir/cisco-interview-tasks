# Static document-tag database
documents_by_tag = {
    "animals": ["doc1", "doc2"],
    "mammals": ["doc3"],
    "birds": ["doc4"],
    "dogs": ["doc5"],
    "cats": ["doc6"],
    "sparrows": ["doc7"]
}

# Tag hierarchy (transitive relationship)
tag_hierarchy = {
    "animals": ["mammals", "birds"],
    "mammals": ["dogs", "cats"],
    "birds": ["sparrows"]
}