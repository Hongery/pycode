
# def test_str() -> str:
#     """_summary_

#     Returns:
#         str: _description_
#     """
#     c =["a"]
#     return c
# from typing import List
# def get_list() -> List[str]:
#     lst = ["PyCon"]
#     lst.append(2019)
#     return [str(x) for x in lst]

#  Expected Generator, Iterable or Iterator

def gen() -> int:  # bad-yield-annotation
  yield 1
c = ["a"]
for range in c:
    print(gen())
# def gen() -> Iterator[int]:
#     # Could also use Generator or Iterable.
#     yield 1