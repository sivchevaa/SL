os_input = input("Input OS(W - Windows, L - Linux): ").strip().upper()
path_input = input("Input path: ").strip()

if os_input == 'W':
    if '\\' in path_input or path_input.startswith(':'):
        print('Yes')
    else:
        print('No')
elif os_input == 'L':
    if path_input.startswith('/'):
        print('Yes')
    else:
        print('No')
else:
    print('No')