from Photo import Photo
from TagsScorer import TagsScorer
from os import path
import os
from FilesHelper import FilesHelper
from random import random
import time
tagsScorer = TagsScorer()

def get_max_horiz(current_photo_tags, horizontal_photos, horizontal_photos_indexes):
  max_horiz = -1
  max_index = -1
  max_score = -1
  for horiz_i in horizontal_photos_indexes:
    horiz_score = tagsScorer.scoreTags(current_photo_tags, horizontal_photos[horiz_i])
    if horiz_score > max_horiz:
      max_horiz = horiz_score
      max_index = horiz_i
      max_score = horiz_score
  return max_score, max_index

def get_max_vert(current_photo_tags, vertical_photos, vertical_photos_indexes):
  left_index = None
  right_index = None
  max_vert_score = -1
  vert_scores = []
  for vert_i in vertical_photos_indexes:
    current_vert_score = tagsScorer.scoreTags(current_photo_tags, vertical_photos[vert_i])
    if current_vert_score > max_vert_score:
      right_index = left_index
      left_index = vert_i
      max_vert_score = current_vert_score
  return left_index, right_index

def solve_file(filepath):
  vertical_photos = []
  horizontal_photos = []
  vertical_photos_ids = []
  photos = []
  horizontal_photos_ids = []
  count = 0
  with open(filepath) as fp:
    N = int(fp.readline().rstrip('\n'))
    for i in range(0, N//100):
      orientation, num_tags, *tags = [s for s in fp.readline().rstrip('\n').split(" ")] 
      tags = set(tags)
      if orientation == 'V':
        vertical_photos.append(tags)
        vertical_photos_ids.append(i)
      else: 
        horizontal_photos.append(tags)
        horizontal_photos_ids.append(i)
      # horizontal_photos.append(tags)
      # horizontal_photos_ids.append(i)
    horizontal_photos_indexes = list(range(0, len(horizontal_photos)))
    vertical_photos_indexes = list(range(0, len(vertical_photos)))
    if len(horizontal_photos_indexes) > 0:
      current_photo_index = horizontal_photos_indexes[0]
      arranged_photos = [[horizontal_photos_ids[current_photo_index]]]
      current_photo_tags = horizontal_photos[0]
      horizontal_photos_indexes.remove(current_photo_index)
    else:
      arranged_photos = [[vertical_photos_indexes[0], vertical_photos_indexes[1]]]
      current_photo_tags = vertical_photos[0].copy()
      current_photo_tags.update(vertical_photos[1])
      vertical_photos_indexes.remove(0)
      vertical_photos_indexes.remove(1)
    score = 0
    while len(horizontal_photos_indexes)>0 or len(vertical_photos_indexes)>0:
      # find max in horizontals
      max_score, max_index = get_max_horiz(current_photo_tags, horizontal_photos, horizontal_photos_indexes)
      left_index, right_index = get_max_vert(current_photo_tags, vertical_photos, vertical_photos_indexes)
      
      joint_vert_score = -1
      if left_index != None:
        if right_index == None:
          right_index = vertical_photos_indexes[-1]
        joint_tags = vertical_photos[right_index].copy()
        joint_tags.update(vertical_photos[left_index])
        joint_vert_score = tagsScorer.scoreTags(current_photo_tags, joint_tags)

      if joint_vert_score > max_score:
        current_photo_tags = joint_tags
        arranged_photos.append([vertical_photos_ids[right_index], vertical_photos_ids[left_index]])
        vertical_photos_indexes.remove(right_index)
        vertical_photos_indexes.remove(left_index)
        score += joint_vert_score
      else:
        arranged_photos.append([horizontal_photos_ids[max_index]])
        current_photo_tags = horizontal_photos[max_index]
        horizontal_photos_indexes.remove(max_index)
        score += max_score
    print(f'Expected score: {score}')
  return arranged_photos


if __name__ == '__main__':
  filesHelper = FilesHelper()
  problems_dir_path = 'qualification_round_2019.in'
  solutions_dir_path = 'qualification_round_2019.out'

  problem_files = filesHelper.get_problem_files(problems_dir_path)
  # problem_files = problem_files[:-1]
  # problem_files = ['c_memorable_moments.txt']
  # problem_files = ['e_shiny_selfies.txt']
  problem_files = ['d_pet_pictures.txt']

  for file in problem_files:
    print(f'Start working on {file}')
    start_time = time.time()
    arranged_photos = solve_file(path.join(os.getcwd(), problems_dir_path, file))
    with open(path.join(os.getcwd(), solutions_dir_path, file), 'w') as f:
      f.write(str(len(arranged_photos)) + '\n')
      for photo in arranged_photos:
        if len(photo) == 1:
          f.write(str(photo[0]) + '\n')
        else:
          f.write(str(photo[0]) + ' ' + str(photo[1]) + '\n')

    print(f'Finished working on {file}')
    print("--- %s seconds ---" % (time.time() - start_time))

    
