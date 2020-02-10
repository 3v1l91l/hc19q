class TagsScorer:
  def scoreTags(self, tags1, tags2):
    intersection = tags1.intersection(tags2)
    diff12 = tags1.difference(tags2)
    diff21 = tags2.difference(tags1)
    return min(len(intersection), len(diff12), len(diff21))
