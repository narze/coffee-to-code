if __name__ == '__main__':
  str = "Coffee"
  str = set(str)
  print("".join([a if a != 'f' else 'd' for a in str]))
