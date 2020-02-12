class TagsScorer:
  def scoreTags(self, tags1, tags2):
    intersection_len = len(tags1.intersection(tags2))
    if intersection_len == 0:
      return 0
    diff12_len = len(tags2) - intersection_len
    if diff12_len == 0:
      return 0
    diff21_len = len(tags1) - intersection_len
    if diff21_len == 0:
      return 0
    return min(intersection_len, diff12_len, diff21_len)