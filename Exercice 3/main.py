def virus(patients0, n):
  grid = [[False for _ in range(n)] for _ in range(n)]

  for x, y in patients0:
    grid[x][y] = True

  infected_count = [len(patients0)]

  while infected_count[-1] < n * n:
    new_infected_count = 0

    for x in range(n):
      for y in range(n):
        if grid[x][y]:
          for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= x + dx < n and 0 <= y + dy < n and not grid[x + dx][y + dy]:
              grid[x + dx][y + dy] = True
              new_infected_count += 1

    infected_count.append(infected_count[-1] + new_infected_count)

  return infected_count

patients0 = [(1, 1)]
n = 3
infected_count = virus(patients0, n)
print(infected_count) 