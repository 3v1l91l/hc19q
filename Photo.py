class Photo:
  max_similarity = 0
  max_similar_photo = None

  def __init__(self, photo_id, orientation, tags, num_tags):
    self.id = photo_id
    self.orientation = orientation
    self.tags = tags
    self.num_tags = num_tags