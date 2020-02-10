from Photo import Photo
from TagsScorer import TagsScorer
from os import path
import os
from FilesHelper import FilesHelper

tagsScorer = TagsScorer()

def solve_file(filepath):
  vertical_photos = []
  horizontal_photos = []
  photos = []
  photos_ids = []
  with open(filepath) as fp:
    N = int(fp.readline().rstrip('\n'))
    for i in range(0, N):
      orientation, num_tags, *tags = [s for s in fp.readline().rstrip('\n').split(" ")] 
      tags = set(tags)
      if orientation == 'V':
        pass
      else: 
        horizontal_photos.append(tags)
        photos_ids.append(i)
  scores = [[-1]*len(horizontal_photos) for x in range(0, len(horizontal_photos))]
  max_score = -1
  max_index = -1
  for i in range(0, len(horizontal_photos)):
    for j in range(0, len(horizontal_photos)):
      if i == j:
        pass
      scores[i][j] = tagsScorer.scoreTags(horizontal_photos[i], horizontal_photos[j])
      current_maxscore = max(scores[i])
      if current_maxscore > max_score:
        max_score = current_maxscore
        max_index = i

  arranged_photos = []
  arranged_photos = [photos_ids[max_index]]
  current_index = max_index
  score = 0
  indexes_available = list(range(0, len(horizontal_photos)))
  while len(arranged_photos) < len(horizontal_photos):
    i_max = indexes_available[0]
    for i in indexes_available:
      if scores[current_index][i] > scores[current_index][i_max]:
        i_max = i
    indexes_available.remove(i_max)
    score += scores[current_index][i_max]
    current_index = i_max
    arranged_photos.append(photos_ids[i_max])
  
  print(f'Expected score: {score}')
  # tag_dict = dict()
  # for photo in horizontal_photos:
  #   for tag in photo.tags:
  #     if tag in tag_dict:
  #       tag_dict[tag].append(photo)
  #     else:
  #       tag_dict[tag] = [photo]
  
  # arranged_photos = [horizontal_photos[0]]
  # for photo in horizontal_photos:
  #   for tag in photo.tags:
  #     tag_dict[tag]

  # slideComparer = SlideComparer()
  # for i in range(0, len(horizontal_photos)-1):
  #   for j in range(i+1, len(horizontal_photos)):
  #     score = slideComparer.compareTwoPhotosSlides(horizontal_photos[i], horizontal_photos[j])
  #     if(score > horizontal_photos[i].max_similarity):
  #       horizontal_photos[i].max_similarity = score
  #       horizontal_photos[i].max_similar_photo = horizontal_photos[j]
  #     if(score > horizontal_photos[j].max_similarity):
  #       horizontal_photos[j].max_similarity = score
  #       horizontal_photos[j].max_similar_photo = horizontal_photos[i]

  #     print(score)

  # arranged_photos = [horizontal_photos[0]]
  # horizontal_photos.remove(horizontal_photos[0])
  # for i in range(0, len(horizontal_photos)):
  #   max_score = 0
  #   max_elem = None
  #   if len(horizontal_photos) == 1:
  #     max_elem = horizontal_photos[len(horizontal_photos)-1]
  #   else:
  #     for j in range(i+1, len(horizontal_photos)):
  #       current_score = tagsScorer.scoreTags(horizontal_photos[i].tags, horizontal_photos[j].tags)
  #       if current_score >= max_score:
  #         max_elem = horizontal_photos[j]
  #   arranged_photos.append(max_elem)
  #   horizontal_photos.remove(max_elem)

  return arranged_photos

if __name__ == '__main__':
  filesHelper = FilesHelper()
  problems_dir_path = 'qualification_round_2019.in'
  solutions_dir_path = 'qualification_round_2019.out'

  # problem_files = filesHelper.get_problem_files(problems_dir_path)
  problem_files = ['c_memorable_moments.txt']

  for file in problem_files:
    print(f'Start working on {file}')
    arranged_photos = solve_file(path.join(os.getcwd(), problems_dir_path, file))
    with open(path.join(os.getcwd(), solutions_dir_path, file), 'w') as f:
      f.write(str(len(arranged_photos)) + '\n')
      for photo in arranged_photos:
        f.write(str(photo) + '\n')
    print(f'Finished working on {file}')
    
