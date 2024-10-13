from collections import deque

tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while tools and substances:
    current_tool = tools[0]
    current_substance = substances[-1]

    result = current_tool * current_substance
    for challenge in challenges:
        if result == challenge:
            challenges.remove(result)
            tools.popleft()
            substances.pop()
            break
    else:
        tools.append(tools.popleft() + 1)
        if current_substance - 1 == 0:
            substances.pop()
        else:
            substances.append(substances.pop() - 1)

    if (not substances or not tools) and challenges:
        print("Harry is lost in the temple. Oblivion awaits him.")
        break
    if not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break

if tools:
    print(f"Tools: {', '.join([f'{num}' for num in tools])}")
if substances:
    print(f"Substances: {', '.join([f'{num}' for num in substances])}")
if challenges:
    print(f"Challenges: {', '.join([f'{num}' for num in challenges])}")
