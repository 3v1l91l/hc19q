
from Photo import Photo
from TagsScorer import TagsScorer
from FilesHelper import FilesHelper
from os import listdir, path
from os.path import isfile, join

filesHelper = FilesHelper()

def extract_tags(photos_tags, photo_id):
  tags = set()
  if len(photo_id) == 2:
    tags.update(photos_tags[int(photo_id[0])])
    tags.update(photos_tags[int(photo_id[1])])
  else:
    tags.update(photos_tags[int(photo_id[0])])
  
  return set(tags)

def judge_file(file):
  print(file)
  photos_tags = []
  file_full_path = filesHelper.get_full_path('qualification_round_2019.in', file)
  with open(file_full_path) as fp:
    N = int(fp.readline().rstrip('\n'))
    for i in range(0, N):
      orientation, num_tags, *tags = [s for s in fp.readline().rstrip('\n').split(" ")] 
      tags = set(tags)
      photos_tags.append(tags)

  file_full_path = filesHelper.get_full_path('qualification_round_2019.out', file)
  photo_ids = []
  with open(file_full_path) as fp:
    N = int(fp.readline().rstrip('\n'))
    for i in range(0, N):
      photo_id = [s for s in fp.readline().rstrip('\n').split(" ")] 
      photo_ids.append(photo_id)

  tagsScorer = TagsScorer()
  score = 0
  for i in range(0, len(photo_ids)-1):
    score += tagsScorer.scoreTags(extract_tags(photos_tags, photo_ids[i]), extract_tags(photos_tags, photo_ids[i+1]))

  print('Score is: ', score)
  return score

if __name__ == '__main__':
  problem_files = filesHelper.get_problem_files()
  solution_files = filesHelper.get_solution_files()

  print("Judging the solutions...")
  score = 0
  for file in solution_files:
    score += judge_file(file)
  
  print(f'Total score: {score}')